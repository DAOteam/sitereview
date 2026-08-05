---
task_id: "BGV-0008"
site_id: "bgremove-video"
title: "Align the full public site with free professional positioning"
status: "needs_decision"
priority: "P0"
source: "user+ai"
created_at: "2026-08-05"
updated_at: "2026-08-05"
prompt_version: 1
---

# BGV-0008 — Align the full public site with free professional positioning

## Scope

All 80 public URLs in the 2026-08-05 sitemap, covering English, Spanish, Portuguese, German, and French, plus shared navigation, footer, calls to action, metadata, Open Graph/Twitter fields when derived from SEO metadata, FAQ/HowTo/WebApplication structured data, and the five English legal pages.

This is a public-copy alignment task. It does not authorize changing processing entitlements, authentication, payment code, databases, or deployment configuration.

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
- Give each user up to three free uses in any rolling 24-hour period and offer no paid option.
- Use the free phase to improve useful engagement, return visits, and SEO authority before introducing monetization later.
- Remove copy that contradicts the free strategy or professional video-background-removal positioning.
- Upgrade low-value language and remove narrow or absolute claims that restrict future development.
- Provide replacement copy rather than modifying the website directly.
- Clear the prior recommendation backlog and create new recommendations from this strategy.

## AI recommendation

Use one precise promise across the site:

> BGRemove is currently free to use. Each account can remove the background from up to three videos in any rolling 24-hour period, with no watermark, subscription, credit pack, or paid upgrade.

Do not use `free forever`, `no card ever`, `we will never charge`, `no plans to grow`, or similar permanent promises. The business intends to monetize later, so describe the current state with words such as `currently`, `today`, and `right now` only where needed for accuracy.

Position BGRemove as purpose-built and professional, not narrow or small. Support that position with concrete value: temporal consistency across frames, stable edges through motion, a real alpha channel, reusable transparent output, and fit with established editing/compositing workflows.

Keep `/pricing/` temporarily to avoid an unnecessary URL migration, but relabel it `Free Access` in navigation and rewrite it as the canonical explanation of the current free allowance. Do not create a new route in this task.

Preserve genuine historical changelog entries, but add a clear current-status notice so old plan launches cannot be mistaken for current offers. Do not rewrite history.

Treat legal pages as fact-sensitive. Draft replacements are included below, but any Terms, Privacy, Acceptable Use, or refund-related change requires a human legal review before publication.

### Finding categories

| Audit requirement | Confirmed examples | Primary affected surfaces |
|---|---|---|
| Conflicts with completely-free positioning | Paid plans, Creator/Studio, Lemon Squeezy, billing, cancellation, refunds, paid retention, paid formats | Homepage FAQ, FAQ, About, Contact, How it works, pricing, tool pages, legal pages, JSON-LD, all five locales |
| Conflicts with professional-tool positioning | `does one thing`, `a first pass, not a finish`, presenting the daily allowance mainly as a product test | Homepage, About, FAQ, agency use case, pricing |
| Low perceived value | `boring middle`, `nothing clever about the product`, `small independent team`, `try it on your worst clip` | About and shared conversion sections |
| Too narrow or absolute for future development | `no plans to grow`, `deliberately no background library`, dismissing all controls, `free forever`, `no card ever`, `almost certainly` | About, homepage FAQ, FAQ, pricing, How it works |

### Proposed replacement copy for review

The following English copy is the proposed source. Localize by meaning for Spanish, Portuguese, German, and French after the English source is approved.

#### Shared navigation, footer, and CTA

| Current | Replace with |
|---|---|
| `Pricing` | `Free Access` |
| Footer link `Refunds` | Remove from the footer while no payment option exists. Keep the legal URL only if needed for an accurate no-payments notice. |
| `Start free` | `Remove a Video Background` |
| `Free clips every day. No watermark, no card.` | `3 free video background removals every 24 hours. No watermark, no card.` |
| Generic secondary CTA `Pricing` | `See Free Access` |

#### Homepage `/`

Keep the approved title and H1:

- Title: `Remove Video Background Online Free - No Watermark`
- H1: `Remove video background online. Free, no watermark.`

Replace:

