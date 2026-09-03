---
site_id: "bgremove-video"
name: "BGRemove"
production_url: "https://bgremove.video/"
changelog_url: "https://bgremove.video/changelog/"
delivery_method: "direct_publish"
target_repository: "not_applicable"
default_branch: "not_applicable"
updated_at: "2026-09-03"
---

# BGRemove 当前待办事项

## 已批准任务

### 统一四种非英语版本的产品事实、导航名称和元数据

- 优先级：`P1`
- 页面或界面：`/de/`、`/es/`、`/fr/`、`/pt/` 下的全部 60 个公开页面，重点包括首页、`/faq/`、`/how-it-works/`、`/pricing/`、三类用例详情页和四个工具页
- 当前问题与线上证据：`2026-09-03` 将四种语言的 15 组对应页面逐页与英文版比较后，页面结构大致相同的部分仍大量使用旧产品事实。四种语言首页继续宣传付费计划、更高分辨率、更长视频、批量上传、API、ProRes 4444、单独蒙版和 PNG 序列，却普遍没有英文首页当前的 60 秒、24 小时保留及换背景完全免费且不限次数说明。四种语言 `/pricing/` 仍写着付费计划“已经设计但尚未开放”，并列出批量上传和 API；导航和 FAQ 分类仍使用“价格/计费”含义，而英文版已使用 `Free Access` 和 `Account and free access`。四种语言 Agency 页面仍声称批量队列、API/webhook、`Studio` 每次 20 个视频、ProRes 4444、优先队列和 90 天保留；Ecommerce、Product Video 和 Remove Background 工具页的 meta description 仍宣传 ProRes 4444、PNG 或付费社交能力。多语言 FAQ、How it works、Creator、Ecommerce、TikTok 和其他工具页也继续出现 `Studio`、批量、付费计划或旧额度。德语、法语和葡萄牙语 Product Video 页仍绝对保证反光和玻璃制品效果；德语独立 FAQ 中 `Is changing a background free?` 对应的结构化答案与可见答案还不完全一致。
- 修改要求：以修正后的最终英语对应页面为产品事实基准，逐页更新德语、西班牙语、法语和葡萄牙语的可见正文、标题、CTA、导航与页脚标签、meta title、meta description、Open Graph/Twitter 文案和 `FAQPage` JSON-LD。所有语言只保留当前真实边界：每个登录账户每 24 小时最多完成 3 次免费去背景；每段最长 60 秒、最大 2 GB；输出为保持源尺寸的透明 VP9 WebM，无水印；源文件和结果保留 24 小时；换背景可添加颜色、模糊、图片或视频并导出 MP4，而且完全免费、不限次数；目前没有付费计划、订阅、积分包、批量上传、`Studio`、API、webhook、优先队列、ProRes 4444、PNG 序列、单独蒙版、90 天保留或站内手动边缘精修。把导航中的 `Pricing` 概念改成各语言自然的 `Free Access` 对应说法，把 FAQ 的“账户与计费”改成“账户与免费使用”对应说法，但保留现有 `/pricing/` URL。先完成英语工具页待办中的事实修正，再把最终英文含义自然翻译到四种语言。反光、玻璃和透明包装只能说明效果取决于透明度、反光和主体与背景的分离程度，并建议先测试代表性素材。
- 验收标准：抓取四种语言的全部 60 个公开页面后，所有页面在额度、输入限制、输出格式、保留期限、免费规则、换背景能力和产品限制方面与最终英文对应页一致；搜索 `Studio`、20 个视频及其本地化表达、API、webhook、优先队列、ProRes 4444、PNG、90 天及其翻译、付费计划、更高分辨率、更长时长、批量上传和精细边缘处理时，不再发现任何将其作为当前能力的肯定承诺。首页、FAQ、How it works、Pricing、三类用例和四个工具页的可见事实、meta description、社交元数据与 JSON-LD 不互相冲突；每个 `FAQPage` 的问题和答案与同页可见内容逐字一致。导航显示本地化的“免费使用”而不是“价格”，但 `/pricing/` 继续返回 `200`，canonical 和 hreflang 不变。
- 不要修改：现有语言 URL、canonical、hreflang、法务正文、认证、实际处理能力、真实额度、数据保留或输出格式。不要要求各语言逐字直译、达到完全相同的单词数或牺牲当地搜索表达；不要虚构定价、套餐、性能指标、成功率、客户案例或尚未上线的能力。

