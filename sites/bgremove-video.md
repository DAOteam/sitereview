---
site_id: "bgremove-video"
name: "BGRemove"
production_url: "https://bgremove.video/"
changelog_url: "https://bgremove.video/changelog/"
delivery_method: "direct_publish"
target_repository: "not_applicable"
default_branch: "not_applicable"
updated_at: "2026-09-13"
---

# BGRemove 当前待办事项

## 已批准任务

### 为 Change Background 页面补齐四种语言版本

- 优先级：`P1`
- 页面或界面：现有英文页 `https://bgremove.video/change-background/`；新增 `https://bgremove.video/es/change-background/`、`https://bgremove.video/pt/change-background/`、`https://bgremove.video/de/change-background/`、`https://bgremove.video/fr/change-background/`
- 当前问题与线上证据：2026-09-12 线上检查确认英文 `/change-background/` 返回 `200`，但西班牙语、巴西葡萄牙语、德语和法语对应 URL 均返回 `404`。英文页没有任何 `hreflang`，四种语言页面也无法通过语言切换器或当前语言的顶部导航直接访问换背景功能，现有多语言覆盖不完整。
- 修改要求：以发布时最新的英文 `/change-background/` 为唯一产品、功能和内容基准，新增西班牙语 `es`、巴西葡萄牙语 `pt-BR`、德语 `de` 和法语 `fr` 四个完整版本。翻译全部可见内容和交互状态，包括 TDK、H1/H2/H3、正文、按钮、辅助说明、背景选项、空状态、作品选择、预览、处理中、导出中、成功、失败与重试提示、FAQ、CTA、图片 alt、导航和页脚；不得只翻译静态正文。四个页面复用英文页相同的换背景组件、版式、案例图、功能能力和限制，不改变“不限次数、完全免费”“图片和视频背景仅在浏览器内处理”“从已去除背景的作品开始”“导出 MP4”等已经公开的产品事实。每个语言页使用自然本地化且唯一的 Title、Meta description、单一 H1 和自引用 canonical；Title 不超过 60 个字符，Meta description 不超过 155 个字符。五个语言版本输出完全一致且互惠的 `hreflang` 集合：`en`、`es`、`pt-BR`、`de`、`fr` 和以英文页为目标的 `x-default`。语言切换器在五个对应页面之间直接切换；四个新 URL 加入 XML Sitemap。把四种语言全站顶部导航中现有英文站对应的 `Change background` 独立入口补齐并本地化，目标指向当前语言的换背景页；页脚 Product 列中的换背景链接也指向当前语言版本。正文中的首页、How it works、Use cases 与具体场景链接优先指向同语言页面。
- 验收标准：四个新 URL 均直接返回 `200`，无重定向、`noindex`、英文占位内容或错误语言；`html lang` 分别为 `es`、`pt-BR`、`de`、`fr`，canonical 均指向自身。五个页面的 `hreflang` 完整互惠，所有目标返回 `200`，语言切换不会回到首页或产生 `404`；Sitemap 同时包含五个 canonical URL。桌面端和移动端逐页检查，首屏工具、作品选择、纯色、模糊、图片、视频背景、自动播放、比例保持和 MP4 导出流程与英文页一致，全部状态使用当前语言且没有文本截断、按钮溢出、重叠或横向滚动。当前语言的顶部和页脚入口可在首页、FAQ、How it works、Use cases、工具页、博客和 Changelog 各抽查至少一页，链接文字本地化且目标正确；可见 FAQ 与 `FAQPage` JSON-LD 的问题、答案和顺序一致。
- 不要修改：英文页面已经确认的产品行为、免费规则、登录规则、输入输出格式、时长与文件大小限制、隐私说明、音频和画面比例行为；不新增编辑时间线、模板、素材库、分辨率选择、批量处理或其他不存在的能力；不创建五种现有语言之外的新语言，不把背景替换描述为会重新消耗去背景额度。

### 新增五种语言的 Blog 入口、列表页与文章结构

