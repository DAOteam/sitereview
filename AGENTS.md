# Recommendation repository agent rules

This repository is the source of truth for website recommendations and execution handoffs. It does not contain website source code.

## Roles

- The recommendation AI creates and updates files under `sites/*/recommendations/`.
- The code execution AI reads approved recommendations and follows the site's `delivery_method`.
- For `pull_request`, the code execution AI modifies the separate target code repository and writes a result under `sites/*/results/`.
- For `direct_publish`, the code execution AI publishes the approved scope through its existing production-connected environment and does not write a result file.
- The recommendation or verification AI checks the public production site and updates recommendation status or the next prompt version.

## Execution gate

Only execute a recommendation when all conditions are true:

1. Its YAML frontmatter contains exactly `status: "approved"`.
2. The matching `site.md` contains a supported `delivery_method`. A real `target_repository` and `default_branch` are required only for `pull_request`.
3. `Final decision`, `Implementation prompt`, and `Acceptance criteria` are complete.
4. For `pull_request`, no result file already claims the same task as `in_progress`.
5. The execution method matches `delivery_method`; never substitute one delivery mode for another.

Never execute `draft`, `needs_decision`, `deferred`, `blocked`, `rejected`, or `superseded` tasks.

## Execution protocol

1. Read the site's `delivery_method` before changing anything.
2. For `pull_request`, create `sites/<site-id>/results/<TASK-ID>-result.md`, work only in the named target repository, open a Pull Request, and record the implementation evidence in the result file.
3. For `direct_publish`, use the execution AI's existing production-connected code environment, run the required checks, publish only the approved scope, and do not create or update a result file.
4. Do not deploy, publish, change billing products, or expose secrets unless the task and selected delivery method explicitly authorize that action.
5. Do not edit the approved recommendation or mark it verified.

## Live verification protocol

1. Treat each site's public production URL as the source of truth when its `site.md` says `audit_source: "public_production"` or establishes the same rule in prose.
2. At every later audit, compare every item in the latest approved recommendation with the current public page and classify it as `verified_online`, `still_open`, `partially_applied`, or `no_longer_relevant`.
3. Remove `verified_online` and `no_longer_relevant` items from the next execution scope. Carry `still_open` items and only the unresolved remainder of `partially_applied` items into the next prompt version under the same task ID.
4. Increment `prompt_version` whenever the executable scope is refreshed after a live audit.
5. Never infer production status from source repositories, result files, branches, commits, or Pull Requests. Mark a recommendation `verified` only from current public-production evidence.
6. For BGRemove, never inspect or use `DAOteam/bgremove` to determine implementation or production state.

## Safety

- Never store credentials, payment secrets, environment variable values, or customer data here.
- Never invent repository URLs, product IDs, API contracts, analytics, rankings, or business decisions.
- For `pull_request`, stop with a blocked result when required information is missing. For `direct_publish`, stop and report the blocker to the user without creating a repository result file.
