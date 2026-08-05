---
task_id: "BGV-0008"
site_id: "bgremove-video"
title: "Align the English public site with free professional positioning"
status: "approved"
priority: "P0"
source: "user+ai"
created_at: "2026-08-05"
updated_at: "2026-08-05"
prompt_version: 2
---

# BGV-0008 — Align the English public site with free professional positioning

## Scope

The 20 English public URLs in the 2026-08-05 sitemap, plus English navigation, footer, calls to action, metadata, Open Graph/Twitter fields when derived from SEO metadata, FAQ/HowTo/WebApplication structured data, and the five English legal pages. Spanish, Portuguese, German, and French are explicitly deferred until the user approves a later localization task.

This is primarily a public-copy alignment task. It also authorizes removing or hiding public purchase, subscription, credit-pack, upgrade, and checkout entry points so users cannot reach a paid offer. It does not authorize changing processing entitlements, deleting billing records, deleting payment-provider products, modifying databases, or deploying.

## Current facts and evidence

Public crawl performed on 2026-08-05 after the user reported that part of the free-positioning update was already online:

- The English homepage title is already `Remove Video Background Online Free - No Watermark` and the `/pricing/` page already says the product is free.
- Shared navigation and footer still label `/pricing/` as `Pricing` across all current locales, and the English footer still links to `Refunds`.
- Homepage visible FAQ and FAQPage JSON-LD still say paid plans provide longer footage, higher resolution, batch uploads, API access, ProRes, matte-only files, and PNG sequences.
- `/faq/` still contains Creator/Studio tiers, paid clip limits, paid retention, Lemon Squeezy, cancellation, purchase, and refund copy in visible HTML and JSON-LD.
- `/about/` still says `A narrow tool, built on purpose`, `does one job`, `no plans to grow any`, `the boring middle`, and `There is nothing clever about the product`, and it includes a paid-plan economics section.
- `/pricing/` says `Paid plans are designed but not open`, `Unlimited days, no card ever`, and frames the product mainly as a way to test whether a matte works rather than as a useful recurring production tool.
- `/contact/` metadata and support categories still mention billing, invoices, and refunds.
- `/how-it-works/` and tool pages still assign formats, resolution, duration, batch, and API capabilities to Creator and Studio tiers.
- `/tools/product-video-background-remover/`, `/tools/remove-background-from-video/`, `/tools/tiktok-background-remover/`, and `/use-cases/agencies/` contain old Studio/Creator or paid-plan claims.
- `/use-cases/agencies/` says the output is `a first pass, not a finish`, weakening the professional value proposition.
- The changelog still contains historical paid-plan releases. These are history rather than current offers, but the page does not clearly mark those entries as obsolete.
- The English Privacy, Refund, Terms, and Acceptable Use pages still describe subscriptions, Lemon Squeezy, payments, refunds, paid retention, and plan limits.
- Spanish, Portuguese, German, and French reproduce the same old plan, payment, Creator, Studio, refund, duration, retention, format, batch, and API language. The old claims appear in both visible content and localized structured data.
- No execution result exists for the former paid-model task BGV-0006. BGV-0001 through BGV-0007 were marked `superseded` before this audit continued.

This crawl verifies public copy, not authenticated workspace behavior. No GSC, analytics, ranking, CTR, or engagement claim is made.

## User proposal

- Temporarily make and position BGRemove as completely free.
- Give each signed-in user three successful video-processing jobs in a 24-hour allowance window that starts with the first successful use. Reset the full allowance to three when that window ends; failed jobs do not consume an allowance.
- Use the free phase to improve useful engagement, return visits, and SEO authority before introducing monetization later.
- Remove copy that contradicts the free strategy or professional video-background-removal positioning.
- Upgrade low-value language and remove narrow or absolute claims that restrict future development.
- Provide replacement copy rather than modifying the website directly.
- Clear the prior recommendation backlog and create new recommendations from this strategy.

## AI recommendation

Use one precise promise across the site:

> BGRemove is currently free to use. Sign in to process up to three videos during a 24-hour allowance window, starting with your first successful video. When the window ends, all three uses reset. Downloads are watermark-free, with no subscription, credit pack, or paid upgrade.

