---
site_id: "bgremove-video"
name: "BGRemove"
production_url: "https://bgremove.video/"
changelog_url: "https://bgremove.video/changelog/"
delivery_method: "direct_publish"
target_repository: "not_applicable"
default_branch: "not_applicable"
updated_at: "2026-08-11"
---

# BGRemove 当前待办事项

## 已批准任务

### 替换首页的编辑工具说明

- 优先级：`P1`
- 页面或界面：`https://bgremove.video/`
- 当前问题与线上证据：首页仍显示 `Exports open natively in the tools you already finish in, Adobe Premiere Pro and After Effects included.`
- 修改要求：将其替换为 `Open the result directly in the editing tools you already use.`
- 验收标准：批准的新句子在线可见，旧句子不再出现。SEO 标题必须保持为 `Remove Video Background Online Free - No Watermark`，H1 必须保持为 `Remove video background online. Free, no watermark.`
- 不要修改：首页其他文案、布局、导航、产品行为或非英文页面。

### 修复 FAQ 支持邮箱前缺少空格的问题

- 优先级：`P1`
- 页面或界面：`https://bgremove.video/faq/`
- 当前问题与线上证据：页面当前显示为 `Still stuck? Write tosupport@bgremove.video.`，`to` 与邮箱地址之间缺少空格。
- 修改要求：准确显示 `Still stuck? Write to support@bgremove.video.`，同时保留 `support@bgremove.video` 指向 `mailto:support@bgremove.video` 的链接；对应的结构化内容在含义上保持一致。
- 验收标准：可见句子包含所需空格，邮箱链接可用，并且页面不再出现 `Write tosupport@bgremove.video`。
- 不要修改：其他 FAQ 内容、页面结构或非英文页面。

### 使用直白语言开头解释透明度

- 优先级：`P1`
- 页面或界面：`https://bgremove.video/tools/remove-background-from-video/`
- 当前问题与线上证据：说明段落仍以 `The tool computes a per-pixel transparency value and stores it as a fourth channel...` 开头，没有先解释用户能看到的结果。
- 修改要求：将该段落替换为 `Each pixel can be fully visible, partly transparent, or invisible. That transparency is stored in an alpha channel alongside the file's red, green, and blue colour channels. Nothing is behind your subject. What goes there is decided later, in your editor, as many times as you like.`
- 验收标准：段落以批准的“完全可见、部分透明或不可见”说明开头，旧的工具视角开头不再出现。
- 不要修改：页面 H1、其他工具文案、产品行为、输出格式或非英文页面。

### 删除账户页简介中过时的账单表述

- 优先级：`P1`
- 页面或界面：登录后的英文页面 `https://bgremove.video/app/account/`
- 当前问题与线上证据：当前没有付费计划或账单选项，但简介仍写着 `Plan, billing and data. Everything destructive on this page asks once and then does exactly what it says.`
- 修改要求：将其替换为 `Account and data. Everything destructive on this page asks once and then does exactly what it says.`
- 验收标准：批准的新简介在线可见，`Plan, billing and data.` 不再出现；单独的发票保留说明继续保留。
- 不要修改：身份验证、账户数据操作、历史发票记录、用量额度行为或非英文账户页面。

### 显示权威的额度重置日期和时间

- 优先级：`P1`
- 页面或界面：登录后的英文页面 `https://bgremove.video/app/account/` 中两处重置摘要
- 当前问题与线上证据：当前额度周期只显示 `Resets 11 Aug 2026` 和 `Resets 11 Aug`，没有可见的具体时间或语义化时间戳。
- 修改要求：额度周期生效后，使用现有服务器或账户额度数据，在两处摘要中显示同一个权威的下次完整重置日期和时间。使用语义化 `<time>` 元素及权威 `datetime`。如果周期尚未开始，不得虚构时间戳；应使用现有的真实状态，或说明周期从第一个成功处理的视频开始。
- 验收标准：额度周期生效时，两处摘要显示相同的真实日期和时间。使用安全的现有测试夹具或自动化测试验证周期尚未开始的状态。继续保留 `Free`、`No charge`、`Up to 3 videos per 24-hour period`、`Up to 60 seconds per video` 和发票保留说明。不得出现付费卡片、价格、`See plans`、`Get notified`、付费 CTA 或空的付费计划容器。
- 不要修改：额度计算、成功任务计数、失败任务处理、身份验证、处理流程、保留策略、下载、历史记录、公开定价页面或非英文页面。

### 更新本次发布的公开更新日志

- 优先级：`P1`
- 页面或界面：`https://bgremove.video/changelog/`
- 当前问题与线上证据：当前已批准的发布批次需要在用户可见的修改上线后增加一条公开更新日志。
- 修改要求：发布已批准的修改后，只新增一条带日期的记录，仅概括本批次实际上线且用户可见的改进。可使用简洁标题，例如 `Clearer guidance and account details`。如果没有任何修改成功上线，则不要新增记录。
- 验收标准：本批次恰好新增一条记录；所有描述均与线上产品一致；文案简洁、面向用户且不包含内部或敏感信息。
- 不要修改：历史记录及其日期。不得提及文件名、组件名、代码架构、仓库、分支、提交、基础设施或服务商配置、成本、密钥、安全敏感实现、客户数据、内部指标、AI 提示词或内部工作流程。
