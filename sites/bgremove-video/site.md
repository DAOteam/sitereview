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

- Primary conversion: Register, process the first free video, then subscribe or buy credits.
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
