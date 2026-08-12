---
site_id: "bgremove-video"
name: "BGRemove"
production_url: "https://bgremove.video/"
changelog_url: "https://bgremove.video/changelog/"
delivery_method: "direct_publish"
target_repository: "not_applicable"
default_branch: "not_applicable"
updated_at: "2026-08-12"
---

# BGRemove 当前待办事项

## 已批准任务

### 将英文首页扩充到约 1300 个可见单词

- 优先级：`P1`
- 页面或界面：英文首页 `https://bgremove.video/`
- 当前问题与线上证据：首页当前 `<main>` 中约有 485 个可见英文单词，整页包含导航和页脚约 580 个英文单词。页面已有清晰的标题、H1、三步流程、能力说明和 FAQ，但对 `AI video background remover` 的定义、适用素材、透明输出用途、输入输出限制及后续编辑流程解释不足。根据用户提供的产品使用反馈，新手下载透明 WebM 后直接用本地浏览器播放时，画面可能仍看起来带着原本的背景；这是正常的预览现象，但用户容易误以为背景没有被移除，也不知道如何使用该文件。当前搜索结果中的同类页面通常会直接回答这些问题，首页的主题覆盖深度与下载后的使用指导仍有明显缺口。
- 修改要求：保留现有首屏、演示、三步流程、能力说明、边缘案例、FAQ 和 CTA，在不重复现有段落的前提下，将英文首页 `<main>` 的可见正文扩充到 `1200–1400` 个英文单词，目标约 `1300` 个。新增约 `750–850` 个自然、具体且面向用户的单词，并至少加入以下内容模块：`What is an AI video background remover?`，用首句直接定义工具并解释逐帧主体分离和透明 alpha 输出；`What footage gives the best result?`，说明主体与背景区分、光线、遮挡、头发、运动模糊、玻璃及暗光等真实适用条件；`Why does my transparent WebM still look like it has the original background?`，面向新手明确说明，直接在本地浏览器中打开 WebM 时，浏览器可能没有按预期应用视频的 alpha channel，而是显示透明像素中仍保留的原始 RGB 画面，因此原来的背景看起来仍然存在；这是正常的直接播放现象，不一定表示去背景失败。说明本地浏览器直接播放不能作为透明度是否有效的可靠验收方法；建议在支持 WebM alpha 的环境中检查，或把视频放到编辑时间线的上层，再把颜色、图片或另一段视频放在下层，确认下层内容能够透过主体周围区域显示；同时说明在网页中使用时，需要浏览器支持相应透明视频编码，并让 `<video>` 位于页面背景或其他元素上方；如果使用的软件不支持 WebM alpha，应查阅该软件对透明视频的正式支持方式或转换为其明确支持的带 alpha 格式，不能通过改扩展名解决；`What can you do with a transparent video?`，说明透明 WebM 可在编辑器中叠加颜色、图片或视频，并覆盖产品视频、社交内容、教程、演示和客户交付等用途；`Transparent output or a replaced background?`，用简短对比帮助用户判断何时保留 alpha、何时在编辑器中替换背景；`Formats, limits, and what happens after upload`，只使用线上已有且可核实的信息说明支持的 MP4、MOV、WebM、M4V、GIF、60 秒上限、每 24 小时 3 个成功视频、无水印和透明 WebM 输出。新增正文使用描述性锚文本链接到 `/how-it-works/`、`/tools/remove-background-from-video/`、`/tools/green-screen-alternative/`、`/use-cases/` 以及与产品视频、创作者和代理机构对应的现有用途页。新增段落必须在服务器返回或首屏加载的 HTML 中可抓取，不得只放在图片、脚本、结构化数据或默认折叠区域。
- 验收标准：英文首页 `<main>` 中可见正文为 `1200–1400` 个英文单词，目标约 `1300` 个；新增模块均有清晰 H2 或 H3，定义型问题在标题后的首段直接作答；WebM 新手模块明确说明“本地浏览器播放时仍看到原背景”可以是正常预览现象，并解释浏览器可能没有按预期应用 alpha channel、原始 RGB 画面仍可被显示；明确指出不能以本地浏览器直接播放作为去背景是否成功的判断依据；提供编辑时间线上下层验证方法、网页叠加用法及软件不支持时的处理原则，并说明改文件扩展名不能创造透明通道；不得承诺所有浏览器、系统播放器或编辑软件都支持 WebM alpha；`remove video background online`、`AI video background remover`、`transparent video`、`alpha channel`、`without a green screen` 和 `no watermark` 仅在语义需要时自然出现，不连续重复或堆砌；新增的站内链接全部返回成功并使用能说明目标内容的锚文本；页面仍只有一个 H1；现有 FAQ 可见内容与 `FAQPage` 结构化数据保持一致；人工通读没有空泛套话、虚构数据或明显 AI 模板化措辞。
- 不要修改：SEO 标题 `Remove Video Background Online Free - No Watermark`、H1 `Remove video background online. Free, no watermark.`、当前 meta description、canonical、hreflang、`WebApplication`、`FAQPage`、`VideoObject` 和 `Organization` 结构化数据、现有产品能力、额度规则、格式支持、保留规则、首屏 CTA、认证或处理流程。不要加入未经证实的速度、质量、准确率、排名、客户评价或兼容性声明，不要通过隐藏文字、关键词列表或重复 FAQ 凑字数，不要修改非英文首页。