Do not use `free forever`, `no card ever`, `we will never charge`, `no plans to grow`, or similar permanent promises. The business intends to monetize later, so describe the current state with words such as `currently`, `today`, and `right now` only where needed for accuracy.

Position BGRemove as purpose-built and professional, not narrow or small. Support that position with concrete value: temporal consistency across frames, stable edges through motion, a real alpha channel, reusable transparent output, and fit with established editing/compositing workflows.

Keep `/pricing/` temporarily to avoid an unnecessary URL migration, but relabel it `Free Access` in navigation and rewrite it as the canonical explanation of the current free allowance. Do not create a new route in this task.

Delete previous paid-plan launch entries from the public changelog, as explicitly directed by the user. Do not delete operational records, invoices, payment records, or source-control history.

Treat legal pages as fact-sensitive. Draft replacements are included below, but any Terms, Privacy, Acceptable Use, or refund-related change requires a human legal review before publication.

### Finding categories

| Audit requirement | Confirmed examples | Primary affected surfaces |
|---|---|---|
| Conflicts with completely-free positioning | Paid plans, Creator/Studio, Lemon Squeezy, billing, cancellation, refunds, paid retention, paid formats | Homepage FAQ, FAQ, About, Contact, How it works, pricing, tool pages, legal pages, JSON-LD, all five locales |
| Conflicts with professional-tool positioning | `does one thing`, `a first pass, not a finish`, presenting the daily allowance mainly as a product test | Homepage, About, FAQ, agency use case, pricing |
| Low perceived value | `boring middle`, `nothing clever about the product`, `small independent team`, `try it on your worst clip` | About and shared conversion sections |
| Too narrow or absolute for future development | `no plans to grow`, `deliberately no background library`, dismissing all controls, `free forever`, `no card ever`, `almost certainly` | About, homepage FAQ, FAQ, pricing, How it works |

### Approved replacement copy

The user approved the following English copy direction on 2026-08-05. Do not localize it in this task; Spanish, Portuguese, German, and French will be handled only after the user approves a separate follow-up.

#### Shared navigation, footer, and CTA

| Current | Replace with |
|---|---|
| `Pricing` | `Free Access` |
| Footer link `Refunds` | Remove from the footer while no payment option exists. Keep the legal URL only if needed for an accurate no-payments notice. |
| `Start free` | `Remove a Video Background` |
| `Free clips every day. No watermark, no card.` | `3 free video background removals per 24-hour allowance window. No watermark, no card.` |
| Generic secondary CTA `Pricing` | `See Free Access` |

#### Homepage `/`

Keep the approved title and H1:

- Title: `Remove Video Background Online Free - No Watermark`
- H1: `Remove video background online. Free, no watermark.`

Replace:

| Element/current copy | Proposed replacement |
|---|---|
| Meta description | `Remove video backgrounds online free with AI. Process up to 3 videos per 24-hour allowance window and export transparent WebM video with no watermark.` |
| Hero supporting line | `AI video matting preserves motion and edge detail, then returns transparent video with a real alpha channel for your editing workflow.` |
| `Free tier included` | `3 free videos per 24-hour window` |
| `Free clips every day, forever...` | `Your first successful video starts a 24-hour allowance window. Process up to 3 videos during that window at no cost; when it ends, all 3 uses reset.` |
| Free FAQ answer mentioning paid plans | `Yes. BGRemove currently has no paid plans, subscriptions, credit packs, or paid upgrades. Sign in to process up to 3 videos per 24-hour allowance window and download without a watermark.` |
| Format FAQ answer with paid tiers | `BGRemove exports transparent WebM video using VP9 with a real alpha channel. This output is available to every signed-in user at no cost.` |
| `This does one thing...` comparison answer | `Canva and Adobe are broad design suites. BGRemove is purpose-built for video background removal, using temporal context across frames to keep edges more stable through motion and returning reusable transparent video for the editor you already use.` |
| Limitations paragraph ending `before you pay for anything` | `Hair, motion blur, and rim light are demanding edge cases that BGRemove is designed to handle. Glass, heavy overlap, and very dark footage remain challenging, so review those results carefully in your editing workflow.` |
| Sign-in answer with vague allowance | `An account keeps jobs associated with you, supports access across devices, and makes the 3-video allowance reliable. Your first successful video starts the 24-hour window; failed jobs do not count.` |
| `There is deliberately no background library here...` | `The transparent result can be placed over colors, images, or footage in your editor and reused across multiple versions instead of baking one background into the file.` |
| `Try it on your worst clip.` | `Test it on real footage.` |
| `today’s free one costs you nothing` | `Use one of your 3 free videos on footage with real motion, hair, or a busy background and judge the transparent result in your own workflow.` |

