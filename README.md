# Website Growth Recommendations

Private multi-site repository for website audit recommendations, approved implementation prompts, and code-execution results.

## Structure

```text
sites/index.md
sites/<site-id>/site.md
sites/<site-id>/decisions.md
sites/<site-id>/recommendations/index.md
sites/<site-id>/recommendations/<TASK-ID>-<slug>.md
sites/<site-id>/results/index.md
sites/<site-id>/results/<TASK-ID>-result.md
templates/
prompts/code-execution-agent.md
```

Only recommendations with `status: "approved"` may be executed.

## Permanent execution-agent prompt

Configure the code execution AI once with [prompts/code-execution-agent.md](prompts/code-execution-agent.md). After that, the AI discovers approved tasks from this repository and does not need a new task-specific handoff prompt for every run.