| Element/current copy | Proposed replacement |
|---|---|
| Meta description | `Remove video backgrounds online free with AI. Process up to 3 videos every 24 hours, export transparent video with no watermark, and pay nothing.` |
| Hero supporting line | `AI video matting preserves motion and edge detail, then returns transparent video with a real alpha channel for your editing workflow.` |
| `Free tier included` | `3 free videos every 24 hours` |
| `Free clips every day, forever...` | `Process up to 3 videos in any rolling 24-hour period at no cost. Download without a watermark and return as your allowance becomes available again.` |
| Free FAQ answer mentioning paid plans | `Yes. BGRemove currently has no paid plans, subscriptions, credit packs, or paid upgrades. Sign in to remove the background from up to 3 videos in any rolling 24-hour period and download without a watermark.` |
| Format FAQ answer with paid tiers | `BGRemove returns transparent video with a real alpha channel instead of flattening your subject onto a color. Every download option currently available in the workspace is offered at no cost.` |
| `This does one thing...` comparison answer | `Canva and Adobe are broad design suites. BGRemove is purpose-built for video background removal, using temporal context across frames to keep edges more stable through motion and returning reusable transparent video for the editor you already use.` |
| Limitations paragraph ending `before you pay for anything` | `Hair, motion blur, and rim light are demanding edge cases that BGRemove is designed to handle. Glass, heavy overlap, and very dark footage remain challenging, so review those results carefully in your editing workflow.` |
| Sign-in answer with vague allowance | `Your account keeps jobs associated with you, supports access across devices, and makes the daily allowance of 3 videos fair and reliable. Google sign-in means BGRemove does not store a separate password.` |
| `There is deliberately no background library here...` | `The transparent result can be placed over colors, images, or footage in your editor and reused across multiple versions instead of baking one background into the file.` |
| `Try it on your worst clip.` | `Test it on real footage.` |
| `today’s free one costs you nothing` | `Use one of your 3 free daily videos on footage with real motion, hair, or a busy background and judge the transparent result in your own workflow.` |

Apply the same answers to visible FAQ and FAQPage JSON-LD.

#### Free-access page `/pricing/`

| Element/current copy | Proposed replacement |
|---|---|
| Title | `Free Video Background Remover – 3 Videos Daily | BGRemove` |
| Meta description | `BGRemove is free to use. Remove backgrounds from up to 3 videos every 24 hours with no watermark, no card, and no paid plan or credit pack.` |
| H1 `It is free. All of it.` | `Professional video background removal, free every day.` |
| Opening paragraph | `Remove backgrounds from up to 3 videos per day with BGRemove’s transparent-video workflow. There is no watermark, subscription, credit pack, checkout, or paid upgrade.` |
| `There is nothing to pay for.` | `Everything currently available in BGRemove is free to use within the daily allowance.` |
| Paragraph mentioning designed but unopened paid plans | `The rolling allowance keeps processing available to more people. You can process up to 3 videos in any 24-hour period, then return as earlier uses leave that window.` |
| `Unlimited days, no card ever` | `Use it again every day—no card required` |
| `No per-export fee and no credits to top up` | `No subscriptions, credit packs, or checkout` |
| H2 `This is not a demo.` | `Full-quality processing, not a restricted demo.` |
| Paragraph framing use as a test | `Use BGRemove for social clips, product footage, client work, and reusable transparent assets. The daily allowance limits volume, not the value of the result.` |

Only list features that the current free workspace actually exposes. Do not claim batch upload, API access, particular output formats, resolution, refinement, background replacement, or retention until verified in code.

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
| `Priced against real cost` and paid-plan paragraph | `Free access with a practical rolling allowance` / `BGRemove currently provides up to 3 free video background removals in any rolling 24-hour period. The allowance keeps processing available while giving users room for recurring creative work.` |
| `A small independent team` | `An independent team focused on video workflows` |
| H2 `The claim is testable.` | `See the result in your own workflow.` |

#### FAQ `/faq/`