Apply the same answers to visible FAQ and FAQPage JSON-LD.

#### Free-access page `/pricing/`

| Element/current copy | Proposed replacement |
|---|---|
| Title | `Free Video Background Remover – 3 Videos per 24 Hours | BGRemove` |
| Meta description | `BGRemove is free to use. Remove backgrounds from up to 3 videos per 24-hour allowance window with no watermark, card, or paid plan.` |
| H1 `It is free. All of it.` | `Professional video background removal, free to use.` |
| Opening paragraph | `Sign in to remove backgrounds from up to 3 videos during a 24-hour allowance window. There is no watermark, subscription, credit pack, checkout, or paid upgrade.` |
| `There is nothing to pay for.` | `Everything currently available in BGRemove is free to use within the 24-hour allowance.` |
| Paragraph mentioning designed but unopened paid plans | `Your first successful video starts the 24-hour window. Complete up to 3 successful jobs before it ends; failed jobs do not count. When the window ends, the full allowance resets to 3.` |
| `Unlimited days, no card ever` | `Return after your allowance resets—no card required` |
| `No per-export fee and no credits to top up` | `No subscriptions, credit packs, or checkout` |
| H2 `This is not a demo.` | `Full-quality processing, not a restricted demo.` |
| Paragraph framing use as a test | `Use BGRemove for social clips, product footage, client work, and reusable transparent assets. The 24-hour allowance limits volume, not the value of the result.` |

Use the confirmed product facts in this recommendation. Do not claim batch upload, API access, refinement, or background replacement. Describe only transparent WebM using VP9 with alpha, source-dimension output, and 24-hour retention.

#### About `/about/`

| Current | Proposed replacement |
|---|---|
| Meta description | `Meet BGRemove, a professional AI video background remover built for stable edges, transparent output, and real editing workflows.` |
| H1 `A narrow tool, built on purpose.` | `Professional video background removal, built for real workflows.` |
| `does one job... no plans to grow any` | `BGRemove turns footage into reusable transparent video for creators, editors, ecommerce teams, and agencies. The current workflow stays focused and fast while the product continues to grow around real production needs.` |
| `BGRemove is the boring middle... nothing clever about the product` | `BGRemove connects licensed temporal-matting technology to a production-ready workflow: secure upload, dependable processing, and transparent files that open in the tools professionals already use.` |
| `Four positions we are not going to move on` | `Principles guiding the product today` |
| `The matte is the product` | `Reusable transparent output is the foundation` |
| Absolute no-flatten claim | `BGRemove prioritizes alpha-enabled output so the subject remains reusable across backgrounds and edits. Additional export workflows should extend that flexibility rather than remove it.` |
| `No controls that do not control anything` section | `Automation first, with room for refinement` |
| Section body dismissing controls | `The current workflow automates the time-consuming first pass and returns editor-ready output. As refinement tools develop, they should solve real edge problems without adding empty controls.` |
| `Say what it cannot do` | `Set clear expectations` |
| `Priced against real cost` and paid-plan paragraph | `Free access with a practical allowance` / `BGRemove currently provides up to 3 successful video background removals per 24-hour allowance window. The full allowance resets when the window ends.` |
| `A small independent team` | `An independent team focused on video workflows` |
| H2 `The claim is testable.` | `See the result in your own workflow.` |

#### FAQ `/faq/`

