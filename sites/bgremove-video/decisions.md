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
- Confirmed 2026-08-07: English marketing copy should be confident, outcome-led, and desire-generating rather than restrained or overly rational.
- Lead with the reusable transparent result and professional workflow value; present free access as the final risk-reversal rather than the product's only value.
- Headlines may be bold, but body copy must substantiate them with confirmed capabilities and must not invent proof, performance, quality, or compatibility claims.
- The homepage H1 is locked exactly as `Remove video background online. Free, no watermark.` All other English marketing copy may change within approved product facts and scope.
- Confirmed 2026-08-09: Apply the BGV-0009 readability pass across all 15 primary English marketing pages while preserving the locked homepage title/H1, current page H1s, approved CTAs, product facts, and marketing-forward voice.
- Lead with plain-language results and benefits. Keep concise professional terminology as secondary detail and explain it at first meaningful use; `/how-it-works/` should retain short technical labels beneath plain-language explanations.
- Keep historical Changelog dates, versions, titles, and historical status, but shorten obsolete entries in place to one plain-language summary and remove detailed old allowances, resolution tiers, output formats, and internal cost explanations. Do not add a collapse interaction.

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
- Confirmed 2026-08-08: The three remaining English legal-page changes under BGV-0008 do not require human legal review. The programming AI may draft and directly publish them after verifying current code, data flows, retention behavior, and approved product rules. It must not invent legal obligations or data practices.

## Authenticated account handling

- Confirmed 2026-08-09: Remove paid-plan marketing and entry points from the English authenticated `/app/account/` page, including `See plans`, paid-plan availability messaging, Creator and Studio prices or plan cards, and `Get notified` controls. Preserve historical billing and legally required records; presentation details for the remaining free-allowance summary are governed by BGV-0011.

## Markets and languages

- Current languages: English, Spanish, Portuguese, French, and German.
- Japanese and Korean are deferred until the existing site and current locales are optimized.

## Recommendation workflow

- The recommendation AI outputs prompts and does not modify the website.
- The code execution AI may execute only recommendations with `status: "approved"`.
- Confirmed 2026-08-07: The programming AI publishes approved BGRemove changes directly through its existing production-connected environment and does not write a result file, Pull Request, Commit link, or other execution feedback to this repository.
- Confirmed 2026-08-07: The public production site at `https://bgremove.video/` is the only source of truth for website audits and implementation verification.
- Do not inspect or use `DAOteam/bgremove` to infer current online copy, implementation status, or reasons that a public page has or has not changed.
- Do not infer production status from recommendation files, result files, commits, branches, or Pull Requests. Verify the relevant public URL directly.
- At every new audit, compare each item in the latest approved recommendation with the live site. Exclude verified items from the next execution scope; carry unimplemented items and the unresolved portion of partially implemented items into the next version.
- Keep the same task ID for this continuing scope and increment `prompt_version` after each live re-audit. Mark it `verified` only after every acceptance criterion is confirmed on the public site.
- The recommendation AI remains read-only toward the website and is not authorized to publish.

## Superseded decisions

- All pricing, subscription, credit-pack, paid-tier, paid-feature, paid-retention, and paid-format decisions confirmed from 2026-07-31 through 2026-08-01 were superseded by the free strategy on 2026-08-05.
- BGV-0001 through BGV-0007 are retained only as history and must not be used as current implementation instructions.