### 补齐四种非英语首页的新版内容和 FAQ

- 优先级：`P1`
- 页面或界面：`https://bgremove.video/de/`、`https://bgremove.video/es/`、`https://bgremove.video/fr/`、`https://bgremove.video/pt/`
- 当前问题与线上证据：`2026-09-03` 英文首页约有 2308 个可见英文单词、14 个 `h2`、16 个 `h3` 和 9 个 FAQ；德语、西班牙语、法语和葡萄牙语首页只有约 954–1147 个可见单词、11 个 `h2`、13 个 `h3` 和 6 个 FAQ。四种语言都缺少英文首页现有的 `One transparent master, many finished scenes`、`One cutout, every aspect ratio` 和 `A cleaner handoff from creator to editor` 三个完整图文模块，也缺少 `What is an AI video background remover?`、`What footage gives the best result?` 和 `Why does my transparent WebM still look like it has the original background?` 三个 FAQ。多语言首页第三步仍主要要求把透明 WebM 放进外部编辑器，没有完整说明站内 `Change Background` 可以添加颜色、模糊、图片或视频并免费导出 MP4；首页卖点仍只写模糊的“免费套餐也可用”，没有像英文首页一样明确显示每 24 小时 3 次。
- 修改要求：把英文首页当前的三组图文模块和三条 FAQ 按原有信息层级、示例逻辑、内部链接和真实产品边界完整本地化到德语、西班牙语、法语和葡萄牙语首页。复用现有真实案例图，不另做简图；为每种语言提供自然、准确的标题、正文、图注和 alt 文本。第三步必须同时说明站内简单换背景与透明 WebM 进入外部编辑器的高级工作流；FAQ 必须解释透明 WebM 直接在本地播放器或浏览器打开时可能仍看见原背景是正常播放表现，并保留英文页当前使用的权威兼容性链接。把首页额度卖点明确翻译为“每个登录账户每 24 小时最多免费去背景 3 次”，同时清楚区分换背景完全免费且不限次数。更新首页对应 `FAQPage` JSON-LD，使 9 个问题与可见 FAQ 完全一致。允许为自然表达调整句长和关键词，不要求机械对齐英文单词数。
- 验收标准：四个多语言首页都具有与英文首页相同的三组新版图文模块、相同的 9 个 FAQ 主题、相同的内部链接意图和相同的产品事实；图文模块使用真实案例图且每张图片有对应语言的准确 alt 文本。每个首页可直接读到每 24 小时 3 次去背景、站内四种换背景类型、免费不限次数换背景、MP4 导出、透明 VP9 WebM 和外部编辑器工作流；不再只引导用户去外部编辑器。可见 FAQ 与 JSON-LD 的 9 组问答逐字一致，不存在遗漏、重复或仍为英文的标题；四种语言在常见桌面与移动宽度下没有截字、重叠或横向溢出。
- 不要修改：英文首页、现有图片主体和演示免责声明、页面 URL、canonical、hreflang、真实产品规则或法务内容。不要把三组图文模块改回 FAQ，不要新增未经证实的兼容性、速度、质量、成功率或商业承诺，也不要为了追求与英文相同的字数而写冗余或不自然的翻译。

### 补齐并完整本地化四种语言的 Use Cases 总览