- 优先级：`P1`
- 页面或界面：新增 `https://bgremove.video/blog/`、`https://bgremove.video/es/blog/`、`https://bgremove.video/pt/blog/`、`https://bgremove.video/de/blog/`、`https://bgremove.video/fr/blog/`；同步五种语言全部公开页面的顶部导航与页脚
- 当前问题与线上证据：2026-09-12 线上检查确认英文及四种本地化 `/blog/` URL 均返回 `404`，顶部导航和页脚也没有 Blog 入口。网站已有工具页、使用场景页和 FAQ，但缺少一个能持续承载具体教程与排错内容的可索引内容中心。用户已批准五种语言同步上线，并要求入口同时放在顶部和页脚。
- 修改要求：创建五个完整本地化的 Blog 列表页，英文 H1 使用 `Video Background Guides`，引言明确这里只发布视频去背景、透明视频、绿幕和背景替换的实用指南，不使用泛化 AI 新闻定位。列表首批只展示本文件批准的 3 篇文章，卡片包含文章主图、标题、简短摘要、实际发布日期和清晰的详情链接；不创建没有内容的分类、标签、作者归档或分页页面。五个列表页分别使用自然本地化的唯一 Title、Meta description、单一 H1、自引用 canonical、Open Graph 和 Twitter 文案；Title 不超过 60 个字符，Meta description 不超过 155 个字符。五个 Blog 列表页及其对应文章页面均输出互惠 `hreflang`：`en`、`es`、`pt-BR`、`de`、`fr` 和英文 `x-default`，并加入 XML Sitemap。页面使用语义化的 `main`、`section`、`article`、标题层级、可读日期 `time` 与 Breadcrumb；列表页使用 `CollectionPage` 或 `Blog`，文章页使用 `BlogPosting` 和 `BreadcrumbList` JSON-LD，结构化数据必须与可见标题、摘要、日期、图片和 URL 一致。文章作者不得编造个人身份或资历，可统一显示并标注组织作者 `BGRemove`，链接到当前语言的 About 页面。
- 修改要求：在五种语言全部公开页面的桌面端和移动端顶部导航增加当前语言的 Blog 独立入口，并在页脚 Resources 列增加同一入口；英文、西班牙语、葡萄牙语、德语和法语可见菜单文字均使用 `Blog`，目标分别指向对应语言列表页。Blog 入口不得塞进 Remove 下拉菜单，也不得替换现有导航项。先让列表页和首批文章全部可访问，再发布全站入口，避免导航指向空页或 `404`。
- 验收标准：五个 Blog 列表页均直接返回 `200`、可索引、canonical 正确且只显示 3 篇已上线文章；五种语言之间可直接切换，不回到首页。桌面端和移动端顶部及页脚均可找到 Blog，在五种语言的首页、换背景页、去绿幕页、FAQ、工具页和 Changelog 抽查时链接均返回 `200`；键盘可以访问，焦点清楚，不破坏现有 Remove 下拉菜单或移动导航。Blog 列表页和 15 个语言文章 URL 全部进入 Sitemap；各语言版本的 canonical、`hreflang`、`html lang`、结构化数据和可见内容一致，无重复 Title、重复 Meta description、空卡片、错误日期、英文残留、布局溢出或孤立文章。每篇文章至少从 Blog 列表页和一处相关产品或指南页面获得上下文内链，并自然回链到对应语言的相关工具页。
- 不要修改：现有 Remove 下拉菜单的两个功能项、登录和账户入口、语言切换逻辑、历史 Changelog 内容或法律页面；不增加评论、用户投稿、点赞、订阅、账户收藏、RSS、站内搜索、分类筛选或 CMS 能力，除非另有明确授权；不生成虚构客户案例、评价、排名、流量、处理速度、效果保证或产品截图。

### 发布首批三篇五语 Blog 指南

- 优先级：`P1`
- 页面或界面：英文及 `es`、`pt`、`de`、`fr` 对应 Blog 文章页，共 15 个语言 URL
- 当前问题与线上证据：Blog 尚未上线。用户已批准首批同时发布 3 篇文章并由审查方确定主题。现有 Sitemap 已覆盖工具、使用场景和 FAQ；首批内容需要补充更具体的拍摄准备、透明 WebM 排错和背景选择问题，同时避免再做一篇与 `/tools/green-screen-alternative/` 抢占同一搜索意图的 Green Screen vs AI 对比文。
- 修改要求：先完成下方 3 篇英文源文，再由英文定稿翻译为西班牙语、巴西葡萄牙语、德语和法语。英文正文每篇约 900–1,400 词，以直接答案开头，使用清晰的 H2/H3、步骤、检查清单或比较表；使用第二人称和具体日常语言，避免空话、关键词堆砌、虚构数字、虚构测试和大品牌口吻。翻译必须自然重写标题、摘要、正文、图片 alt、CTA 和元数据，不逐词硬译，不改变产品事实。三个英文 URL 和主题如下：
  1. `/blog/record-video-for-ai-background-removal/`；Title/H1：`How to Record Video for Cleaner AI Background Removal`。回答如何通过主体与背景分离、柔和正面光、完整构图、控制快速动作、保留头发和手部边缘、避免与背景过度相近的服装、使用原始清晰文件和先测试困难片段来提高自动抠像可用性；明确 AI 仍可能在飞散头发、重度运动模糊、玻璃、反光物体和遮挡处失误。正文自然链接到当前语言首页、How it works 和相关 Use cases。
  2. `/blog/transparent-webm-background/`；Title/H1：`Why Your Transparent WebM Still Shows a Background`。开头直接说明本地播放器或浏览器标签页可能没有正确合成 VP9 WebM 的 alpha channel，因此看到原背景、黑色或其他底色不一定代表透明数据丢失。解释 alpha channel 与容器/编码的区别，给出把视频放到支持 VP9 WebM alpha 的编辑器或网页实色图层上方进行验证的步骤，说明重命名 `.webm` 为 `.mp4` 不会转换编码或保留透明度；对 CapCut、Premiere 或其他编辑器只描述“取决于版本、平台和编码支持”，不作绝对兼容承诺。正文自然链接到当前语言首页、换背景页和 How it works。
  3. `/blog/choose-video-background/`；Title/H1：`How to Choose a Background for Your Video`。用一张清楚的比较表和实际场景分别说明 Solid Color、Blur、Image、Video 四种背景的适用情况、优点和需要检查的风险；覆盖主体对比度、品牌色、画面留白、文字位置、横竖比例、背景运动强度、循环接缝以及先预览再导出的选择方法。明确图片或视频背景在 BGRemove 中仅在浏览器内组合、背景替换不限次数且免费，最终导出 MP4；不把它写成完整视频编辑器。正文自然链接到当前语言换背景页、首页和相关 Use cases。
