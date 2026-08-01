---
task_id: "BGV-0006"
site_id: "bgremove-video"
title: "Replace pricing with free credits, subscriptions, and packs"
status: "needs_decision"
priority: "P1"
source: "user+ai"
created_at: "2026-07-31"
updated_at: "2026-08-01"
prompt_version: 5
---

# BGV-0006 — Replace pricing with free credits, subscriptions, and packs

## Scope

Pricing, free-credit copy, FAQ, account and billing UI, checkout, payment webhooks, credit ledger, metadata, structured data, and current locales.

## Current facts and evidence

On 2026-07-31, the public pricing page still advertised recurring daily free usage, Creator at $19/month, Studio at $49/month, and “No export credits to top up.” These conflict with the proposed model.

The user confirmed on 2026-08-01 that there are no active paid Creator or Studio subscribers.

## User proposal

- Use free credits, two subscriptions, and three one-time credit packs.
- Give each newly registered user 5 credits once, allowing 5 seconds of processed video.
- One-time packs:
  - Starter: $8, 150 credits, 2.5 minutes.
  - Creator: $25, 600 credits, 10 minutes, marked Most popular.
  - Pro: $59, 1,800 credits, 30 minutes.
- Subscriptions:
  - Plus: $9.99/month or $49.99/year, 350 credits/month.
  - Pro: $24.99/month or $124.99/year, 1,200 credits/month.
- Support monthly and annual billing.
- Allow free, subscription, and one-time credit balances to coexist in one account while keeping their sources separately traceable.
- Let subscription credits accumulate without expiry while the subscription remains active.
- When a cancellation takes effect at the end of the paid period, freeze unused subscription credits instead of deleting them.
- Reactivating any monthly or annual subscription plan unlocks all previously frozen subscription credits.

## AI recommendation

- Use one shared rule: 1 credit equals 1 second of processed source video.
- Say “Save more than 50%” for annual billing; the proposed annual prices save about 58% versus twelve monthly payments.
- Store prices and credit allowances in one configuration source shared by all locales.
- Remove contradictory old pricing from metadata, FAQ, JSON-LD, account UI, checkout, and other public pages.
- Preserve failure refunds and enforce idempotent payment webhooks.
- Keep legacy subscribers safe until a migration policy is confirmed.
- Display available and frozen balances separately; keep credit-source ledgers distinct for refunds, cancellation, and auditability.

## Open decisions

1. Do the free credits cover both background removal and background replacement across all supported output modes?
2. How do resolution, retention, batch upload, ProRes, and API access map to Plus and Pro?

## Final decision

Confirmed on 2026-07-31:

- Purchased one-time credits never expire and remain available until used.
- The 5 registration credits never expire and remain available until used.

Confirmed on 2026-08-01:

- Registration, subscription, and one-time purchased credits can coexist in one account, but their sources remain separately recorded.
- While a subscription is active, deduct subscription credits first, registration credits second, and purchased one-time credits last.
- Monthly and annual subscriptions add their plan allowance monthly; annual plans do not grant the full annual allowance upfront.
- Subscription credits roll over and accumulate without a cap while the subscription remains active.
- A scheduled cancellation does not change access during the already-paid period.
- When the final paid subscription period ends, freeze all unused subscription-derived credits; do not delete or expire them.
- Starting any monthly or annual subscription plan unfreezes all previously accumulated subscription credits.
- Switching plans or billing cycles without an inactive gap does not freeze credits.
- Registration and purchased one-time credits remain usable when subscription-derived credits are frozen.
- If a renewal payment fails, do not issue a new period's credits. Existing credits remain usable only through the already-paid entitlement period.
- At the paid-through timestamp, freeze unused subscription-derived credits if renewal has not succeeded. A later successful payment or new subscription unfreezes them without duplicating the period's credit grant.
- There are no active paid Creator or Studio subscribers, so no legacy-plan migration or grandfathering is required. Preserve historical orders and billing records.

The remaining open decisions still require user confirmation. This task must not be executed yet.

## Implementation prompt

