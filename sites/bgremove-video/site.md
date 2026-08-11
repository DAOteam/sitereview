---
site_id: "bgremove-video"
task_prefix: "BGV"
name: "BGRemove"
production_url: "https://bgremove.video/"
target_repository: "not_applicable"
default_branch: "not_applicable"
delivery_method: "direct_publish"
audit_source: "public_production"
recommendation_owner: "website-growth-ai"
execution_owner: "code-execution-ai"
---

# BGRemove

## Business context

- Current strategy: BGRemove is temporarily a completely free product with no paid plans, subscriptions, credit packs, or paid upgrades.
- Free allowance: The first successful job starts a 24-hour window. Up to three successful jobs may complete in it; failed jobs do not count. The full allowance resets to three when the window ends.
- Primary conversion: Sign in, complete a successful free video-background removal, and return after the allowance resets.
- Growth goal: Improve useful engagement, repeat visits, brand trust, and organic-search authority before introducing monetization later.
- Copy direction: Confident and marketing-forward. Lead with the transparent result, motion-edge value, asset reuse, and editing/compositing outcomes; use free access as the conversion risk-reversal.
- Locked homepage H1: `Remove video background online. Free, no watermark.`
- Audience: Video creators and editors.
- Markets: United States, Canada, Europe, Australia and Oceania, Japan, Korea, and Singapore.
- Current languages: English, Spanish, Portuguese, French, and German.
- Planned languages: Japanese and Korean, deferred until current locales are stable.
- Current content rollout: English first. Spanish, Portuguese, French, and German changes require separate user authorization after the English implementation is complete.

## Execution boundary

- Recommendations live in this repository.
- The programming AI uses its own current production-connected code environment and publishes approved changes directly.
- `DAOteam/bgremove` is not used for execution handoff, implementation-state checks, or production verification.
- The programming AI does not create Pull Requests for BGRemove. It writes a versioned execution-attempt receipt under `results/`; the receipt records diagnostics but is never production-verification evidence.
- The execution AI may act only on tasks with `status: "approved"`.
- Direct publication is authorized only for the exact scope of an approved recommendation whose implementation prompt allows publication. Billing-product creation and unrelated production configuration still require separate authorization.

## Audit evidence boundary

- The current public production site at `https://bgremove.video/` is the only source of truth for content audits and implementation verification.
- Do not inspect or use `DAOteam/bgremove` to infer what is online, whether a recommendation has been implemented, or why a public page has not changed.
- Do not infer production status from recommendation/result files, commits, branches, or Pull Requests; fetch and inspect the relevant public URL.
- The user confirms that code is maintained and published through a separate direct-to-production workflow. The recommendation AI never publishes; it verifies the next public version directly.
- At each audit, compare the latest approved recommendation item by item with current public pages. Omit verified items from the next scope, and carry unimplemented or partially implemented items into the next `prompt_version` under the same task ID.
- Execution receipts may distinguish not-claimed, stale-version, blocked, partial, published, and smoke-test outcomes, but they must never determine whether an item is online.
