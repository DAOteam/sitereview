---
site_id: "hepo"
name: "Hepo"
production_url: "https://hepo.ai/"
changelog_url: "not_established"
delivery_method: "not_established"
target_repository: "not_established"
default_branch: "not_established"
updated_at: "2026-08-13"
---

# Hepo 当前待办事项

## 待决事项

### 统一全站的免费版、付费版与核心价值承诺

- 优先级：`P0`
- 页面或界面：`https://hepo.ai/`、`https://hepo.ai/pricing/`、`https://hepo.ai/features/` 及各功能页、`https://hepo.ai/about/`
- 当前问题：首页标题和页面标题强调 “Ten sites”，但首页元描述、定价页和用户提供的产品规则均为无限网站；首页、功能页和 About 页反复写 “The AI is the only thing that ever costs you anything.”，而定价页同时显示 Pro 和 Business 还提供更长的消息历史、统计与录像留存、更多邮箱、更大的知识库、去除品牌等付费权益；定价页还称免费版为 “The whole product”，会让访客无法判断付费究竟只购买 AI 用量，还是也购买高级功能。
- 需要决定：确认唯一的商业规则和全站统一文案，并确认是否把“无限网站、无限坐席、无限人工对话”提升为首页首屏的主要差异点。
- 选项与取舍：推荐将首页 H1 改为 `Live chat stays free. Forever.`，副标题改为 `Run customer support from one inbox with an AI agent, per-site knowledge bases, session replay and analytics. Unlimited websites, agents and human conversations stay free.`，并把全站重复的收费说明统一为 `Human chat stays free. Paid plans add higher AI, replay and retention limits, plus advanced features.`。这样首屏先突出永久免费在线客服，再用具体模块证明 Hepo 是全能客服产品；品牌定位不再局限于网站，也没有提前声称尚未上线的 App 支持，同时避免让访客误以为 AI Agent 和录像额度也无限免费。删除 “Ten sites” 和“只有 AI 会收费”的绝对表述。

### 重写全部公开页面的 SEO Title 与 Meta Description

