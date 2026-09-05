---
site_id: "bgremove-video"
name: "BGRemove"
production_url: "https://bgremove.video/"
changelog_url: "https://bgremove.video/changelog/"
delivery_method: "direct_publish"
target_repository: "not_applicable"
default_branch: "not_applicable"
updated_at: "2026-09-04"
---

# BGRemove 当前待办事项

## 已批准任务

### 修正四种非英语版本仍残留的旧产品事实与导航名称

- 优先级：`P1`
- 页面或界面：`/de/`、`/es/`、`/fr/`、`/pt/` 下的公开页面，重点是全站导航、`/pricing/`、`/faq/`、`/tools/tiktok-background-remover/`、`/tools/product-video-background-remover/` 和法语 `/use-cases/agencies/`
- 当前问题与线上证据：`2026-09-04` 重新抓取四种语言的 60 个公开页面后，很多正文已经更新，但仍有一组可见事实明显过期。四种语言导航仍分别显示 `Preise`、`Precios`、`Tarifs` 和 `Preços`，而不是“免费使用”含义。四个 `/pricing/` 仍把精修边缘、批量上传和 API 列为能力，部分语言还写着付费计划“已设计但未开放”。四个 `/faq/` 仍声称付费计划可处理 10 分钟视频，四个 TikTok 工具页也仍宣传付费版 10 分钟时长。四个 Product Video 工具页都对反光、玻璃和上釉材质直接回答“可以”，并在没有说明需要外部工具的情况下建议对透明包装手动清理，容易让用户误以为站内提供边缘精修。法语 Agency 页仍把批量队列作为已有能力。
- 修改要求：以最终英语对应页为事实基准，修正上述页面的可见正文、导航标签、meta description、Open Graph/Twitter 文案和 `FAQPage` JSON-LD。所有语言只保留当前真实边界：每个登录账户每 24 小时最多完成 3 次免费去背景；每段最长 60 秒、最大 2 GB；输出为保持源尺寸的透明 VP9 WebM，无水印；源文件和结果保留 24 小时；换背景完全免费且不限次数。目前没有付费计划、批量上传、API 或站内手动边缘精修。把导航和 FAQ 分类中的“价格/计费”概念改成各语言自然的“免费使用”，但保留 `/pricing/` URL。反光、玻璃和透明包装只能说明效果取决于透明度、反光和主体与背景的分离程度，并建议先测试代表性素材。
- 验收标准：重新抓取四种语言的 60 个公开页面后，不再发现付费 10 分钟、精修边缘、批量上传、API 或尚未开放的付费计划等当前能力承诺。四个 FAQ 和 TikTok 页都只说明最长 60 秒；四个 Product Video 页对反光和透明包装使用谨慎表述，如果提到手动精修则明确说明需要外部编辑器；法语 Agency 页不再声称支持批量队列。可见内容、meta description、社交元数据和 JSON-LD 不互相冲突，FAQ 结构化答案与可见答案一致。全站导航显示本地化的“免费使用”，`/pricing/` 继续返回 `200`，canonical 和 hreflang 不变。
- 不要修改：现有语言 URL、canonical、hreflang、法务正文、认证、实际处理能力、真实额度、数据保留或输出格式。不要要求各语言逐字直译、达到完全相同的单词数或牺牲当地搜索表达；不要虚构定价、套餐、性能指标、成功率、客户案例或尚未上线的能力。

### 修正四种非英语首页的额度说明、第三步和内部链接