- 优先级：`P2`
- 页面或界面：`https://bgremove.video/de/use-cases/`、`https://bgremove.video/es/use-cases/`、`https://bgremove.video/fr/use-cases/`、`https://bgremove.video/pt/use-cases/`
- 当前问题与线上证据：英文 `/use-cases/` 约有 767 个可见英文单词、12 个 `h2` 和 3 个 `h3`，包含 Product video、Social content、Agency delivery 三类工作流的详细说明，以及 `Which workflow fits your video?` 和 `Why the transparent file is the deliverable` 两个选择与价值模块。四个本地化总览只有约 287–362 个可见单词、10 个 `h2` 且没有对应的 3 个 `h3`，缺少三类工作流的具体输入、用途、风险和详情页链接，也缺少选择指南与透明母版价值说明。四种语言页面还都直接显示未翻译的英文标题 `Not sure which workflow fits?`，其 CTA 没有完整同步英文页当前的最长 60 秒和每 24 小时 3 次规则。
- 修改要求：完整本地化英文 Use Cases 总览当前的三类工作流详情、`Which workflow fits your video?`、`Why the transparent file is the deliverable` 和结尾 CTA。每类工作流都要保留“适合谁、输入是什么、透明结果用于什么、素材风险是什么、去哪里看详情”的信息结构，并链接到对应语言已经存在的 Product、Creator 和 Agency 详情页。把 `Not sure which workflow fits?` 及所有残留英文界面文字翻译为该页面语言；CTA 自然表达最长 60 秒、每个登录账户每 24 小时最多成功去背景 3 次、无水印，并继续链接到当前本地化 Free Access 页面。翻译应围绕各语言真实搜索表达优化，但不得改变英文页的事实和选择逻辑。
- 验收标准：四个本地化 Use Cases 总览具有与英文页相同的内容模块、三类工作流说明、选择指南、透明母版价值说明和 CTA；三类工作流分别链接到正确的同语言详情页。页面中不存在 `Not sure which workflow fits?` 或其他无意保留的英文标题；60 秒、每 24 小时 3 次、透明 WebM、无水印及换背景工作流与英文版一致。各语言 title、meta description、Open Graph/Twitter 文案、可见 H1/H2/H3 和内部链接都使用对应语言且无 404。
- 不要修改：英文 Use Cases 页面、现有本地化详情页 URL、canonical、hreflang、用例分类或真实产品边界。不要强制各语言达到相同字数，不要新增行业、客户、数据、成效或产品能力，也不要把不同语言入口统一重定向到英文页。

### 修正英语工具页的过期换背景说明和过度质量承诺

- 优先级：`P1`
- 页面或界面：`https://bgremove.video/tools/remove-background-from-video/` 和 `https://bgremove.video/tools/product-video-background-remover/`
- 当前问题与线上证据：`/tools/remove-background-from-video/` 仍写着背景只能稍后在外部编辑器决定，并明确声称 `We do not offer flattening as an export option`，但站内已经可以为透明视频添加颜色、模糊、图片或视频并导出 MP4。`/tools/product-video-background-remover/` 对 `Does it handle reflective products?` 直接回答 `Yes.`，并承诺玻璃表面和反光材质会保留高光；这与首页和 FAQ 对玻璃、透明物体及复杂边缘仍然困难的谨慎说明冲突，降低页面可信度。
- 修改要求：在 `/tools/remove-background-from-video/` 的 `Removed background` 段落中，用 `Nothing is behind your subject. You can add a color, blur, image, or video in Change Background and export an MP4, or keep the transparent WebM for an external editor.` 替换只允许外部编辑器的绝对说法，并把 `Change Background` 设为指向 `/change-background/` 的描述性链接。把 `Can I get an MP4 with a white background instead?` 的回答替换为 `Yes. Open the finished clip in Change Background, choose white under Colour, and export an MP4. Keep the transparent WebM if you may want another background later.`，同步可见 FAQ 与 `FAQPage` JSON-LD。把 Product Video 页反光产品答案替换为 `Reflective products can work, but results vary with transparency, glare, and how clearly the product separates from the background. Chrome and glazed surfaces may retain highlights; clear glass and transparent packaging remain difficult. Test one representative clip before processing a larger set.`，同步结构化数据。
- 验收标准：两个页面均不再出现 `We do not offer flattening as an export option`、只能在外部编辑器换背景或反光和玻璃材质必然成功的绝对说法；指定英文替换文案逐字出现，`Change Background` 链接返回 `200`。可见 FAQ 与各自 `FAQPage` JSON-LD 完全一致，页面对玻璃和透明物体的限制与首页及独立 FAQ 保持一致。
- 不要修改：透明 WebM 作为可复用主文件的推荐、VP9 alpha 说明、站内换背景支持的四种类型、MP4 导出能力或外部编辑器高级工作流。不要新增成功率、兼容性保证、自动光线匹配、批量处理、API、手动边缘精修或其他未上线能力。

### 补上首页处理结果状态的额度提示