- 优先级：`P1`
- 页面或界面：站点地图 `https://hepo.ai/sitemap-0.xml` 当前列出的全部 23 个公开页面
- 当前问题：23 个站点地图页面当前均有唯一 Title、Meta Description、自引用 Canonical 和 H1，不存在批量缺失或重复；主要问题是核心商业页面的标题偏品牌叙事，未清楚表达搜索类别。首页使用 “Hepo. Ten sites. One inbox. Never offline.”，与无限网站规则冲突且会把 Hepo 的长期定位限制在网站；Product 总览使用 “Five modules, one visitor record”，AI Agent 页面使用 “An AI agent that drafts, and waits”，都没有直接承接 `live chat`、`customer support platform`、`AI customer service agent` 等页面主题。Live Chat 功能页可以继续承接面向网站的具体搜索意图，但首页应保持渠道中立，为未来 App 等渠道保留空间。部分 Meta 也没有完整呈现免费版的无限网站、无限坐席、无限人工对话，以及付费版还包含更高额度与高级功能的真实规则。
- 需要决定：确认以下 23 个页面的关键词映射与英文替换文案。当前没有 Google Search Console 查询数据或经验证的搜索量，因此这些词基于页面内容和英文 SaaS 类别意图选择，不声称具有特定流量或排名；上线后应根据真实展现、点击率和查询词迭代。
- 选项与取舍：推荐采用以下唯一版本。全部 Title 均不超过 60 个英文字符，全部 Meta Description 均不超过 160 个英文字符；Title 以页面主要意图为中心并在适合时以 `Hepo` 收尾，Meta 只使用已由用户确认或线上可验证的产品事实：

  | 页面 | 建议 Title | Title 字符数 | 建议 Meta Description | Meta 字符数 |
  | --- | --- | ---: | --- | ---: |
  | `https://hepo.ai/` | `Free Forever Live Chat & AI Customer Support Agent` | 50 | `Free forever live chat for unlimited websites, agents and conversations. Includes an AI agent allowance, knowledge base, session replay and website analytics.` | 158 |
  | `https://hepo.ai/about/` | `About Hepo \| Live Chat & AI Customer Support Agent` | 50 | `Learn why Hepo combines live chat, an AI customer support agent, session replay and analytics in one visitor record for teams managing multiple brands.` | 151 |
  | `https://hepo.ai/contact/` | `Contact Hepo \| Sales, Support & Security Questions` | 50 | `Contact Hepo about sales, onboarding, support, security reviews or self-hosting. Send a specific question and get a direct reply from the team.` | 143 |
  | `https://hepo.ai/docs/` | `Hepo Docs \| Live Chat, Widget & AI Agent Guides` | 47 | `Learn how to install Hepo, configure the AI customer support agent, use the live chat widget API, embed the console and export customer data.` | 141 |
  | `https://hepo.ai/docs/agent-setup/` | `Configure Your AI Customer Support Agent \| Hepo` | 47 | `Configure Hepo's AI customer support agent with a handbook, per-site knowledge base, permissions, business functions, testing and human handoff.` | 144 |
  | `https://hepo.ai/docs/business-apis/` | `AI Agent Business API Integration Guide \| Hepo` | 46 | `Connect Hepo's AI agent to your business systems through server-side functions. Keep API keys private and control actions that require approval.` | 144 |
  | `https://hepo.ai/docs/embed-console/` | `Embed the Customer Support Console \| Hepo` | 41 | `Embed Hepo's customer support console inside your admin, ERP or back office so your team can handle live chat without switching tools.` | 134 |
  | `https://hepo.ai/docs/export-and-delete/` | `Export & Delete Customer Support Data \| Hepo` | 44 | `Export conversations, contacts and recordings from Hepo, delete individual visitors, and understand what account closure and retention remove.` | 142 |
  | `https://hepo.ai/docs/install/` | `Install the Hepo Live Chat Widget \| Hepo` | 40 | `Add Hepo live chat to any site with one async script tag. Learn where to place it, verify the widget and configure chat, replay and analytics.` | 142 |
  | `https://hepo.ai/docs/widget-api/` | `Live Chat Widget API Documentation \| Hepo` | 41 | `Use the Hepo live chat widget API to identify signed-in visitors, control the widget, pass customer attributes and respond to widget events.` | 140 |
  | `https://hepo.ai/features/` | `All-in-One Customer Support Platform with AI \| Hepo` | 51 | `Run live chat, an AI agent, per-site knowledge bases, session replay, website analytics and support email together across unlimited websites.` | 141 |
  | `https://hepo.ai/features/ai-agent/` | `AI Customer Service Agent with Knowledge Base \| Hepo` | 52 | `Create a knowledge base for each website. Hepo's AI agent searches it before answering visitors, works within your rules and hands off to your team.` | 148 |
  | `https://hepo.ai/features/analytics/` | `Free Website Analytics for Customer Support \| Hepo` | 50 | `Track sessions, traffic sources, pages and funnels for free. Connect website analytics to live chat and AI conversations on the same visitor record.` | 148 |
  | `https://hepo.ai/features/email-channel/` | `Shared Customer Support Inbox for Chat & Email \| Hepo` | 53 | `Manage support email and live chat in one inbox. Keep threads intact, translate messages and use the same AI agent across both customer channels.` | 145 |
  | `https://hepo.ai/features/live-chat/` | `Free Forever Live Chat for Unlimited Websites \| Hepo` | 52 | `Use live chat free forever across unlimited websites, agents and human conversations. Manage every site from one inbox with two-way translation.` | 144 |
  | `https://hepo.ai/features/session-replay/` | `Session Replay for Website Customer Support \| Hepo` | 50 | `See what visitors did before they contacted support. Hepo links each session replay to the same visitor and conversation, with form inputs masked.` | 146 |
  | `https://hepo.ai/integrations/` | `Live Chat Widget Integrations & One-Line Install \| Hepo` | 55 | `Install Hepo's live chat widget with one script. Identify signed-in visitors, connect supported platforms and embed the support console in your admin.` | 150 |
  | `https://hepo.ai/legal/cookies/` | `Cookies, Local Storage & Consent \| Hepo` | 39 | `Learn which cookies and local storage keys Hepo and its live chat widget use, how long they last, and how consent applies to analytics and replay.` | 146 |
  | `https://hepo.ai/legal/dpa/` | `Data Processing Agreement \| Hepo` | 32 | `Read Hepo's data processing terms for customer conversations, session replay and analytics, including security measures, subprocessors and transfers.` | 149 |
  | `https://hepo.ai/legal/privacy/` | `Privacy Policy for Customer Support Data \| Hepo` | 47 | `Learn what account, conversation, visitor, session replay and analytics data Hepo processes, why it is used, how long it is kept and how to delete it.` | 150 |
  | `https://hepo.ai/legal/terms/` | `Terms of Service for Live Chat & AI Support \| Hepo` | 50 | `Read the terms for using Hepo live chat, AI customer support agent, session replay, analytics and email, including accounts, billing and cancellation.` | 150 |
  | `https://hepo.ai/pricing/` | `Free Forever Live Chat & AI Agent Pricing \| Hepo` | 48 | `Start free forever with unlimited websites, agents and human conversations, plus limited AI agent and session replay usage. Upgrade for higher limits.` | 150 |
  | `https://hepo.ai/security/` | `AI Support Security & Session Replay Privacy \| Hepo` | 51 | `See how Hepo masks form inputs, protects customer conversations, controls AI actions and handles storage, retention and data deletion.` | 134 |

  上线时同一页面的 `og:title`、`og:description`、`twitter:title`、`twitter:description` 应与新 Title 和 Meta 保持一致；首页 JSON-LD 中的 `Organization.description` 与 `WebSite.description` 应改为不包含 “Ten sites” 或“只有 AI 收费”暗示的准确产品描述。保留现有 URL、自引用 Canonical、英文页面语言和每页唯一 H1；不要在无关页面机械重复 `Free Forever` 或 `AI Agent`，也不要声称排名、搜索量、客户结果或未上线能力。验收时重新抓取 sitemap 全部 URL，确认 23 个 Title 和 23 个 Meta 均唯一，Title 均不超过 60 个字符且 Meta 均不超过 160 个字符。