- 优先级：`P1`
- 页面或界面：`https://bgremove.video/de/`、`https://bgremove.video/es/`、`https://bgremove.video/fr/`、`https://bgremove.video/pt/`
- 当前问题与线上证据：`2026-09-04` 四个首页已经上线三组本地化图文模块、9 个 FAQ 主题和对应语言的图片 alt 文本，这些完成内容不再列为待办。剩余问题有四处：首屏卖点仍只表达“免费版也可用”，没有明确每 24 小时 3 次；第三步的标题已提到设置新背景，但正文仍只要求把 WebM 放进外部编辑器，没有介绍站内换背景和 MP4 导出；“背景移除后能否更换背景”的 FAQ 答案仍声称只能在外部编辑器处理，甚至称站内刻意不提供背景功能；三组新图文模块中的 Product、Creator、Agency 和 Use Cases 链接仍指向无语言前缀的英文 URL，而不是同语言页面。
- 修改要求：把首屏额度卖点自然改为“每个登录账户每 24 小时最多免费去背景 3 次”的同语言表达。重写第三步正文和换背景 FAQ 答案，同时说明可以在站内 `Change Background` 添加颜色、模糊、图片或视频并免费导出 MP4，也可以把透明 WebM 放入外部编辑器完成文字、复杂布局或不同画幅。FAQ 可见答案与 `FAQPage` JSON-LD 必须一致。把新图文模块的四类 Use Cases 链接分别改为 `/de/`、`/es/`、`/fr/`、`/pt/` 下已存在的对应路径。保留已上线的三组图文模块、9 个 FAQ、真实案例图、本地化 alt 和其他结构化数据。
- 验收标准：四个首页首屏均明确显示每 24 小时 3 次免费去背景；第三步和换背景 FAQ 都同时说明站内四种换背景类型、免费 MP4 导出和外部编辑器工作流，不再声称站内没有背景功能。新图文模块的 Product、Creator、Agency 和 Use Cases 链接全部返回 `200` 且保持当前页面语言；不再把德语、西班牙语、法语或葡萄牙语用户送到英文详情页。现有三组图文模块、9 个 FAQ、图片、alt 和 JSON-LD 不回退。
- 不要修改：英文首页、现有图片主体和演示免责声明、页面 URL、canonical、hreflang、真实产品规则或法务内容。不要把三组图文模块改回 FAQ，不要新增未经证实的兼容性、速度、质量、成功率或商业承诺，也不要为了追求与英文相同的字数而写冗余或不自然的翻译。

### 补齐并完整本地化四种语言的 Use Cases 总览

- 优先级：`P2`
- 页面或界面：`https://bgremove.video/de/use-cases/`、`https://bgremove.video/es/use-cases/`、`https://bgremove.video/fr/use-cases/`、`https://bgremove.video/pt/use-cases/`
- 当前问题与线上证据：`2026-09-04` 英文 `/use-cases/` 仍有 12 个 `h2` 和 3 个 `h3`，包含 Product video、Social content、Agency delivery 三类工作流的详细说明，以及 `Which workflow fits your video?` 和 `Why the transparent file is the deliverable` 两个选择与价值模块。四个本地化总览仍只有 10 个 `h2` 且没有对应的 3 个 `h3`，缺少三类工作流的具体输入、用途、风险和详情页链接，也缺少选择指南与透明母版价值说明。四种语言页面都继续显示未翻译的 `Not sure which workflow fits?`，CTA 也没有完整同步最长 60 秒和每 24 小时 3 次规则。
- 修改要求：完整本地化英文 Use Cases 总览当前的三类工作流详情、`Which workflow fits your video?`、`Why the transparent file is the deliverable` 和结尾 CTA。每类工作流都要保留“适合谁、输入是什么、透明结果用于什么、素材风险是什么、去哪里看详情”的信息结构，并链接到对应语言已经存在的 Product、Creator 和 Agency 详情页。把 `Not sure which workflow fits?` 及所有残留英文界面文字翻译为该页面语言；CTA 自然表达最长 60 秒、每个登录账户每 24 小时最多成功去背景 3 次、无水印，并继续链接到当前本地化 Free Access 页面。翻译应围绕各语言真实搜索表达优化，但不得改变英文页的事实和选择逻辑。
- 验收标准：四个本地化 Use Cases 总览具有与英文页相同的内容模块、三类工作流说明、选择指南、透明母版价值说明和 CTA；三类工作流分别链接到正确的同语言详情页。页面中不存在 `Not sure which workflow fits?` 或其他无意保留的英文标题；60 秒、每 24 小时 3 次、透明 WebM、无水印及换背景工作流与英文版一致。各语言 title、meta description、Open Graph/Twitter 文案、可见 H1/H2/H3 和内部链接都使用对应语言且无 404。
- 不要修改：英文 Use Cases 页面、现有本地化详情页 URL、canonical、hreflang、用例分类或真实产品边界。不要强制各语言达到相同字数，不要新增行业、客户、数据、成效或产品能力，也不要把不同语言入口统一重定向到英文页。

