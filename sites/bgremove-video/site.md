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
- Free allowance: Each account can process up to three videos in any rolling 24-hour period; this is not a calendar-day reset.
- Primary conversion: Sign in, complete a successful free video-background removal, and return as the rolling allowance becomes available again.
- Growth goal: Improve useful engagement, repeat visits, brand trust, and organic-search authority before introducing monetization later.
- Audience: Video creators and editors.
- Markets: United States, Canada, Europe, Australia and Oceania, Japan, Korea, and Singapore.
- Current languages: English, Spanish, Portuguese, French, and German.
- Planned languages: Japanese and Korean, deferred until current locales are stable.

## Execution boundary

- Recommendations live in this repository.
- Website source code repository: `https://github.com/DAOteam/bgremove`.
- Code changes must be delivered through a Pull Request; direct commits to the default branch are not allowed.
- The execution AI may act only on tasks with `status: "approved"`.
- Deployment, billing-product creation, and production configuration require separate authorization.
