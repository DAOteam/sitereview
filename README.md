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

Each website has exactly one Markdown file, written in Chinese. YAML keys, URLs, identifiers, and exact website copy retain their required original language. The file contains only work that is currently open:

- `已批准任务`: implementation-ready work the code execution AI may execute.
- `待决事项`: current work that requires the website owner's decision and must not be executed.

Whenever approved implementation work exists, the file also contains exactly one approved public-changelog task for that release batch. The entry must describe only user-visible changes that actually ship and must omit internal or sensitive details. If nothing ships, no entry is published. The task stays open until the public entry is verified online.

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
3. Execute only `已批准任务` using the file's `delivery_method`.
4. After successful delivery, publish exactly one sanitized changelog entry summarizing only the changes actually online.
5. Do not edit the task file or write results into this repository.
6. The next live audit removes work that is actually online, including the completed changelog task.

Create a new website from [templates/site-todo.md](templates/site-todo.md). Use a stable lowercase `site_id` for the filename.
