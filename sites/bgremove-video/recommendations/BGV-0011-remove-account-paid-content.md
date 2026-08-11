---
task_id: "BGV-0011"
site_id: "bgremove-video"
title: "Remove paid-plan content from the authenticated account page"
status: "approved"
priority: "P1"
source: "user+ai"
created_at: "2026-08-09"
updated_at: "2026-08-11"
prompt_version: 6
scope_fingerprint: "sha256:0891191bc333d3dbfaa3d598b7cacbf2af02b63fc0c914b1af13d2e352804240"
---

# BGV-0011 — Remove paid-plan content from the authenticated account page

## Active execution scope

<!-- ACTIVE_SCOPE_START -->
Prompt version: 6

### BGV-0011-A — Remove stale billing introduction

- Target: authenticated English `https://bgremove.video/app/account/`
- Required present: `Account and data. Everything destructive on this page asks once and then does exactly what it says.`
- Required absent: `Plan, billing and data.`
- Verification: assert the rendered signed-in page contains the approved introduction and preserves the separate invoice-retention sentence before and after publication.

### BGV-0011-B — Show authoritative reset date and time

- Target: both reset summaries on authenticated English `https://bgremove.video/app/account/`
- Required condition for an active window: both summaries show the same authoritative next full-reset date and time; semantic `<time>` elements expose the authoritative timestamp through `datetime`.
- Required condition for no window: no reset timestamp is fabricated; verify this state through an existing safe fixture or automated test rather than mutating a real account.
- Required preserved content: `Free`, `No charge`, `Up to 3 videos per 24-hour period`, `Up to 60 seconds per video`, and the invoice-retention sentence.
- Required absent: paid plan cards, prices, `See plans`, `Get notified`, paid CTAs, or empty paid-plan containers.
- Verification: record the automated no-window test separately from the signed-in active-window production smoke test. Either required state left `not_tested` makes the attempt `partial`, not complete.
<!-- ACTIVE_SCOPE_END -->

## Scope

The authenticated English account page at `https://bgremove.video/app/account/`. This task covers paid-plan marketing, plan-selection and notification controls, and the accuracy of the remaining free-allowance summary.

## Current facts and evidence

Evidence is a user-provided screenshot of the authenticated account page dated 2026-08-09. The screenshot shows:

- A current `Free` plan card with `3m per period`, a reset date, `No charge`, and a `See plans` button.
- A message stating that paid plans are not open for sign-up yet and inviting users to choose a plan for future notification.
- Paid `Creator` and `Studio` cards with `$19` and `$49` prices, paid allowance or resolution claims, and `Get notified` buttons.

The user confirms that this paid content is still present after sign-in and directs that it be deleted. The page is authenticated, so this recommendation pass does not claim an independent public reproduction; the screenshot is treated as user-confirmed evidence.

The confirmed current product rule is that BGRemove has no paid plans, subscriptions, credit packs, paid upgrades, or purchase options. Each signed-in account may complete up to three successful video jobs during a 24-hour allowance window that starts with the first successful job; failed jobs do not count, and the full allowance resets when the window ends. Each input may be up to 60 seconds.

## Live re-audit — 2026-08-11

Classification: `partially_applied`.

Verified online and removed from the next execution scope:

- `See plans`, the paid-plan availability message, Creator and Studio cards, `$19` and `$49` prices, paid allowance/resolution claims, and `Get notified` controls are absent from the authenticated English account page.
- The remaining summary displays `Free`, `No charge`, `Up to 3 videos per 24-hour period`, and `Up to 60 seconds per video`.
- No replacement paid CTA or empty paid-plan card remains, and the visible account layout is compact.

Still open and retained in prompt version 3:

1. The account-page introduction still says `Plan, billing and data. Everything destructive on this page asks once and then does exactly what it says.` The current product has no billing option, so `billing` is stale current-product language.
2. Both visible allowance summaries show only a reset date (`Resets 11 Aug 2026` and `Resets 11 Aug`) with no time, `datetime`, title, or accessible time label. This does not satisfy the approved requirement to show the real next full-reset date and time for an active window.

The separate sentence explaining that invoices are retained where tax law requires is allowed historical/legal context and is not classified as paid-product marketing.

