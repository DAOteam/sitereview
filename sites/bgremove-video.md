---
site_id: "bgremove-video"
name: "BGRemove"
production_url: "https://bgremove.video/"
changelog_url: "https://bgremove.video/changelog/"
delivery_method: "direct_publish"
target_repository: "not_applicable"
default_branch: "not_applicable"
updated_at: "2026-09-11"
---

# BGRemove 当前待办事项

## 已批准任务

### 修正 Remove Green Screen 首屏左右工作区未对齐

- 优先级：`P1`
- 页面或界面：`https://bgremove.video/green-screen-remover/` 的首屏双栏工作区
- 当前问题与线上证据：用户于 2026-09-11 提供的生产页面截图显示，在已登录且最近作品为空的桌面状态下，左侧 `Upload a Green Screen Video` 标题和格式说明位于有边框的上传卡片外，右侧 `Your recent clips` 标题位于右侧卡片内，导致右侧卡片从标题位置开始，而左侧卡片低约一组标题与说明的高度；左右卡片的上边缘、下边缘和整体高度均未对齐。2026-09-11 未登录桌面端线上复核也出现相同结构性错位，说明问题不只存在于单一账号或作品状态。
- 修改要求：把桌面端首屏工作区整理为同一个两列网格行中的两个同级外层卡片。左侧卡片必须从 `Upload a Green Screen Video` 开始，把该标题、格式说明、上传/登录/处理/结果区域、免费次数和限制信息全部包含在同一个外边框内；右侧卡片从其自身标题开始，显示当前账号状态对应的示例、最近作品或空状态。两个外层卡片使用相同的顶部起点、外边框、圆角、外层内边距和高度规则，网格采用等高拉伸；内容较多的一侧撑高该行时，另一侧外层卡片同步拉伸到相同高度，不使用负边距、位移或固定裁切高度伪造对齐。保留左右内部内容各自需要的分区和留白，不要求内部每一行水平对应。
- 验收标准：在 `1024px` 及以上桌面视口，左右两个外层卡片的上边缘和下边缘位置差均不超过 `2px`，外层高度一致；左侧标题与格式说明完整位于左侧边框内，且与右侧标题采用一致的卡片头部内边距；分别验证未登录初始状态、已登录且最近作品为空、已登录且存在一条及多条作品、上传中、处理中、完成、失败和额度用尽状态，任何状态都不会让其中一张卡片单独下移、脱离网格、溢出或被裁切；内容增加时两张外层卡片共同增高。小于桌面断点时按首页现有顺序堆叠，不强制两个卡片等高，但标题与说明仍留在各自卡片内，页面无横向滚动、文字遮挡或按钮溢出。
- 不要修改：首屏 H1、介绍文案、上传与处理能力、登录规则、免费额度、格式与时长限制、输出格式、示例内容、最近作品数据和交互；除本文件单独批准的模块顺序调整外，不修改首页、换背景页、绿幕页首屏以外的正文、图片、SEO 元数据、结构化数据、导航或页脚。该修复属于轻微布局调整，不新增或修改公开 Changelog。

### 将 No Green Screen 转折模块移动到首屏工作区下方

