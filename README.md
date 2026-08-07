# Website Growth Recommendations

Private multi-site repository for website audit recommendations and approved implementation prompts. Execution results are optional and used only by sites whose delivery method requires repository feedback.

## Structure

```text
sites/index.md
sites/<site-id>/site.md
sites/<site-id>/decisions.md
sites/<site-id>/recommendations/index.md
sites/<site-id>/recommendations/<TASK-ID>-<slug>.md
sites/<site-id>/results/index.md
sites/<site-id>/results/<TASK-ID>-result.md  # only when delivery_method requires it
templates/
prompts/code-execution-agent.md
```

Only recommendations with `status: "approved"` may be executed.

## Permanent execution-agent prompt

Configure the code execution AI once with [prompts/code-execution-agent.md](prompts/code-execution-agent.md). After that, the AI discovers approved tasks and follows each site's delivery method without needing a new task-specific handoff prompt.

For a `direct_publish` site, the code execution AI publishes the approved scope through its existing production-connected environment and does not write a result file. The next audit verifies the public site, removes completed items, and carries unresolved or partially applied items into the next `prompt_version` of the same recommendation.
