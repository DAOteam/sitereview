---
task_id: "BGV-0006"
site_id: "bgremove-video"
title: "Replace pricing with free credits, subscriptions, and packs"
status: "needs_decision"
priority: "P1"
source: "user+ai"
created_at: "2026-07-31"
updated_at: "2026-07-31"
prompt_version: 1
---

# BGV-0006 — Replace pricing with free credits, subscriptions, and packs

## Scope

Pricing, free-credit copy, FAQ, account and billing UI, checkout, payment webhooks, credit ledger, metadata, structured data, and current locales.

## Current facts and evidence

On 2026-07-31, the public pricing page still advertised recurring daily free usage, Creator at $19/month, Studio at $49/month, and “No export credits to top up.” These conflict with the proposed model.

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

## AI recommendation

- Use one shared rule: 1 credit equals 1 second of processed source video.
- Say “Save more than 50%” for annual billing; the proposed annual prices save about 58% versus twelve monthly payments.
- Store prices and credit allowances in one configuration source shared by all locales.
- Remove contradictory old pricing from metadata, FAQ, JSON-LD, account UI, checkout, and other public pages.
- Preserve failure refunds and enforce idempotent payment webhooks.
- Keep legacy subscribers safe until a migration policy is confirmed.

## Open decisions

1. Do one-time credits expire?
2. Can credit sources stack, and what is the consumption order?
3. Does an annual subscription grant credits monthly or grant the full year upfront? AI recommends monthly grants.
4. Do subscription credits roll over?
5. Do legacy Creator/Studio subscribers keep their existing plan or migrate?
6. Do the free credits cover both background removal and background replacement across all supported output modes?
7. How do resolution, retention, batch upload, ProRes, and API access map to Plus and Pro?

## Final decision

Pending user confirmation. This task must not be executed yet.

## Implementation prompt

```text
DRAFT — DO NOT EXECUTE UNTIL THIS RECOMMENDATION HAS status: "approved".

Inspect the existing BGRemove pricing configuration, credit ledger, account UI, checkout flow, Lemon Squeezy integration, webhooks, metadata, FAQ, JSON-LD, locales, tests, and fixtures before changing code. Do not invent product IDs, Variant IDs, environment variables, migration rules, expiry rules, or entitlements.

Confirmed proposed values:
- 1 credit = 1 second of processed source video.
- New users receive 5 credits once; the free allowance never renews.
- Starter pack: $8 / 150 credits / 2m30s / $3.20 per minute.
- Creator pack: $25 / 600 credits / 10m / $2.50 per minute / Most popular.
- Pro pack: $59 / 1,800 credits / 30m / $1.97 per minute.
- Plus monthly: $9.99 / 350 credits per month / about 5m50s / $1.71 per minute.
- Plus annual: $49.99 per year; grant timing remains pending.
- Pro monthly: $24.99 / 1,200 credits per month / 20m / $1.25 per minute.
- Pro annual: $124.99 per year; grant timing remains pending.

Keep the current BGRemove visual system. Structure the pricing page as hero, free plan, one-time packs, annual-savings message, Plus/Pro subscriptions with Monthly/Yearly control, shared features, billing FAQ, and final CTA.

Remove every contradictory reference to daily free clips, 24-hour free resets, Creator $19/month, Studio $49/month, and “No export credits to top up.” Synchronize visible copy, metadata, Open Graph/Twitter metadata, FAQPage JSON-LD, account and balance UI, checkout parameters, payment webhooks, API responses, tests, fixtures, and English, Spanish, Portuguese, French, and German. Do not add Japanese or Korean.

Before implementation, replace every pending rule in this prompt with the final approved decision. If any pending rule remains, stop and report the blocker.

Do not migrate or cancel legacy subscribers without an approved migration policy. Make payment webhook handling idempotent. Failed processing must not permanently consume credits. Do not deploy or create live payment products unless separately authorized.

After implementation, report the old implementation locations, changed files, plan mapping, manual payment configuration, legacy-user risks, checks run, and any remaining old-pricing search matches.
```

## Acceptance criteria

- Prices, credits, time conversions, checkout parameters, and displayed copy agree.
- Free credits are granted once and never refresh.
- Public copy, metadata, structured data, billing UI, and backend use the same rules.
- Webhook retries cannot duplicate credits and failed jobs do not permanently charge credits.
- Existing customers keep access and balances until an approved migration handles them.
- Five current locales remain consistent; Japanese and Korean are not added.
- Relevant tests, type checks, and build checks pass.

## Out of scope

- Creating live payment products or Variant IDs.
- Migrating existing subscribers before approval.
- Production deployment.