- 优先级：`P1`
- 页面或界面：英文首页 `https://bgremove.video/` 去背景处理完成后的左侧结果卡，以及右侧 `Your recent clips` 作品列表
- 当前问题与线上证据：`2026-09-03` 在生产环境登录状态下复查时，首页在线资源已经包含精确文案 `Remove up to 3 video backgrounds for free every 24 hours.`，但处理完成后的结果卡实际只显示文件名、时长、分辨率、`Download` 和 `Run another`，没有把这句额度提示呈现给用户。桌面端两个操作按钮已经同排，右侧每条作品的下载和换背景入口也已经存在。
- 修改要求：让首页去背景功能模块在每个实际状态中呈现且只呈现一句额度提示，文案精确为 `Remove up to 3 video backgrounds for free every 24 hours.`。重点补上当前缺失的处理完成状态；未登录上传、已登录上传、处理中、失败和额度耗尽状态也不得遗漏或重复。提示靠近上传、剩余额度或结果操作区域，使用可读但不抢过主操作的辅助文字样式，不添加标题、第二句、额度卡片或同一区域内的重复提示。保留当前桌面端 `Download` 和 `Run another` 的并排布局，并确保两者在 `390px` 宽移动端仍同排、等宽、完整可见。
- 验收标准：未登录上传、已登录上传、处理中、失败、额度耗尽和处理完成状态下，首页功能模块都只出现一次完整文案 `Remove up to 3 video backgrounds for free every 24 hours.`，且不被截断或拆成多句；页面其他位置现有且准确的简短免费额度说明无需删除。处理完成后，`Download` 和 `Run another` 在 `390px`、`768px` 和常见桌面宽度下始终同排、等高、完整可见且无横向滚动；两个按钮分别继续下载当前透明视频和开始另一次处理。右侧每条作品现有的下载、换背景和正确预选行为不得回退。
- 不要修改：右侧现有的逐作品操作、下载文件内容、再次处理流程、作品排序、缩略图、日期、时长、分辨率、过期规则、真实额度、认证、用户作品数据、去背景处理或换背景合成行为。不要删除页面其他位置准确的营销说明，也不要让两个左侧按钮在移动端变成难以点击的小按钮。

### 修正首页残留的换背景绝对表述

- 优先级：`P1`
- 页面或界面：英文首页 `https://bgremove.video/`
- 当前问题与线上证据：`2026-09-03` 复查生产环境时，英文首页 `A cleaner handoff from creator to editor` 模块末段仍写着 `BGRemove only creates the transparent video.`，与已上线的站内换背景和 MP4 导出功能冲突。
- 修改要求：把该模块末段完整替换为：`BGRemove creates the transparent video and can also add a color, blur, image, or video before exporting an MP4. It does not host team projects, manage versions, collect comments, or build every channel layout. Use an editor when you need text, complex layouts, or different frame sizes.` 保留透明 WebM 进入外部编辑器的高级工作流，不要删除或贬低该路径。
- 验收标准：首页不再出现 `BGRemove only creates the transparent video.`；指定替换段落逐字出现且无需执行 JavaScript即可读取。该模块同时准确表达站内简单换背景与外部编辑器高级工作流，不再与首页 FAQ、换背景页、独立 FAQ 或 Free Access 页面冲突。
- 不要修改：每 24 小时 3 次去背景的真实额度、失败任务是否计数、去背景输入限制、透明 WebM 输出、换背景支持的四种类型、浏览器本地合成、MP4 导出或保留期限。不要声称换背景包含自动光线匹配、复杂排版、文字、字幕、画幅转换、背景素材库或其他未上线功能，也不要把外部编辑器从高级工作流说明中完全删除。

### 完成图片、视频背景及导出结果的比例与播放验证