| Element/current copy | Proposed replacement |
|---|---|
| Meta description | `Answers about free daily use, transparent video, edge quality, clip limits, privacy, file retention, and account access.` |
| H1 `Questions, answered without a sales voice.` | `Clear answers about video background removal.` |
| Output answer with Creator/Studio | `BGRemove returns a transparent video file with a real alpha channel. Every output option shown in the current workspace is available at no cost. Choose the option that fits your browser, editor, or compositing workflow.` |
| Per-clip answer with paid plans | `Each account can process up to 3 videos per day. The upload workspace shows the current per-clip duration and file limits before processing.` |
| Input-format answer ending `almost certainly go through` | `BGRemove accepts common video formats including MP4, MOV, WebM, M4V, and GIF. The upload workspace checks the file before processing and shows the current size and format requirements.` |
| Matte-adjustment answer dismissing all controls | `BGRemove currently focuses on automatic matting and transparent output. For frame-level correction today, continue in a compatible editor using the refinement or alpha-enabled output available in your workspace.` |
| Retention answer with Creator/Studio | Replace with the single retention rule verified in the current implementation; do not mention plans or tiers. |
| Stored-data answer mentioning plan, card, Lemon Squeezy | Describe only data the current free implementation actually stores. Remove payment-provider and billing claims if those data flows are inactive. |
| H2 `Account and billing` | `Account and free access` |
| Free-plan answer | `BGRemove currently gives each account up to 3 free video background removals in any rolling 24-hour period. There is no watermark, card, subscription, credit pack, or paid upgrade.` |
| `How do I cancel?` | `Are there any paid plans?` |
| Cancellation answer | `No. BGRemove currently has no paid plan or recurring subscription to cancel.` |
| `Do you offer refunds?` | `Why is there a daily limit?` |
| Refund answer | `Video processing uses metered infrastructure. The rolling limit keeps free access available to more people. Each use becomes available again after it leaves the 24-hour window.` |
| `A day of free clips settles... the only question` | `Use the daily allowance on the footage you actually edit—social video, product shots, client work, or motion-heavy clips—and evaluate the result where it matters: in your workflow.` |

Mirror every visible FAQ change in FAQPage JSON-LD.

#### Contact `/contact/`

| Current | Proposed replacement |
|---|---|
| Meta description mentioning billing | `Get help with a failed matte, account access, privacy request, or product question. Contact the BGRemove team directly.` |
| `Billing, invoices, refunds` | `Account and access` |
| Billing description | `Questions about sign-in, the daily allowance, saved jobs, or access across devices.` |

#### How it works `/how-it-works/`

| Current | Proposed replacement |
|---|---|
| Format/tier cards | Show only formats currently available to every user, with no Creator/Studio/tier labels. Verify exact formats first. |
| `the only way those edges ever look right` | `Per-pixel alpha preserves partial transparency around hair, motion blur, and semi-transparent fabric instead of forcing every edge into a hard cutout.` |
| `there is nothing for you to adjust... more controls would not have saved it` | `Upload your clip, follow the processing status, and download a transparent result. The current workflow prioritizes fast automatic matting and editor-ready output, with room for meaningful refinement tools as the product develops.` |
| `Reading about a matte proves nothing.` | `See temporal video matting on your own footage.` |

Synchronize the HowTo JSON-LD with the verified output-format copy.

#### Tool and use-case pages

| Page/current issue | Proposed replacement |
|---|---|
| `/tools/product-video-background-remover/`: Studio/API/batch claims | `Create reusable transparent product footage for listings, campaigns, and seasonal creative without tracing every edge by hand.` Only add batch/API details if they are actually available free. |
| `/tools/remove-background-from-video/`: Creator/Studio resolution and paid format claims | `BGRemove preserves the uploaded aspect ratio, including vertical and square video. The upload workspace shows the current duration, file-size, resolution, and download options—all currently available at no cost.` |
| `/tools/remove-background-from-video/` meta | `Remove a video background online and export transparent video with a real alpha channel for web, editing, and compositing workflows.` |
| `/tools/tiktok-background-remover/`: paid-plan duration | `Your workspace shows the current per-clip duration limit. Each account can process up to 3 videos per day at no cost.` |
| `/tools/tiktok-background-remover/`: broad claim that studio-trained tools handle vertical video badly | `Short-form vertical footage combines handheld motion, busy rooms, and changing light. Temporal video matting uses context across frames to keep the subject edge more stable through those conditions.` |
| `/use-cases/agencies/` meta | `Automated video matting for agency workflows. Preserve transparent edges and move client footage into professional editing and compositing tools.` |
| `/use-cases/agencies/`: `a first pass, not a finish` | `Automated matting handles the bulk of routine edge work and gives artists a strong production starting point. Review hero shots and complex occlusion in your compositing tool, then refine only the frames that need it.` |
| `/use-cases/agencies/`: Studio/batch/API claims | `Prepare transparent source files for client edits, campaign variants, and compositing handoffs.` Add batch/API specifics only if verified available free. |

Do not confuse `paid social`—a marketing channel—with a paid BGRemove plan. It may remain when the context is unambiguous.

