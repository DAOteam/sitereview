---
site_id: "vidou"
name: "Vidou"
production_url: "https://vidou.ai/"
changelog_url: "not_established"
delivery_method: "not_established"
target_repository: "not_established"
default_branch: "not_established"
updated_at: "2026-10-04"
---

# Vidou 当前待办事项

## 已批准任务

### 重构四个工具页的图文排版并替换低质量说明图

- 优先级：`P1`
- 页面或界面：`https://vidou.ai/image-to-video/`、`https://vidou.ai/text-to-video/`、`https://vidou.ai/text-to-image/`、`https://vidou.ai/image-edit/`
- 当前问题与线上证据：2026-10-04 对四个工具页进行桌面和 390px 移动端视觉复核时，生成表单之后的内容均采用重复的“标题＋长段落”单列结构，章节之间只有纵向间距，步骤、设置、提示词方法、检查清单和 FAQ 没有形成可快速扫描的层级；桌面端正文占据长而松散的纵向页面，移动端所有 FAQ 默认展开，使页面进一步拉长。现有说明图把标题、说明和小标签直接烘焙进深紫黑位图：桌面端懒加载前出现大面积空黑框，移动端加载后文字缩得过小，且图片视觉与页面荧光绿工具界面脱节，不能有效解释操作。
- 修改要求：保留四个工具表单、登录、credits、生成参数、`My Creations`、现有已批准英文事实和 SEO 字段，重新实现表单上方的页面标题区及表单下方的内容展示。四页共享同一套 Vidou 暗色设计语言，但不得复制成完全相同的模板；使用黑色与石墨灰为底、`#75fb4c` 或当前品牌绿为主强调色，紫色只能作为极少量辅助色。具体执行如下：

  1. 把每页当前位于表单下方的 H1 和导语移动到工具表单上方，形成紧凑页面标题区；H1 桌面端 36–44px、移动端 30–34px，导语最大宽度 68ch。标题区与工具表单之间保留 28–36px，避免 H1 与主操作分离。
  2. 工具表单之后使用最大宽度 1120px 的内容容器；桌面端章节间距 72–88px，移动端 48–56px；正文默认 16–18px、行高至少 1.65、单行宽度不超过 70ch。禁止继续用六到七组相同的裸 H2＋段落纵向堆叠。
  3. 每页使用四种明确不同的内容模块：三步工作流卡片、一个左右不对称的主视觉模块、一个原生 HTML 设置或提示词组件、一个双栏检查清单；FAQ 作为最后一个独立模块。连续使用相同布局不得超过两节，桌面端至少出现两处双栏或非对称构图，移动端全部安全折叠为单栏且顺序保持“标题 → 说明 → 视觉或操作”。
  4. 三步工作流使用 `01`、`02`、`03` 数字标记和统一线性图标，桌面端三列、移动端单列；每卡只保留一个短标题和不超过两句话，不把整段正文塞入卡片。
  5. 将当前说明图中的步骤、比例、分辨率、Prompt 结构和编辑约束改成可响应的真实 HTML/CSS 内容组件，不再把可读文字烘焙进位图。Image to Video 页面使用比例框、480p/720p/1080p 选项和 Audio 状态组成设置矩阵；Text to Video 页面使用 Subject、Action、Setting、Camera、Lighting & Mood、Pace 六段 Prompt Builder；Text to Image 页面使用 Subject、Setting、Composition、Lighting、Style / Mood、Details 六段 Prompt Builder 与比例预览；Image Editor 页面使用 Target、Change、Preserve、Constraints 四段 Edit Recipe。组件必须使用语义化标题、列表或分组，不伪装成可点击控件；若视觉上像按钮但不可操作，必须改为静态标签或卡片样式。
  6. 将 `Prepare`、`Review`、`Use cases` 等现有内容改为带图标的双栏检查清单或 2×2 信息卡，不新增能力声明。每个条目使用短标题加一句解释；桌面端两栏，移动端单栏。Text to Video 的 `image to video workflow` 内链继续保留且只作为正文链接。
  7. FAQ 改为原生按钮控制的手风琴；默认只展开第一项，其余收起。每个问题按钮必须支持键盘、具有可见 `focus-visible` 状态、使用 `aria-expanded` 与关联面板 ID；展开动画只改变高度与透明度并尊重 `prefers-reduced-motion`。无 JavaScript 时问答内容仍须可读取或使用原生 `<details>` / `<summary>`。
  8. 删除四页当前八个低质量信息图在正文和社交预览中的使用：`advanced-image-to-video-workflow.webp`、`image-to-video-settings-guide.webp`、`text-to-video-prompt-structure.webp`、`text-to-video-format-guide.webp`、`text-to-image-prompt-structure.webp`、`text-to-image-aspect-ratio-guide.webp`、`ai-image-edit-workflow.webp`、`image-edit-prompt-anatomy.webp`。未被其他公开页面引用时同时删除对应 600w/700w 变体；若仍被引用，只移除本次页面引用并保留文件。
  9. 为每页制作一张新的原创编辑式主视觉，正文图不包含任何文字、数字、按钮标签、Vidou 输出示例或伪造前后对比；四张图采用一致的黑色、石墨灰和荧光绿体系，避免紫色渐变、通用 3D 球体、空洞科技光效和模拟仪表盘。资产均输出 1600×1000 WebP 和 800w 响应式版本：

     - `image-to-video-editorial.webp`：一张静态画面自然分解为连续电影帧与克制运动轨迹，表现“从图像到运动”，不展示人物身份、文字或产品结果；alt 为 `Editorial illustration of a still image expanding into a sequence of motion frames`。
     - `text-to-video-editorial.webp`：抽象场景元素沿时间轴逐步形成镜头节奏，表现文字意图、场景和运动之间的关系，不使用 Prompt 文本或虚构成片；alt 为 `Editorial illustration of scene elements forming along a video timeline`。
     - `text-to-image-editorial.webp`：构图、光线、色彩和主体层次从抽象形状中组合成完整画面，表现视觉指令的分层，不显示输入框或生成结果；alt 为 `Editorial illustration of composition, lighting, color, and subject layers forming an image`。
     - `image-editor-editorial.webp`：同一画面以图层、选区边缘和局部调整区域展开，表现可控编辑过程，不做 before/after 对比或效果承诺；alt 为 `Editorial illustration of image layers and a focused adjustment area`。

     新图放在各页三步工作流之后的非对称主视觉模块中：桌面端图像约占 58%，旁边放一组不超过四项的关键说明；移动端图像位于说明之后。图片必须有 `width="1600"`、`height="1000"`、正确 `srcset` 与 `sizes`，作为首屏以下资源使用 `loading="lazy"` 和 `decoding="async"`。Open Graph 与 Twitter 分享图同步改为对应新资产，并提供 1600×1000 尺寸和相同 alt。
  10. 不增加持续循环动画、滚动劫持、横向跑马灯、玻璃拟态叠层或成排同尺寸卡片。允许一次轻微的进入动画或悬停反馈，但只用于说明层级，必须使用 transform/opacity、可被打断并尊重 reduced motion。
