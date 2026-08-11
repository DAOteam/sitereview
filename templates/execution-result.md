---
task_id: "{{PREFIX}}-0001"
site_id: "{{SITE_ID}}"
prompt_version: 1
scope_fingerprint: "sha256:{{ACTIVE_SCOPE_SHA256}}"
attempt: 1
delivery_method: "{{pull_request_OR_direct_publish}}"
evidence_authority: "non_authoritative_execution_receipt"
status: "in_progress"
started_at: "{{ISO_DATETIME}}"
completed_at: null
published_at: null
code_repository: "{{TARGET_REPOSITORY_OR_NOT_APPLICABLE}}"
code_branch: "{{BRANCH_OR_NOT_APPLICABLE}}"
commit_or_pr: null
---

# Execution attempt — {{PREFIX}}-0001 v1 attempt 01

This file records an execution attempt. It cannot verify production and must not be used to mark the recommendation `implemented` or `verified`.

Allowed receipt statuses are `in_progress`, `published`, `partial`, or `blocked` for `direct_publish`, and `in_progress`, `implemented`, or `blocked` for `pull_request`.

## Version handshake

- Task: `{{PREFIX}}-0001`
- Prompt version: `1`
- Scope fingerprint: `sha256:{{ACTIVE_SCOPE_SHA256}}`
- Stable item IDs: `{{PREFIX}}-0001-A`
- Delivery method: `{{pull_request_OR_direct_publish}}`

## Item results

| Item ID | Result | Evidence |
|---|---|---|
| `{{PREFIX}}-0001-A` | `not_tested` | Pending |

## Summary

{{RESULT}}

## Files changed

{{FILES}}

## Checks run

{{COMMANDS_AND_RESULTS}}

## Publication

{{PUBLISH_RESULT_OR_NOT_APPLICABLE}}

## Production smoke test

{{LIVE_RESULT_FOR_DIRECT_PUBLISH_OR_NOT_APPLICABLE}}

## Manual actions required

{{MANUAL_ACTIONS}}

## Risks or blockers

{{RISKS}}