| Element/current copy | Proposed replacement |
|---|---|
| Meta description | `Answers about free access, 60-second videos, transparent WebM output, edge quality, 24-hour file retention, and account access.` |
| H1 `Questions, answered without a sales voice.` | `Clear answers about video background removal.` |
| Output answer with Creator/Studio | `BGRemove exports transparent WebM video using VP9 with a real alpha channel. This output is available to every signed-in user at no cost and preserves the source video's dimensions.` |
| Per-clip answer with paid plans | `Each video can be up to 60 seconds long. BGRemove does not impose a separate file-size cap, and output preserves the source video's dimensions.` |
| Input-format answer ending `almost certainly go through` | `BGRemove accepts MP4, MOV, WebM, M4V, and GIF. Videos can be up to 60 seconds long.` |
| Matte-adjustment answer dismissing all controls | `BGRemove currently focuses on automatic matting and transparent WebM output. It does not currently include manual edge refinement or a second-pass refinement mode.` |
| Retention answer with Creator/Studio | `Source uploads and generated transparent videos are retained for 24 hours, then removed. Download the result before it expires.` |
| Stored-data answer mentioning plan, card, Lemon Squeezy | Describe only data the current free implementation actually stores. Remove payment-provider and billing claims if those data flows are inactive. |
| H2 `Account and billing` | `Account and free access` |
| Free-plan answer | `BGRemove currently gives each signed-in account up to 3 successful video background removals per 24-hour allowance window. The first successful video starts the window, failed jobs do not count, and all 3 uses reset when the window ends. There is no watermark, card, subscription, credit pack, or paid upgrade.` |
| `How do I cancel?` | `Are there any paid plans?` |
| Cancellation answer | `No. BGRemove currently has no paid plan or recurring subscription to cancel.` |
| `Do you offer refunds?` | `How does the 24-hour allowance work?` |
| Refund answer | `Video processing uses metered infrastructure. The 3-video allowance keeps free access available to more people. Your first successful video starts a 24-hour window, and the full allowance resets when that window ends.` |
| `A day of free clips settles... the only question` | `Use the free allowance on the footage you actually edit—social video, product shots, client work, or motion-heavy clips—and evaluate the result where it matters: in your workflow.` |

Mirror every visible FAQ change in FAQPage JSON-LD.

#### Contact `/contact/`

| Current | Proposed replacement |
|---|---|
| Meta description mentioning billing | `Get help with a failed matte, account access, privacy request, or product question. Contact the BGRemove team directly.` |
| `Billing, invoices, refunds` | `Account and access` |
| Billing description | `Questions about sign-in, the 24-hour allowance, saved jobs, or access across devices.` |

#### How it works `/how-it-works/`

| Current | Proposed replacement |
|---|---|
| Format/tier cards | Show only `Transparent WebM (VP9 with alpha)` with no Creator, Studio, or tier labels. State that output preserves the source video's dimensions. |
| `the only way those edges ever look right` | `Per-pixel alpha preserves partial transparency around hair, motion blur, and semi-transparent fabric instead of forcing every edge into a hard cutout.` |
| `there is nothing for you to adjust... more controls would not have saved it` | `Upload your clip, follow the processing status, and download a transparent result. The current workflow prioritizes fast automatic matting and editor-ready output, with room for meaningful refinement tools as the product develops.` |
| `Reading about a matte proves nothing.` | `See temporal video matting on your own footage.` |

Synchronize the HowTo JSON-LD with the verified output-format copy.

#### Tool and use-case pages

| Page/current issue | Proposed replacement |
|---|---|
| `/tools/product-video-background-remover/`: Studio/API/batch claims | `Create reusable transparent product footage for listings, campaigns, and seasonal creative without tracing every edge by hand.` Do not claim batch processing or API access. |
| `/tools/remove-background-from-video/`: Creator/Studio resolution and paid format claims | `Upload an MP4, MOV, WebM, M4V, or GIF up to 60 seconds long. BGRemove preserves the source video's dimensions and exports transparent WebM using VP9 with alpha—at no cost and without a watermark.` |
| `/tools/remove-background-from-video/` meta | `Remove a video background online and export transparent video with a real alpha channel for web, editing, and compositing workflows.` |
| `/tools/tiktok-background-remover/`: paid-plan duration | `Process videos up to 60 seconds long. Each signed-in account can complete up to 3 successful jobs per 24-hour allowance window at no cost.` |
| `/tools/tiktok-background-remover/`: broad claim that studio-trained tools handle vertical video badly | `Short-form vertical footage combines handheld motion, busy rooms, and changing light. Temporal video matting uses context across frames to keep the subject edge more stable through those conditions.` |
| `/use-cases/agencies/` meta | `Automated video matting for agency workflows. Preserve transparent edges and move client footage into professional editing and compositing tools.` |
| `/use-cases/agencies/`: `a first pass, not a finish` | `Automated matting handles the bulk of routine edge work and gives artists a strong production starting point. Review hero shots and complex occlusion in your compositing tool, then refine only the frames that need it.` |
| `/use-cases/agencies/`: Studio/batch/API claims | `Prepare transparent source files for client edits, campaign variants, and compositing handoffs.` Do not claim batch processing or API access. |