- 优先级：`P2`
- 页面或界面：`https://bgremove.video/green-screen-remover/` 的 `No Green Screen? Remove Any Background With AI.` 模块
- 当前问题与线上证据：用户于 2026-09-11 明确要求把该模块移动到首屏下方。2026-09-11 线上页面的实际内容顺序为：首屏工具工作区 → `A Green Screen Remover That Does Not Need a Perfect Screen` 卖点区 → `AI Green Screen Remover vs. Chroma Key` 对比区 → `No Green Screen? Remove Any Background With AI.` 转折模块。该模块距离首屏过远，无法在用户看完专用工具后立即承接“没有绿幕、只想去除普通背景”的相邻需求。
- 修改要求：移动整个 `No Green Screen? Remove Any Background With AI.` 区块，使其成为首屏标题、介绍和双栏工具工作区结束后的第一个正文模块，并位于 `A Green Screen Remover That Does Not Need a Perfect Screen` 卖点区之前。移动时保留现有 H2、正文、`Remove Video Background` 按钮、按钮目标 `/`、模块容器、视觉样式和可访问语义，不复制第二份模块，不通过 CSS 视觉排序制造与 DOM 不一致的顺序。
- 验收标准：桌面端和移动端的可见顺序及 DOM 顺序均为：首屏双栏工作区 → `No Green Screen? Remove Any Background With AI.` → `A Green Screen Remover That Does Not Need a Perfect Screen` → `AI Green Screen Remover vs. Chroma Key`；页面只出现一次该转折模块；按钮文字仍为 `Remove Video Background` 且点击后进入 `/`；移动后模块与首屏及后续卖点区之间使用页面现有一致的区块间距和分隔方式，无异常大空白、重叠、跳跃或横向滚动。
- 不要修改：该模块及其他模块的英文文案、标题级别、链接目标、视觉设计和交互；不修改首屏功能、其他正文模块、SEO 元数据、结构化数据、导航或页脚。该调整属于内容顺序优化，不新增或修改公开 Changelog。

### 补充 Chroma Key 定义、FAQ 与适用边界

- 优先级：`P1`
- 页面或界面：`https://bgremove.video/green-screen-remover/` 的 `What Is Green Screen Removal (Chroma Key)?` 定义段、`AI Green Screen Remover vs. Chroma Key` 对比区和 FAQ
- 当前问题与线上证据：2026-09-11 线上页面的定义段仍以 `Green screen removal, also called chroma keying...` 开头，没有直接解释 chroma key green screen 是物理背景还是处理方法；FAQ 没有正面回答 chroma key 与 green screen 的关系，现有 `Can I use BGRemove with a blue screen or another solid-color background?` 主要从工具侧回答；对比区只简短提及 manual chroma key remover，没有独立说明什么情况下手动工具更合适。线上可见正文中 `chroma key green screen` 精确词组当前出现 0 次。
- 修改要求：严格按下方英文定稿完成四处修改，标点和大小写保持一致：
  1. 在 H2 `What Is Green Screen Removal (Chroma Key)?` 下，把现有第一句 `Green screen removal, also called chroma keying, separates a filmed subject from a colored backdrop so the background can become transparent or be replaced.` 完整替换为下方“定义段开头英文定稿”的两句；紧随其后的 `A traditional chroma key remover looks for a selected shade of green...` 及后续正文保持不动。
  2. 在可见 FAQ 列表最前面新增下方“新增首条 FAQ 英文定稿”；同步添加到 `FAQPage` JSON-LD 的第一项。
  3. 把现有 `Can I use BGRemove with a blue screen or another solid-color background?` 问答完整替换为下方“替换 blue-screen FAQ 英文定稿”，保持它在其他既有 FAQ 中的相对位置；其中 `Remove Video Background` 继续作为自然锚文本链接到 `/`。同步替换 `FAQPage` JSON-LD 对应项。
  4. 在 `AI Green Screen Remover vs. Chroma Key` 对比表及现有结尾句 `Use BGRemove when you want the subject separated automatically. Use a full editor when you need to adjust the matte frame by frame.` 之后，新增下方 H3 和正文；它仍属于同一个对比区，不新增 H2 或独立顶级区块。

#### 定义段开头英文定稿

```text
A chroma key green screen is a backdrop in one flat color — nearly always bright green — that you shoot against so the background can be replaced later. Green screen removal, also called chroma keying, separates the subject from that backdrop so the area behind it becomes transparent or takes on a new scene.
```

#### 新增首条 FAQ 英文定稿

```text
Q: What is the difference between chroma key and green screen?

A: A green screen is the physical backdrop — the cloth or wall in one flat green that you shoot against. Chroma key (chroma keying) is the color-based process of removing that backdrop afterward. The two words get used interchangeably, which is why people search for chroma key green screen as if it were one thing: it means a green backdrop that is going to be keyed out. The same technique applies to blue screens and other solid colors, so the screen does not have to be green — chroma key is the method, not the color.
```