### 补充 Use Cases 汇总页的搜索意图覆盖

- 优先级：`P2`
- 页面或界面：英文页面 `https://bgremove.video/use-cases/`
- 当前问题与线上证据：该页面 `<main>` 当前约有 182 个可见英文单词，只用三段简短介绍指向产品视频、社交内容和代理机构页面。页面能够被抓取并有自引用 canonical，但内容不足以帮助搜索用户比较场景、判断适配条件或选择下一步，作为用途主题的汇总页过薄。
- 修改要求：将该页面 `<main>` 的可见正文扩充到 `550–750` 个英文单词。保留现有三个用途入口，分别补充适用对象、典型输入、透明输出的后续用途、需要留意的素材条件和指向对应详情页的描述性链接；新增一个简洁的 `Which workflow fits your video?` 判断区块，按电商产品素材、创作者或讲解视频、代理机构多版本交付给出直接选择建议；新增一个简短段落说明透明输出可复用于不同背景和版式，而不是再次处理源视频。内容必须与各详情页分工明确，汇总页负责选择和导航，具体操作细节留给详情页。
- 验收标准：页面 `<main>` 中可见正文为 `550–750` 个英文单词；三个用途均有独立标题、具体说明和可用的描述性内部链接；判断区块能让用户仅阅读该页就选择合适用途；页面继续只有一个 H1，标题、canonical 和现有用途 URL 不变；正文没有重复首页的大段文字，也不与三个详情页争抢完全相同的主标题和段落。
- 不要修改：现有用途详情页、非英文页面、产品能力、额度、价格、格式、处理行为或导航结构。不要虚构客户案例、转化数据、行业统计、处理速度或效果保证。

### 修复工具页结构化面包屑中的无效父级 URL

- 优先级：`P1`
- 页面或界面：英文、西班牙语、葡萄牙语、德语和法语的全部 `/tools/<tool-name>/` 页面及其 `BreadcrumbList` 结构化数据
- 当前问题与线上证据：各语言工具详情页的 `BreadcrumbList` 都把中间层指向对应的 `/tools/` 父级，例如英文页指向 `https://bgremove.video/tools/`。实际检查中，`/tools/`、`/es/tools/`、`/pt/tools/`、`/de/tools/` 和 `/fr/tools/` 均返回 403，且这些父级 URL 不在 sitemap 中。Google 将面包屑用于理解页面在站点层级中的位置，无效父级会传递错误的导航关系。
- 修改要求：选择一种与真实站点结构一致的处理方式并全语言统一：如果不准备提供工具汇总页，则从每个工具详情页的可见面包屑和 `BreadcrumbList.itemListElement` 中删除无效 `/tools/` 中间层，使用“首页 → 当前工具页”的有效路径；如果保留该中间层，则必须建立对应语言的可访问、可索引、具有自引用 canonical 的工具汇总页，将其加入站内导航和 sitemap，并提供指向所有工具详情页的描述性链接。不得让结构化数据指向 3xx、4xx、登录页或不存在的 URL。
- 验收标准：五种语言所有工具详情页的每一个面包屑 URL 最终返回 200；结构化面包屑与页面可见层级一致；当前位置是最后一项且 URL 为当前 canonical；不存在指向 `/tools/` 系列 403 页的 `ListItem`；用 Schema.org 验证器或 Google Rich Results Test 检查时没有面包屑错误；若新建汇总页，其 hreflang、canonical 和 sitemap 关系完整且页面不是薄链接列表。
- 不要修改：工具详情页 URL、现有 canonical、页面主内容、产品能力或非工具页面。不要为了保留三层结构创建空白、noindex 或仅供结构化数据使用的伪页面。

