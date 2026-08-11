---
site_id: "bgremove-video"
name: "BGRemove"
production_url: "https://bgremove.video/"
delivery_method: "direct_publish"
target_repository: "not_applicable"
default_branch: "not_applicable"
updated_at: "2026-08-11"
---

# BGRemove current tasks

## Approved tasks

### Replace the homepage editing-tools sentence

- Priority: `P1`
- Page or surface: `https://bgremove.video/`
- Problem and live evidence: The homepage still displays `Exports open natively in the tools you already finish in, Adobe Premiere Pro and After Effects included.`
- Required change: Replace it with `Open the result directly in the editing tools you already use.`
- Acceptance criteria: The approved sentence is visible and the old phrase is absent. Keep the SEO title exactly `Remove Video Background Online Free - No Watermark` and the H1 exactly `Remove video background online. Free, no watermark.`
- Do not change: Other homepage copy, layout, navigation, product behavior, or non-English pages.

### Fix the FAQ support-email spacing

- Priority: `P1`
- Page or surface: `https://bgremove.video/faq/`
- Problem and live evidence: The visible sentence renders as `Still stuck? Write tosupport@bgremove.video.`
- Required change: Render exactly `Still stuck? Write to support@bgremove.video.` while keeping `support@bgremove.video` linked to `mailto:support@bgremove.video`. Keep matching structured content aligned in meaning.
- Acceptance criteria: The visible sentence contains the required space, the email link works, and `Write tosupport@bgremove.video` is absent.
- Do not change: Other FAQ content, page structure, or non-English pages.

### Lead the transparency explanation with plain language

- Priority: `P1`
- Page or surface: `https://bgremove.video/tools/remove-background-from-video/`
- Problem and live evidence: The explanation still begins `The tool computes a per-pixel transparency value and stores it as a fourth channel...` before explaining the visible result.
- Required change: Replace that paragraph with `Each pixel can be fully visible, partly transparent, or invisible. That transparency is stored in an alpha channel alongside the file's red, green, and blue colour channels. Nothing is behind your subject. What goes there is decided later, in your editor, as many times as you like.`
- Acceptance criteria: The paragraph begins with the approved visible/partly transparent/invisible explanation and the old tool-centered opening is absent.
- Do not change: The page H1, other tool copy, product behavior, output format, or non-English pages.

### Remove stale billing language from the account introduction

- Priority: `P1`
- Page or surface: Authenticated English `https://bgremove.video/app/account/`
- Problem and live evidence: The introduction still says `Plan, billing and data. Everything destructive on this page asks once and then does exactly what it says.` even though there is no current paid plan or billing option.
- Required change: Replace it with `Account and data. Everything destructive on this page asks once and then does exactly what it says.`
- Acceptance criteria: The approved introduction is visible and `Plan, billing and data.` is absent. The separate invoice-retention sentence remains.
- Do not change: Authentication, account data actions, historical invoice records, allowance behavior, or non-English account pages.

### Show the authoritative allowance reset date and time

- Priority: `P1`
- Page or surface: Both reset summaries on authenticated English `https://bgremove.video/app/account/`
- Problem and live evidence: The active allowance window shows only `Resets 11 Aug 2026` and `Resets 11 Aug`, without a visible time or semantic timestamp.
- Required change: When a window is active, show the same authoritative next full-reset date and time in both summaries using existing server/account quota data. Use semantic `<time>` elements with the authoritative `datetime`. When no window has started, do not fabricate a timestamp; use an existing truthful state or explain that the window starts with the first successful video.
- Acceptance criteria: An active window shows the same real date and time in both summaries. A safe existing fixture or automated test verifies the no-window state. `Free`, `No charge`, `Up to 3 videos per 24-hour period`, `Up to 60 seconds per video`, and the invoice-retention sentence remain. No paid cards, prices, `See plans`, `Get notified`, paid CTA, or empty paid-plan container appears.
- Do not change: Allowance calculation, successful-job counting, failed-job treatment, authentication, processing, retention, downloads, historical records, the public pricing page, or non-English pages.
