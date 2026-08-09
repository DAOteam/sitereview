---
task_id: "BGV-0011"
site_id: "bgremove-video"
title: "Remove paid-plan content from the authenticated account page"
status: "needs_decision"
priority: "P1"
source: "user+ai"
created_at: "2026-08-09"
updated_at: "2026-08-09"
prompt_version: 1
---

# BGV-0011 — Remove paid-plan content from the authenticated account page

## Scope

The authenticated English account page at `https://bgremove.video/app/account/`. This task covers paid-plan marketing, plan-selection and notification controls, and the accuracy of the remaining free-allowance summary.

## Current facts and evidence

Evidence is a user-provided screenshot of the authenticated account page dated 2026-08-09. The screenshot shows:

- A current `Free` plan card with `3m per period`, a reset date, `No charge`, and a `See plans` button.
- A message stating that paid plans are not open for sign-up yet and inviting users to choose a plan for future notification.
- Paid `Creator` and `Studio` cards with `$19` and `$49` prices, paid allowance or resolution claims, and `Get notified` buttons.

The user confirms that this paid content is still present after sign-in and directs that it be deleted. The page is authenticated, so this recommendation pass does not claim an independent public reproduction; the screenshot is treated as user-confirmed evidence.

The confirmed current product rule is that BGRemove has no paid plans, subscriptions, credit packs, paid upgrades, or purchase options. Each signed-in account may complete up to three successful video jobs during a 24-hour allowance window that starts with the first successful job; failed jobs do not count, and the full allowance resets when the window ends. Each input may be up to 60 seconds.

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

1. Free summary wording. AI recommendation: replace `3m per period` with `Up to 3 videos per 24-hour period` and add `Up to 60 seconds per video` as secondary text.
2. Remaining action on the free summary card. AI recommendation: remove `See plans` without adding another button; keep the account page focused on allowance status. If a CTA is desired later, use a separate approved navigation or tool-entry decision rather than silently repurposing the paid button.
3. `No charge` label. AI recommendation: retain it if it fits the compact summary because it accurately describes the current state, but remove it if the redesigned card communicates free access clearly without it.

Until these presentation decisions are confirmed, this recommendation is not executable.

## Final decision

The user has confirmed deletion of all paid-related content from the authenticated account page. The final free-summary wording, remaining action, and treatment of `No charge` are pending.

## Implementation prompt

```text
NOT EXECUTABLE. BGV-0011 has status needs_decision. Wait for the user to confirm the free-summary wording, whether the remaining card has any action, and whether `No charge` stays.
```

## Acceptance criteria

- Provisional: `/app/account/` contains no `See plans` button, paid-plan availability message, Creator or Studio paid card, price, paid allowance, paid resolution promise, or `Get notified` control.
- Provisional: no other current-product paid plan, subscription, upgrade, credit-pack, checkout, pricing, or paid waitlist marketing remains anywhere in the rendered English account page.
- Provisional: removed content leaves no empty card, layout column, divider, click target, keyboard focus stop, accessible label, modal trigger, or off-screen text.
- Provisional: the account page retains a clear, accurate free-allowance summary based on real existing allowance data.
- Provisional: the summary does not describe the allowance as `3m per period`; it follows the final approved job-based wording and duration detail.
- Provisional: an active reset date/time comes from the real allowance state, and an account with no started window is not shown a fabricated reset.
- Provisional: the page makes no `free forever`, permanent-pricing, or other absolute promise that restricts future monetization.
- Provisional: the account page has no broken spacing or horizontal overflow after removal at desktop and 320px, 360px, 390px, and 430px CSS viewport widths.
- Provisional: authentication, profile/security controls, sign-out, job history, downloads, and other unrelated account behavior continue to work.
- Provisional: the actual allowance, counting, reset, duration, and retention behavior are unchanged.
- Provisional: historical transactions, invoices, provider records, legally required records, and dormant billing infrastructure are not deleted.
- Provisional: verification is performed in the actual signed-in production account page after publication, not inferred from a source repository or implementation report.

## Out of scope

- Introducing replacement paid plans, prices, subscriptions, credit packs, checkout, billing portals, or waitlists.
- Changing the public `/pricing/` URL or other public-page copy already governed by separate recommendations.
- Changing authentication, allowance enforcement, processing, retention, or video output behavior.
- Deleting historical billing, transaction, invoice, customer, payment-provider, or legally required records.
- Spanish, Portuguese, French, or German account-page changes until the user separately authorizes localization.