### 统一并校正 WebM alpha 兼容性说明

- 优先级：`P1`
- 页面或界面：所有语言中提及透明 WebM、浏览器、CapCut、Premiere、After Effects、DaVinci Resolve 或 Final Cut 的首页、`/how-it-works/`、FAQ、工具页和用途页
- 当前问题与线上证据：站内存在多处过于绝对且彼此不一致的兼容性表述，例如 `Drops straight into a browser, Premiere, or DaVinci Resolve.`、`Works in CapCut, Premiere, DaVinci Resolve, the browser`、`CapCut reads WebM with alpha... Same for Premiere, Resolve and Final Cut.`。这与用户提供的真实使用反馈“本地浏览器直接播放时可能仍看起来带着原背景”冲突。公开官方资料能确认 Chrome 网页中的 WebM VP8/VP9 alpha 用法，也明确指出 Safari 不支持相关 alpha transparency；Adobe 和 Apple 官方资料能说明 alpha compositing 的原理，但当前没有足够官方证据支持站内对所有列举软件直接导入 WebM alpha 的无条件承诺。事实不一致会同时削弱 SEO 信任与 AI 引用可靠性。
- 修改要求：盘点并统一所有语言中的同类表述。把“直接可用于任意浏览器或列举的所有编辑器”改为带边界的事实说明：WebM 文件包含 VP9 alpha；网页播放是否正确显示透明度取决于浏览器对该编码与 alpha 的支持；本地直接打开不是可靠验收方法；编辑软件的导入支持取决于软件、版本、操作系统和已安装的解码器。只保留能由当前官方文档或实际支持矩阵证明的具体软件名称，并在说明兼容性的页面提供靠近对应陈述的官方资料链接。若某编辑器不能直接可靠导入 WebM alpha，说明应转换为该软件官方支持的带 alpha 中间格式，并明确改扩展名无效。同步修改可见 FAQ 与对应 `FAQPage` 答案，保证所有语言含义一致。
- 验收标准：全站不再出现未经限定的 `drops straight into`、`works in`、`take anywhere` 或“所有浏览器/编辑器均支持”等兼容性承诺；首页新增的新手模块与其他页面没有冲突；WebM、VP9、alpha channel、浏览器预览和编辑器导入的说明在各页面一致；每项具体第三方兼容性结论都有当前官方来源和适用版本或平台边界；可见 FAQ 与 JSON-LD 完全一致；至少测试一个支持 WebM alpha 的网页叠加场景和一个不支持或忽略 alpha 的直接播放场景，并确认页面描述符合实际结果。
- 不要修改：BGRemove 实际输出格式、编码、处理流程或用户文件。不要虚构兼容性，不要引用论坛、营销软文或搜索摘要作为唯一证据，不要承诺第三方软件未来版本行为，也不要在公开更新日志中写内部测试环境或实现细节。

### 完善可核实的品牌实体结构化信息

