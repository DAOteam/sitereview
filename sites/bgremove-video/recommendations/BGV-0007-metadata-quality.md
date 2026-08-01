---
task_id: "BGV-0007"
site_id: "bgremove-video"
title: "Improve core-page titles and metadata quality"
status: "needs_decision"
priority: "P1"
source: "user+ai"
created_at: "2026-08-01"
updated_at: "2026-08-01"
prompt_version: 2
---

# BGV-0007 — Improve core-page titles and metadata quality

## Scope

Audit and improve the SEO titles and meta descriptions for the 15 core page patterns in the five current locales: English, Spanish, Portuguese, German, and French. This task covers metadata sources and shared title-generation logic, not page-body rewrites.

The five English legal pages are excluded. Pricing metadata is documented here but remains an implementation dependency of BGV-0006 because it must not publish the new commercial terms before that task is approved and implemented.

## Current facts and evidence

Public crawl performed on 2026-08-01:

- All 80 URLs found in the public sitemap returned HTTP 200.
- No crawled page was missing a title, meta description, H1, or canonical.
- No duplicate title or meta description was found within the same locale.
- All crawled canonicals were self-referencing and every page exposed six hreflang entries.
- The English homepage title is malformed: it repeats a long list of integration and editing-tool names twice after the brand.
- The pricing description still advertises the old daily-free allowance and the old Creator and Studio prices.
- The core remove-background tool description advertises PNG sequence output, which conflicts with the confirmed transparent-output format list.
- Several informational and hub-page titles are generic, including `About | BGRemove`, `FAQ | BGRemove`, `How it works | BGRemove`, and `Use cases | BGRemove`.
- Character-count review found 22 titles over 60 characters, 36 titles under 30 characters, 16 descriptions over 165 characters, and 4 descriptions under 110 characters. These are review heuristics only, not Google limits.
- GSC is not connected, so this audit makes no claim about impressions, click-through rate, rankings, or which query Google currently uses for each page.

## User proposal

Review the website with the SEO audit workflow and improve weak titles and meta descriptions. The user specifically identified that many page titles and descriptions do not communicate the pages well.

## AI recommendation

Prioritize metadata that is malformed, inaccurate, stale, generic, or poorly aligned with page intent. Do not rewrite good, unique descriptions merely to reach a character-count target.

Fix the shared title-generation source that appends repeated tool names to the homepage. Use one clear primary intent per title, keep the brand once, and avoid keyword stuffing or repeated boilerplate.

The following English titles are the approved source copy:

| Page | Proposed English title |
|---|---|
| `/` | `Remove Video Background Online Free – No Watermark | BGRemove` |
| `/about/` | `About BGRemove | AI Video Background Remover` |
| `/changelog/` | `BGRemove Changelog | Video Background Remover Updates` |
| `/contact/` | `Contact BGRemove Support | Video Background Removal Help` |
| `/faq/` | `Video Background Remover FAQ | BGRemove` |
| `/how-it-works/` | `How AI Video Background Removal Works | BGRemove` |
| `/pricing/` | `Video Background Remover Pricing | BGRemove` |
| `/tools/green-screen-alternative/` | `Green Screen Alternative for Video | BGRemove` |
| `/tools/product-video-background-remover/` | `Product Video Background Remover | BGRemove` |
| `/tools/remove-background-from-video/` | `Remove Background from Video Online | BGRemove` |
| `/tools/tiktok-background-remover/` | `TikTok Video Background Remover | BGRemove` |
| `/use-cases/` | `Video Background Removal Use Cases | BGRemove` |
| `/use-cases/agencies/` | `Video Matting & Rotoscoping for Agencies | BGRemove` |
| `/use-cases/creators/` | `Remove Video Background for Creators | BGRemove` |
| `/use-cases/ecommerce/` | `Ecommerce Video Background Remover | BGRemove` |

Recommended English description changes:

| Page | Action | Proposed English description |
|---|---|---|
| `/` | Replace only with or after BGV-0006 | `Remove video backgrounds online with AI. Start with 5 free seconds, export transparent WebM with no watermark, or unlock more formats and background replacement.` |
| `/pricing/` | Owned by BGV-0006 | `Start with 5 free credits, buy a one-time credit pack, or subscribe monthly or yearly. Compare BGRemove plans for video background removal.` |
| `/tools/remove-background-from-video/` | Replace inaccurate format list | `Remove a video background online and export transparent WebM VP9, MOV ProRes, or MKV VP9. No green screen or frame-by-frame masking.` |
| Other core pages | Preserve by default | Keep the current unique, page-specific description unless a locale review finds an inaccurate claim or unnatural wording. |

Translate by meaning and search intent, not word for word. Each localized title and description must be written naturally in its page language and must preserve the same product facts. Do not add Japanese or Korean in this task.

## Open decisions

