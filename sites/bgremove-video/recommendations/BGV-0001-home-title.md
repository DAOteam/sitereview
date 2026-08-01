---
task_id: "BGV-0001"
site_id: "bgremove-video"
title: "Fix duplicated English homepage title"
status: "superseded"
priority: "P1"
source: "ai"
created_at: "2026-07-31"
updated_at: "2026-08-01"
prompt_version: 1
superseded_by: "BGV-0007"
---

# BGV-0001 — Fix duplicated English homepage title

Superseded by [BGV-0007](BGV-0007-metadata-quality.md). Do not execute this file.

## Scope

English homepage SEO title and shared title-generation logic.

## Current facts and evidence

The public English homepage title repeats several editing-tool names after the brand, diluting the primary topic.

## User proposal

Pending.

## AI recommendation

Use:

`Remove Video Background Online Free – No Watermark | BGRemove`

Make the smallest possible change to the title source and duplication logic.

## Open decisions

- User approval of the proposed title.

## Final decision

Pending.

## Implementation prompt

```text
Draft only. Do not execute until this task is approved.

Locate the English homepage title source and determine whether the duplication comes from page configuration, an SEO component, or a shared template. Change the final English homepage title to:

Remove Video Background Online Free – No Watermark | BGRemove

Do not rewrite the H1, body, meta description, canonical, hreflang, robots, or structured data. Check all five current languages for shared-template regressions and run the smallest relevant tests or build check.
```

## Acceptance criteria

- The rendered English homepage contains one clear, non-duplicated title.
- Other pages and languages gain no title regression.
- Canonical and hreflang remain unchanged.

## Out of scope

- Homepage copy redesign.
- Deployment.
