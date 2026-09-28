---
site_id: "fastimg"
name: "FastImg"
production_url: "https://fastimg.ai/"
changelog_url: "https://fastimg.ai/changelog/"
delivery_method: "not_established"
target_repository: "not_established"
default_branch: "not_established"
updated_at: "2026-09-28"
---

# FastImg 当前待办事项

## 已批准任务

### 缩短德语首页 Meta Description

- 优先级：`P2`
- 页面或界面：https://fastimg.ai/de/
- 当前问题与线上证据：2026-09-28 复测时，线上德语首页的 Meta Description、`og:description` 和 `twitter:description` 仍均为 `Bearbeite Bilder mit Prompts in FastImg. Für immer kostenlos, mit unbegrenzten Bearbeitungen, ohne Anmeldung und ohne Wasserzeichen. Mache jeden Schritt rückgängig und exportiere PNG-Dateien.`，共 191 个字符，明显长于通常可展示的搜索摘要，关键的 PNG 下载信息可能被截断。该页其他技术信号正常：直接返回 200，Canonical 自引用，`lang="de"`，并输出完整的 `en`、`es`、`pt`、`fr`、`de`、`ja` 和 `x-default` 双向 `hreflang`。
- 修改要求：将德语首页 Meta Description 逐字替换为 `Bearbeite Bilder mit KI-Prompts – kostenlos, unbegrenzt, ohne Anmeldung, ohne Wasserzeichen. Verfeinere jeden Schritt und lade dein Ergebnis als PNG herunter.`。同步将 `og:description` 和 `twitter:description` 替换为完全相同的文案，使三处描述一致。
- 验收标准：德语首页的 Meta Description、`og:description` 和 `twitter:description` 都与指定文案逐字一致，长度为 158 个 Unicode 字符；页面仍直接返回 200，Canonical、robots、`html lang`、`hreflang`、Title、H1、可见正文、JSON-LD 和页面布局不变。Sitemap 中该 URL 的 `lastmod` 更新为实际发布日期。
- 不要修改：不要调整德语首页的 Title、H1、正文、图片、内链、Canonical、`hreflang`、结构化数据或首屏利益点；不要修改其他语言页面。