### 修正英语工具页的过期换背景说明和过度质量承诺

- 优先级：`P1`
- 页面或界面：`https://bgremove.video/tools/remove-background-from-video/` 和 `https://bgremove.video/tools/product-video-background-remover/`
- 当前问题与线上证据：`2026-09-04` 复查时，`/tools/remove-background-from-video/` 仍写着背景只能稍后在外部编辑器决定，并明确声称 `We do not offer flattening as an export option`，但站内已经可以为透明视频添加颜色、模糊、图片或视频并导出 MP4。`/tools/product-video-background-remover/` 也仍对 `Does it handle reflective products?` 直接回答 `Yes.`，并承诺玻璃表面和反光材质会保留高光；这与首页和 FAQ 对玻璃、透明物体及复杂边缘仍然困难的谨慎说明冲突。
- 修改要求：在 `/tools/remove-background-from-video/` 的 `Removed background` 段落中，用 `Nothing is behind your subject. You can add a color, blur, image, or video in Change Background and export an MP4, or keep the transparent WebM for an external editor.` 替换只允许外部编辑器的绝对说法，并把 `Change Background` 设为指向 `/change-background/` 的描述性链接。把 `Can I get an MP4 with a white background instead?` 的回答替换为 `Yes. Open the finished clip in Change Background, choose white under Colour, and export an MP4. Keep the transparent WebM if you may want another background later.`，同步可见 FAQ 与 `FAQPage` JSON-LD。把 Product Video 页反光产品答案替换为 `Reflective products can work, but results vary with transparency, glare, and how clearly the product separates from the background. Chrome and glazed surfaces may retain highlights; clear glass and transparent packaging remain difficult. Test one representative clip before processing a larger set.`，同步结构化数据。
- 验收标准：两个页面均不再出现 `We do not offer flattening as an export option`、只能在外部编辑器换背景或反光和玻璃材质必然成功的绝对说法；指定英文替换文案逐字出现，`Change Background` 链接返回 `200`。可见 FAQ 与各自 `FAQPage` JSON-LD 完全一致，页面对玻璃和透明物体的限制与首页及独立 FAQ 保持一致。
- 不要修改：透明 WebM 作为可复用主文件的推荐、VP9 alpha 说明、站内换背景支持的四种类型、MP4 导出能力或外部编辑器高级工作流。不要新增成功率、兼容性保证、自动光线匹配、批量处理、API、手动边缘精修或其他未上线能力。

### 简化首页工作区的剩余免费次数提示

- 优先级：`P1`
- 页面或界面：英文首页 `https://bgremove.video/` 去背景处理完成后的左侧结果卡，以及右侧 `Your recent clips` 作品列表
- 当前问题与线上证据：`2026-09-04` 首页工作区的在线文案模板仍为 `{left} left in this window`，用户实际会看到类似 `3/3 left in this window` 的提示。这句话没有说明剩余的是免费去背景次数，也没有直接表达 24 小时额度周期。处理完成后的结果卡仍需确保能看到剩余免费次数。桌面端 `Download` 和 `Run another` 已经同排，右侧每条作品的下载和换背景入口也已经存在。
- 修改要求：把已登录状态的动态剩余次数文案改为 `{left} free removals remaining in this 24-hour window.`。`{left}` 沿用现有的“剩余次数/总次数”值，例如剩余 3 次时显示 `3/3 free removals remaining in this 24-hour window.`。工作区同一状态只显示这一句额度提示，不要再叠加 `Remove up to 3 video backgrounds for free every 24 hours.` 或其他同义说明。在已登录上传、处理中、失败、额度耗尽和处理完成状态中都使用真实的剩余数量，额度耗尽时显示 `0/3 free removals remaining in this 24-hour window.`。未登录状态无法获取个人剩余量时，仅显示 `3 free removals every 24 hours.`，不伪造 `3/3` 状态。提示靠近上传、剩余额度或结果操作区域，使用不抢过主操作的辅助文字样式。保留当前桌面端 `Download` 和 `Run another` 的并排布局，并确保两者在 `390px` 宽移动端仍同排、等宽、完整可见。
- 验收标准：已登录且分别剩余 3、2、1、0 次时，首页工作区分别显示 `3/3`、`2/3`、`1/3`、`0/3` 开头的 `free removals remaining in this 24-hour window.`；未登录时显示 `3 free removals every 24 hours.`。上传前、处理中、失败、额度耗尽和处理完成状态均只出现一句额度提示，没有 `3/3 left in this window`、句意重复、截断或数量错误。处理完成后，`Download` 和 `Run another` 在 `390px`、`768px` 和常见桌面宽度下始终同排、等高、完整可见且无横向滚动；两个按钮分别继续下载当前透明视频和开始另一次处理。右侧每条作品现有的下载、换背景和正确预选行为不得回退。
- 不要修改：右侧现有的逐作品操作、下载文件内容、再次处理流程、作品排序、缩略图、日期、时长、分辨率、过期规则、真实额度、认证、用户作品数据、去背景处理或换背景合成行为。不要删除页面其他位置准确的营销说明，也不要让两个左侧按钮在移动端变成难以点击的小按钮。

