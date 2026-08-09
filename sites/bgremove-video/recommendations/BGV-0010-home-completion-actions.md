---
task_id: "BGV-0010"
site_id: "bgremove-video"
title: "Improve tool navigation, result actions, and mobile layout"
status: "approved"
priority: "P1"
source: "user+ai"
created_at: "2026-08-09"
updated_at: "2026-08-09"
prompt_version: 5
---

# BGV-0010 — Improve tool navigation, result actions, and mobile layout

## Scope

The English homepage primary navigation, the completed-job state of the functional upload/processing area in the homepage hero, and the homepage `Your recent clips` list on narrow mobile viewports. This task covers the Remove entry point, completed-result action layout, and horizontal overflow caused by long uploaded filenames or other non-shrinking card content.

## Current facts and evidence

Evidence is a user-provided annotated screenshot dated 2026-08-09. It shows the completed result filename and video details followed by:

- A primary `Download` button.
- A secondary `Run another` button on a lower row.
- An `Open the full workspace ↗` text link to the right of `Run another`.
- A horizontal divider separating `Download` from the lower actions.

The user's blue annotation identifies `Open the full workspace ↗` for removal. The red annotation identifies `Download` and `Run another` as the two actions that should remain and be placed side by side.

This state is authenticated or job-dependent and was not independently reproduced during this recommendation pass. The screenshot is treated as user-confirmed evidence of the current interface.

A second user-provided mobile screenshot dated 2026-08-09 shows:

- A long generated filename extending beyond the right edge of the viewport in the completed-result panel.
- The divider and lower action row also extending beyond the visible card area; `Open the full workspace` is clipped off-screen.
- The outer right edge of the `Your recent clips` card extending beyond the viewport.
- Recent-clip metadata occupying one long horizontal row that does not comfortably fit the narrow card.

The user confirms that long uploaded filenames can make both the functional card and work-list cards overflow to the right on mobile.

A third user-provided desktop screenshot dated 2026-08-09 shows that the primary navigation begins with `How it works` and has no explicit `Remove` item. The user requests a `Remove` item immediately before `How it works`, linking to the homepage.

## User proposal

1. Delete the `Open the full workspace ↗` link and its text from the homepage completed-job state.
2. Place `Download` and `Run another` in one horizontal row, arranged left and right.
3. On mobile, prevent long uploaded filenames from making the functional result card or work-list cards overflow beyond the right edge of the screen.
4. Add `Remove` to the top navigation immediately before `How it works`, and link it to the homepage.

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

### Remove navigation entry

- Add a visible `Remove` link as the first item in the English primary navigation, immediately before `How it works`.
- Link `Remove` to the English homepage root (`/`). Do not create a new route or point it to a separate authenticated workspace URL.
- Use a real anchor and preserve the navigation's existing hover, focus, keyboard, and accessibility behavior. On the homepage, follow the site's existing active-link convention and use `aria-current="page"` if the navigation already supports it.
- Apply the same item and ordering to the mobile navigation or menu: `Remove`, then `How it works`, followed by the existing items.
- Keep the BGRemove logo's existing homepage link unchanged. The new text link is an additional explicit route for users who understand the main tool area as their workspace.
- Ensure the added item does not make the desktop navigation overflow or crowd at supported widths. At narrow widths, rely on the existing responsive mobile menu pattern rather than clipping or shrinking labels until they are difficult to read.
- This new persistent navigation entry replaces the discoverability role of the completion-panel `Open the full workspace ↗` link, which should still be removed as specified above.

### Mobile overflow treatment

- Fix the intrinsic sizing problem at the card and child-layout level. Flex and grid children that contain filenames or metadata must be allowed to shrink, typically through an equivalent of `min-width: 0`.
- Keep every homepage functional/result card and every recent-clip card within the viewport: `max-width: 100%`, border-box sizing, and responsive internal columns or rows.
- Do not use a global `overflow-x: hidden` on the page as the primary fix. Hiding the overflow would leave clipped controls and inaccessible content.
- Completed-result filename recommendation: allow up to two readable lines on mobile, break very long unspaced strings safely, then clamp or truncate. Preserve the full filename in the element's accessible name and an appropriate non-layout-dependent full-text affordance such as `title` where useful.
- Recent-clip filename recommendation: keep the compact row to one line with ellipsis when space is limited. The text container must shrink while the thumbnail remains a fixed, non-shrinking size.
- Use safe wrapping for hostile filename shapes, including long strings with no spaces, underscores, hyphens, Unicode characters, and a file extension. An equivalent of `overflow-wrap: anywhere` may be used where wrapping is intended.
- Let duration, resolution, expiry, date, or other secondary metadata wrap onto another line or use a responsive grid. Do not force all metadata into one unbreakable row.
- Ensure action rows, dividers, thumbnails, text blocks, and card borders derive their width from the available container rather than fixed or content-sized minimum widths.
- Preserve the actual stored filename and download filename. This is a presentation fix only; do not rename uploads or generated files.
- Validate the page at 320px, 360px, 390px, and 430px CSS viewport widths with both ordinary and deliberately long filenames.

## Open decisions

None. The user approved all four recommended options on 2026-08-09.

## Final decision

Approved on 2026-08-09:

1. Remove the homepage completion-panel `Open the full workspace ↗` element.
2. At widths where two comfortable buttons fit, place equal-width `Download` and `Run another` buttons in one row, with Download on the left and visually primary. On narrow mobile screens, stack the two full-width buttons with Download first.
3. Show the completed-result filename on up to two lines on mobile. Use a one-line ellipsis in compact recent-clip rows while preserving the full accessible and downloaded filename.
4. Eliminate mobile horizontal overflow at the card and child-layout level.
5. Add `Remove` immediately before `How it works` in the English desktop and mobile navigation, linking to `/`.
6. Do not change Spanish, Portuguese, French, or German navigation in this task.

