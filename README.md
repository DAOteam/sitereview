# Current website tasks

This repository is a deliberately minimal handoff between a website recommendation AI and a code execution AI.

## Structure

```text
AGENTS.md
README.md
templates/site-todo.md
prompts/code-execution-agent.md
sites/<site-id>.md
```

Each website has exactly one Markdown file. That file contains only work that is currently open:

- `Approved tasks`: implementation-ready work the code execution AI may execute.
- `Needs decision`: current work that requires the website owner's decision and must not be executed.

Completed and no-longer-relevant work is deleted during the next live audit. Partially completed work is shortened to its unresolved remainder. The repository intentionally keeps no audit history, task history, prompt versions, execution receipts, result files, or archives.

## Audit workflow

1. Select `sites/<site-id>.md`.
2. Audit the live production website within the user's requested scope.
3. Recheck every existing task against production.
4. Rewrite the file with only unresolved and newly discovered work.
5. Commit and push when repository synchronization is authorized.

## Code workflow

1. Select the website to modify.
2. Read its single file under `sites/`.
3. Execute only `Approved tasks` using the file's `delivery_method`.
4. Do not edit the task file or write results into this repository.
5. The next live audit removes work that is actually online.

Create a new website from [templates/site-todo.md](templates/site-todo.md). Use a stable lowercase `site_id` for the filename.