- Choose whether the five current locales are delivered in one Pull Request or whether English is approved first and localized copy follows. The AI recommendation is to approve English as the source first, then include all five current locales in one implementation Pull Request after localized copy review.
- BGV-0006 must be approved before the homepage and pricing descriptions can publish the new free-credit and paid-feature rules.

## Final decision

On 2026-08-01, the user approved the complete 15-page English title matrix in this document.

The task remains `needs_decision` until the localization delivery approach is confirmed and the BGV-0006 dependency is resolved. Approval of the English titles alone does not authorize implementation.

## Implementation prompt

```text
Draft only. Do not execute until this task has status: "approved".

Target repository: https://github.com/DAOteam/bgremove
Delivery method: Pull Request. Never commit directly to the default branch and do not deploy.

Goal
Improve title and meta-description quality for the 15 approved core page patterns in English, Spanish, Portuguese, German, and French. Fix the malformed homepage title output while preserving the site's currently healthy canonical and hreflang implementation.

Before editing
1. Locate the actual metadata source for every scoped route and the shared title-generation or SEO component.
2. Identify why the English homepage appends the integration/tool-name list twice. Fix the source or composition logic; do not hide the rendered result with client-side manipulation.
3. Confirm whether BGV-0006 is approved and implemented. If not, do not publish homepage or pricing copy that states its new credits, prices, retention, formats, or feature-access rules. Record that dependency in the result file.
4. Inspect the existing user-facing mapping for the exact transparent format identifiers `webm_vp9`, `mov_proresks`, and `mkv_vp9`. Use accurate, existing display labels and do not invent a codec profile.

Required changes
1. Apply the approved English title matrix from BGV-0007 to the corresponding routes.
2. Create natural, intent-equivalent localized titles for Spanish, Portuguese, German, and French. Do not mechanically translate or force an English word order.
3. Update the remove-background tool description so it no longer advertises PNG sequence output and describes only confirmed transparent formats.
4. Update the homepage and pricing descriptions only when the BGV-0006 dependency permits it. Remove old daily-free, Creator $19, Studio $49, and PNG sequence claims wherever they occur in scoped metadata once their replacement facts are approved.
5. Preserve the other current descriptions by default. Change one only when it is inaccurate, duplicated by the metadata template, or unnatural in that locale, and explain the reason in the Pull Request.
6. Keep title, meta description, Open Graph title/description, and Twitter title/description semantically consistent where those fields exist.
7. Keep legal-page metadata unchanged. Do not add Japanese or Korean.

Writing constraints
- Give every page one clear search intent and a unique, descriptive title.
- Use `BGRemove` no more than once in a title.
- Avoid keyword stuffing, repeated integration names, generic boilerplate, unsupported superlatives, and invented product claims.
- Treat character counts as review signals, not hard pass/fail limits. Prefer clear, accurate copy that is likely to display well.
- Preserve the current locale on every localized route.

Do not change
- H1s, body copy, page layout, pricing implementation, billing logic, structured data, canonical URLs, hreflang architecture, robots directives, sitemap routing, or deployment configuration unless a minimal metadata-source fix strictly requires it.
- Do not expand scope to keyword-cannibalization decisions that require GSC evidence.

Verification
1. Run the fastest relevant build, typecheck, or metadata tests available in the repository.
2. Render or extract metadata for all 80 current sitemap URLs in a production-like build.
3. Confirm every URL still has a title, meta description, H1, self-referencing canonical, and the existing six hreflang entries.
4. Confirm no title or description duplicates within a locale.
5. Confirm the homepage title contains no appended or duplicated integration/tool-name list.
6. Confirm scoped metadata contains no stale pricing claims or PNG sequence claim after the relevant dependency is implemented.
7. Confirm all titles and descriptions match the route language and all factual claims match the approved product rules.
8. Include before/after metadata tables, commands run, results, and any BGV-0006 dependency in the result file and Pull Request.
```

## Acceptance criteria

- All 15 core page patterns have unique, descriptive, intent-aligned titles in each of the five current locales.
- The English homepage title is exactly the approved copy and contains no duplicated tool-name suffix.
- The core remove-background tool metadata no longer advertises PNG sequence output.
- Homepage and pricing descriptions do not expose unapproved commercial terms and, after BGV-0006 implementation, contain no old daily-free or old-price claims.
- Existing descriptions that are already accurate, unique, and page-specific are preserved unless the Pull Request documents a clear reason to change them.
- Open Graph and Twitter metadata remain semantically aligned with the normal title and description where implemented.
- All 80 current sitemap URLs continue to return a title, meta description, H1, self-referencing canonical, and the existing hreflang set.
- No new duplicate title or description is introduced within a locale.
- Build and relevant checks pass, and the Pull Request contains a before/after metadata table.

## Out of scope

- Legal-page copy rewrites.
- H1, body copy, page layout, or conversion-flow changes.
- Pricing or billing implementation; that belongs to BGV-0006.
- Keyword-cannibalization decisions without GSC data.
- Japanese or Korean localization.
- Deployment or publishing.
