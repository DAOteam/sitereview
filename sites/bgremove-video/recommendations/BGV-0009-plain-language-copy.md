---
task_id: "BGV-0009"
site_id: "bgremove-video"
title: "Make English user-facing copy easier to understand"
status: "approved"
priority: "P1"
source: "user+ai"
created_at: "2026-08-09"
updated_at: "2026-08-11"
prompt_version: 3
---

# BGV-0009 — Make English user-facing copy easier to understand

## Scope

Readability and natural-English review of the 15 primary English public marketing pages: homepage, About, Changelog, Contact, FAQ, How It Works, Free Access, four tool pages, and four use-case pages. This task does not cover legal copy, non-English localization, page structure, product behavior, or SEO metadata unless visible copy and metadata share the same incorrect factual statement.

## Current facts and evidence

Public pages were read line by line on 2026-08-09. The public production site was the only evidence source; no source repository was inspected.

The site now has a strong overall voice and several headings that are clear, memorable, and worth preserving. However, three recurring issues make parts of the site harder to understand than necessary:

1. Some copy assumes the reader already understands professional compositing terminology.
2. Some sentences prioritize wit or insider language over immediate meaning.
3. Two pages still contain factual remnants that conflict with the current product.

### P0 factual remnants discovered during the readability review

- `/use-cases/` still says `The free clip exists for exactly that. Ten seconds is enough...`, contradicting the current maximum duration of 60 seconds and the allowance of up to 3 successful videos per 24-hour window.
- `/contact/` still offers form topics `Billing or refunds` and `API and integration`, although BGRemove currently has no paid product and no public API.

These two misses were not identified by the previous exact-phrase verification and require correction regardless of the broader readability decision.

### Copy that should remain unchanged

- Homepage H1: `Remove video background online. Free, no watermark.`
- Homepage SEO title: `Remove Video Background Online Free - No Watermark`
- `/about/` H1: `Professional video matting, without the production overhead.`
- `/how-it-works/` H1: `From raw footage to a reusable transparent layer.`
- `/pricing/` H1: `Professional video cutouts. Free to use.`
- Current tool-page and use-case H1s.
- Primary CTA: `Remove My Video Background`
- Final CTA heading: `Your next transparent video is one upload away.`

### Live re-audit — 2026-08-11

Classification: `still_open`.

The 15 in-scope English production pages were checked again from the live site in a signed-in browser session. BGV-0009 has not been implemented:

- All four audited homepage old phrases remain, including `Three steps, one of which is yours.`, `a per-pixel matte is solved`, and `Exports open natively in the tools you already finish in`. None of the approved replacements appeared.
- All three audited About-page old passages remain and none of their approved replacements appeared.
- How It Works still contains the audited specialist or unclear phrases including `The first frame is segmented`, `temporal memory`, `muxed back into a container`, `Occlusion is survivable`, `Alpha channel baked in`, and `The queue is the whole interface`.
- Free Access still contains `True of every clip you run` and `A real alpha channel, not a matte painted onto grey`.
- Contact still displays `Billing or refunds` and `API and integration`; neither approved replacement is present.
- The Use Cases hub still contains the obsolete ten-second statement, while the approved 60-second and three-per-window replacement is absent. Shared use-case pages still contain four instances of `The matte is the asset, not the finished frame`, and creator/ecommerce still contain two `Cut to alpha` steps.
- Multiple approved tool-page terminology replacements remain undone, including `standoff so the light does not wrap`, `the key tears`, `cyclorama`, `Why the container matters`, `edge from swimming`, and the duplicate `Resolve, DaVinci` naming.
- Changelog retains the current free-access entry and historical labels, but still exposes old seconds-budget, 720p/1080p, ProRes, matte-only, and PNG-sequence details.
- The locked homepage SEO title and H1 remain correct and must continue to be preserved.

The full approved v3 prompt below remains in scope; no item is removed as already completed.

## User proposal

Review the main user-facing pages from the reader's perspective and identify English copy that is difficult, awkward, unclear, or unnatural.

## AI recommendation

Use progressive disclosure: lead with plain language that any video creator can understand, then introduce the professional term once with a short explanation. Keep `alpha channel`, `video matting`, `WebM`, and `VP9` where technically useful, but do not require the reader to understand `muxed`, `container`, `cyclorama`, `studio plate`, `specular highlight`, `occlusion`, or database terminology to understand the product.

### Priority replacements

