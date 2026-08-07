---
site_id: "{{SITE_ID}}"
task_prefix: "{{PREFIX}}"
name: "{{SITE_NAME}}"
production_url: "{{URL}}"
target_repository: "pending"
default_branch: "pending"
delivery_method: "pending"
audit_source: "public_production"
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
- For `pull_request`, website source code lives in `target_repository` and `default_branch` must be real.
- For `direct_publish`, set repository fields to `not_applicable`; the programming AI uses its existing production-connected environment and writes no result file.
- The execution AI may act only on tasks with `status: approved`.
- Choose and confirm `delivery_method` before approving the first task; never infer it.
- Publishing requires an approved task that explicitly authorizes it.
- Verify implementation against the configured audit source; when it is public production, carry unimplemented or partially implemented items into the next prompt version.