#### Changelog `/changelog/`

Add above historical entries:

> Current status: BGRemove is free to use, with up to 3 video background removals per account in any rolling 24-hour period and no paid plans or purchase options. Older entries below describe previous product experiments and are kept as a transparent release history; they are not current offers.

Do not delete or rewrite dated historical entries. Update the changelog structured data or page context only as needed to keep the current-status notice visible and indexable.

#### English legal pages

These are drafting directions, not legal advice, and require human legal review:

- `/legal/privacy/`: remove current-payment and Lemon Squeezy collection claims only after code confirms those data flows are inactive. Describe the actual free-account and job data currently stored.
- `/legal/refunds/`: replace the paid refund policy with a short current-status notice: `BGRemove currently does not sell subscriptions, credit packs, or paid upgrades, so there is no purchase to refund. If you believe you were charged in error, contact support@bgremove.video.` Remove the footer link unless legal review requires it.
- `/legal/terms/`: replace `Plans, payment and quota` with `Free access and rolling allowance`; describe up to three uses in any rolling 24-hour period and remove purchase, billing-period, cancellation, paid-retention, Creator/Studio, and amount-paid liability language after legal review.
- `/legal/acceptable-use/`: replace `plan limits` with `daily usage limits`; remove `without refund` language where no payment exists.
- Keep historical billing records or legally required disclosures out of public current-product copy unless counsel confirms they remain necessary.

### Language rules

- Apply the approved meaning across English, Spanish, Portuguese, German, and French in the same Pull Request.
- Write natural local-language copy; do not mechanically translate English syntax.
- Use the local equivalent of `Free Access`, not `Pricing`.
- Preserve `paid social` and third-party subscription comparisons only when clearly distinguished from BGRemove pricing.
- Do not add Japanese or Korean.

## Open decisions

1. Confirm the current per-clip duration, resolution, download formats, file retention, background-replacement access, batch upload, refined-edge pass, and API availability for every free user. Public pages currently contradict one another.
2. Confirm whether `/legal/refunds/` should remain as a no-payments notice or redirect to Terms after legal review.
3. Obtain human legal approval for changes to Terms, Privacy, Acceptable Use, and refund-related copy.

## Resolved implementation details

- Confirmed by the user on 2026-08-05: Each account may process up to three videos in any rolling 24-hour period. The allowance does not reset at a fixed calendar-day boundary.

## Final decision

Confirmed by the user on 2026-08-05:

- BGRemove is temporarily completely free.
- Each user receives up to three free uses in any rolling 24-hour period.
- The three-use allowance is calculated over a rolling 24-hour window rather than by calendar day.
- There are no paid options during this phase.
- The free strategy is intended to improve useful engagement, repeat visits, and SEO authority before later monetization.
- Previous recommendations are superseded.
- The audit must remove conflicting free/paid messaging, strengthen professional positioning, raise perceived value, and avoid narrow or permanent claims that restrict future development.

The three implementation details listed under Open decisions remain pending. This task must not be executed until they are resolved and the status changes to `approved`.

## Implementation prompt

