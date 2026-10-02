---
site_id: "vidou"
name: "Vidou"
production_url: "https://vidou.ai/"
changelog_url: "not_established"
delivery_method: "not_established"
target_repository: "not_established"
default_branch: "not_established"
updated_at: "2026-10-02"
---

# Vidou 当前待办事项

## 已批准任务

### 将旧版 `/pro/` 永久归并到当前 Image to Video 工作区

- 优先级：`P1`
- 页面或界面：`https://vidou.ai/pro/`、`https://vidou.ai/image-to-video/`
- 当前问题与线上证据：`https://vidou.ai/pro/` 仍直接返回 200，并公开展示旧版 Image to Video 界面、固定 `10` Credits、720p、7 天保留和旧的比例选项；当前导航、About 和首页已不再链接该入口，当前工作区 `https://vidou.ai/image-to-video/` 则展示 480p、720p、1080p 等另一套公开界面。旧入口继续可索引会保留两套互相冲突的产品能力和积分说明。
- 修改要求：让 `/pro/` 对所有请求执行单次永久 301 重定向到 `https://vidou.ai/image-to-video/`，停止输出旧页面的 HTML、Canonical、Open Graph、Twitter 和结构化数据；清除 `/pro/` 页面内部的自引用入口，不改动当前工作区内容。Sitemap 已不包含 `/pro/`，保持现状。
- 验收标准：请求 `https://vidou.ai/pro/` 首次响应为 301，`Location` 为 `https://vidou.ai/image-to-video/`，只发生一次跳转且最终页面返回 200；搜索引擎和普通访问者均无法再获得旧版 `/pro/` HTML；全站公开导航、About、Blog、页脚和 Sitemap 均不存在指向 `/pro/` 的链接。
- 不要修改：不要把旧版固定积分数、720p、7 天保留或旧比例选项迁移到当前工作区；不要重定向其他四个工具页；不要改动已完成的 About 页面和 Sitemap URL 集合。

### 为第一篇 Blog 补充唯一的正文工具页锚文本

- 优先级：`P1`
- 页面或界面：`https://vidou.ai/blog/how-to-animate-a-photo-with-ai/`
- 当前问题与线上证据：文章已返回 200，指定 Title、Meta Description、H1、Canonical、Open Graph、Twitter、Article JSON-LD、三张响应式配图、Complete Guide 内链和结尾 CTA 按钮均已上线；但 `Step 3: Upload the Image` 第一段仍是无链接文本 `Open Vidou's Image-to-Video workspace...`，当前正文只有结尾 CTA 指向 `https://vidou.ai/image-to-video/`，尚未满足“一个正文关键词锚文本加一个结尾 CTA 按钮”的最新 Blog 规则。页面头部只显示类型、发布日期和阅读时间，没有可见作者署名；Article JSON-LD 则将作者声明为组织 `Vidou` 并链接到首页，页面可见信息与结构化作者信息不完整对应。
- 修改要求：只将 `Step 3: Upload the Image` 第一段替换为 `Open Vidou's [AI image-to-video generator](https://vidou.ai/image-to-video/) and choose the photo you want to animate. The current interface accepts JPEG, PNG, and WebP images.`；正文锚文本必须渲染为可抓取的 `<a href="https://vidou.ai/image-to-video/">AI image-to-video generator</a>`。保留结尾 `Animate Your Photo With Vidou` CTA 按钮及其同一目标 URL。在文章类型、发布日期和阅读时间所在的头部元信息区域增加可见署名 `By Vidou`，其中 `Vidou` 链接到 `https://vidou.ai/about/`；同步保持 Article JSON-LD `author.@type` 为 `Organization`、`author.name` 为 `Vidou`，并将 `author.url` 设为 `https://vidou.ai/about/`。
- 验收标准：正文只出现一次锚文本 `AI image-to-video generator`，结尾只出现一次视觉上明确的 CTA 按钮；文章主体中 `https://vidou.ai/image-to-video/` 共出现两次且不存在其他工具页 URL；两个工具链接均可抓取、可键盘聚焦并直接返回 200。页面头部可见 `By Vidou`，作者链接返回 200，Article JSON-LD 的作者类型、名称和 URL 与可见署名一致；现有 Complete Guide 内链、首次发布日期、全文、三张图片和其他 SEO 元数据保持不变，不因本次小改动增加或刷新 `dateModified`。
- 不要修改：不要改写文章其他句子、标题、FAQ、图片、Alt、首次发布日期或其他元数据；不要增加第三个工具页链接，不要把正文锚文本改成品牌名、裸 URL、`click here` 或其他关键词；不要把结尾 CTA 降级为普通正文链接；不要虚构个人作者、头像、履历、审阅者或测试经历。

### 增加公开页面的基础安全响应头

- 优先级：`P2`
- 页面或界面：`https://vidou.ai/` 及所有同域公开 HTML 页面
- 当前问题与线上证据：2026-10-02 检查首页、`/pro/`、About、Blog、两篇文章和四个工具页时，所有 200 HTML 响应均只返回 `Strict-Transport-Security: max-age=31536000`，未返回 `Content-Security-Policy`、`Content-Security-Policy-Report-Only`、`X-Content-Type-Options`、`Referrer-Policy`、`Permissions-Policy` 或 `X-Frame-Options`。页面同时加载同域资源和 Hepo 客服，当前没有响应头限制资源来源、页面嵌入和未使用的浏览器能力。
- 修改要求：先以 `Content-Security-Policy-Report-Only` 覆盖首页、四个工具页、Pricing、Blog、About 和法律页，按实际资源逐项收敛到 `'self'` 与经过核验的必要来源；清除违规后切换为强制 `Content-Security-Policy`。至少设置 `default-src 'self'`、`object-src 'none'`、`base-uri 'self'`、限制 `form-action`，并使用 `frame-ancestors 'none'`；为 Hepo 客服只开放其实际需要的最小来源。同步返回 `X-Content-Type-Options: nosniff`、`Referrer-Policy: strict-origin-when-cross-origin` 和禁止未使用摄像头、麦克风、地理位置能力的 `Permissions-Policy`；继续保留现有 HSTS。
- 验收标准：所有公开 HTML 的 200 响应均返回强制 CSP、`X-Content-Type-Options: nosniff`、`Referrer-Policy: strict-origin-when-cross-origin` 和预期 Permissions Policy；CSP 不包含 `*`，不为解决问题而新增宽泛的 `unsafe-eval`，且 `frame-ancestors 'none'` 生效；首页视频、图片、四个工具页、登录入口、Pricing、Blog、About、法律页和 Hepo 客服在桌面与移动端无 CSP 阻断错误；现有 HSTS 仍为 `max-age=31536000` 或更严格值。
- 不要修改：不要禁用 HTTPS、HSTS、客服或现有核心资源；不要把开发域、localhost、未使用第三方域或通配符加入生产策略；不要在公开文件中记录 CSP 违规报告里的用户数据、完整查询参数或其他敏感信息。