### 由法律顾问核定公开法律文本并消除数据规则矛盾

- 优先级：`P0`
- 页面或界面：`https://hepo.ai/legal/privacy/`、`https://hepo.ai/legal/terms/`、`https://hepo.ai/legal/dpa/`、`https://hepo.ai/legal/cookies/`、`https://hepo.ai/pricing/`
- 当前问题：四个法律页面均公开声明文本尚未经过适用司法辖区的法律顾问审核，并提示访客在依赖前索取另一份可执行版本；Privacy 页面称对象存储和模型提供商会在 DPA 中具名，但公开 DPA 只写 “Object storage provider” 和 “Model provider”；Terms 写会话记录保留到用户删除或关闭账户，而定价页写 Free 为 14 天、Pro 为 1 年、Business 为无限；Terms 还写 AI 额度用完后 replay 不受影响，但定价页另有每月可拉取录像数量限制。这些差异直接影响采购、隐私合规和付费决策。
- 需要决定：确认签约主体、适用法律、真实子处理商、数据存储地区、各套餐的消息与录像保留规则、额度耗尽行为，以及公开网页和可签署版本之间的法律关系；由合格法律顾问审核后再发布最终文本。
- 选项与取舍：推荐在继续扩大公开获客前完成一次完整法律审核，并让公开 Privacy、Terms、DPA、Cookies 与定价表使用同一套事实；若暂时无法完成，则应明显标注 beta/邀请制并停止把未审文本包装成可直接用于采购的 DPA。前者降低长期法律与信任风险，后者上线更快但会限制企业转化。

### 明确 Hepo 当前是公开上线、开放测试还是封闭测试

- 优先级：`P1`
- 页面或界面：`https://hepo.ai/`、`https://hepo.ai/about/`、`https://hepo.ai/contact/`、`https://hepo.ai/docs/`、`https://hepo.ai/integrations/`
- 当前问题：首页写 “Open for new sites — free plan, no card” 并直接提供自助注册，About 页却写 “The closed beta is still open” 和仅运行少量真实网站，Contact 仍有 “Joining the beta”，Docs 说明 beta 期间尚无公开状态页，Integrations 也标注插件处于 beta。访客无法判断产品是否适合正式生产使用、是否需要申请，以及自助注册后的服务承诺是什么。
- 需要决定：确定当前正式产品阶段、允许进入的客户范围、可承诺的支持与稳定性级别，并统一所有入口的阶段名称和 CTA。
- 选项与取舍：若已公开上线，删除 closed beta/申请加入表述并保留自助注册；若仍是受控测试，将首页 CTA 改为申请加入并说明准入和支持范围；若是开放 beta，统一使用 “Open beta” 并说明哪些能力仍在测试。公开上线转化阻力最低，受控测试更利于控制服务风险，开放 beta 是两者之间的折中。

### 清楚介绍供 AI Agent 检索的按网站知识库功能