## Second live re-audit — 2026-08-11

Classification: `still_open` with no change since prompt version 3.

- The introduction still renders `Plan, billing and data. Everything destructive on this page asks once and then does exactly what it says.`
- The two allowance summaries still render only `Resets 11 Aug 2026` and `Resets 11 Aug`, with no visible time or semantic `datetime`, title, or accessible time label.
- Previously removed plan cards, prices, `See plans`, and `Get notified` controls remain absent; the approved Free, No charge, allowance, duration, and invoice-retention content remains intact.

Prompt version 4 therefore retains the same two-item implementation scope and removes nothing further.

## Third live re-audit — 2026-08-11

Classification: `still_open` with no change since prompt version 4.

- The authenticated English account page still renders `Plan, billing and data. Everything destructive on this page asks once and then does exactly what it says.`; the approved `Account and data` replacement is absent.
- The active allowance window still renders `Resets 11 Aug 2026` in the main Free summary and `Resets 11 Aug` in the compact quota summary. Neither summary shows a visible time, and the page exposes no semantic `<time>` element carrying `datetime`, title, or accessible time text.
- Previously removed paid-plan messages, prices, plan cards, `See plans`, and `Get notified` controls remain absent. `Free`, `No charge`, the approved allowance and duration text, and the legally relevant invoice-retention sentence remain present.
- The current session has an active allowance window, so the no-window empty state could not be independently verified in this audit.

Prompt version 5 therefore retains the same two-item implementation scope and removes nothing further.

## Handoff protocol refresh — 2026-08-11

Prompt version 6 keeps the same two substantive items as version 5. It adds stable item IDs, an active-scope fingerprint, separate automated and signed-in verification requirements, a required execution-attempt receipt, and post-publication production smoke checks. No previously removed paid interface is returned to scope.

## User proposal

Delete paid-related content from the signed-in `/app/account/` page.

## AI recommendation

### Remove the paid-plan interface

- Remove the `See plans` button and its complete interactive element, route action, modal trigger, event handler, and reserved layout space from the account page.
- Remove the paid-plan availability message beginning `Paid plans are not open for sign-up yet`.
- Remove the complete `Creator` and `Studio` plan cards shown in the screenshot, including prices, paid allowances, resolution promises, descriptions, `Get notified` controls, and any associated notification form or modal that is reachable only from these cards.
- Inspect the remainder of the rendered account page and remove any additional current-product subscription, upgrade, price, paid tier, credit-pack, checkout, waitlist, or billing-marketing block not visible in the screenshot.
- Do not merely hide these blocks with CSS. They should not remain as off-screen content, keyboard focus stops, accessible names, click targets, or empty containers.
- Remove account-page links into a current paid purchase or plan-selection flow. Do not create replacement paid CTAs during the completely-free phase.

### Keep a clear free-usage summary

- Retain a compact account summary that identifies the current access as free and shows real allowance state from the existing account/quota data.
- Replace the ambiguous `3m per period` wording. It can be read as three minutes per period and does not clearly express the confirmed job-based allowance.
- AI-recommended English meaning: `Up to 3 videos per 24-hour period`, with `Up to 60 seconds per video` as secondary information.
- When an allowance window is active, show the real next full-reset date and time in a format users can understand. Do not calculate a new client-side rule that could disagree with the server's allowance state.
- When no allowance window has started, do not show a fabricated future reset time. Use the existing truthful state or a short explanation that the 24-hour window starts with the first successful video.
- Keep `No charge` only if it helps the existing account summary; it must not be paired with an upgrade implication. Do not use absolute future promises such as `Free forever` or `We will never charge`.
- After removing the paid sections, tighten the account-page layout so it does not leave large blank areas, empty card borders, broken dividers, or unnecessary scrolling on desktop or mobile.

### Preserve unrelated account functions and records

- Preserve authentication, profile, account security, sign-out, allowance enforcement, job history, download access, and other unrelated account functions.
- This is a user-interface and copy change. Do not delete historical transactions, invoices, payment-provider records, legally required records, customer data, or dormant billing infrastructure under this task.
- Do not change the actual free allowance, successful-job counting, reset behavior, video-duration validation, or retention policy.

## Open decisions