### 修正首页残留的换背景绝对表述

- 优先级：`P1`
- 页面或界面：英文首页 `https://bgremove.video/`
- 当前问题与线上证据：`2026-09-04` 复查生产环境时，英文首页 `A cleaner handoff from creator to editor` 模块末段仍写着 `BGRemove only creates the transparent video.`，与已上线的站内换背景和 MP4 导出功能冲突。
- 修改要求：把该模块末段完整替换为：`BGRemove creates the transparent video and can also add a color, blur, image, or video before exporting an MP4. It does not host team projects, manage versions, collect comments, or build every channel layout. Use an editor when you need text, complex layouts, or different frame sizes.` 保留透明 WebM 进入外部编辑器的高级工作流，不要删除或贬低该路径。
- 验收标准：首页不再出现 `BGRemove only creates the transparent video.`；指定替换段落逐字出现且无需执行 JavaScript即可读取。该模块同时准确表达站内简单换背景与外部编辑器高级工作流，不再与首页 FAQ、换背景页、独立 FAQ 或 Free Access 页面冲突。
- 不要修改：每 24 小时 3 次去背景的真实额度、失败任务是否计数、去背景输入限制、透明 WebM 输出、换背景支持的四种类型、浏览器本地合成、MP4 导出或保留期限。不要声称换背景包含自动光线匹配、复杂排版、文字、字幕、画幅转换、背景素材库或其他未上线功能，也不要把外部编辑器从高级工作流说明中完全删除。

### 完成图片、视频背景及导出结果的比例与播放验证

- 优先级：`P1`
- 页面或界面：`https://bgremove.video/change-background/` 的 `Image`、`Video` 背景预览和 `Export MP4`
- 当前问题与线上证据：`2026-09-04` 公开页面复查无法替用户登录、上传本地图片或视频，也不能触发 MP4 导出，因此 `Image`、`Video` 以及最终导出文件是否使用同一套正确比例和播放逻辑仍未得到生产验证。上一次已确认 `Colour` 和 `Blur` 背景保持人物原始比例、水平居中并在选择后自动播放，但用户提供的截图曾显示 `Image` 背景会把同类竖屏人物横向拉伸，所以原任务仍不能判定为完成。
- 修改要求：使用安全的测试素材验证 `Image` 和 `Video` 两种背景；如果任一模式仍会拉伸、裁切或改变前景比例，则让其复用已经在 `Colour` 和 `Blur` 中生效的源视频固有尺寸与等比缩放逻辑。图片或视频背景可以等比覆盖并裁切边缘，但前景视频和输出画布不能变形。选择或更换图片、视频背景后自动播放合成预览；视频背景与前景的播放、暂停、跳转和循环保持同步。最终 `Export MP4` 必须保持源透明视频的宽高比，并与预览构图一致。若线上现有实现已经全部满足要求，只补充必要的自动化回归测试，不要为了制造代码改动而改写正常逻辑。
- 验收标准：分别用横屏、竖屏和接近方形的透明作品，搭配横屏、竖屏和方形的图片及视频背景进行交叉测试；每次选择或更换背景后，前景比例与 `None`、`Colour` 和 `Blur` 状态一致且自动播放，视频背景与前景同步。`390px`、`768px` 和常见桌面宽度下无横向溢出。导出每种代表组合的 MP4，用媒体信息确认输出宽高比与源透明视频一致，并抽查首帧、中间帧和末帧，确认无拉伸且与预览构图一致。相关回归测试覆盖源尺寸、显示尺寸和导出尺寸的比例计算。
- 不要修改：已经验证正常的 `Colour`、`Blur` 行为、源透明视频、用户素材、背景类型、前景透明度、主体位置、导出编码格式、帧率、时长、音频规则或浏览器本地处理方式。不要上传真实用户素材，不要通过固定为 `16:9`、裁切前景、拉伸背景、降低清晰度或关闭自动播放来规避问题。

