---
site_id: "bgremove-video"
name: "BGRemove"
production_url: "https://bgremove.video/"
changelog_url: "https://bgremove.video/changelog/"
delivery_method: "direct_publish"
target_repository: "not_applicable"
default_branch: "not_applicable"
updated_at: "2026-10-14"
---

# BGRemove 当前待办事项

## 已批准任务

### 修正 llms.txt 的过期产品事实并收录图片去背景工具

- 优先级：`P1`
- 页面或界面：`https://bgremove.video/llms.txt`
- 当前问题与线上证据：线上 `llms.txt` 仍把 BGRemove 描述成纯视频工具，并写有“1 个免费 10 秒视频”、Creator `$19/月`、Studio `$49/月`、ProRes 4444、PNG sequence 和 bare matte 等已不符合当前产品的内容；线上 `https://bgremove.video/pricing/` 当前明确为每个账号每 24 小时最多 3 个成功视频、单段最长 60 秒、仅输出带 VP9 alpha 的透明 WebM、无订阅或结账。`llms.txt` 也完全没有新上线的 `https://bgremove.video/remove-image-background/`，会让引用该文件的 AI 系统返回错误价格、额度、格式和产品范围。
- 修改要求：完整重写 `llms.txt` 中的摘要与 Product 段，删除所有已下线的付费方案、旧视频额度和当前不提供的导出格式。品牌摘要同时说明图片与视频去背景；视频条目只保留“每 24 小时 3 个成功任务、最长 60 秒、透明 WebM with VP9 alpha、原尺寸、无水印、文件保留 24 小时”；新增 `Remove Image Background` 条目并链接 `https://bgremove.video/remove-image-background/`，只写线上已验证的“JPG/PNG/WebP 输入、原尺寸透明 PNG 输出、每 24 小时 20 张图片、无水印、图片额度与视频额度分开、文件保留 24 小时”。Pricing、FAQ、About 等现有条目的摘要同步到线上当前事实。
- 验收标准：直接访问 `https://bgremove.video/llms.txt` 能看到图片工具及其规范 URL；全文不再出现 `$19`、`$49`、Creator、Studio、`10-second`、ProRes、PNG sequence 或 bare matte；所有额度、时长、输出和保留时间与对应线上页面一致。
- 不要修改：不要增加未上线的套餐、API、批处理、导出格式、匿名上传或模型能力；不要把页面宣传语当成未经验证的性能指标。

### 统一品牌实体页面对图片与视频产品的描述

- 优先级：`P1`
- 页面或界面：`https://bgremove.video/about/` 及 `/es/about/`、`/pt/about/`、`/de/about/`、`/fr/about/`；全站页脚；五种语言页面共用的 `Organization` 结构化数据
- 当前问题与线上证据：图片去背景工具已经在五种语言上线并进入主导航与站点地图，但 About 页标题、主标题和正文仍只把 BGRemove 定义为视频抠像产品，英文页仍使用“An independent team focused on video workflows”；页脚仍写“Video matting…”；图片工具五个语言版本的 `Organization.description` 仍是英文且只描述视频。这些互相冲突的实体信息会削弱搜索引擎和 AI 系统对 BGRemove 当前产品范围的判断。
- 修改要求：保留“BGRemove 起源于视频去背景”的事实，但把 About 页首屏、产品范围段落和页脚品牌简介更新为同时覆盖图片与视频。英文核心实体描述统一为：`BGRemove removes backgrounds from images and videos, returning full-size transparent PNGs for photos and transparent WebM with VP9 alpha for videos.`；西班牙语、葡萄牙语、德语和法语页面使用自然的本地化表述，不保留英文描述。About 页同时列明两个独立免费额度：图片每 24 小时 20 张，视频每 24 小时 3 个成功任务；不要把两者合并成一个额度。将同一事实同步到各语言页面的 `Organization.description`，并将 About 页 title、meta description 与 H1 从“仅视频”改为能准确覆盖两类产品的本地化文案。
- 验收标准：五种语言 About 页、全站页脚和 `Organization` JSON-LD 均明确包含图片与视频两类去背景能力；各语言结构化数据使用对应语言；这些品牌实体位置不再把 BGRemove 定义为只提供视频去背景；图片与视频额度、输出格式互不混淆。
- 不要修改：首页及视频专题页针对视频搜索意图的主标题和正文定位；不要宣称未上线的统一工作区、跨产品批处理或额外导出格式。