- 优先级：`P2`
- 页面或界面：英文首页 `https://bgremove.video/` 的 `Organization` 结构化数据，并保持各语言共享实体引用一致
- 当前问题与线上证据：当前 `Organization` 已包含 `name`、`url`、`description`、支持邮箱和注册地址，但没有把 About 页面公开显示的法定名称 `BGRemove d.o.o.` 表达为 `legalName`，也没有 `contactPoint` 或 `logo`。Google 官方说明这些适用的 Organization 属性有助于理解和消歧品牌实体；当前页面已有足够的公开事实，可以在不虚构社交账号或注册标识的前提下补全核心实体信息。
- 修改要求：继续使用唯一稳定的 `@id` `https://bgremove.video/#organization`。增加 `legalName: "BGRemove d.o.o."`；使用现有公开支持邮箱增加 `contactPoint`，其中 `@type` 为 `ContactPoint`、`contactType` 为 `customer support`、`email` 为 `support@bgremove.video`，并只声明网站实际提供的语言；如站点已有满足 Google 图片要求、可公开抓取且至少 112×112 的代表性品牌 logo，则增加其绝对 URL，否则本批次不新增 `logo`，不得临时把空白图标或不合格 favicon 当作 logo。只在首页或单一组织说明页维护完整实体对象，其他页面继续通过同一 `@id` 引用，避免多份内容漂移。
- 验收标准：首页 `Organization` JSON-LD 可解析，`name`、`legalName`、`url`、`email`、`contactPoint` 和 `address` 与 About、Contact 页面可见信息一致；全站没有多个相互冲突的 Organization 实体；若加入 logo，其 URL 返回 200、可索引、尺寸至少 112×112 且白色背景下可识别；Rich Results Test 或 Schema.org 验证没有关键错误。
- 不要修改：公司名称、地址、邮箱或任何法定信息的可见内容。不要虚构电话、成立日期、税号、VAT、LEI、员工数、社交账号、评价、奖项或外部实体链接；不要仅为了字段完整度添加无法公开核实的数据。

### 验证额度周期尚未开始的状态

- 优先级：`P1`
- 页面或界面：登录后的英文页面 `https://bgremove.video/app/account/` 在尚未开始额度周期时的状态
- 当前问题与线上证据：当前登录账号已有生效中的额度周期，线上页面已能确认两处摘要显示相同的真实日期、时间和 `datetime`，但无法通过该账号验证额度周期尚未开始时是否会避免虚构时间戳。
- 修改要求：仅使用现有的安全测试夹具或自动化测试验证额度周期尚未开始的状态。该状态必须显示真实的现有状态，或说明周期从第一个成功处理的视频开始，并且不得生成虚构时间戳。本任务只做验证；如果验证失败，停止并报告，不要发布修改。
- 验收标准：安全测试夹具或自动化测试通过，证明额度周期尚未开始时不会显示虚构的重置时间。若无法运行相应测试，则明确报告为未验证，不得声称任务完成。
- 不要修改：线上产品、额度计算、成功任务计数、失败任务处理、身份验证、处理流程、保留策略、下载、历史记录、公开定价页面或非英文页面。本验证任务不需要新增公开更新日志。

### 更新本次发布的公开更新日志

- 优先级：`P1`
- 页面或界面：`https://bgremove.video/changelog/`
- 当前问题与线上证据：当前新增的首页、用途页、导航层级和兼容性说明优化尚未发布，因此公开更新日志还没有对应的用户可见记录。
- 修改要求：完成并发布本批次实际上线的 SEO 与 GEO 改进后，只新增一条带日期的公开记录。文案只面向用户概括首页说明更完整、不同视频用途更容易选择、透明视频兼容性说明更准确或工具页导航更清晰等真实上线变化；如果本批次没有任何页面修改成功上线，则不要新增记录。品牌结构化数据等纯搜索引擎内部改动不必单独向用户描述。
- 验收标准：本批次恰好新增一条记录；只描述实际上线且用户可见的内容改进；所有描述与线上页面一致，简洁、脱敏且不包含内部实现信息。
- 不要修改：历史记录及其日期。不得提及文件名、组件名、代码架构、仓库、分支、提交、基础设施或服务商配置、成本、密钥、安全敏感实现、客户数据、内部指标、AI 提示词或内部工作流程。
