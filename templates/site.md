---
site_id: "{{SITE_ID}}"
task_prefix: "{{PREFIX}}"
name: "{{SITE_NAME}}"
production_url: "{{URL}}"
target_repository: "pending"
default_branch: "pending"
delivery_method: "pull_request"
recommendation_owner: "website-growth-ai"
execution_owner: "code-execution-ai"
---

# {{SITE_NAME}}

## Business context

- Primary conversion: {{PRIMARY_CONVERSION}}
- Audience: {{AUDIENCE}}
- Markets: {{MARKETS}}
- Current languages: {{LANGUAGES}}

## Execution boundary

- Recommendation files live in this repository.
- Website source code lives in `target_repository`.
- The execution AI may act only on tasks with `status: approved`.
- The execution AI must use the configured `delivery_method`; default to Pull Request for new sites.
- Deployment requires separate explicit authorization.