### 为图片工具补充可验证来源与页面级实体数据

- 优先级：`P2`
- 页面或界面：`https://bgremove.video/remove-image-background/` 及 `/es/`、`/pt/`、`/de/`、`/fr/` 对应页面
- 当前问题与线上证据：页面 FAQ 声称使用“BiRefNet, an open-source segmentation model built for high-resolution foreground extraction”，但没有链接到模型的官方项目或论文；当前 JSON-LD 只有 `Organization`、`BreadcrumbList` 和 `FAQPage`，没有描述该在线图片工具本身的页面级实体。页面已有清晰步骤、限制和 FAQ，不需要继续堆砌泛化段落，当前 GEO 缺口主要是来源可核验性和机器可读的工具实体。
- 修改要求：在“What model does the work?”答案中把 BiRefNet 名称链接到官方项目 `https://github.com/ZhengPeng7/BiRefNet`，并在链接附近明确其论文名称 `Bilateral Reference for High-Resolution Dichotomous Image Segmentation`；四个翻译页提供对应语言的自然表述，但保留模型名、论文名和官方 URL。每个页面新增与可见内容一致的 `WebApplication` JSON-LD，至少包含本地化 `name`、`description`、规范 `url`、`applicationCategory: "MultimediaApplication"`、`operatingSystem: "Any"`、`inLanguage`、`offers.price: "0"` 和 `offers.priceCurrency: "USD"`；不要加入评分、评论、虚构作者或不可见功能。
- 验收标准：五个图片工具页面均能从可见 FAQ 直接打开 BiRefNet 官方项目；结构化数据解析无语法错误，`WebApplication.url` 与各页 canonical 一致，语言字段与页面一致，描述、免费价格、输入输出和额度均可在页面可见正文中得到验证。
- 不要修改：不要把 BiRefNet 描述为 BGRemove 自研模型；不要写“最佳”“SOTA”或无法由线上产品证明的精度、速度和排名；不要移除现有 `FAQPage`、`BreadcrumbList` 或 canonical/hreflang。

### 优化四种翻译页的搜索摘要与示例图替代文本

- 优先级：`P2`
- 页面或界面：`https://bgremove.video/es/remove-image-background/`、`/pt/remove-image-background/`、`/de/remove-image-background/`、`/fr/remove-image-background/`
- 当前问题与线上证据：四个翻译页的 meta description 当前分别约为 159、156、167、180 个字符，德语和法语尤其容易在搜索结果中被截断；四页的两张首屏前后对比图都仍使用英文 alt，形成明显的本地化与图片可访问性缺口。canonical 和五语言 hreflang 已正确，无需重做。
- 修改要求：将 meta description 分别替换为以下文本：西班牙语 `Quita el fondo de una foto en segundos. PNG transparente a tamaño completo, pelo suelto intacto. Gratis: 20 imágenes al día, sin marca de agua.`；葡萄牙语 `Remova o fundo de uma foto em segundos e baixe um PNG transparente em tamanho original. Preserva fios soltos. Grátis: 20 imagens por dia, sem marca d’água.`；德语 `Fotohintergrund in Sekunden entfernen. Transparentes PNG in voller Größe, feine Haare erhalten. Kostenlos: 20 Bilder täglich, ohne Wasserzeichen.`；法语 `Supprimez le fond d’une photo en quelques secondes. PNG transparent en taille réelle, cheveux préservés. Gratuit : 20 images/jour, sans filigrane.`。同时将每页原图与去背景结果图的 alt 改为准确的本地化描述，不包含关键词堆砌，并同步对应的 `og:description` 与 `twitter:description`。
- 验收标准：四页 description 均不超过 155 个字符且与各页可见事实一致；Open Graph 与 Twitter 描述同步；两张示例图在四页均不再出现英文 alt，且分别能说明“原始街景人像”和“保留发丝、透明背景的处理结果”；canonical 与现有 hreflang 组合保持正确。
- 不要修改：英文页当前 50 字符 title 和 145 字符 description；不要更改页面 URL、语言目录、图片内容或已正确的 canonical/hreflang。