Do not confuse `paid social`—a marketing channel—with a paid BGRemove plan. It may remain when the context is unambiguous.

#### Changelog `/changelog/`

Delete public changelog entries whose subject is a previous paid plan, subscription, paid tier, credit pack, purchase flow, or paid entitlement. Keep unrelated release history. This instruction applies only to public changelog content; do not alter source-control history, operational records, invoices, or legally required payment records.

#### English legal pages

These are drafting directions, not legal advice, and require human legal review:

- `/legal/privacy/`: remove current-payment and Lemon Squeezy collection claims only after code confirms those data flows are inactive. Describe the actual free-account and job data currently stored.
- `/legal/refunds/`: retain the URL but replace the paid refund policy with: `BGRemove currently does not sell subscriptions, credit packs, or paid upgrades, so there is no purchase to refund. If you believe you were charged in error, contact support@bgremove.video.` Remove its footer link.
- `/legal/terms/`: replace `Plans, payment and quota` with `Free access and 24-hour allowance`; describe the confirmed window and reset behavior and remove purchase, billing-period, cancellation, paid-retention, Creator/Studio, and amount-paid liability language after legal review.
- `/legal/acceptable-use/`: replace `plan limits` with `24-hour usage limits`; remove `without refund` language where no payment exists.
- Keep historical billing records or legally required disclosures out of public current-product copy unless counsel confirms they remain necessary.

### Language rules

- Change English only in this Pull Request.
- Do not change Spanish, Portuguese, German, or French copy, metadata, structured data, navigation labels, or legal content. The user will authorize localization after the English implementation is complete.
- Do not add Japanese or Korean.
- Preserve `paid social` and third-party subscription comparisons when the subject is clearly not a BGRemove paid offer.

## Resolved implementation details

- The first successful processing job starts a 24-hour allowance window. Up to three successful jobs may complete in that window. Failed jobs do not count. When the window ends, the allowance resets to three all at once.
- Sign-in is required.
- Maximum video duration is 60 seconds.
- There is no separate product-enforced file-size limit.
- Output preserves the source video's dimensions; there is no lower plan-based resolution cap.
- Accepted inputs are MP4, MOV, WebM, M4V, and GIF.
- The only transparent output is `webm_vp9`, presented to users as transparent WebM using VP9 with alpha. It is free and has no watermark.
- Custom background replacement is not currently available.
- Batch upload/processing, manual or second-pass edge refinement, API, and webhooks are not currently available.
- Source uploads and generated transparent outputs are retained for 24 hours. There is no background-replacement output to retain.
- Keep `/pricing/` but relabel its English navigation entry and page purpose as `Free Access`.
- Keep `/legal/refunds/` as a no-current-payments notice, but remove its footer link.
- Delete previous paid-plan entries from the public changelog.
- Remove or hide public purchase, subscription, credit-pack, upgrade, and checkout entry points. Do not delete historical billing data or provider records.
- English copy is approved. Do not update Spanish, Portuguese, French, or German until separately authorized.
- Draft English legal copy from the real code and data flows, and mark it for human legal review before merge.
- The approved positioning emphasizes professional temporal consistency, motion edges, alpha output, reusable transparent assets, and editing/compositing workflows.
- Avoid permanent promises including `free forever`, `we will never charge`, and `no plans to grow`.

## Final decision

Confirmed by the user on 2026-08-05:

