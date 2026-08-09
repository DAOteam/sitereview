---
task_id: "BGV-0010"
site_id: "bgremove-video"
title: "Simplify homepage completed-job actions"
status: "needs_decision"
priority: "P2"
source: "user+ai"
created_at: "2026-08-09"
updated_at: "2026-08-09"
prompt_version: 1
---

# BGV-0010 — Simplify homepage completed-job actions

## Scope

The completed-job state of the functional upload/processing area in the homepage hero. This task concerns only the action area displayed after a video finishes processing successfully.

## Current facts and evidence

Evidence is a user-provided annotated screenshot dated 2026-08-09. It shows the completed result filename and video details followed by:

- A primary `Download` button.
- A secondary `Run another` button on a lower row.
- An `Open the full workspace ↗` text link to the right of `Run another`.
- A horizontal divider separating `Download` from the lower actions.

The user's blue annotation identifies `Open the full workspace ↗` for removal. The red annotation identifies `Download` and `Run another` as the two actions that should remain and be placed side by side.

This state is authenticated or job-dependent and was not independently reproduced during this recommendation pass. The screenshot is treated as user-confirmed evidence of the current interface.

## User proposal

1. Delete the `Open the full workspace ↗` link and its text from the homepage completed-job state.
2. Place `Download` and `Run another` in one horizontal row, arranged left and right.

## AI recommendation

- Apply the change only to the homepage hero's successful completed-job state.
- Remove the complete `Open the full workspace ↗` interactive element, not only its visible text. It must not leave an empty clickable area, focus stop, icon, accessible label, or layout column.
- Use one action row with `Download` on the left and `Run another` on the right.
- Keep `Download` visually primary and `Run another` visually secondary.
- Give both buttons the same height and a consistent gap. Prefer two balanced columns when the available width supports them.
- Remove or reposition the current horizontal divider so it no longer forces the two retained actions into separate rows. Do not leave a short or visually orphaned rule.
- Preserve the existing behavior of both buttons: Download must still download the completed result, and Run another must still reset or reopen the upload flow exactly as it does now.
- Preserve filename, duration, resolution, completion state, keyboard focus styling, and accessible button names.
- Do not remove a separate workspace link elsewhere on the site or inside the authenticated workspace; this recommendation targets only the link shown in the homepage completion panel.

## Open decisions

1. Responsive behavior below the width where two comfortable buttons fit. AI recommendation: keep the side-by-side layout on desktop and tablet; on narrow mobile screens, stack `Download` above `Run another` at full width rather than shrinking labels or creating horizontal overflow.
2. Button widths on the horizontal row. AI recommendation: use equal flexible widths for visual balance while keeping Download's primary styling.

These decisions may be confirmed together with additional interface issues the user plans to provide. Until then, this recommendation is not executable.

## Final decision

Pending the responsive and button-width decisions. The user has confirmed removal of the homepage completion-panel workspace link and side-by-side placement of the two retained actions on the shown wide layout.

## Implementation prompt

```text
NOT EXECUTABLE. BGV-0010 has status needs_decision. Wait for the user to confirm the responsive behavior and button-width rule, and for any additional related homepage-completion issues to be added.
```

## Acceptance criteria

- Provisional: the homepage successful completed-job panel contains no `Open the full workspace ↗` text, link, icon, empty focus target, or reserved layout space.
- Provisional: Download appears on the left and Run another on the right in one row at the approved wide viewport.
- Provisional: Download remains the primary action and Run another remains secondary.
- Provisional: the divider no longer splits the two buttons into separate rows or leaves an orphaned line.
- Provisional: both button behaviors, filename, duration, resolution, keyboard access, focus states, and accessible names remain functional.
- Provisional: no separate workspace navigation outside this homepage completion panel is removed.
- Provisional: responsive behavior matches the final confirmed rule and introduces no overflow or clipped labels.
- Provisional: final completion is verified from the actual public completed-job state, not from source code alone.

## Out of scope

- Changing video processing, download generation, job state, allowance consumption, authentication, or upload behavior.
- Removing workspace navigation outside the homepage completed-job panel.
- Changing button labels, completion metadata, colors, typography, or the overall homepage hero design beyond the minimum layout work described above.
- Non-English localization unless the completed-state action labels are intentionally shared and the user later approves that scope.