```text
DRAFT ONLY. DO NOT EXECUTE WHILE THIS RECOMMENDATION HAS status: "needs_decision".

Target repository: https://github.com/DAOteam/bgremove
Delivery method: Pull Request. Do not deploy or merge.

Goal
Align every public BGRemove page in English, Spanish, Portuguese, German, and French with the approved current strategy: BGRemove is a professional video-background-removal tool, currently free, with up to three video-processing uses per account in any rolling 24-hour period and no paid plans, subscriptions, credit packs, paid upgrades, or purchase path.

Scope boundary
This task changes public copy, SEO metadata, derived social metadata, visible navigation/footer/CTA labels, and corresponding FAQPage/HowTo/WebApplication structured data. It does not authorize changes to processing entitlements, authentication, payment code, databases, infrastructure, or deployment. If product behavior conflicts with the final approved copy, stop and report the conflict instead of changing behavior or publishing inaccurate copy.

Before editing
1. Read BGV-0008 Final decision, the resolved Open decisions, site.md, and decisions.md.
2. Inspect the current repository sources for every public route and shared localized component.
3. Verify current free-user behavior for the rolling allowance, per-clip duration, resolution, formats, retention, background replacement, batch, refinement, and API before using any feature claim.
4. Build a before-change inventory for all 80 sitemap URLs, including title, meta description, visible paid/tier language, navigation/footer labels, and JSON-LD strings.
5. If the code exposes any active purchase path or if authenticated behavior contradicts “no paid option,” stop and record a separate blocker; do not silently rewrite product logic in this copy task.

Required copy changes
1. Apply the approved English replacement matrix in BGV-0008.
2. Localize the approved meaning naturally into Spanish, Portuguese, German, and French in the same Pull Request.
3. Change shared `Pricing` labels to the local equivalent of `Free Access`; keep the existing `/pricing/` URL for this task.
4. Remove current BGRemove plan, subscription, checkout, credit-pack, purchase, cancellation, refund, Creator, Studio, and paid-tier claims from active marketing pages, metadata, and structured data.
5. Do not remove `paid social` when it clearly means advertising, or third-party paid-plan comparisons when the subject is unambiguous.
6. Keep dated changelog history, add the approved current-status notice, and do not present historical plans as current offers.
7. Replace low-value or restrictive phrases including `narrow tool`, `does one job`, `does one thing`, `no plans to grow`, `boring middle`, `nothing clever about the product`, `deliberately no`, `first pass, not a finish`, and claims that using one clip merely tests the product.
8. Replace permanent promises including `free forever`, `no card ever`, `we will never charge`, or equivalent localized wording. Describe the current state accurately without blocking later monetization.
9. Position the product with concrete professional value: temporal consistency, stable motion edges, real alpha, reusable transparent output, and compatibility with editing/compositing workflows. Do not invent quality statistics, customer proof, or unsupported capabilities.
10. Make visible FAQ and FAQPage JSON-LD answers identical in meaning. Synchronize HowTo and WebApplication JSON-LD with visible current copy.
11. Apply legally reviewed wording to the English legal pages. Do not improvise legal terms or remove factual privacy disclosures without checking current data flows.

Verification
1. Run relevant content, localization, type, and build checks.
2. Render or crawl all 80 sitemap URLs from a production-like build.
3. Confirm every current locale has the correct free-access navigation, title/meta, visible copy, and structured data.
4. Search active current-product pages for old terms and localized equivalents: paid plan, subscription, price, pricing, purchase, checkout, credit pack, Creator, Studio, Lemon Squeezy, cancellation, paid retention, and refund. Every remaining match must be justified as changelog history, legal necessity, paid-social context, or a clearly identified third-party comparison.
5. Search for the prohibited low-value and permanent phrases listed above and their localized equivalents.
6. Confirm the homepage title remains exactly `Remove Video Background Online Free - No Watermark`.
7. Confirm public copy accurately says up to three uses in any rolling 24-hour period, does not imply a fixed calendar-day reset, and does not claim unlimited use or permanent free access.
8. Confirm no unverified feature, format, resolution, retention, batch, API, background replacement, or quality claim was introduced.
9. Include a before/after table, remaining-search-match explanations, commands, and results in the Pull Request and execution result.

Do not deploy, publish, merge, add Japanese/Korean, change product logic, or execute any superseded recommendation.
```

## Acceptance criteria

- All 80 public sitemap URLs consistently describe the current free strategy in their own locale.
- No active current-product page implies BGRemove has a paid plan, purchase path, subscription, credit pack, or paid upgrade.
- Shared navigation and footer use `Free Access` or a natural localized equivalent instead of `Pricing`.
- The homepage and free-access page clearly state up to three free video-background removals in any rolling 24-hour period, no watermark, and no current paid option.
- The exact homepage title remains unchanged.
- Visible FAQ, metadata, Open Graph/Twitter derivatives, and structured data do not contradict one another.
- Old paid-plan changelog entries are clearly marked historical rather than deleted.
- Legal copy has documented human review and accurately reflects current code and data flows.
- No active copy describes BGRemove as narrow, boring, low-value, merely a demo/test, permanently limited, or unwilling to grow.
- Professional positioning is supported by concrete workflow value without invented proof or unsupported features.
- No copy promises permanent free access or blocks future monetization.
- Five current locales are updated together; Japanese and Korean are not added.
- Relevant build and content checks pass, and the Pull Request contains a complete before/after inventory.

## Out of scope

- Changing daily allowance, processing limits, feature access, authentication, payment code, database schema, or account behavior.
- Creating or deleting payment-provider products.
- New pages, URL migrations, redirects, keyword-expansion pages, or site redesign.
- GSC/ranking conclusions without data.
- Japanese or Korean localization.
- Deployment, publishing, or merging.
