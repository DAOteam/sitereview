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

All recommendation files under `sites/` must be written in Chinese. Keep YAML keys, URLs, identifiers, code symbols, product names, and exact source or replacement copy in their required original language.

## Recommendation and verification AI

The recommendation/verification AI owns `sites/*.md`.

For every audit:

1. Read the selected website file and the current public production site.
2. Check every existing task against the live site.
3. Delete completed or no-longer-relevant tasks completely.
4. Keep unresolved tasks, rewriting partially completed tasks to contain only the remaining work.
5. Add newly discovered tasks that are within the user's requested audit scope.
6. Rewrite the website file in place. Never append audit history, completion notes, verification logs, dates of past checks, versions, or receipts.
7. Put directly authorized, implementation-ready work under `已批准任务`.
8. Put work that requires a business, legal, pricing, product, data, localization, migration, or publishing decision under `待决事项`. Do not infer approval.
9. When approved implementation work remains, include exactly one approved task to update the public changelog for that release batch. Keep that task until its entry is verified online, even if the other work is already complete; remove it only after verification.
10. If nothing remains, keep the website file and write `当前没有待办事项。`

Public production is the source of truth for live verification. Source code, commits, branches, Pull Requests, chats, and implementation claims cannot prove that a task is complete.

For BGRemove, never inspect or use `DAOteam/bgremove` to determine audit findings or production status.

## Code execution AI

The code execution AI treats the selected `sites/<site-id>.md` as its complete task brief.

1. Sync the latest recommendation repository state.
2. Read the selected website file completely.
3. Read `delivery_method` before changing code.
4. Execute only tasks under `已批准任务`. Never execute `待决事项`.
5. By default, complete all approved tasks in the selected website file unless the user limits the scope.
6. Follow each task's required change, acceptance criteria, and do-not-change boundary exactly.
7. After publishing the approved changes, add exactly one public changelog entry for the batch. Describe only changes that actually shipped; if nothing ships, do not add an entry.
8. Do not edit or delete the website task file. The recommendation/verification AI removes completed work after checking production.
9. Do not create result files, receipts, histories, or status updates in this repository.

Delivery methods:

- `direct_publish`: use the existing authorized production-connected workspace, run relevant checks, publish the approved scope, and smoke-test production. Do not create a Pull Request unless the website file explicitly changes the delivery method.
- `pull_request`: require a real `target_repository` and `default_branch`, create a focused branch and Pull Request, and do not merge or publish without separate authorization.

Stop instead of guessing when delivery metadata is missing, instructions conflict, required secrets are unavailable, or the requested work would expand beyond the approved task.

## File format

Create new website files from `templates/site-todo.md`.

Every website frontmatter must include `changelog_url`, using a real public URL or `not_established`. If the website has no established public changelog, put choosing or creating one and the otherwise-ready release scope under `待决事项`; do not leave executable work under `已批准任务` and never invent a location.

Every current task in `sites/*.md` must use these Chinese field labels:

- `优先级`
- `页面或界面`
- `当前问题与线上证据`
- `修改要求`
- `验收标准`
- `不要修改`

Decision tasks use `当前问题`, `需要决定`, and `选项与取舍`.

Use concrete visible outcomes and exact replacement copy when wording matters. Do not fabricate metrics, rankings, product capabilities, customer evidence, or implementation details.

The release changelog is public-facing. It may mention only truthful user-visible features, fixes, usability improvements, and supported product behavior. Never include file or component names, architecture, repositories, branches, commits, infrastructure or provider configuration, costs, secrets, security-sensitive implementation details, customer data, internal metrics, AI prompts, or internal workflows.

## Git

- Fetch before editing and never force-push over remote work.
- Keep one logical update per commit.
- Recommendation updates may rewrite a website file completely because it intentionally represents only the current state.
- Commit and push only when the user has authorized repository synchronization.