| Page | Current copy | Why it is difficult | Recommended replacement |
|---|---|---|---|
| `/` | `Three steps, one of which is yours.` | Clever but unclear. | `Three simple steps from upload to transparent video.` |
| `/` | `Download transparent video, or put any background behind it` | Can sound as though BGRemove replaces the background inside the app. | `Download your transparent video and add any background in your editor.` |
| `/` | `a per-pixel matte is solved` | Passive and technical. | `The AI creates a precise transparent edge around your subject in every frame.` |
| `/` | `Exports open natively in the tools you already finish in` | `finish in` is unnatural. | `Open the result directly in the editing tools you already use.` |
| `/about/` | `lighting it with three heads they did not own` | `heads` is unexplained production jargon. | `setting up multiple lights and equipment they may not own` |
| `/about/` | Paragraph beginning `Video matting became commercially viable around 2025...` | Dense history, unsupported timing, and too much technical context before customer value. | `Modern video matting can keep a subject’s edge stable across frames, including hair and motion blur. BGRemove turns that technology into a simple online workflow for creators and editors.` |
| `/about/` | `a visitor who discovers that on their third upload...` | Hypothetical and oddly specific. | `We explain difficult footage before you upload, so you know what to expect from glass, overlapping subjects, and low-light video.` |
| `/how-it-works/` | `The first frame is segmented...` | `segmented` and `first-frame mask` assume technical knowledge. | `The AI finds your subject automatically, so you do not need to draw an outline before processing starts.` |
| `/how-it-works/` | `temporal memory`, `per-frame propagation`, `continuous alpha, 0 to 1` | Research terminology interrupts the explanation. | Explain the benefit first: `The AI follows your subject across frames to reduce flicker and keep edges stable as the video moves.` Keep technical terms only as optional secondary labels. |
| `/how-it-works/` | `The matte is muxed back into a container...` | `muxed` and `container` are unnecessary for most users. | `BGRemove exports the result as transparent WebM, preserving the alpha channel for editing and compositing.` |
| `/how-it-works/` | `Occlusion is survivable` | Unnatural phrasing and specialist terminology. | `The subject is easier to keep track of when an object briefly passes in front.` |
| `/how-it-works/` | `Alpha channel baked in` | `baked in` can imply flattened pixels and is technically confusing. | `Transparency preserved in the file.` |
| `/how-it-works/` | `The queue is the whole interface` | Cryptic and product-centered. | `A simple workflow from upload to download.` |
| `/faq/` | `it is where they beat frame-by-frame image cutouts by the widest margin` | Unclear pronouns and a broad comparative claim. | `Hair is one of the hardest edges to preserve. Following the subject across frames helps individual strands remain more stable than processing each frame separately.` |
| `/faq/` | `that deletion is immediate rather than a flag on a row` | Exposes database implementation language. | `When you delete a file, it is removed immediately.` |
| `/faq/` | `a row per job` | Database terminology is irrelevant to users. | `basic details for each processing job, such as its status and timestamps` |
| `/faq/` | `One provider means one place your credentials live` | Awkward and can create security confusion. | `Google sign-in lets you use BGRemove without creating another password.` |
| `/faq/` | `Still stuck? Write tosupport@bgremove.video.` | The source HTML has no space before the email link. | `Still stuck? Write to support@bgremove.video.` |
| `/pricing/` | `True of every clip you run` | Sounds unnatural. | `Included with every successful video` |
| `/pricing/` | `A real alpha channel, not a matte painted onto grey` | Mixes two specialist concepts. | `A genuinely transparent background you can change later` |

### Tool-page terminology

Keep the pages' professional credibility, but translate the first occurrence of specialist terms:

| Current term or phrase | Plain-language direction |
|---|---|
| `standoff so the light does not wrap` | Explain that the subject needs distance from the screen to prevent green reflections. |
| `the key tears` | `the cutout develops uneven or broken edges` |
| `spill pass in the grade` | `remove green reflections from skin, hair, and clothing during editing` |
| `cyclorama` | `dedicated studio backdrop` |
| `studio plates` | `controlled studio footage` |
| `contact shadow in the final composite` | `a realistic shadow in the finished edit` |
| `One matte serves all three` | `One transparent video works across all three.` |
| `locked to its backdrop the moment it is graded` | `locked to its original background once the edit is finalized` |
| `shot on a sweep` | `filmed on a studio backdrop` |
| `specular highlights` | `natural reflections and highlights` |
| `manual cleanup pass on those SKUs` | `manual edge cleanup on those products` |
| `Why the container matters` | `Why the file format matters` |
| `per-pixel transparency value ... fourth channel` | Explain first that each pixel can be fully visible, partly transparent, or invisible; name the alpha channel second. |
| `edge from swimming` | `edge from wobbling or shifting between frames` |
| `motion artefacts read at any resolution` | `flicker remains visible even on a small phone screen` |

Also remove the duplicate naming in `Works in CapCut, Premiere, Resolve, DaVinci, the browser`; Resolve and DaVinci Resolve are the same product.

### Use-case pages

