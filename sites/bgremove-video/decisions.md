# BGRemove confirmed decisions

Only decisions explicitly confirmed by the user belong here.

## Product

- The product removes video backgrounds, exports transparent video, and can replace the background with a custom image.

## Credits

- Confirmed 2026-07-31: Purchased one-time credits never expire and remain available until used.
- Confirmed 2026-07-31: The 5 credits granted once at registration never expire and remain available until used.
- Confirmed 2026-08-01: Registration, subscription, and purchased credit balances can coexist, but their sources remain separately traceable.
- Confirmed 2026-08-01: While a subscription is active, consume subscription credits first, registration credits second, and purchased credits last.
- Confirmed 2026-08-01: Monthly and annual plans grant credits monthly; annual plans do not grant the full year upfront.
- Confirmed 2026-08-01: Subscription credits roll over and accumulate without expiry or a cap while the subscription remains active.
- Confirmed 2026-08-01: A cancellation takes effect only after the final paid period; then unused subscription-derived credits are frozen rather than deleted.
- Confirmed 2026-08-01: Starting any monthly or annual subscription plan unfreezes all previously frozen subscription credits.
- Confirmed 2026-08-01: Registration and purchased credits remain usable while subscription-derived credits are frozen.
- Confirmed 2026-08-01: A failed renewal grants no new credits; existing balances remain usable only through the current paid-through timestamp.
- Confirmed 2026-08-01: If payment is still unsuccessful at the paid-through timestamp, freeze unused subscription-derived credits. A later successful retry or new subscription unfreezes them without duplicating a period grant.

## Legacy pricing

- Confirmed 2026-08-01: There are no active paid Creator or Studio subscribers.
- No legacy-plan migration or grandfathering is required when replacing the old pricing, but historical orders, invoices, and billing records must be preserved.

## Background replacement entitlement

- Confirmed 2026-08-01: Registration credits support background removal only; free-only users cannot use custom background replacement.
- Confirmed 2026-08-01: One-time pack and subscription customers can use both background removal and custom background replacement.
- Confirmed 2026-08-01: Charge video duration once for a completed background-processing job. Changing backgrounds or re-exporting a retained result does not consume more credits.
- Confirmed 2026-08-01: After a free-only user completes a paid pack or subscription purchase, background replacement can be unlocked for a retained free-processed result without charging the removal duration again.

## Paid feature parity

- Confirmed 2026-08-01: Every paid pack and subscription customer receives the same product capabilities; paid offers differ only by price, credit allowance, and effective unit cost.
- Confirmed 2026-08-01: Features including 4K output, refined edge processing, batch upload, API/webhooks, priority processing, transparent output, and custom background replacement are available to every paid user.

## Transparent output formats

- Confirmed 2026-08-01: Transparent-background output supports only these exact internal format identifiers: `webm_vp9`, `mov_proresks`, and `mkv_vp9`.
- Other format values must not be offered for transparent-background output.
- Confirmed 2026-08-01: Free users can select only `webm_vp9` for transparent-background output.
- Confirmed 2026-08-01: Every paid user can select `webm_vp9`, `mov_proresks`, and `mkv_vp9`.

## File retention

- Confirmed 2026-08-01: A processing task funded only by registration credits is retained for 24 hours from successful completion.
- Confirmed 2026-08-01: A task using any subscription or purchased one-time credits is retained for 7 days from successful completion.
- Source uploads and retained derivatives share the same fixed expiry. Re-exporting, changing backgrounds, cancellation, or paying later does not extend it.
- Media expiry or user deletion removes media files but preserves credit-ledger entries, invoices, payment records, and necessary non-media audit history.

## Markets and languages

- Current languages: English, Spanish, Portuguese, French, and German.
- Japanese and Korean are deferred until the existing site and current locales are optimized.

## Recommendation workflow

- The recommendation AI outputs prompts and does not modify the website.
- The code execution AI may execute only recommendations with `status: "approved"`.
