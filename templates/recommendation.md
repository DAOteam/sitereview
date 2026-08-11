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
scope_fingerprint: "sha256:{{ACTIVE_SCOPE_SHA256}}"
---

# {{PREFIX}}-0001 — {{TITLE}}

## Active execution scope

<!-- ACTIVE_SCOPE_START -->
Prompt version: 1

### {{PREFIX}}-0001-A — {{SHORT_ITEM_NAME}}

- Target: {{URL_OR_STATE}}
- Required present or condition: {{EXPECTED_RESULT}}
- Required absent: {{OLD_OR_FORBIDDEN_RESULT}}
- Verification: {{AUTOMATED_BUILD_PREVIEW_OR_PRODUCTION_CHECK}}
<!-- ACTIVE_SCOPE_END -->

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

- `{{PREFIX}}-0001-A`: {{TESTABLE_CRITERION}}

## Out of scope

- {{EXPLICIT_EXCLUSION}}