- Replace `/use-cases/` opening `Different footage, different failure modes... what is sitting on your drive` with: `Different footage creates different edge challenges. Choose the workflow that best matches your video.`
- Replace every `The matte is the asset, not the finished frame` with: `The transparent video becomes a reusable asset for every version you create.`
- Replace `Cut to alpha` with `Remove the background` in creator and ecommerce workflow steps.
- Replace `Ratings come from the failure modes of the underlying matting models, not from a marketing deck.` with: `These notes show where BGRemove works well and where footage may need extra review.`
- Replace `occlusion` with `objects passing in front of the subject` on the Agency page.
- Replace ecommerce terms `studio sweep`, `lifestyle plate`, `specular highlights`, and `budget a manual pass` with `studio background`, `lifestyle footage`, `natural reflections`, and `plan for some manual edge cleanup`.
- Replace shared `Run one clip through it.` headings with the more action-oriented `Create your transparent video.`
- Remove the obsolete `/use-cases/` sentence about one free ten-second clip. Recommended replacement: `Not sure which workflow fits? Upload a real clip up to 60 seconds long and turn it into a reusable transparent video. Each signed-in account can complete up to 3 successful videos per 24-hour allowance window.`

### Contact and Changelog

- Replace Contact form topic `Billing or refunds` with `Account and free access`.
- Replace Contact form topic `API and integration` with `Product question` or remove it if `Something else` is sufficient.
- Keep Changelog's current top entry. Shorten older historical entries to the release title, date, and one-sentence summary, or visually collapse them by default. Detailed obsolete allowance, resolution, output-format, and internal cost explanations make the current rules harder to identify even though they are labelled historical.

### Voice rules for the rewrite

- Preserve the confident, marketing-forward tone.
- Do not make every sentence short or generic; keep vivid lines when their meaning is immediate.
- Explain the result before the mechanism: `stable transparent edge` before `temporal matting`, and `transparent file` before `alpha channel`.
- Use one main idea per sentence.
- Prefer familiar verbs: `find`, `follow`, `remove`, `keep`, `download`, `add`, and `reuse`.
- Do not remove accurate limitations or professional terms that help high-intent editors; define them in plain language at first use.
- Do not introduce unsupported speed, quality, compatibility, customer, or performance claims.

## Open decisions

Resolved on 2026-08-09. The user approved all three recommended options without modification.

## Final decision

Confirmed by the user on 2026-08-09:

- Apply one English-only readability pass across all 15 reviewed marketing pages, including both mandatory factual corrections.
- On `/how-it-works/`, use plain-language explanations as the primary copy and keep concise technical labels only as secondary detail for professional credibility.
- Keep historical Changelog entries, but shorten obsolete details in place. Do not add a collapse interaction or redesign the page.
- Apply every exact replacement and terminology direction under `AI recommendation` unless the quoted live sentence has already changed before execution.
- Preserve all copy listed under `Copy that should remain unchanged`, including the locked homepage title and H1 and all currently approved page H1s.
- Preserve the marketing-forward, confident voice while making body copy easier for ordinary creators and light-to-moderate editors to understand.
- Change English only. Do not localize Spanish, Portuguese, French, or German and do not add Japanese or Korean.

## Implementation prompt

