---
task_id: "BGV-0011"
site_id: "bgremove-video"
title: "Remove paid-plan content from the authenticated account page"
status: "approved"
priority: "P1"
source: "user+ai"
created_at: "2026-08-09"
updated_at: "2026-08-09"
prompt_version: 2
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
Implement BGV-0011 in BGRemove's current production-connected environment and publish only this approved scope after checks pass. Do not modify this recommendation repository or create an execution-result file.

Target the authenticated English account page at `/app/account/` only.

1. Remove paid-plan content and controls
- Remove the entire `See plans` button, including its route action, modal trigger, event handler, accessible label, focus stop, and reserved layout space. Do not add a replacement button.
- Remove the message beginning `Paid plans are not open for sign-up yet`.
- Remove the complete Creator and Studio paid-plan cards, including `$19`, `$49`, paid allowances, resolution promises, descriptions, `Get notified` buttons, and any notification form or modal reachable only from these controls.
- Inspect the rest of the rendered English account page and remove any other current-product paid plan, price, subscription, upgrade, credit-pack, checkout, paid waitlist, or billing-marketing block.
- Remove account-page links into current plan-selection or purchase flows. Do not create replacement paid CTAs.
- Remove these elements from rendering and interaction; do not merely hide them with CSS or leave empty cards, columns, dividers, off-screen text, click targets, or keyboard focus stops.

2. Keep an accurate free-allowance summary
- Retain a compact summary identifying the current access as `Free` and retain the current-state label `No charge`.
- Replace `3m per period` with the exact primary allowance text `Up to 3 videos per 24-hour period`.
- Add the secondary text `Up to 60 seconds per video`.
- Continue to render allowance state from the existing authoritative account/quota data. Do not implement a separate client-side allowance calculation.
- When the 24-hour window is active, show the real next full-reset date and time in an understandable format.
- When no window has started, do not fabricate a reset timestamp. Keep a truthful existing empty state or explain that the 24-hour window starts with the first successful video.
- Do not add `Free forever`, `We will never charge`, or any other permanent monetization promise.
- Tighten the page layout after removal so there are no large empty sections, empty borders, broken dividers, unnecessary scrolling, or mobile overflow.

3. Preserve unrelated behavior and data
- Do not change authentication, profile or security controls, sign-out, job history, downloads, allowance enforcement, successful-job counting, failed-job treatment, reset behavior, duration validation, retention, processing, or output behavior.
- Do not delete historical transactions, invoices, payment-provider records, customer data, legally required records, or dormant billing infrastructure.
- Do not change the public `/pricing/` page or Spanish, Portuguese, French, or German account-page content under this task.

4. Checks and publication
- Verify signed-in account states with no started allowance window, an active window, and an exhausted allowance where those states can be safely reproduced with existing test data. Confirm every value comes from real account state.
- Check desktop and 320px, 360px, 390px, and 430px CSS viewport widths. Confirm no removed paid element remains in visible content, keyboard navigation, accessibility output, or reserved layout space.
- Confirm unrelated account controls and navigation still work.
- After the relevant checks pass, publish this exact scope through the existing direct-to-production workflow.
```

## Acceptance criteria

- `/app/account/` contains no `See plans` button, paid-plan availability message, Creator or Studio paid card, price, paid allowance, paid resolution promise, or `Get notified` control.
- No other current-product paid plan, subscription, upgrade, credit-pack, checkout, pricing, or paid waitlist marketing remains anywhere in the rendered English account page.
- Removed content leaves no empty card, layout column, divider, click target, keyboard focus stop, accessible label, modal trigger, or off-screen text.
- The account page retains `Free`, `No charge`, the exact allowance text `Up to 3 videos per 24-hour period`, and the secondary text `Up to 60 seconds per video`.
- The free-allowance summary is based on real existing allowance data and does not display `3m per period`.
- An active reset date/time comes from the real allowance state, and an account with no started window is not shown a fabricated reset.
- The page makes no `free forever`, permanent-pricing, or other absolute promise that restricts future monetization.
- The account page has no broken spacing or horizontal overflow after removal at desktop and 320px, 360px, 390px, and 430px CSS viewport widths.
- Authentication, profile/security controls, sign-out, job history, downloads, and other unrelated account behavior continue to work.
- The actual allowance, counting, failed-job treatment, reset, duration, and retention behavior are unchanged.
- Historical transactions, invoices, provider records, legally required records, and dormant billing infrastructure are not deleted.
- Spanish, Portuguese, French, and German account-page content is unchanged.
- Verification is performed in the actual signed-in production account page after publication, not inferred from a source repository or implementation report.

## Out of scope

- Introducing replacement paid plans, prices, subscriptions, credit packs, checkout, billing portals, or waitlists.
- Changing the public `/pricing/` URL or other public-page copy already governed by separate recommendations.
- Changing authentication, allowance enforcement, processing, retention, or video output behavior.
- Deleting historical billing, transaction, invoice, customer, payment-provider, or legally required records.
- Spanish, Portuguese, French, or German account-page changes until the user separately authorizes localization.
