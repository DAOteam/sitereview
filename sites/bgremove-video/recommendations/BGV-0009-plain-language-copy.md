---
task_id: "BGV-0009"
site_id: "bgremove-video"
title: "Make English user-facing copy easier to understand"
status: "needs_decision"
priority: "P1"
source: "user+ai"
created_at: "2026-08-09"
updated_at: "2026-08-09"
prompt_version: 1
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

1. Approve one English-only readability pass across all 15 reviewed marketing pages, including the two mandatory factual fixes? AI recommendation: yes.
2. On `/how-it-works/`, keep technical labels as secondary detail beneath plain-language explanations, or remove most research terminology entirely? AI recommendation: keep concise secondary labels for professional credibility.
3. For historical Changelog entries, shorten obsolete detail in place or collapse older entries in the interface? AI recommendation: shorten them in place to avoid a UI change.

## Final decision

Pending user confirmation. This recommendation is not executable.

## Implementation prompt

```text
NOT EXECUTABLE. BGV-0009 has status needs_decision. Wait until the user confirms the scope, technical-detail treatment, and Changelog treatment, then replace this block with a complete versioned implementation prompt.
```

## Acceptance criteria

- Provisional: all approved visible-copy replacements are present on the live English pages.
- Provisional: no visible page states a ten-second current limit, a paid support topic, or a current API support topic.
- Provisional: specialist terms are either necessary for the page's intent or explained in plain language at first use.
- Provisional: locked titles, H1s, factual product rules, structured data meaning, and non-English pages are unchanged unless explicitly approved.
- Provisional: final completion is verified only from the public production site.

## Out of scope

- Changing the homepage H1 or approved page H1s.
- Product behavior, allowance logic, authentication, processing, retention, formats, or feature access.
- Non-English localization.
- Page redesign, navigation changes, new pages, URL changes, or SEO keyword expansion.
- Legal-page rewriting.