None. The user approved all three recommended options on 2026-08-09.

## Final decision

Approved on 2026-08-09:

1. Delete all paid-plan marketing and entry points from the authenticated English account page.
2. Replace `3m per period` with `Up to 3 videos per 24-hour period` and add `Up to 60 seconds per video` as secondary text.
3. Remove `See plans` without adding a replacement button.
4. Retain `No charge` as an accurate current-state label, without any upgrade implication or permanent-free promise.
5. Preserve real allowance data, unrelated account behavior, historical billing records, and dormant billing infrastructure.

## Implementation prompt

```text
Delivery method: direct_publish.
This is the approved BGV-0011 prompt version 6. The substantive scope is unchanged from version 5; version 6 adopts the repository's active-scope handshake and receipt protocol. Validate the scope fingerprint, create a versioned execution-attempt receipt, use the programming AI's current production-connected environment, and publish only this remaining English account-page scope after every required item passes. Do not use DAOteam/bgremove as an execution handoff or production-status source, create a Pull Request, or modify recommendation files. Creating and updating the required non-authoritative receipt under this site's `results/` directory is allowed and required.

Target `/app/account/` only.

1. BGV-0011-A — Remove stale billing language from the introduction
- Replace `Plan, billing and data. Everything destructive on this page asks once and then does exactly what it says.` with `Account and data. Everything destructive on this page asks once and then does exactly what it says.`
- Do not remove the separate legally relevant invoice-retention sentence from the data section.

2. BGV-0011-B — Show the real reset date and time
- In both the main Free summary and the compact quota summary, show the real next full-reset date and time when an allowance window is active. Use the existing authoritative server/account quota timestamp; do not create a separate client-side allowance calculation.
- Use a clear localized English display that includes both date and time. Where a semantic `<time>` element is used, set its `datetime` value to the authoritative timestamp.
- When no allowance window has started, do not fabricate a reset date or time. Keep a truthful empty state or state that the 24-hour window starts with the first successful video.

3. Preserve completed work and unrelated behavior
- Keep `Free`, `No charge`, `Up to 3 videos per 24-hour period`, and `Up to 60 seconds per video` unchanged.
- Do not reintroduce `See plans`, paid-plan messages, Creator or Studio cards, prices, paid allowances, `Get notified`, paid CTAs, or empty paid-plan layout.
- Do not change authentication, account data actions, job history, downloads, allowance enforcement, counting, failed-job treatment, reset logic, duration, retention, processing, output behavior, historical billing records, or legally required records.
- Do not change the public `/pricing/` page or any non-English account page.

4. Verification and publication
- Verify an active window shows the same authoritative reset date and time in both account summaries.
- Verify a no-window state does not show a fabricated timestamp where that state can be safely tested.
- Confirm the removed paid interface remains absent and unrelated account controls still work.
- After checks pass, publish this exact remaining scope through the existing direct-to-production workflow.
```

## Acceptance criteria

- `BGV-0011-A`: The introduction no longer describes the current account page as containing `billing`; it uses the approved `Account and data` replacement.
- `BGV-0011-B`: When an allowance window is active, both visible summaries show the same real next full-reset date and time from authoritative account data.
- `BGV-0011-B`: A no-window state does not show a fabricated reset timestamp, verified through an existing safe fixture or automated test.
- The legally relevant invoice-retention sentence remains.
- `Free`, `No charge`, `Up to 3 videos per 24-hour period`, and `Up to 60 seconds per video` remain unchanged.
- No removed paid-plan content, price, notification control, CTA, empty container, or focus target returns.
- Authentication, account data actions, job history, downloads, allowance behavior, processing, retention, historical records, and non-English pages remain unchanged.
- Verification is performed in the actual signed-in production account page after publication, not inferred from a source repository or implementation report.

## Out of scope

- Introducing replacement paid plans, prices, subscriptions, credit packs, checkout, billing portals, or waitlists.
- Changing the public `/pricing/` URL or other public-page copy already governed by separate recommendations.
- Changing authentication, allowance enforcement, processing, retention, or video output behavior.
- Deleting historical billing, transaction, invoice, customer, payment-provider, or legally required records.
- Spanish, Portuguese, French, or German account-page changes until the user separately authorizes localization.
