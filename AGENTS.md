# Recommendation repository agent rules

This repository is the source of truth for website recommendations and execution handoffs. It does not contain website source code.

## Roles

- The recommendation AI creates and updates files under `sites/*/recommendations/`.
- The code execution AI reads approved recommendations and follows the site's `delivery_method`.
- For `pull_request`, the code execution AI modifies the separate target code repository and writes a result under `sites/*/results/`.
- For `direct_publish`, the code execution AI publishes through its existing production-connected environment and writes a non-authoritative execution-attempt receipt under `sites/*/results/`.
- The recommendation or verification AI checks the public production site and updates recommendation status or the next prompt version.

## Execution gate

Only execute a recommendation when all conditions are true:

1. Its YAML frontmatter contains exactly `status: "approved"`.
2. The matching `site.md` contains a supported `delivery_method`. A real `target_repository` and `default_branch` are required only for `pull_request`.
3. `Final decision`, `Implementation prompt`, and `Acceptance criteria` are complete.
4. No result or receipt already claims the same task, prompt version, and attempt as `in_progress`.
5. The execution method matches `delivery_method`; never substitute one delivery mode for another.
6. The active-scope fingerprint validates, and the task's stable item IDs match the current prompt version.

Never execute `draft`, `needs_decision`, `deferred`, `blocked`, `rejected`, or `superseded` tasks.

## Execution protocol

1. Read the site's `delivery_method` before changing anything.
2. For `pull_request`:
   - Create `sites/<site-id>/results/<TASK-ID>-result.md`.
   - Work only in the named target repository, open a Pull Request, and record implementation evidence in the result file.
   - Never merge or publish unless separately authorized.
3. For `direct_publish`:
   - Create `sites/<site-id>/results/<TASK-ID>-v<VERSION>-attempt-<NN>.md` from the template before modifying production code.
   - Use the next unused two-digit attempt number, record the task/version/fingerprint handshake, mark the receipt `in_progress`, and add or update its row in `results/index.md`.
   - Use the execution AI's existing production-connected code environment, run every item-level check, publish only the approved scope, perform the required production smoke test, and update the receipt to `published`, `partial`, or `blocked`.
   - Treat the receipt as diagnostic evidence only. It must never set the recommendation to `implemented` or `verified`, and it must never be used as proof that production satisfies the task.
4. Do not deploy, publish, change billing products, or expose secrets unless the task and selected delivery method explicitly authorize that action.
5. Do not edit the approved recommendation or mark it verified.

## Live verification protocol

1. Treat each site's public production URL as the source of truth when its `site.md` says `audit_source: "public_production"` or establishes the same rule in prose.
2. At every later audit, compare every item in the latest approved recommendation with the current public page and classify it as `verified_online`, `still_open`, `partially_applied`, or `no_longer_relevant`.
3. Remove `verified_online` and `no_longer_relevant` items from the next execution scope. Carry `still_open` items and only the unresolved remainder of `partially_applied` items into the next prompt version under the same task ID, preserving stable item IDs where the requirement is unchanged.
4. Increment `prompt_version` whenever the executable scope is refreshed after a live audit.
5. Never infer production status from source repositories, execution receipts, result files, branches, commits, or Pull Requests. Receipts may diagnose whether a version was claimed, checked, published, or blocked, but only current public-production evidence may verify an item.
6. For BGRemove, never inspect or use `DAOteam/bgremove` to determine implementation or production state.

## Safety

- Never store credentials, payment secrets, environment variable values, or customer data here.
- Never invent repository URLs, product IDs, API contracts, analytics, rankings, or business decisions.
- For `pull_request`, stop with a blocked result when required information is missing. For `direct_publish`, stop, update the current attempt receipt to `blocked`, and report the blocker without publishing.
- For `direct_publish`, never record credentials, customer data, signed-in account identifiers, cookies, or environment values in an execution receipt.

## Active-scope protocol

1. Approved recommendations must place `Active execution scope` immediately after the title and before historical evidence.
2. The active scope must be bounded by `ACTIVE_SCOPE_START` and `ACTIVE_SCOPE_END`, contain stable item IDs, and match the YAML `scope_fingerprint`.
3. Before editing, the execution AI must echo `task_id`, `prompt_version`, `scope_fingerprint`, delivery method, and item IDs, then run `python3 scripts/validate_handoffs.py`.
4. Every item must finish as `pass`, `fail`, or `not_tested`. `fail` or required `not_tested` means the attempt is `partial` or `blocked`, never fully complete.
5. Exact-copy tasks should define URL-level required-present and required-absent assertions. Stateful tasks should separate safe automated checks, signed-in production checks, and states that require fixtures.
6. A successful receipt for the current prompt version prevents duplicate execution while independent verification is pending. A later prompt version is a new executable scope.
7. Every site with one or more approved recommendations must list each approved task exactly once in its recommendation index execution queue, with a matching prompt version.

## Daily operations protocol

1. Follow `DAILY_OPERATIONS.md` for the reusable cross-site operating cycle.
2. Start each daily cycle by syncing the recommendation repository, running `python3 scripts/validate_handoffs.py`, and then running `python3 scripts/daily_queue.py`.
3. Recommendation/verification and code execution run independently. Each fetches the latest repository state at the start and pushes its own state transition at the end; the repository is the only inter-agent handoff channel.
4. A site's first queued task is a gate. An `in_progress`, `published`, `partial`, or `blocked` receipt for its current prompt version prevents the code execution AI from advancing to a later task for that site until the recommendation/verification AI reconciles it.
5. Across sites that are ready for execution, choose one queue head by P0, P1, P2, P3, then `created_at`, then `task_id`. Execute at most one task per daily code run.
6. A daily audit performs lightweight change detection and deep-checks only changed, failed, expired, or explicitly requested pages. It creates at most one main growth task and never auto-approves unresolved business decisions.
7. The recommendation/verification AI consumes `verify_online`, `review_partial`, `resolve_blocker`, and invalid-receipt states. The code execution AI consumes only `execute` and never bypasses another queue-head state.
8. Neither AI sends task instructions, execution summaries, or completion claims to the other through a person. Each push is a complete asynchronous handoff.