#### 替换 blue-screen FAQ 英文定稿

```text
Q: Can I chroma key a background that is not green?

A: Yes. Chroma key works on any backdrop that holds one distinct, evenly lit color. Blue is the classic alternative and the usual choice when the subject is wearing green, since the key color should not match anything on the person. BGRemove does not depend on a key color at all — it identifies the subject instead — so blue screens, other solid-color backdrops, and ordinary rooms all work. If your footage was not shot against green, use Remove Video Background for the general workflow.
```

#### 对比区新增 H3 英文定稿

```text
H3: When a chroma key remover still wins

A chroma key remover gives you control that an automatic tool cannot: frame-level adjustment of the matte. If a shot has flyaway hair against an evenly lit screen, smoke, glass, or reflective props, or a camera move where the edge has to hold in every frame, working with a manual chroma key remover in a full editor is the better route — you can set the key color, soften the edge, and suppress spill one frame at a time. Use BGRemove for the cutouts that do not need that level of hand work.
```

- 验收标准：URL、Title、Meta description、canonical、唯一 H1 和全部现有 H2 保持不变；定义段开头与三个新增或替换文案逐字匹配定稿，旧定义第一句和旧 blue-screen 问答不再出现；`chroma key green screen` 精确词组在整个可见英文正文中恰好出现 2 次，分别位于定义段开头和新增首条 FAQ，不通过隐藏文本、alt、元数据或结构化数据之外的重复内容补词。可见 FAQ 总数由 10 条变为 11 条，新问题排在第一位；可见 FAQ 与 `FAQPage` JSON-LD 的 11 条问题、答案、顺序和措辞一致且可解析。新增 H3 位于指定结尾句之后、对比区结束之前，标题层级正确；桌面端与移动端没有异常空白、溢出、重复模块或阅读顺序错误。完成英文修改后，四个待新增语言版本必须以这版最新英文内容为源文，四处内容不得遗漏或继续使用旧版本。
- 不要修改：页面 URL、Title、Meta description、H1、H2 骨架、其他正文、其他 FAQ 的内容与顺序、现有对比表、功能、产品事实、CTA、图片、导航、结构化数据实体类型或索引信号。该任务属于内容补充，不新增 Changelog 记录，也不得把它写入本文件现有的多语言发布 Changelog。

### 为四种语言的全站顶部导航补齐 Remove 下拉菜单

