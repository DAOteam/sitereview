---
task_id: "BGV-0009"
site_id: "bgremove-video"
title: "Make English user-facing copy easier to understand"
status: "approved"
priority: "P1"
source: "user+ai"
created_at: "2026-08-09"
updated_at: "2026-08-11"
prompt_version: 6
scope_fingerprint: "sha256:388761f5c11d039f1e6c96a47a02802db92e70310adf108dc5a01f7a2cf3e658"
---

# BGV-0009 — Make English user-facing copy easier to understand

## Active execution scope

<!-- ACTIVE_SCOPE_START -->
Prompt version: 6

### BGV-0009-A — Homepage editing-tools sentence

- Target: `https://bgremove.video/`
- Required present: `Open the result directly in the editing tools you already use.`
- Required absent: `Exports open natively in the tools you already finish in`
- Verification: assert the rendered English homepage contains the required sentence, excludes the old phrase, and preserves the locked title and H1 before and after publication.

### BGV-0009-B — FAQ email spacing

- Target: `https://bgremove.video/faq/`
- Required present: visible text `Still stuck? Write to support@bgremove.video.` and link target `mailto:support@bgremove.video`
- Required absent: visible text `Write tosupport@bgremove.video`
- Verification: assert both rendered text spacing and the working mail link before and after publication; keep matching structured content aligned in meaning.

### BGV-0009-C — Plain-language transparency explanation

- Target: `https://bgremove.video/tools/remove-background-from-video/`
- Required present: `Each pixel can be fully visible, partly transparent, or invisible.` followed by the approved alpha-channel explanation in the Implementation prompt.
- Required absent: `The tool computes a per-pixel transparency value and stores it as a fourth channel`
- Verification: assert the rendered paragraph leads with the required plain-language sentence and excludes the old tool-centered opening before and after publication.
<!-- ACTIVE_SCOPE_END -->

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

### Second live re-audit — 2026-08-11

Classification: `partially_applied`.

The same 15 live English pages were checked again after a new publication. Most of BGV-0009 is now online:

- About, How It Works, Free Access, Contact, the use-case pages, and almost all tool-page terminology now follow the approved clearer wording.
- Contact now displays `Account and free access` and `Product question`.
- The Use Cases hub now states the 60-second maximum and three successful removals per 24-hour allowance window; the obsolete ten-second statement is absent.
- All four shared reusable-asset lines and both `Cut to alpha` steps were replaced as approved.
- Changelog now uses short `Historical entry` summaries. Its remaining generic sentence mentioning that old entries may have contained a `seconds budget` is a current-state disclaimer, not obsolete detailed allowance information, so it is accepted.
- The locked homepage SEO title and H1 remain unchanged.

Only these three items remain open for prompt version 4:

1. Homepage still says `Exports open natively in the tools you already finish in, Adobe Premiere Pro and After Effects included.`
2. FAQ still renders `Still stuck? Write tosupport@bgremove.video.` without a space before the email link.
3. `/tools/remove-background-from-video/` still leads with `The tool computes a per-pixel transparency value and stores it as a fourth channel...` instead of first explaining in plain language that pixels can be fully visible, partly transparent, or invisible and naming the alpha channel second.

### Third live re-audit — 2026-08-11

Classification: `still_open` with no change since prompt version 4.

- The homepage still renders `Exports open natively in the tools you already finish in, Adobe Premiere Pro and After Effects included.` and does not render the approved replacement.
- FAQ still visibly renders `Still stuck? Write tosupport@bgremove.video.` without a space before the working email link.
- `/tools/remove-background-from-video/` still begins the transparency explanation with `The tool computes a per-pixel transparency value and stores it as a fourth channel...`; the approved visible/partly transparent/invisible explanation is absent.
- The locked homepage SEO title and H1 remain exact. The previously corrected Contact labels, Use Cases allowance statement, shortened Changelog entries, and other audited plain-language replacements show no detected regression across the 15 in-scope English pages.

Prompt version 5 therefore retains the same three-item implementation scope and removes nothing further.

