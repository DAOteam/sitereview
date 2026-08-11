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

# {{SITE_NAME}} 当前待办事项

## 已批准任务

### {{TASK_TITLE}}

- 优先级：`{{P0_TO_P3}}`
- 页面或界面：`{{URL_OR_UI_STATE}}`
- 当前问题与线上证据：{{CURRENT_PROBLEM}}
- 修改要求：{{IMPLEMENTATION_READY_CHANGE}}
- 验收标准：{{TESTABLE_OUTCOME}}
- 不要修改：{{EXPLICIT_BOUNDARY}}

### 更新本次发布的公开更新日志

- 优先级：`{{P0_TO_P3}}`
- 页面或界面：`{{CHANGELOG_URL_OR_not_established}}`
- 当前问题与线上证据：当前已批准的发布批次需要在用户可见的修改上线后增加一条公开更新日志。
- 修改要求：发布已批准的修改后，只新增一条带日期的记录，仅概括本批次实际上线且用户可见的变化。如果没有任何修改成功上线，则不要新增记录。
- 验收标准：本批次恰好新增一条记录；所有描述均与线上产品一致；文案简洁、面向用户且不包含内部或敏感信息。
- 不要修改：历史记录及其日期。不得提及文件名、组件名、代码架构、仓库、分支、提交、基础设施或服务商配置、成本、密钥、安全敏感实现、客户数据、内部指标、AI 提示词或内部工作流程。

## 待决事项

### {{DECISION_TITLE}}

- 优先级：`{{P0_TO_P3}}`
- 页面或界面：`{{URL_OR_UI_STATE}}`
- 当前问题：{{ISSUE}}
- 需要决定：{{QUESTION_FOR_OWNER}}
- 选项与取舍：{{CONCISE_OPTIONS}}