### 补充 Organization 的公开法定名称

- 优先级：`P2`
- 页面或界面：英文首页 `https://bgremove.video/` 的 `Organization` 结构化数据
- 当前问题与线上证据：`2026-09-04` 首页公开的 `Organization` JSON-LD 已包含支持邮箱和 `contactPoint`，但仍没有把 About 页面公开显示的法定名称 `BGRemove d.o.o.` 表达为 `legalName`。
- 修改要求：继续使用 `https://bgremove.video/#organization` 作为唯一稳定的组织 `@id`，只增加 `legalName: "BGRemove d.o.o."`。其他页面继续通过同一 `@id` 引用该实体。
- 验收标准：首页 `Organization` JSON-LD 可解析，`legalName` 与 About 页面公开名称完全一致；全站不存在名称或 `@id` 冲突；Schema.org 验证没有关键错误。
- 不要修改：可见公司名称、地址、邮箱、现有 `contactPoint` 或其他法定信息。不要虚构电话、注册标识、税号、社交账号、评价、奖项或外部实体链接。

### 纠正当前公开更新日志并记录剩余改进

- 优先级：`P1`
- 页面或界面：`https://bgremove.video/changelog/`
- 当前问题与线上证据：`2026-09-04` 公开更新日志已新增 `Sep 4, 2026 · Improvement · 2.0 · The German, Spanish, French and Portuguese pages catch up`。该记录声称四种语言的付费套餐、批量上传、API、额外导出格式和保留期说明已全部纠正，Use Cases 总览也已完全翻译，但线上仍有付费 10 分钟、批量上传、API、手动精修等旧承诺，四个 Use Cases 页也仍缺失模块并显示英文 `Not sure which workflow fits?`。该记录中关于四个首页已增加三组图文模块和三条 FAQ 的内容则已在线。
- 修改要求：立即把 `Sep 4, 2026` 记录改成只描述当时确实已上线的内容：四个多语言首页新增了三组图文工作流说明和三条常见问题。删除“所有旧产品事实已纠正”、“Use Cases 已完全翻译”以及“换背景规则已在各处一致”等尚未成立的说法。本批次其余待办实际发布后，再新增恰好一条带真实发布日期的用户向记录，只概括已在生产环境验证的产品事实修正、多语言 Use Cases、首页额度提示、英语说明修正、结构化数据或换背景比例与播放改进。任何未发布或未验证的项目都不得写入。
- 验收标准：`Sep 4, 2026` 记录与当时已上线的四个首页内容一致，不再声称尚未完成的全站事实统一或 Use Cases 完整翻译。剩余工作发布后恰好新增一条记录，内容简洁、脱敏、面向用户，且每一项都能在线上直接验证。`2026-08-31` 及更早的记录和日期保持不变。
- 不要修改：`2026-08-31` 及更早的历史记录和日期。不得提及文件名、组件名、代码架构、仓库、分支、提交、基础设施、服务商配置、成本、密钥、安全敏感实现、客户数据、内部指标、AI 提示词或内部工作流程。
