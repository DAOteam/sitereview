---
task_id: "{{PREFIX}}-0001"
site_id: "{{SITE_ID}}"
title: "{{TITLE}}"
status: "draft"
priority: "P2"
source: "ai"
created_at: "{{YYYY-MM-DD}}"
updated_at: "{{YYYY-MM-DD}}"
prompt_version: 1
---

# {{PREFIX}}-0001 — {{TITLE}}

## Scope

{{PAGES_AND_SYSTEMS}}

## Current facts and evidence

{{EVIDENCE}}

## User proposal

{{USER_PROPOSAL}}

## AI recommendation

{{AI_RECOMMENDATION}}

## Open decisions

{{OPEN_DECISIONS}}

## Final decision

{{FINAL_DECISION}}

## Implementation prompt

```text
{{ONLY_EXECUTABLE_WHEN_STATUS_IS_APPROVED}}
```

## Acceptance criteria

- {{TESTABLE_CRITERION}}

## Out of scope

- {{EXPLICIT_EXCLUSION}}