- 优先级：`P1`
- 页面或界面：`https://bgremove.video/change-background/` 的 `Image`、`Video` 背景预览和 `Export MP4`
- 当前问题与线上证据：`2026-09-03` 在生产环境登录状态下使用竖屏 `480p` 作品复查时，`Colour` 和 `Blur` 背景已经保持人物原始比例、水平居中并在选择后自动播放，说明这两个模式的线上问题已修复。用户此前提供的线上截图显示 `Image` 背景曾把同类竖屏人物横向拉伸；本轮线上审计不能替用户上传本地图片或视频，也没有触发 MP4 导出，因此 `Image`、`Video` 以及最终导出文件是否使用同一套正确比例和播放逻辑仍未得到生产验证，不能把原任务整体判定为完成。
- 修改要求：使用安全的测试素材验证 `Image` 和 `Video` 两种背景；如果任一模式仍会拉伸、裁切或改变前景比例，则让其复用已经在 `Colour` 和 `Blur` 中生效的源视频固有尺寸与等比缩放逻辑。图片或视频背景可以等比覆盖并裁切边缘，但前景视频和输出画布不能变形。选择或更换图片、视频背景后自动播放合成预览；视频背景与前景的播放、暂停、跳转和循环保持同步。最终 `Export MP4` 必须保持源透明视频的宽高比，并与预览构图一致。若线上现有实现已经全部满足要求，只补充必要的自动化回归测试，不要为了制造代码改动而改写正常逻辑。
- 验收标准：分别用横屏、竖屏和接近方形的透明作品，搭配横屏、竖屏和方形的图片及视频背景进行交叉测试；每次选择或更换背景后，前景比例与 `None`、`Colour` 和 `Blur` 状态一致且自动播放，视频背景与前景同步。`390px`、`768px` 和常见桌面宽度下无横向溢出。导出每种代表组合的 MP4，用媒体信息确认输出宽高比与源透明视频一致，并抽查首帧、中间帧和末帧，确认无拉伸且与预览构图一致。相关回归测试覆盖源尺寸、显示尺寸和导出尺寸的比例计算。
- 不要修改：已经验证正常的 `Colour`、`Blur` 行为、源透明视频、用户素材、背景类型、前景透明度、主体位置、导出编码格式、帧率、时长、音频规则或浏览器本地处理方式。不要上传真实用户素材，不要通过固定为 `16:9`、裁切前景、拉伸背景、降低清晰度或关闭自动播放来规避问题。

### 补充 Organization 的公开法定名称

- 优先级：`P2`
- 页面或界面：英文首页 `https://bgremove.video/` 的 `Organization` 结构化数据
- 当前问题与线上证据：`2026-09-03` 首页当前公开的 `Organization` JSON-LD 已包含支持邮箱和 `contactPoint`，但仍没有把 About 页面公开显示的法定名称 `BGRemove d.o.o.` 表达为 `legalName`。
- 修改要求：继续使用 `https://bgremove.video/#organization` 作为唯一稳定的组织 `@id`，只增加 `legalName: "BGRemove d.o.o."`。其他页面继续通过同一 `@id` 引用该实体。
- 验收标准：首页 `Organization` JSON-LD 可解析，`legalName` 与 About 页面公开名称完全一致；全站不存在名称或 `@id` 冲突；Schema.org 验证没有关键错误。
- 不要修改：可见公司名称、地址、邮箱、现有 `contactPoint` 或其他法定信息。不要虚构电话、注册标识、税号、社交账号、评价、奖项或外部实体链接。

### 更新本次发布的公开更新日志

- 优先级：`P1`
- 页面或界面：`https://bgremove.video/changelog/`
- 当前问题与线上证据：`2026-09-03` 复查公开更新日志时，最新记录仍是 `2026-08-31` 的 `A page for changing a video background`。首页每条作品的换背景入口、全宽编辑区、居中的 MP4 导出、完全免费且不限次数的提示、编辑器内多作品选择、作品深链接预选、切换作品时重置背景、竖屏素材在纯色与模糊背景下的比例修复和自动播放、多语言失效链接修复以及页脚菜单已经上线但尚未记录；图片与视频背景及最终导出比例尚未完成生产验证，首页处理完成状态的额度提示、英语与非英语产品说明仍待修正，不能提前声称尚未验证或尚未上线的改进已经发布。
- 修改要求：本批次其余工作成功发布后只新增一条带日期的公开记录。只概括实际在线且用户可见的改进：可以从首页每条已完成作品进入换背景，并在编辑器中切换其他有效作品；切换作品会同步预览并清除上一条作品的临时背景；换背景编辑区更宽，MP4 导出更明显；预览和导出保持源视频比例，选择背景后自动播放；首页功能区清楚提示每 24 小时可免费去背景 3 次；相关页面区分有限的去背景额度与完全免费、不限次数的换背景；多语言页面不再链接到不存在的页面，产品说明与当前免费功能保持一致；页脚能分别找到两个产品功能和说明资源。若其中任何一项没有成功发布，就从记录中删除对应说法；如果没有任何新的用户可见改进成功发布，则不要新增记录。
- 验收标准：本批次恰好新增一条记录；内容简洁、脱敏、面向用户并与线上实际状态一致；`2026-08-31` 及更早的历史记录和日期保持不变。
- 不要修改：历史记录及其日期。不得提及文件名、组件名、代码架构、仓库、分支、提交、基础设施、服务商配置、成本、密钥、安全敏感实现、客户数据、内部指标、AI 提示词或内部工作流程。