- 修改要求：每篇文章使用独立且准确的 Meta description、摘要和社交分享文案；Title 不超过 60 个字符，Meta description 不超过 155 个字符。英文与四个翻译版本沿用同一英文 slug，仅增加语言前缀，形成每篇 5 个互惠版本；每页自引用 canonical，并包含 `en`、`es`、`pt-BR`、`de`、`fr` 与英文 `x-default`。每篇文章生成一张独立、真实自然的编辑场景主图，同一篇的五种语言可复用同一无文字图片；不得伪造 BGRemove 界面、用户成果或客户素材，如需展示产品操作只能使用发布时真实线上界面截图。所有图片提供当前语言的描述性 alt，设置明确尺寸并使用响应式、压缩后的现代格式。文章末尾放一个与主题直接相关的简短 CTA，不用多个重复按钮。
- 验收标准：3 篇英文文章和 12 篇翻译文章均返回 `200`、可索引、无占位符；每组五语文章内容主题与产品事实一致，语言自然完整，语言切换器直达对应文章。三个主题的 Title/H1、开头答案、主体结构、边界说明、内链和 CTA 均符合要求；第二篇没有把播放器显示问题一概判定为处理失败，第三篇没有声称换背景会消耗去背景额度。每页只有一个 H1，标题层级连续，发布日期真实一致，`BlogPosting` 与 Breadcrumb JSON-LD 可解析且与可见信息一致；全部 URL 位于 Sitemap，图片没有人物畸形、错误界面、嵌入文字、裁切主体或显著生成瑕疵。检查五种语言全文，不出现虚构指标、第三方兼容保证、英文残留或与现有落地页重复的大段正文。
- 不要修改：现有首页、换背景页、去绿幕页和工具页的核心关键词定位；不新增 Green Screen vs AI Background Removal 文章，不复制 `/tools/green-screen-alternative/` 的搜索意图；不编造作者履历、统计数据、搜索量、客户证言、商业许可、处理质量或第三方软件当前功能；不要使用 `in today's digital world`、`unleash`、`elevate`、`seamless`、`supercharge`、`revolutionize` 等空泛表达。

### 更新本批多语言功能与 Blog 上线的公开 Changelog

- 优先级：`P2`
- 页面或界面：`https://bgremove.video/changelog/` 及 `es`、`pt`、`de`、`fr` 对应语言 Changelog
- 当前问题与线上证据：四种语言的 Change Background 页面、五种语言 Blog 列表与首批文章尚未上线，因此当前公开 Changelog 没有这批内容。新增四个完整本地化功能页、五语 Blog 和全站入口属于用户可以发现的重要更新，应在实际发布后记录；普通元数据、翻译修正或内部实现过程不应进入 Changelog。
- 修改要求：仅在本文件批准的四个 Change Background 本地化页面、五个 Blog 列表页、首批 15 个语言文章页面以及顶部/页脚入口全部上线并通过生产验证后，在五种语言 Changelog 顶部各新增一条按实际发布日期记录的本地化条目。英文条目只表达：`Change Background is now available in Spanish, Portuguese, German, and French. The new BGRemove blog also launches in five languages with practical guides for cleaner cutouts, transparent WebM, and choosing a video background.` 四种翻译准确传达相同事实，不增加功能承诺。
- 验收标准：五个 Changelog 页面各有且仅有一条日期一致、语言正确的新记录；条目只说明 Change Background 新增四种语言，以及五语 Blog 和三类首批指南已经上线。任一对应页面、文章、导航或页脚入口未实际发布时，不得提前写入；条目不出现仓库、文件、组件、提交、供应商、成本、内部指标、关键词、SEO 策略、提示词或实现细节。
- 不要修改：已有历史条目、日期、版本和顺序；不为同一发布事项创建多条记录，不在 Changelog 中列出轻微排版、元数据、翻译校对、结构化数据或内部技术工作。
