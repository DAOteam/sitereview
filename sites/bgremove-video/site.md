---
site_id: "bgremove-video"
task_prefix: "BGV"
name: "BGRemove"
production_url: "https://bgremove.video/"
target_repository: "https://github.com/DAOteam/bgremove"
default_branch: "main"
delivery_method: "pull_request"
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
- Website source code repository: `https://github.com/DAOteam/bgremove`.
- Code changes must be delivered through a Pull Request; direct commits to the default branch are not allowed.
- The execution AI may act only on tasks with `status: "approved"`.
- Deployment, billing-product creation, and production configuration require separate authorization.

## Audit evidence boundary

- The current public production site at `https://bgremove.video/` is the only source of truth for content audits and implementation verification.
- Do not inspect or use `DAOteam/bgremove` to infer what is online, whether a recommendation has been implemented, or why a public page has not changed.
- Do not infer production status from recommendation/result files, commits, branches, or Pull Requests; fetch and inspect the relevant public URL.
- The user reports that code is maintained and published through a separate direct-to-production workflow. This establishes the audit evidence boundary but does not itself change the execution gate above or authorize the recommendation AI to publish.
