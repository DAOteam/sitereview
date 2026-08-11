# Global rules for Codex

## Operating principles

- Prefer small, reviewable diffs unless the user explicitly requests a larger refactor.
- Before editing, identify the files to change and state the plan in 3–6 bullets.
- Never invent APIs, configurations, repository URLs, or file paths.
- Preserve existing style and architecture unless the approved task requires a change.

## Safety and secrets

- Never store secrets, tokens, private keys, environment values, credentials, cookies, signed-in identities, or customer data in this repository.
- Ask for secrets only through environment variables when implementation genuinely requires them.
- Do not add analytics, telemetry, or unrelated network calls.

## Repository purpose

This repository contains only current website work. It does not store website source code, audit history, completed tasks, execution receipts, prompt versions, result logs, or archives.

Each website has exactly one file:

```text
sites/<site-id>.md
```

The file is the complete current handoff for that website. Its YAML frontmatter contains only the operational metadata required to identify and deliver the work. Its body contains only current approved tasks and current items awaiting a user decision.

## Recommendation and verification AI

The recommendation/verification AI owns `sites/*.md`.

For every audit:

1. Read the selected website file and the current public production site.
2. Check every existing task against the live site.
3. Delete completed or no-longer-relevant tasks completely.
4. Keep unresolved tasks, rewriting partially completed tasks to contain only the remaining work.
5. Add newly discovered tasks that are within the user's requested audit scope.
6. Rewrite the website file in place. Never append audit history, completion notes, verification logs, dates of past checks, versions, receipts, or changelogs.
7. Put directly authorized, implementation-ready work under `Approved tasks`.
8. Put work that requires a business, legal, pricing, product, data, localization, migration, or publishing decision under `Needs decision`. Do not infer approval.
9. If nothing remains, keep the website file and write `No current tasks.`

Public production is the source of truth for live verification. Source code, commits, branches, Pull Requests, chats, and implementation claims cannot prove that a task is complete.

For BGRemove, never inspect or use `DAOteam/bgremove` to determine audit findings or production status.

## Code execution AI

The code execution AI treats the selected `sites/<site-id>.md` as its complete task brief.

1. Sync the latest recommendation repository state.
2. Read the selected website file completely.
3. Read `delivery_method` before changing code.
4. Execute only tasks under `Approved tasks`. Never execute `Needs decision`.
5. By default, complete all approved tasks in the selected website file unless the user limits the scope.
6. Follow each task's required change, acceptance criteria, and do-not-change boundary exactly.
7. Do not edit or delete the website task file. The recommendation/verification AI removes completed work after checking production.
8. Do not create result files, receipts, histories, or status updates in this repository.

Delivery methods:

- `direct_publish`: use the existing authorized production-connected workspace, run relevant checks, publish the approved scope, and smoke-test production. Do not create a Pull Request unless the website file explicitly changes the delivery method.
- `pull_request`: require a real `target_repository` and `default_branch`, create a focused branch and Pull Request, and do not merge or publish without separate authorization.

Stop instead of guessing when delivery metadata is missing, instructions conflict, required secrets are unavailable, or the requested work would expand beyond the approved task.

## File format

Create new website files from `templates/site-todo.md`.

Every current task must contain:

- Priority
- Page or surface
- Current problem and live evidence
- Required change
- Acceptance criteria
- Do not change

Use concrete visible outcomes and exact replacement copy when wording matters. Do not fabricate metrics, rankings, product capabilities, customer evidence, or implementation details.

## Git

- Fetch before editing and never force-push over remote work.
- Keep one logical update per commit.
- Recommendation updates may rewrite a website file completely because it intentionally represents only the current state.
- Commit and push only when the user has authorized repository synchronization.