### Handoff protocol refresh — 2026-08-11

Prompt version 6 keeps the same three substantive items as version 5. It adds stable item IDs, an active-scope fingerprint, deterministic present/absent assertions, a required execution-attempt receipt, and post-publication production smoke checks. No previously completed copy is returned to scope.

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
This is the approved BGV-0009 prompt version 6. The substantive scope is unchanged from version 5; version 6 adopts the repository's active-scope handshake and receipt protocol. Validate the scope fingerprint, create a versioned execution-attempt receipt, use the programming AI's current production-connected environment, and publish only the remaining scope below after every required item passes. Do not use DAOteam/bgremove as an execution handoff or production-status source, create a Pull Request, or modify recommendation files. Creating and updating the required non-authoritative receipt under this site's `results/` directory is allowed and required.

1. BGV-0009-A — Homepage compatible-software sentence
- Replace `Exports open natively in the tools you already finish in, Adobe Premiere Pro and After Effects included.` with `Open the result directly in the editing tools you already use.`

2. BGV-0009-B — FAQ email spacing
- Fix the visible FAQ sentence so it renders exactly as `Still stuck? Write to support@bgremove.video.` with a space between `to` and the linked email address.
- Keep the email address as a working mail link and keep any matching FAQPage JSON-LD aligned in meaning.

3. BGV-0009-C — Plain-language transparency explanation
- On `/tools/remove-background-from-video/`, replace the paragraph beginning `The tool computes a per-pixel transparency value and stores it as a fourth channel...` with:
  `Each pixel can be fully visible, partly transparent, or invisible. That transparency is stored in an alpha channel alongside the file's red, green, and blue colour channels. Nothing is behind your subject. What goes there is decided later, in your editor, as many times as you like.`
- Lead with the visible/partly transparent/invisible explanation exactly as written; keep `alpha channel` as the secondary professional term.

Boundaries and regression checks
- Preserve all other English copy already corrected under BGV-0009, including Contact labels, Use Cases allowance facts, shortened Changelog entries, How It Works explanations, About copy, Free Access copy, and other tool/use-case terminology.
- Preserve homepage SEO title exactly: `Remove Video Background Online Free - No Watermark`.
- Preserve homepage H1 exactly: `Remove video background online. Free, no watermark.`
- Preserve approved H1s and CTAs, product behavior and facts, URLs, layout, navigation, legal pages, form behavior, and all non-English pages.
- Do not introduce unsupported claims, paid options, unsupported features, or permanent-free promises.
- Run relevant content, type, and build checks; confirm the three old strings are absent and the three approved replacements render correctly.
- After checks pass, publish this exact remaining scope through the existing direct-to-production workflow. Do not mark the task verified; the recommendation AI will verify the live site.
```

## Acceptance criteria

- `BGV-0009-A`: Homepage displays `Open the result directly in the editing tools you already use.` and no longer contains `Exports open natively in the tools you already finish in`.
- `BGV-0009-B`: FAQ visibly renders `Still stuck? Write to support@bgremove.video.` with correct spacing and a working email link; matching structured content remains aligned in meaning.
- `BGV-0009-C`: `/tools/remove-background-from-video/` leads with the approved fully visible/partly transparent/invisible explanation before naming the alpha channel, and the old tool-centered sentence is absent.
- All previously verified BGV-0009 copy remains unchanged and no old ten-second, paid-support, API-support, detailed Changelog, or deferred-locale regression appears.
- The homepage SEO title, homepage H1, approved page H1s, CTAs, confirmed product facts, layout, navigation, form behavior, and non-English pages remain unchanged.
- No unsupported claim, paid option, unsupported feature, or permanent-free promise is introduced.
- Final completion is verified only from the public production site.

## Out of scope

- Changing the homepage H1 or approved page H1s.
- Product behavior, allowance logic, authentication, processing, retention, formats, or feature access.
- Non-English localization.
- Page redesign, navigation changes, new pages, URL changes, or SEO keyword expansion.
- Legal-page rewriting.