- 优先级：`P1`
- 页面或界面：`https://bgremove.video/es/`、`https://bgremove.video/pt/`、`https://bgremove.video/de/`、`https://bgremove.video/fr/` 下的全部公开页面及其桌面端、移动端顶部导航
- 当前问题与线上证据：用户于 2026-09-11 指出其他语言版本顶部没有下拉菜单。2026-09-11 线上复核西班牙语首页确认，顶部导航直接从 `Cómo funciona` 开始，没有英文站已经上线的 `Remove` 下拉入口，也没有 `Quitar fondo de vídeo` 和去绿幕两个功能选项；葡萄牙语、德语和法语页面使用相同的旧版本地化导航结构。若只在四个新去绿幕页自身增加入口，用户从其他本地化页面仍无法通过顶部导航发现这项功能。
- 修改要求：让 `es`、`pt`、`de`、`fr` 下所有公开页面的顶部导航与英文站使用同一套可访问下拉菜单结构，并放在其他主导航项之前。每个菜单只包含两个同语言功能链接：西班牙语菜单标题 `Quitar`，选项 `Quitar fondo de vídeo` → `/es/`、`Quitar pantalla verde` → `/es/green-screen-remover/`；巴西葡萄牙语菜单标题 `Remover`，选项 `Remover fundo de vídeo` → `/pt/`、`Remover fundo verde` → `/pt/green-screen-remover/`；德语菜单标题 `Entfernen`，选项 `Videohintergrund entfernen` → `/de/`、`Greenscreen entfernen` → `/de/green-screen-remover/`；法语菜单标题 `Supprimer`，选项 `Supprimer l’arrière-plan d’une vidéo` → `/fr/`、`Supprimer un fond vert` → `/fr/green-screen-remover/`。复用英文导航现有的视觉、展开状态、焦点管理、点击菜单外关闭和 Escape 关闭行为；桌面端和移动端均显示同样两个选项。四个去绿幕链接必须与对应语言页面同时上线，不能先发布指向 `404` 的菜单项。
- 验收标准：从四种语言的首页、How it works、FAQ、Pricing、Use cases、各使用场景页、各工具页和 Changelog 中各抽查至少一页，桌面端与移动端顶部均能找到当前语言的 Remove 下拉菜单；菜单标题和两个选项与定稿一致，不出现英文残留或混用其他语言；两个链接分别进入当前语言的首页和去绿幕页面且直接返回 `200`。鼠标点击、触屏点击、Tab、Enter 或 Space、Escape 均可完成展开、访问和关闭；展开状态通过 `aria-expanded` 或等效语义正确暴露，焦点可见，菜单外点击可关闭，当前页状态清楚；菜单不会挤压、遮挡、换行破坏其他导航项，也不造成横向滚动。
- 不要修改：四种语言现有其他导航项的文字、顺序和目标；英文导航；页脚 Product 列；登录、账号和语言切换器行为。不要在菜单中增加 Change Background、定价或其他第三个选项；不要在对应去绿幕页面上线前发布失效链接。

### 为 Remove Green Screen 页面补齐四种语言版本

- 优先级：`P1`
- 页面或界面：新增 `https://bgremove.video/es/green-screen-remover/`、`https://bgremove.video/pt/green-screen-remover/`、`https://bgremove.video/de/green-screen-remover/`、`https://bgremove.video/fr/green-screen-remover/`；同步英文页、语言切换、内部链接、`hreflang` 与 XML Sitemap
- 当前问题与线上证据：2026-09-11 线上验证显示，上述西班牙语、葡萄牙语、德语和法语 URL 均返回 `404`；英文 `https://bgremove.video/green-screen-remover/` 只有自引用 canonical，没有任何 `rel="alternate" hreflang`；`https://bgremove.video/sitemap-0.xml` 也只包含英文去绿幕页。网站其他核心页面已经具备 `en`、`es`、`pt-BR`、`de`、`fr` 和 `x-default` 的互惠语言标注，因此新功能页目前与全站既有多语言覆盖不一致。
- 修改要求：
  1. 先完成并验证本文件批准的英文 Chroma Key 定义、FAQ 与适用边界修改，再以该最新版线上英文 `/green-screen-remover/` 为唯一功能与内容基准，新增西班牙语（URL 前缀 `es`）、巴西葡萄牙语（URL 前缀 `pt`，语言代码 `pt-BR`）、德语 `de` 和法语 `fr` 四个完整页面。逐项本地化页面全部可见文字，包括 TDK、H1/H2/H3、正文、功能卡片、比较表、步骤、实用建议、使用场景、FAQ、CTA、按钮、辅助说明、图片 alt、空状态、上传与处理状态、失败提示和免费额度信息；不得只翻译静态正文而保留英文功能界面。翻译须使用各语言面向普通用户的自然表达，不逐词硬译，不更改任何产品事实、数字、格式、限制、免费规则、登录规则或适用边界。四个页面必须复用英文页相同的功能组件、布局、图片和语义结构，并同时包含本文件已批准的首屏卡片对齐及模块顺序调整。
  2. 每个页面使用本地化且唯一的 Title、Meta description 和单一 H1；核心主题分别采用下列自然表达，Title 保持不超过 60 个字符，Meta description 不超过 155 个字符：西班牙语 `Eliminar la pantalla verde de un vídeo online gratis`，巴西葡萄牙语 `Remover fundo verde de vídeo online grátis`，德语 `Greenscreen aus Video kostenlos online entfernen`，法语 `Supprimer le fond vert d’une vidéo en ligne gratuitement`。不要把英文关键词机械插入非英文正文。每个语言页使用自引用 canonical；五个页面都输出完全相同且互惠的 `hreflang` 集合：`en`、`es`、`pt-BR`、`de`、`fr`，并以英文页作为 `x-default`。语言切换器在五个页面之间切换到对应页面，不回退到各语言首页或返回 `404`。
  3. 把四个新 URL 加入 `sitemap-0.xml`；正文链接优先指向同语言的首页、`how-it-works`、`tools/green-screen-alternative`、`use-cases/creators` 和 `use-cases/ecommerce`，只有确实没有对应语言页时才回退到英文页。每种语言的可见 FAQ 与该页 `FAQPage` JSON-LD 逐字一致；Open Graph 与 Twitter 文案使用当前语言，图片可继续复用已审核的专属分享图，并设置准确的本地化图片 alt。新页面必须继承本文件单独批准的全站本地化 Remove 下拉菜单。