```text
DRAFT — DO NOT EXECUTE UNTIL THIS RECOMMENDATION HAS status: "approved".

Inspect the existing BGRemove pricing configuration, credit ledger, account UI, checkout flow, Lemon Squeezy integration, webhooks, metadata, FAQ, JSON-LD, locales, tests, and fixtures before changing code. Do not invent product IDs, Variant IDs, environment variables, migration rules, expiry rules, or entitlements.

Confirmed proposed values:
- 1 credit = 1 second of processed source video.
- New users receive 5 credits once; the free allowance never renews.
- Registration credits and purchased one-time credits never expire; they remain available until used.
- Keep registration, subscription, and purchased credit buckets separately traceable while displaying a combined available balance.
- Monthly and annual plans grant their allowance monthly. Annual plans do not grant twelve months of credits upfront.
- Active subscription credits roll over and accumulate indefinitely without a cap.
- Consume credits in this order while a subscription is active: subscription credits, registration credits, purchased one-time credits.
- A scheduled cancellation leaves all credits usable through the final paid period. When that period ends, freeze only the remaining subscription-derived credits.
- Frozen subscription credits are retained but unavailable. Starting any monthly or annual subscription plan immediately unfreezes the full frozen subscription balance.
- Registration and one-time purchased credits remain usable even when subscription credits are frozen.
- A failed renewal never grants new credits. Continue access only until the existing paid-through timestamp, then freeze unused subscription-derived credits if payment is still unsuccessful.
- A later successful retry or new subscription unfreezes the frozen subscription balance and resumes grants without issuing the same period twice.
- The user confirmed there are no active paid Creator or Studio subscribers. Replace the old purchase paths without building a legacy-plan migration flow, but preserve all historical orders, invoices, and audit records. If implementation evidence reveals an active legacy subscription, stop and report the conflict instead of changing it.
- Starter pack: $8 / 150 credits / 2m30s / $3.20 per minute.
- Creator pack: $25 / 600 credits / 10m / $2.50 per minute / Most popular.
- Pro pack: $59 / 1,800 credits / 30m / $1.97 per minute.
- Plus monthly: $9.99 / 350 credits per month / about 5m50s / $1.71 per minute.
- Plus annual: $49.99 per year, granting 350 credits each subscription month.
- Pro monthly: $24.99 / 1,200 credits per month / 20m / $1.25 per minute.
- Pro annual: $124.99 per year, granting 1,200 credits each subscription month.

Keep the current BGRemove visual system. Structure the pricing page as hero, free plan, one-time packs, annual-savings message, Plus/Pro subscriptions with Monthly/Yearly control, shared features, billing FAQ, and final CTA.

Remove every contradictory reference to daily free clips, 24-hour free resets, Creator $19/month, Studio $49/month, and “No export credits to top up.” Synchronize visible copy, metadata, Open Graph/Twitter metadata, FAQPage JSON-LD, account and balance UI, checkout parameters, payment webhooks, API responses, tests, fixtures, and English, Spanish, Portuguese, French, and German. Do not add Japanese or Korean.

Before implementation, replace every pending rule in this prompt with the final approved decision. If any pending rule remains, stop and report the blocker.

Make payment webhook handling idempotent. Failed processing must not permanently consume credits. Do not delete historical billing records. Do not deploy or create live payment products unless separately authorized.

After implementation, report the old implementation locations, changed files, plan mapping, manual payment configuration, legacy-user risks, checks run, and any remaining old-pricing search matches.
```

## Acceptance criteria

- Prices, credits, time conversions, checkout parameters, and displayed copy agree.
- Free credits are granted once and never refresh.
- Registration credits and purchased one-time credits do not expire.
- Credit sources remain separately traceable and use the confirmed deduction order.
- Subscription credits accrue monthly, roll over without a cap, and never expire while the subscription is active.
- Ending the final paid period freezes only subscription-derived credits; registration and purchased credits remain available.
- Reactivating any subscription plan restores the full frozen subscription balance exactly once.
- Failed renewals grant no new credits; freeze occurs at the existing paid-through timestamp, and later recovery must not duplicate grants.
- Public copy, metadata, structured data, billing UI, and backend use the same rules.
- Webhook retries cannot duplicate credits and failed jobs do not permanently charge credits.
- Old Creator and Studio purchase paths are removed or disabled without deleting historical billing records.
- If any active legacy subscription is discovered, implementation stops without modifying that subscription.
- Five current locales remain consistent; Japanese and Korean are not added.
- Relevant tests, type checks, and build checks pass.

## Out of scope

- Creating live payment products or Variant IDs.
- Migrating existing subscribers before approval.
- Production deployment.