- BGRemove is temporarily completely free.
- Each signed-in user receives up to three successful processing jobs in a 24-hour allowance window that starts with the first successful job.
- Failed jobs do not count; when the window ends, all three uses reset together.
- There are no paid options during this phase.
- Videos may be up to 60 seconds, with no separate product-enforced file-size limit. Output preserves the source dimensions.
- Inputs are MP4, MOV, WebM, M4V, and GIF. The only transparent output is watermark-free `webm_vp9`.
- Files are retained for 24 hours.
- Background replacement, batch processing, edge refinement, API, and webhooks are not available.
- The free strategy is intended to improve useful engagement, repeat visits, and SEO authority before later monetization.
- Previous recommendations are superseded.
- The audit must remove conflicting free/paid messaging, strengthen professional positioning, raise perceived value, and avoid narrow or permanent claims that restrict future development.
- English is approved for implementation now. Existing localized versions are deferred.
- Previous paid-related public changelog entries should be deleted.
- Public purchase and checkout entry points should be removed or hidden.

All implementation decisions are resolved. The user approved the English copy direction and execution scope on 2026-08-05.

## Implementation prompt

```text
Target repository: https://github.com/DAOteam/bgremove
Delivery method: Pull Request. Do not deploy or merge.

Goal
Align every English public BGRemove page with the approved current strategy: BGRemove is a professional video-background-removal tool that is currently free. A signed-in account may complete up to three successful processing jobs in a 24-hour allowance window that starts with its first successful job. Failed jobs do not count, and the full allowance resets to three when the window ends. There are no paid plans, subscriptions, credit packs, paid upgrades, or public purchase paths.

Scope boundary
This task changes English public copy, SEO metadata, derived social metadata, visible navigation/footer/CTA labels, corresponding FAQPage/HowTo/WebApplication structured data, and public purchase/checkout entry points. It does not authorize changing allowance logic, processing entitlements, authentication, databases, infrastructure, payment-provider products, billing records, or deployment. If current behavior conflicts with the confirmed product facts below, stop and report the conflict instead of changing core behavior or publishing inaccurate copy.

Confirmed product facts
- Sign-in is required.
- The first successful job starts the 24-hour allowance window.
- A maximum of three successful jobs may complete in that window; failed jobs do not count.
- The full allowance resets to three when the window ends.
- Each input may be up to 60 seconds. There is no separate product-enforced file-size limit.
- Accepted inputs: MP4, MOV, WebM, M4V, and GIF.
- Preserve the source video's dimensions in output.
- The only transparent output is `webm_vp9`, described publicly as transparent WebM using VP9 with alpha.
- Output has no watermark.
- Source uploads and generated transparent output are retained for 24 hours.
- Custom background replacement, batch processing, manual/second-pass edge refinement, API, and webhooks are not available.

Before editing
1. Read BGV-0008 Final decision, Resolved implementation details, site.md, and decisions.md.
2. Inspect the current repository sources for all 20 English public routes and any shared component an English change would touch.
3. Verify the confirmed facts against code. If allowance, processing, retention, or authentication behavior conflicts, stop and record a blocker rather than changing product behavior in this task.
4. Build a before-change inventory for the 20 English sitemap URLs, including title, meta description, visible paid/tier language, navigation/footer labels, and JSON-LD strings.
5. Identify every publicly reachable purchase, subscription, credit-pack, upgrade, and checkout entry point. Remove or hide it so a user cannot reach a paid offer. Preserve dormant backend code, historical billing records, and payment-provider records unless a separate approved task authorizes changes.

Required copy changes
1. Apply the approved English replacement matrix in BGV-0008.
2. Change English only. Do not modify Spanish, Portuguese, French, or German content, metadata, structured data, or labels, even when they share components.
3. Change the English `Pricing` label to `Free Access`; keep the existing `/pricing/` URL.
4. Remove current BGRemove plan, subscription, checkout, credit-pack, purchase, cancellation, refund, Creator, Studio, and paid-tier claims from active marketing pages, metadata, and structured data.
5. Do not remove `paid social` when it clearly means advertising, or third-party paid-plan comparisons when the subject is unambiguous.
6. Delete previous paid-plan, subscription, tier, credit-pack, purchase-flow, and paid-entitlement entries from the public changelog. Keep unrelated release history and do not alter Git history or operational/payment records.
7. Replace low-value or restrictive phrases including `narrow tool`, `does one job`, `does one thing`, `no plans to grow`, `boring middle`, `nothing clever about the product`, `deliberately no`, `first pass, not a finish`, and claims that using one clip merely tests the product.
8. Replace permanent promises including `free forever`, `no card ever`, `we will never charge`, or equivalent wording. Describe the current state accurately without blocking later monetization.
9. Position the product with concrete professional value: temporal consistency, stable motion edges, real alpha, reusable transparent output, and compatibility with editing/compositing workflows. Do not invent quality statistics, customer proof, or unsupported capabilities.
10. Make visible FAQ and FAQPage JSON-LD answers identical in meaning. Synchronize HowTo and WebApplication JSON-LD with visible current copy.
11. Use the confirmed facts exactly: 60 seconds, no separate product file-size cap, source dimensions preserved, the five accepted input formats, `webm_vp9` only, no watermark, 24-hour retention, login required, and no background replacement/batch/refinement/API/webhooks.
12. Keep `/legal/refunds/`, replace it with the approved no-current-payments notice, and remove its footer link.
13. Draft the other English legal changes from actual code and data flows. Mark them for human legal review before merge; do not invent data practices or remove factual disclosures without verification.

Verification
1. Run relevant content, type, and build checks.
2. Render or crawl all 20 English sitemap URLs from a production-like build.
3. Confirm English navigation, title/meta, visible copy, and structured data are aligned. Confirm non-English routes were not changed by this Pull Request.
4. Search active English current-product pages for: paid plan, subscription, price, pricing, purchase, checkout, credit pack, Creator, Studio, Lemon Squeezy, cancellation, paid retention, and refund. Every remaining match must be justified as legal necessity, paid-social context, or a clearly identified third-party comparison. Previous paid-product changelog matches are not allowed.
5. Search for the prohibited low-value and permanent phrases listed above.
6. Confirm the homepage title remains exactly `Remove Video Background Online Free - No Watermark`.
7. Confirm copy accurately describes the anchored 24-hour allowance window and full reset; it must not imply calendar-day reset or per-use rolling restoration.
8. Confirm the exact feature limits in Confirmed product facts and that no unsupported feature or quality claim was introduced.
9. Include a before/after table, remaining-search-match explanations, commands, and results in the Pull Request and execution result.

Do not deploy, publish, merge, localize non-English pages, add Japanese/Korean, change core product logic, delete billing/provider records, or execute any superseded recommendation.
```