- 验收标准：四个新 URL 均直接返回 `200`，没有重定向、`noindex`、错误语言或英文占位正文；`html lang` 依次为 `es`、`pt-BR`、`de`、`fr`，canonical 均指向自身；五个语言页面都具有互惠且无缺项、无重复、URL 全部返回 `200` 的 `hreflang` 集合，`x-default` 指向英文页；四个新 URL 出现在 Sitemap 且英文页继续保留。桌面端和移动端逐页检查，标题、功能状态、比较表、步骤、FAQ、CTA、导航和页脚均使用当前语言，无英文残留、截断、溢出或布局破坏；功能流程、额度显示、透明 WebM 下载和进入换背景流程与英文页一致。语言切换器可从任意版本直接切到另外四个对应版本；各语言页的首页及内容内链进入相同语言页面，所有链接返回 `200`；结构化数据可解析并与可见内容一致。
- 不要修改：英文页已经确认的产品能力、数字、价格状态、免费额度、认证规则、格式、时长、文件大小、无水印声明、数据处理说明、内容边界和关键词定位；不创建英语与四种现有语言之外的新语言；不为本地化页面编造速度、效果保证、客户数据、评价、编辑器兼容保证、商业授权或本地处理能力。

### 更新多语言页面上线的公开 Changelog

- 优先级：`P2`
- 页面或界面：`https://bgremove.video/changelog/` 及其 `es`、`pt`、`de`、`fr` 对应语言页面
- 当前问题与线上证据：四种语言的 Remove Green Screen 页面及相应的全站顶部入口尚未上线，因此当前 Changelog 没有这次语言覆盖扩展。一次新增四个完整本地化功能页并让四种语言的全站导航都可直接访问它，属于值得用户了解的重要更新；同批次的首屏对齐和模块移动属于小型布局调整，不应写入更新日志。
- 修改要求：仅在四种语言页面及全站本地化 Remove 菜单全部上线并通过生产验证后，为同一个发布事项在五个语言 Changelog 顶部各新增一条按实际发布日期记录的本地化条目；每个 Changelog 页面只新增一条。英文正文使用：`Remove Green Screen is now available in Spanish, Portuguese, German, and French, with matching navigation in each language.` 其他四条准确翻译该句，不增加功能承诺，也不提首屏对齐、模块移动或实现过程。
- 验收标准：五个 Changelog 页面各有且仅有一条日期一致、语言正确的新记录；条目只说明 Remove Green Screen 新增四种语言及对应语言导航，不出现仓库、文件、组件、提交、供应商、成本、内部指标、提示词或实现细节；任一语言页或相应导航未实际上线时，不得提前发布该批次条目。
- 不要修改：现有历史条目、日期、版本和顺序；不得为同一发布事项在同一语言页面重复创建记录，也不得把本批次的小型布局调整写入 Changelog。