- 验收标准：四页桌面端与 390px 移动端均先显示清晰 H1/导语，再进入工具表单；表单后内容可在 10 秒内通过模块标题、步骤卡、原生设置或 Prompt 组件和检查清单理解主要流程，不再是连续裸段落。每页只显示一张新的无内嵌文字主视觉，旧八张信息图不再出现在正文、Open Graph 或 Twitter 元数据；新图无空黑框、模糊、小字或明显压缩损伤。四页至少各包含三步工作流、页面专属的原生视觉组件、双栏检查模块和可访问 FAQ；在 1280px、768px、390px 下无横向滚动、裁切、重叠或超出视口的聊天按钮。所有交互元素有可见键盘焦点，FAQ 状态可被辅助技术读取，图片有准确 alt 和固定尺寸；页面现有表单功能、参数、登录、credits、canonical、Title、Meta、结构化数据中的事实与内链继续正常。
- 不要修改：不要改变生成表单、API、账户、credits、比例、分辨率、时长、Audio 或生成逻辑；不要新增模型、质量、速度、免费额度、保存期限或效果保证；不要使用竞品素材、第三方截图、未经授权照片、虚构 Vidou 输出、虚构用户案例或 before/after；不要把首页免费无需登录的定位复制到专用工具页；不要给可见功能名称增加连字符。

### 将 CSP 从 Report-Only 切换为强制策略

- 优先级：`P2`
- 页面或界面：`https://vidou.ai/` 及所有同域公开 HTML 页面
- 当前问题与线上证据：2026-10-04 复核首页、四个工具页、Blog、首篇文章、About、Pricing、法律页和 `/pro/` 时，所有响应继续返回 `X-Content-Type-Options: nosniff`、`Referrer-Policy: strict-origin-when-cross-origin`、`Permissions-Policy: camera=(), microphone=(), geolocation=()`、`X-Frame-Options: DENY` 和 `Strict-Transport-Security: max-age=31536000`；`/pro/` 继续单次 301 到当前 Image to Video 工作区。但这些响应仍只有 `Content-Security-Policy-Report-Only`，没有强制 `Content-Security-Policy`，所以资源来源与 `frame-ancestors 'none'` 尚未由浏览器实际阻止。
- 修改要求：检查当前 Report-Only 策略的真实违规报告，在首页、四个工具页、登录入口、Pricing、Blog、About、法律页和 Hepo 客服均无必要资源被阻断后，把当前已验证策略以 `Content-Security-Policy` 强制响应头覆盖所有公开 HTML。强制策略至少保留 `default-src 'self'`、`object-src 'none'`、`base-uri 'self'`、受限的 `form-action` 和 `frame-ancestors 'none'`，并继续只允许已经核验的同域、API、Google 登录、Hepo 客服及现有图片来源；Report-Only 可以删除，或仅用于测试比强制策略更严格的后续规则，不能替代强制策略。
- 验收标准：所有公开 HTML 的 200 响应和 `/pro/` 的 301 响应均返回强制 `Content-Security-Policy`；策略不包含 `*`，不新增 `unsafe-eval`、开发域、localhost 或未使用第三方域，且 `frame-ancestors 'none'` 生效；首页视频、图片、四个工具页、登录入口、Pricing、Blog、About、法律页和 Hepo 客服在桌面与移动端无 CSP 阻断错误；现有 `nosniff`、Referrer Policy、Permissions Policy、`X-Frame-Options: DENY` 和 `Strict-Transport-Security: max-age=31536000` 继续存在。
- 不要修改：不要禁用 HTTPS、HSTS、Google 登录、Hepo 客服或现有核心资源；不要为消除违规而使用通配符、增加 `unsafe-eval` 或开放未核验来源；不要在公开文件中记录 CSP 违规报告里的用户数据、完整查询参数或其他敏感信息。
