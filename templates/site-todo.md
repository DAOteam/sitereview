---
site_id: "{{SITE_ID}}"
name: "{{SITE_NAME}}"
production_url: "{{PRODUCTION_URL}}"
changelog_url: "{{CHANGELOG_URL_OR_not_established}}"
delivery_method: "{{direct_publish_OR_pull_request}}"
target_repository: "{{not_applicable_OR_REAL_REPOSITORY}}"
default_branch: "{{not_applicable_OR_REAL_BRANCH}}"
updated_at: "{{YYYY-MM-DD}}"
---

# {{SITE_NAME}} current tasks

## Approved tasks

### {{TASK_TITLE}}

- Priority: `{{P0_TO_P3}}`
- Page or surface: `{{URL_OR_UI_STATE}}`
- Problem and live evidence: {{CURRENT_PROBLEM}}
- Required change: {{IMPLEMENTATION_READY_CHANGE}}
- Acceptance criteria: {{TESTABLE_OUTCOME}}
- Do not change: {{EXPLICIT_BOUNDARY}}

### Update the public changelog for this release

- Priority: `{{P0_TO_P3}}`
- Page or surface: `{{CHANGELOG_URL_OR_not_established}}`
- Problem and live evidence: The current approved release batch requires one public changelog entry after its user-visible changes are published.
- Required change: After publishing the approved changes, add exactly one dated entry summarizing only the user-visible changes that actually shipped. If nothing ships, do not add an entry.
- Acceptance criteria: Exactly one new entry represents this release batch, every claim matches the live product, and the wording is concise, user-facing, and free of internal or sensitive details.
- Do not change: Historical entries or dates. Do not mention file or component names, code architecture, repositories, branches, commits, infrastructure or provider configuration, costs, secrets, security-sensitive implementation details, customer data, internal metrics, AI prompts, or internal workflows.

## Needs decision

### {{DECISION_TITLE}}

- Priority: `{{P0_TO_P3}}`
- Page or surface: `{{URL_OR_UI_STATE}}`
- Current issue: {{ISSUE}}
- Decision required: {{QUESTION_FOR_OWNER}}
- Options and tradeoff: {{CONCISE_OPTIONS}}