## Acceptance criteria

- All 20 English public sitemap URLs consistently describe the current free strategy.
- No English current-product page or publicly reachable UI offers a paid plan, purchase path, subscription, credit pack, checkout, or paid upgrade.
- English navigation uses `Free Access` instead of `Pricing`; the `/pricing/` URL remains unchanged.
- The homepage and free-access page clearly explain the 3-use anchored 24-hour allowance window, full reset, no watermark, and no current paid option.
- The exact homepage title remains unchanged.
- Visible FAQ, metadata, Open Graph/Twitter derivatives, and structured data do not contradict one another.
- Previous paid-product changelog entries are removed from the public changelog; unrelated release history remains.
- `/legal/refunds/` remains available at its URL with the approved no-current-payments notice but is removed from the footer.
- Draft legal copy accurately reflects current code and data flows and is clearly marked for human legal review before merge.
- No active copy describes BGRemove as narrow, boring, low-value, merely a demo/test, permanently limited, or unwilling to grow.
- Professional positioning is supported by concrete workflow value without invented proof or unsupported features.
- No copy promises permanent free access or blocks future monetization.
- MP4, MOV, WebM, M4V, and GIF inputs; 60-second duration; no separate file-size cap; source-dimension output; `webm_vp9`; no watermark; login requirement; and 24-hour retention are stated accurately where relevant.
- No page claims custom background replacement, batch processing, manual/second-pass refinement, API access, or webhooks are currently available.
- Spanish, Portuguese, French, and German are unchanged; Japanese and Korean are not added.
- Relevant build and content checks pass, and the Pull Request contains a complete before/after inventory.

## Out of scope

- Changing allowance, processing limits, feature access, authentication, database schema, or account behavior.
- Creating or deleting payment-provider products.
- Deleting backend billing code, historical billing records, invoices, or payment-provider records. Removing or hiding public purchase and checkout entry points is in scope.
- New pages, URL migrations, redirects, keyword-expansion pages, or site redesign.
- GSC/ranking conclusions without data.
- Any non-English localization.
- Deployment, publishing, or merging.