### 增加覆盖不同主体的真实图片去背景案例

- 优先级：`P2`
- 页面或界面：`https://bgremove.video/remove-image-background/` 及 `/es/`、`/pt/`、`/de/`、`/fr/` 对应页面，在“Why the Edge Holds Where Simple Cut-Outs Break”之后、“Where It Struggles”之前
- 当前问题与线上证据：线上页面主内容约 5,134px 高，但只有首屏同一张人像的原图与透明结果两个图层；从优势说明、限制、三步流程到末尾 CTA 均没有其他图片。单一人像只能证明发丝场景，无法直观看出页面正文声称的商品硬边、宠物毛发和复杂日常背景处理效果，也使长页面中段形成连续的大块纯文字。
- 修改要求：新增一个本地化的真实案例区，标题表达“不同主体的实际处理结果”，固定展示 3 组由当前线上工具真实生成、未经人工修边的前后对比：①不透明包装或普通商品，展示清晰硬边；②猫或狗，展示毛发边缘；③复杂日常背景中的全身人物，展示轮廓与衣物边缘。每组同时显示原图和透明 PNG 结果，明确标注 Original / Background removed，并用一句短说明指出该案例需要观察的边缘类型；所有可见标题、标签、说明和 alt 在西班牙语、巴西葡萄牙语、德语、法语页面完整本地化。素材必须为自有、明确许可或可合法使用的图片，并在需要时保留来源标注；结果必须直接来自当前产品，不得人工补边、换主体、使用客户文件或暗示客户案例。区块位于首屏案例之后，作为能力证据，不重复首屏上传 CTA。
- 验收标准：五种语言页面均新增且只新增同一套 3 组案例，每组可同时辨认原图与真实透明结果；三组分别覆盖商品、宠物毛发和复杂背景全身人物，不重复首屏近景发丝人像；桌面端布局清晰，390px 宽移动端无横向溢出、异常裁切、文字压图或过小标签。所有新增图片声明固有宽高，使用响应式尺寸和现代图片格式，并在进入视口前懒加载；关闭 JavaScript 后仍能看到静态前后图及说明。每张图的本地化 alt 能区分主体、原图或处理结果，不出现关键词堆砌。
- 不要修改：现有首屏人像素材、对比滑块、上传与登录流程、产品额度、输出格式、限制说明、FAQ、canonical、hreflang 或现有页面顺序。不要选用玻璃、水、透明包装、薄纱、主体与背景同色或多人重叠等页面已明确列为弱项的素材；不要为该普通内容增强新增或扩写公开 Changelog 记录。

### 更新本次发布的公开更新日志

- 优先级：`P1`
- 页面或界面：`https://bgremove.video/changelog/` 及四个对应语言版本
- 当前问题与线上证据：图片去背景是新的用户可见产品能力，已经在五种语言页面、主导航和站点地图上线，但线上 Changelog 最新记录仍停留在 2026-09-13，全文没有图片去背景发布记录。
- 修改要求：完成并发布上述整改后，在五种语言 Changelog 各新增一条同批次记录，日期使用实际发布日。英文标题使用 `Image background removal is now available`，正文使用 `BGRemove can now remove a photo background and return a full-size transparent PNG. It accepts JPG, PNG and WebP, keeps fine hair and soft edges, includes 20 free image removals per 24-hour window, and is available in English, Spanish, Portuguese, German and French.`；其他语言使用事实完全一致的自然本地化版本。本条只概括图片去背景这一项重要用户功能，不记录 `llms.txt`、元数据、alt、结构化数据或其他 SEO/GEO 维护。
- 验收标准：五种语言 Changelog 各有且只有一条对应新记录，日期为实际发布日；记录所述输入格式、输出、额度和语言范围均与线上产品一致；语言切换后能看到同一发布事实的本地化版本。
- 不要修改：历史记录及其日期。不得提及文件名、组件名、代码架构、仓库、分支、提交、基础设施或服务商配置、成本、密钥、安全敏感实现、客户数据、内部指标、AI 提示词或内部工作流程。