```text
Delivery method: direct_publish.
This is the approved BGV-0009 prompt version 3. A live re-audit on 2026-08-11 found the full task still open. Use the programming AI's existing production-connected code environment. Do not inspect or use DAOteam/bgremove. Run the required checks and publish only the approved English visible-copy scope. Do not create a Pull Request or write an execution result to the recommendation repository.

Goal
Make the 15 primary English marketing pages easier to understand without flattening the confident brand voice or removing useful professional credibility. Lead with the user-visible result, explain technical terms in plain language at first use, and keep concise specialist labels only as secondary detail.

Public evidence and scope
1. Before editing, fetch the current public version of each page in BGV-0009 Scope. The public site is the only evidence of what still needs correction.
2. Apply every approved replacement, terminology mapping, use-case instruction, Contact correction, Changelog instruction, and voice rule under BGV-0009 `AI recommendation`.
3. If an exact quoted sentence has already been corrected online, skip it rather than rewriting the surrounding section.
4. Change visible English copy only, plus the minimum shared content or visible-label logic required to render it correctly.
5. When an edited FAQ answer also appears in FAQPage JSON-LD, keep the visible and structured versions identical in meaning.

Mandatory factual corrections
1. On `/use-cases/`, remove the obsolete one-free-ten-second-clip statement. Replace it with: `Not sure which workflow fits? Upload a real clip up to 60 seconds long and turn it into a reusable transparent video. Each signed-in account can complete up to 3 successful video background removals per 24-hour allowance window.`
2. On `/contact/`, replace visible topic `Billing or refunds` with `Account and free access`.
3. On `/contact/`, replace visible topic `API and integration` with `Product question`. Preserve internal form values or backend contracts if changing them would alter form behavior; this task authorizes the user-facing label change, not a backend integration change.

Required readability treatment
1. Apply every exact row in `Priority replacements`.
2. Apply every mapping and instruction in `Tool-page terminology`, including removing the duplicate Resolve/DaVinci naming.
3. Apply every instruction in `Use-case pages`.
4. On `/how-it-works/`, put the plain-language benefit in the primary body copy. Keep terms such as temporal memory, per-frame propagation, continuous alpha, and VP9 only as concise secondary labels where the existing design already supports secondary detail. Do not add a new interaction or redesign.
5. Define `alpha channel`, `video matting`, `WebM`, and `VP9` in plain language at first meaningful use. Later occurrences may use the short professional term.
6. Remove database implementation language, unexplained production jargon, unclear pronouns, passive constructions, and clever phrases whose meaning is not immediate.
7. Preserve vivid, concise lines whose meaning is already clear. Do not turn the site into generic SaaS copy.

Changelog treatment
1. Preserve the current top `Current free access` entry and its current facts.
2. Preserve each older entry's date, version, title, and `Historical configuration — no longer current` status where applicable.
3. Shorten each older entry in place to one plain-language summary sentence.
4. Remove visible obsolete detail about old allowances, clip counts, seconds budgets, resolution tiers, output formats, and internal processing cost. Do not add accordions, collapse controls, or other UI changes.

Locked content and boundaries
- Preserve homepage SEO title exactly: `Remove Video Background Online Free - No Watermark`.
- Preserve homepage H1 exactly: `Remove video background online. Free, no watermark.`
- Preserve every H1 and CTA listed under `Copy that should remain unchanged` and all other current tool/use-case H1s.
- Preserve current product facts: sign-in required; first successful job starts the 24-hour window; up to 3 successful jobs; failed jobs do not count; full reset when the window ends; 60-second maximum; no separate file-size cap; MP4/MOV/WebM/M4V/GIF input; source dimensions preserved; transparent WebM using VP9 with alpha; no watermark; 24-hour retention; no background replacement, batch processing, refinement, API, webhooks, or paid option.
- Do not change product logic, account behavior, authentication, processing, retention, formats, form submission behavior, databases, infrastructure, legal pages, SEO metadata, URL structure, page layout, or navigation.
- Do not change Spanish, Portuguese, French, or German pages and do not add Japanese or Korean.
- Do not add unsupported speed, quality, compatibility, customer, cost, or performance claims.

Verification before publication
1. Run relevant content, type, and build checks.
2. Render or crawl all 15 English pages from a production-like build.
3. Search for every old phrase and specialist term listed in BGV-0009. Explain or remove each remaining match according to the approved rules.
4. Confirm `/use-cases/` contains no current ten-second rule and accurately states the 60-second and 3-per-window rules.
5. Confirm Contact no longer shows `Billing or refunds` or `API and integration`, and verify form submission behavior is unchanged.
6. Confirm FAQ visible answers and FAQPage JSON-LD remain aligned.
7. Confirm the locked homepage title, homepage H1, all approved page H1s, and primary/final CTA copy are unchanged.
8. Confirm no product fact, paid option, unsupported feature, or permanent-free promise was introduced.
9. Spot-check the corresponding Spanish, Portuguese, French, and German routes for English-copy leakage.
10. After checks pass, publish directly through the existing production workflow. Do not mark this task verified; the recommendation AI will perform the next live audit.
```

## Acceptance criteria

- All exact replacements and terminology directions under `AI recommendation` are present in the live English pages where the old copy still existed at execution time.
- No visible page states a ten-second current limit, a paid support topic, or a current API support topic.
- `/use-cases/` accurately states the 60-second maximum and up to 3 successful video background removals per 24-hour allowance window.
- Contact uses `Account and free access` and `Product question`, and form submission behavior remains unchanged.
- Plain-language benefits precede technical labels on `/how-it-works/`; remaining specialist terms are necessary and explained at first meaningful use.
- Historical Changelog entries retain their dates, versions, titles, and historical status but no longer expose obsolete detailed allowances, resolution tiers, output formats, or internal cost explanations.
- The homepage SEO title, homepage H1, approved page H1s, primary CTA, final CTA heading, and confirmed product facts are unchanged.
- FAQ visible answers and FAQPage JSON-LD remain aligned in meaning.
- No unsupported claim, paid option, unsupported feature, permanent-free promise, or English-copy leakage into deferred locales is introduced.
- Relevant checks pass, and final completion is verified only from the public production site.

## Out of scope

- Changing the homepage H1 or approved page H1s.
- Product behavior, allowance logic, authentication, processing, retention, formats, or feature access.
- Non-English localization.
- Page redesign, navigation changes, new pages, URL changes, or SEO keyword expansion.
- Legal-page rewriting.