- 优先级：`P1`
- 页面或界面：`https://hepo.ai/`、`https://hepo.ai/features/`、主导航、页脚、站点地图
- 当前问题：Hepo 的知识库是由客户为自己的某个网站创建和维护的内容集合，AI Agent 回答该网站访客的问题前会先从对应知识库检索内容；它不是 Hepo 的帮助中心或产品文档。当前定价页虽列出 “Knowledge base and quick replies” 及 Business 的更大知识库，AI Agent 页面也提到知识库，但 Product 总览和首页没有把“按网站建立知识库、回答前先检索”作为明确能力说明。潜在客户难以快速确认知识库与网站的对应关系、AI 如何使用内容，以及免费与付费容量如何区分。
- 需要决定：确认可公开说明的真实能力，包括一个网站是否对应一个独立知识库、支持的内容创建或导入方式、内容更新方式、检索范围、回答无匹配内容时的行为，以及各套餐容量限制。
- 选项与取舍：推荐先把知识库作为 AI Agent 的关键子功能，在首页、Product 总览和 AI Agent 页面增加清晰说明，并从 Pricing 对应条目链接过去；只有在需要承接 “AI customer service knowledge base” 等独立搜索需求时，再新增 `Knowledge base` 功能落地页。此建议不涉及建立 Hepo 帮助中心，也不要求把知识库改造成独立顶级产品模块。

### 建立真实的公开服务状态入口

- 优先级：`P1`
- 页面或界面：全站页脚的 “Status” 链接、`https://hepo.ai/docs/`
- 当前问题：全站页脚的 “Status” 实际链接到 Docs 首页；Docs 的 “Service status” 明确说明公开状态页尚未上线，事故只发到社区频道并邮件通知工作区所有者。对承载客服、录像和 AI 自动回复的 SaaS 来说，访客点击 Status 却看不到当前状态、历史事故或订阅入口，会削弱生产可用性的可信度。
- 需要决定：是否建立并持续维护公开状态页，以及公开哪些组件、历史事故和订阅方式。
- 选项与取舍：推荐建立真实状态页并让页脚直达；若当前无法持续维护，则把页脚标签改为 “Service status policy” 并直接定位到 Docs 对应段落，不再让 “Status” 暗示已有实时页面。真实状态页信任更强，但需要长期运营纪律。

### 修正注册链接首次加载时短暂显示登录表单

- 优先级：`P2`
- 页面或界面：从 `https://hepo.ai/pricing/` 等营销页面进入 `https://hepo.ai/app/#signup` 的未登录移动端流程
- 当前问题：在 390×844 的隔离未登录环境中，从定价页导航到 `#signup` 后，地址栏已是注册 URL，但首轮渲染仍显示 “Sign in to Hepo”；刷新或新开该 URL 后才稳定显示 “Create your account”。这会在慢设备或网络下让高意向访客误以为需要已有账户。
- 需要决定：是否批准将 URL 模式判断提前到首屏渲染，并把“营销页 Start free → 注册表单”的冷启动和客户端导航加入回归测试。
- 选项与取舍：推荐本批次修复，要求首次可交互状态直接呈现注册表单且不闪现登录表单；也可暂时接受短暂闪烁，但会继续损耗移动端注册信心。

### 增加可核验的真实使用证据

- 优先级：`P2`
- 页面或界面：`https://hepo.ai/`、`https://hepo.ai/features/`、`https://hepo.ai/pricing/`
- 当前问题：首页大量演示数据明确标注为脚本答案、模型化流量或 demo workspace sample data，About 又称已有少量真实网站，但全站没有经授权的客户名称、案例、引述、公开使用规模或可核验结果。交互演示能解释产品，却不能单独证明真实环境中的可靠性和价值。
- 需要决定：是否有可公开且经客户授权的证据，以及允许披露的范围；不得把内部或演示数据包装成真实客户结果。
- 选项与取舍：优先发布一到两个有客户许可的短案例，包含场景、使用模块和可核验的定性结果；若暂时不能披露品牌，可使用经批准的匿名案例并明确样本范围；若没有任何可公开证据，继续只保留演示但不要加入未经证实的数字。实名案例信任最高，匿名案例隐私更稳妥但说服力较弱。

### 确定交付方式并建立公开更新日志

- 优先级：`P1`
- 页面或界面：推荐任务仓库与待建立的公开更新日志
- 当前问题：当前没有已确认的 `direct_publish` 或 `pull_request` 交付方式，也没有已建立的公开更新日志 URL；Terms 已承诺依赖功能变更会通过 changelog 通知，但全站导航和站点地图中没有可验证的 changelog。
- 需要决定：选择本网站后续修改的交付方式；若选择 Pull Request，提供真实目标仓库和默认分支；同时确定并公开一个长期维护的 changelog URL。
- 选项与取舍：已有受控生产工作区且希望直接发布时选择 `direct_publish`；需要代码审查时选择 `pull_request` 并提供仓库与默认分支。更新日志可建立独立页面并加入页脚，或使用现有公开产品更新页，但必须能长期访问、保留历史记录并只描述真实上线且用户可见的变化。
