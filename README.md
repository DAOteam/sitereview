# Website Growth Recommendations

Private multi-site repository for website audit recommendations, approved implementation prompts, and execution-attempt receipts. A receipt records what an execution AI attempted; it never proves that production is correct.

## Structure

```text
sites/index.md
sites/<site-id>/site.md
sites/<site-id>/decisions.md
sites/<site-id>/recommendations/index.md
sites/<site-id>/recommendations/<TASK-ID>-<slug>.md
sites/<site-id>/results/index.md
sites/<site-id>/results/<TASK-ID>-result.md  # pull_request result
sites/<site-id>/results/<TASK-ID>-v<VERSION>-attempt-<NN>.md  # direct_publish receipt
templates/
prompts/code-execution-agent.md
```

Only recommendations with `status: "approved"` may be executed.

For the reusable morning-review, one-task execution, and post-publication verification cycle, follow [DAILY_OPERATIONS.md](DAILY_OPERATIONS.md). Run `python3 scripts/daily_queue.py` for the current cross-site action dashboard.

## Permanent execution-agent prompt

Configure the code execution AI once with [prompts/code-execution-agent.md](prompts/code-execution-agent.md). After that, the AI discovers approved tasks and follows each site's delivery method without needing a new task-specific handoff prompt.

For a `direct_publish` site, the code execution AI verifies the task/version/scope fingerprint, creates a non-authoritative attempt receipt, publishes the approved scope through its existing production-connected environment, and records item-level checks plus a production smoke test. The receipt is diagnostic evidence only. The next independent audit still verifies the public site, removes completed items, and carries unresolved or partially applied items into the next `prompt_version` of the same recommendation.

Each recommendation index with approved tasks must define an explicit execution queue. The execution AI takes the first approved queued task that has no successful receipt for its current prompt version. Active instructions belong near the top of each recommendation; historical audits remain below them.
