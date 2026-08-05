# BGRemove confirmed decisions

Only currently active decisions explicitly confirmed by the user belong above the superseded-history section.

## Current free strategy

- Confirmed 2026-08-05: BGRemove is temporarily positioned and operated as a completely free product.
- Confirmed 2026-08-05: Sign-in is required to use the free allowance.
- Confirmed 2026-08-05: The first successful processing job starts a 24-hour allowance window. Up to three successful jobs may complete within that window; failed jobs do not count. At the end of the window, the full allowance resets to three.
- Confirmed 2026-08-05: There are no paid plans, subscriptions, one-time credit packs, paid upgrades, or other purchase options during this phase.
- Confirmed 2026-08-05: The purpose of the free phase is to improve useful engagement, repeat visits, trust, and SEO authority before monetization is introduced later.
- Because monetization may return later, public copy must describe the current state without promises such as “free forever,” “no card ever,” “we will never charge,” or “no plans to add.”

## Product positioning

- BGRemove is a professional, purpose-built video-background-removal tool for creators and editors.
- Its value should be expressed through concrete workflow benefits such as temporal consistency, stable edges, transparent output, reusable assets, and compatibility with editing and compositing workflows.
- Public copy must not describe the product as small, boring, low-value, a demo, merely a test, or a tool with no intention to grow.
- Public copy must not unnecessarily restrict future background, editing, refinement, output, workflow, or integration capabilities.

## Product

- The product removes video backgrounds and exports transparent video for use in editing and compositing workflows.
- Maximum input duration is 60 seconds.
- There is no separate product-enforced file-size limit.
- Accepted input formats are MP4, MOV, WebM, M4V, and GIF.
- Output preserves the source video's dimensions.
- Transparent output uses only `webm_vp9`, presented publicly as transparent WebM using VP9 with alpha.
- Output has no watermark.
- Source uploads and generated transparent outputs are retained for 24 hours.
- Custom background replacement is not currently available.
- Batch upload/processing, manual or second-pass edge refinement, API, and webhooks are not currently available.

## Public content handling

- Keep `/pricing/` and relabel its English purpose as `Free Access`.
- Keep `/legal/refunds/` as a no-current-payments notice and remove its footer link.
- Delete previous paid-product entries from the public changelog while preserving unrelated release history and non-public records.
- Remove or hide public purchase, subscription, credit-pack, upgrade, and checkout entry points. Do not delete historical billing data or payment-provider records under BGV-0008.
- English copy is approved for implementation. Spanish, Portuguese, French, and German must wait for separate user authorization.
- English legal copy should be drafted from real code and data flows and marked for human legal review before merge.

## Markets and languages

- Current languages: English, Spanish, Portuguese, French, and German.
- Japanese and Korean are deferred until the existing site and current locales are optimized.

## Recommendation workflow

- The recommendation AI outputs prompts and does not modify the website.
- The code execution AI may execute only recommendations with `status: "approved"`.

## Superseded decisions

- All pricing, subscription, credit-pack, paid-tier, paid-feature, paid-retention, and paid-format decisions confirmed from 2026-07-31 through 2026-08-01 were superseded by the free strategy on 2026-08-05.
- BGV-0001 through BGV-0007 are retained only as history and must not be used as current implementation instructions.
