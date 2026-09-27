---
site_id: "fastimg"
name: "FastImg"
production_url: "https://fastimg.ai/"
changelog_url: "https://fastimg.ai/changelog/"
delivery_method: "not_established"
target_repository: "not_established"
default_branch: "not_established"
updated_at: "2026-09-27"
---

# FastImg 当前待办事项

## 已批准任务

### 缩短德语首页 Meta Description

- 优先级：`P2`
- 页面或界面：https://fastimg.ai/de/
- 当前问题与线上证据：2026-09-27 线上德语首页 Meta Description 为 `Bearbeite Bilder mit Prompts in FastImg. Für immer kostenlos, mit unbegrenzten Bearbeitungen, ohne Anmeldung und ohne Wasserzeichen. Mache jeden Schritt rückgängig und exportiere PNG-Dateien.`，共 191 个字符，明显长于通常可展示的搜索摘要，关键的 PNG 下载信息可能被截断。该页其他技术信号正常：直接返回 200，Canonical 自引用，`lang="de"`，并输出完整的 `en`、`es`、`pt`、`fr`、`de`、`ja` 和 `x-default` 双向 `hreflang`。
- 修改要求：将德语首页 Meta Description 逐字替换为 `Bearbeite Bilder mit KI-Prompts – kostenlos, unbegrenzt, ohne Anmeldung, ohne Wasserzeichen. Verfeinere jeden Schritt und lade dein Ergebnis als PNG herunter.`。同步将 `og:description` 和 `twitter:description` 替换为完全相同的文案，使三处描述一致。
- 验收标准：德语首页的 Meta Description、`og:description` 和 `twitter:description` 都与指定文案逐字一致，长度为 158 个 Unicode 字符；页面仍直接返回 200，Canonical、robots、`html lang`、`hreflang`、Title、H1、可见正文、JSON-LD 和页面布局不变。Sitemap 中该 URL 的 `lastmod` 更新为实际发布日期。
- 不要修改：不要调整德语首页的 Title、H1、正文、图片、内链、Canonical、`hreflang`、结构化数据或首屏利益点；不要修改其他语言页面。

### 补发移动端适配与多语言功能页的公开变更日志

- 优先级：`P1`
- 页面或界面：https://fastimg.ai/changelog/
- 当前问题与线上证据：2026-09-27 线上 Changelog 最新条目仍是 2026-09-23 的 `Text-to-image generation and new editing tools`。生产环境已在 2026-09-26 上线 30 个西班牙语、葡萄牙语、法语、德语和日语功能页，全部返回 200，具有自引用 Canonical、完整的六语言及 `x-default` `hreflang`、本地化内容和结构化数据，Sitemap 已收录全部 43 个公开页面。`/app/` 在 390×844 和 320×568 视口的初始与文字输入状态也已无横向溢出，底部主按钮高 44px，点击 `Generate from text` 会聚焦输入框且不创建空白图。这些用户可发现的重要更新仍未记录。
- 修改要求：在现有 2026-09-23 条目之前新增日期 `September 26, 2026`、标题 `Mobile editor improvements and localized tool pages`，正文逐字使用 `FastImg now offers its image generator and editing tool pages in Spanish, Portuguese, French, German, and Japanese. We also improved the mobile editor so the prompt field and Generate button stay accessible without overlap, with larger touch targets and safe-area spacing.`。保留现有所有历史条目与日期，并将 Sitemap 中 Changelog URL 的 `lastmod` 更新为该条目实际发布日期。
- 验收标准：Changelog 顶部显示 `September 26, 2026`、指定标题和指定正文，逐字一致且位于 2026-09-23 条目之前。页面继续返回 200、允许索引并使用自引用 Canonical；Sitemap 中 Changelog `lastmod` 为 2026-09-26。从条目描述的五种语言功能页及移动端输入区、Generate、触控目标和安全区改进都能在生产环境复现；未完成的生成稳定性和客服遮挡修复不得写入该条目。
- 不要修改：不要为每种语言或每个功能拆分多条记录，不要改写或删除已有历史条目与日期；不要在公开变更日志中提及文件、组件、CSS 类、代码、仓库、分支、提交、部署、测试设备、内部指标、翻译流程、生成供应商或客服供应商。
