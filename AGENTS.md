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

The file is the complete current execution handoff for that website. Its YAML frontmatter contains only the operational metadata required to identify and deliver the work. Its body contains only current approved, implementation-ready tasks. Never put open questions, alternative options, recommendations awaiting selection, or items awaiting a user decision in `sites/*.md`.

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
7. Convert every retained or newly discovered finding into one concrete, implementation-ready task under `已批准任务`. Choose the strongest evidence-based implementation path instead of listing alternatives or asking the execution AI to decide.
8. Never create a `待决事项` section or use decision-task fields in `sites/*.md`. If a safe execution plan genuinely depends on missing business, legal, pricing, product, data, localization, migration, or publishing facts, ask the user for those facts in the conversation before adding that task. After receiving the answer, write only the resolved execution plan. Do not invent missing facts and do not preserve the question in the file. Missing delivery, repository, or branch routing may remain `not_established` in YAML, but must never become a body task or weaken the specificity of the implementation plan; the code execution AI will stop on that metadata until it is supplied.
9. When approved implementation work includes a significant user-facing update, include exactly one approved task to update the public changelog for that release batch. Do not create a changelog task for routine image replacements, copy or typo corrections, metadata-only SEO changes, minor visual adjustments, internal refactors, or ordinary maintenance. Keep an applicable changelog task until its entry is verified online, even if the other work is already complete; remove it only after verification.
10. If nothing remains, keep the website file and write `当前没有待办事项。`

Public production is the source of truth for live verification. Source code, commits, branches, Pull Requests, chats, and implementation claims cannot prove that a task is complete.

For BGRemove, never inspect or use `DAOteam/bgremove` to determine audit findings or production status.

## Code execution AI

The code execution AI treats the selected `sites/<site-id>.md` as its complete task brief.

1. Sync the latest recommendation repository state.
2. Read the selected website file completely.
3. Read `delivery_method` before changing code.
4. Execute all tasks under `已批准任务` unless the user limits the scope.
5. Follow each task's required change, acceptance criteria, and do-not-change boundary exactly.
6. After publishing approved changes, add a public changelog entry only when the selected website task file contains an approved changelog task. Describe only significant changes that actually shipped; if nothing significant ships, do not add an entry.
7. Do not edit or delete the website task file. The recommendation/verification AI removes completed work after checking production.
8. Do not create result files, receipts, histories, or status updates in this repository.

Delivery methods:

- `direct_publish`: use the existing authorized production-connected workspace, run relevant checks, publish the approved scope, and smoke-test production. Do not create a Pull Request unless the website file explicitly changes the delivery method.
- `pull_request`: require a real `target_repository` and `default_branch`, create a focused branch and Pull Request, and do not merge or publish without separate authorization.

Stop instead of guessing when delivery metadata is missing, instructions conflict, required secrets are unavailable, or the requested work would expand beyond the approved task.

## File format

Create new website files from `templates/site-todo.md`.

Every website frontmatter must include `changelog_url`, using a real public URL or `not_established`. If significant approved work requires a changelog and the website has no established public changelog, ask the user in the conversation for the real changelog location before finalizing the file; never invent a location and never put the unresolved choice in the website file. Minor work that does not require a changelog may remain under `已批准任务` with `changelog_url: "not_established"`.

Every current task in `sites/*.md` must use these Chinese field labels:

- `优先级`
- `页面或界面`
- `当前问题与线上证据`
- `修改要求`
- `验收标准`
- `不要修改`

Every task must be an execution plan, not a recommendation menu. State the selected change in `修改要求`, make `验收标准` observable and testable, and use `不要修改` to bound the work. Do not use `当前问题`, `需要决定`, or `选项与取舍` in `sites/*.md`.

Use concrete visible outcomes and exact replacement copy when wording matters. Do not fabricate metrics, rankings, product capabilities, customer evidence, legal facts, or implementation details. If any required fact cannot be verified or safely inferred, obtain it from the user before writing the task file.

The release changelog is public-facing and reserved for significant updates users would reasonably want to discover: new user-facing features or pages, material workflow or navigation redesigns, important compatibility improvements, and fixes for serious user-visible failures. Do not record routine image replacements, copy or typo corrections, metadata-only SEO changes, minor spacing or styling adjustments, internal refactors, or ordinary maintenance unless the user explicitly requests it. When a batch mixes significant and minor work, mention only the significant changes. Entries may mention only truthful user-visible features, fixes, usability improvements, and supported product behavior. Never include file or component names, architecture, repositories, branches, commits, infrastructure or provider configuration, costs, secrets, security-sensitive implementation details, customer data, internal metrics, AI prompts, or internal workflows.

## Git

- Fetch before editing and never force-push over remote work.
- Keep one logical update per commit.
- Recommendation updates may rewrite a website file completely because it intentionally represents only the current state.
- Commit and push only when the user has authorized repository synchronization.