## Implementation prompt

```text
Implement BGV-0010 in BGRemove's current production-connected environment and publish only this approved scope after checks pass. Do not modify this recommendation repository or create an execution-result file.

Target the English homepage experience only.

1. Primary navigation
- Add a real anchor labeled `Remove` as the first primary navigation item, immediately before `How it works`.
- Set its destination to the English homepage root `/`; do not create a new route or send it to a separate authenticated workspace route.
- Add the same item in the same relative order to the English mobile navigation/menu.
- Preserve the logo's existing homepage link, all existing navigation items, keyboard access, visible focus states, hover behavior, and the site's existing active-page convention. Use `aria-current="page"` on the homepage if the navigation already supports that convention.
- Ensure the added item does not cause desktop navigation overflow, clipping, collision, or illegible compression.

2. Homepage completed-result actions
- In the successful completed-job state of the homepage hero tool, remove the entire `Open the full workspace ↗` interactive element, including its icon, link or handler, accessible label, focus stop, layout column, and reserved space.
- Keep `Download` and `Run another`. At widths where both labels fit comfortably, place them in one horizontal row with equal flexible widths, equal heights, and a consistent gap: Download on the left, Run another on the right.
- Keep Download visually primary and Run another visually secondary.
- On narrow mobile widths where a two-column row would crowd or overflow, stack two full-width buttons vertically with Download first. Do not shrink labels or controls to force a horizontal layout.
- Remove or reposition the current divider so it neither separates the two actions into different rows nor leaves an orphaned rule.
- Preserve both actions' current behavior and accessible names, plus the completed filename, duration, resolution, state, and focus treatment.

3. Mobile overflow and filename presentation
- Fix intrinsic sizing in the homepage functional/result card and `Your recent clips` cards. Allow filename and metadata flex/grid children to shrink, keep cards and internal rows within their available container, and use responsive wrapping rather than content-sized minimum widths.
- Do not use global page-level `overflow-x: hidden` as the primary fix and do not leave any control clipped off-screen.
- On mobile, display the main completed-result filename on no more than two readable lines. Safely wrap hostile long strings where intended, then clamp or truncate. Preserve the full filename in its accessible name and a non-layout-dependent full-text affordance such as the existing detail behavior or a useful `title`.
- In compact recent-clip rows, display the filename on one line with ellipsis. Keep the thumbnail fixed and non-shrinking while the text column can shrink.
- Allow date, duration, resolution, expiry, and other secondary metadata to wrap or move to a responsive row/grid instead of forcing one unbreakable line.
- Preserve the actual stored filename and download filename. Do not rename uploaded or generated files.

4. Scope and checks
- Do not change Spanish, Portuguese, French, or German navigation or copy.
- Do not change processing, downloads, job state, allowance consumption, authentication, upload behavior, or authenticated workspace routing.
- Verify ordinary and deliberately long filenames containing spaces, no spaces, underscores, hyphens, Unicode characters, and extensions.
- Check the completed-result state, recent clips, and navigation on desktop and at 320px, 360px, 390px, and 430px CSS viewport widths. Confirm there is no document or card horizontal overflow and every interactive element remains visible and keyboard accessible.
- After the relevant checks pass, publish this exact scope through the existing direct-to-production workflow.
```

## Acceptance criteria

- The homepage successful completed-job panel contains no `Open the full workspace ↗` text, link, icon, empty focus target, or reserved layout space.
- Download appears on the left and Run another on the right in one equal-width row when space permits; on narrow mobile screens, two full-width buttons stack with Download first.
- Download remains the primary action and Run another remains secondary.
- The divider no longer splits the two buttons into separate rows or leaves an orphaned line.
- Both button behaviors, filename, duration, resolution, keyboard access, focus states, and accessible names remain functional.
- No separate workspace navigation outside this homepage completion panel is removed.
- The English desktop primary navigation contains `Remove` immediately before `How it works`, and the link target is `/`.
- The English mobile navigation or menu contains the same `Remove` item in the same relative order.
- The new navigation item is keyboard accessible, has visible focus treatment, follows the existing active-page convention, and does not change the logo's homepage link.
- Adding `Remove` causes no desktop navigation overflow, clipping, illegible compression, or collision at supported widths.
- Spanish, Portuguese, French, and German navigation and copy are unchanged.
- At 320px, 360px, 390px, and 430px CSS viewport widths, the document, functional result card, and recent-clips cards do not exceed the viewport width.
- The main completed-result filename uses no more than two lines on mobile; compact recent-clip filenames use one-line ellipsis.
- Long filenames with spaces, no spaces, underscores, hyphens, Unicode characters, and extensions wrap or truncate according to the approved rule without widening a card.
- The full stored and downloaded filename is unchanged; compact visual truncation does not remove the full accessible name.
- Thumbnails remain correctly sized, text columns shrink, and secondary metadata wraps without clipping or covering another control.
- The fix does not rely only on global page-level overflow clipping and leaves no off-screen interactive element.
- Final completion is verified from the actual production completed-job state, not from source code or an implementation report alone.

## Out of scope

- Changing video processing, download generation, job state, allowance consumption, authentication, or upload behavior.
- Removing other workspace navigation outside the homepage completed-job panel or changing the logo link.
- Creating a new Remove route, changing authenticated routing, or changing where the homepage tool runs.
- Changing button labels, completion metadata, colors, typography, or the overall homepage hero design beyond the minimum layout work described above.
- Renaming, shortening, or mutating stored/uploaded/generated filenames.
- Non-English localization unless the completed-state action labels are intentionally shared and the user later approves that scope.
