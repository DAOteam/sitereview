---
site_id: "bgremove-video"
name: "BGRemove"
production_url: "https://bgremove.video/"
changelog_url: "https://bgremove.video/changelog/"
delivery_method: "direct_publish"
target_repository: "not_applicable"
default_branch: "not_applicable"
updated_at: "2026-09-02"
---

# BGRemove 当前待办事项

## 已批准任务

### 解除全站抓取与索引封锁

- 优先级：`P0`
- 页面或界面：`https://bgremove.video/robots.txt`、所有 sitemap 中的公开规范页面及其生产响应头
- 当前问题与线上证据：`2026-09-02` 线上 `robots.txt` 返回 `User-agent: *` 和 `Disallow: /`，阻止所有搜索引擎抓取整个网站；同时 sitemap 中的 81 个公开 URL 虽然都返回 `200`，但每个页面响应头都包含 `X-Robots-Tag: noindex, nofollow, noarchive, nosnippet`。因此即使 sitemap、canonical、title 和正文存在，搜索引擎仍被明确要求不要抓取、不要索引也不要跟随链接；站点限定搜索当前也没有返回结果。
- 修改要求：把生产 `robots.txt` 改为允许抓取所有公开营销页、功能落地页、帮助页、用例页、工具页、公司页和法务页，并加入 `Sitemap: https://bgremove.video/sitemap-index.xml`。继续阻止真正不应公开抓取的认证、账户、用户作品和接口路径，包括现有 `/api/`、`/app/`、`/login` 及其他私有路由；不要重新开放用户数据或私有页面。移除所有公开规范 HTML 页面的 `X-Robots-Tag: noindex, nofollow, noarchive, nosnippet`，公开页面不得再通过响应头或 `<meta name="robots">` 输出 `noindex` 或 `nofollow`。404、错误页、认证页、账户页、用户作品页和接口响应继续保持 `noindex`，不能为了修复 SEO 而让它们进入索引。保持现有 HTTPS、HSTS、自引用 canonical 和 sitemap URL 不变。
- 验收标准：线上 `robots.txt` 返回 `200`，不再包含全站 `Disallow: /`，明确引用 `https://bgremove.video/sitemap-index.xml`；Googlebot 和普通匿名请求都能抓取 sitemap 中全部 81 个公开 URL。逐一请求这些 URL 时均返回 `200`，响应头和 HTML 中都不存在 `noindex` 或 `nofollow`，canonical 继续指向当前规范 URL；随机 404、`/api/`、`/app/`、`/login` 及其他私有页面仍不可索引。使用 robots 测试、URL Inspection 或等效工具时，首页、`/change-background/`、四种语言首页和四个英语工具页均显示“允许抓取、允许索引”。
- 不要修改：公开页面 URL、canonical 主机、HTTPS 跳转、用户认证、用户作品访问控制、接口权限、sitemap 中现有的 81 个规范 URL 或 404 状态。不要把私有页面加入 sitemap，也不要用 JavaScript 动态修改 robots 指令。

### 修复多语言页面的 404 功能链接和无效语言标记

- 优先级：`P1`
- 页面或界面：德语、西班牙语、法语和葡萄牙语公开页面，以及英语法务页的语言入口与 `hreflang`
- 当前问题与线上证据：全站抓取发现，德语、西班牙语、法语和葡萄牙语各有 15 个 sitemap 页面链接到不存在的 `/de/change-background/`、`/es/change-background/`、`/fr/change-background/` 或 `/pt/change-background/`，共 60 个页面把用户和爬虫送到 `404`。英语的 `/legal/terms/`、`/legal/privacy/`、`/legal/acceptable-use/`、`/legal/cookies/` 和 `/legal/refunds/` 还输出 40 个指向不存在的本地化法务页的可见语言链接，以及 20 个指向相同 404 地址的 `hreflang`；这些目标全部返回 `404` 并 canonical 到 `/404/`。
- 修改要求：在尚未建立本地化换背景页之前，所有德语、西班牙语、法语和葡萄牙语页面中的 `Change Video Background` 对应入口都指向真实存在的英语页面 `https://bgremove.video/change-background/`，保留各页面现有的本地化链接文字，但不得继续生成带语言前缀的虚假地址；不要为解决链接错误而自动创建内容空白或机器占位的本地化落地页。英语法务页只为真实存在且内容等价的语言版本输出可见切换链接和 `hreflang`；当前没有法务翻译时，删除指向 20 个不存在目标的 `hreflang`，语言菜单不得再链接到本地化法务 404，可将语言切换入口导向相应语言首页并清楚表达这是切换站点语言，而不是法务翻译。所有 `hreflang` 集合必须自引用、互相返回且只包含返回 `200` 的 canonical URL。
- 验收标准：重新抓取全部 81 个 sitemap URL 后，站内链接中不再出现 `/de/change-background/`、`/es/change-background/`、`/fr/change-background/`、`/pt/change-background/` 或任何不存在的本地化法务 URL；四种语言的换背景入口均返回 `200` 并落到 `/change-background/`。五个英语法务页的可见语言入口没有 404，源代码中不存在指向 404 的 `hreflang`；全站所有内部链接和全部 `hreflang` 目标都返回 `200`、使用自引用 canonical，且不存在重定向链。
- 不要修改：已经存在的德语、西班牙语、法语和葡萄牙语页面 URL、英语换背景页、英语法务正文或 canonical。不要虚构法务翻译，不要把不等价的语言首页标记为法务页的 `hreflang` 等价版本，也不要用软 404 或全部重定向到首页来掩盖错误。

### 清理非英语页面中的过期产品能力和付费承诺

- 优先级：`P1`
- 页面或界面：`/de/`、`/es/`、`/fr/`、`/pt/` 下的所有公开页面，重点包括各语言首页、`/pricing/`、`/use-cases/agencies/` 和 `/tools/product-video-background-remover/`
- 当前问题与线上证据：当前英语页面说明 BGRemove 没有付费计划、批量处理或 API，成功去背景额度为每 24 小时 3 次，最长 60 秒，输出为保留源尺寸的透明 VP9 WebM，文件保留 24 小时。非英语页面仍公开宣传已经不存在或从未上线的能力：德语和西班牙语首页声称存在付费计划、更高分辨率、更长视频、批量上传、API、ProRes 4444、单独蒙版和 PNG 序列；多语言 Pricing 页仍列出精细边缘处理、批量上传和 API；四种语言的 Agency 与 Product Video 页面声称 `Studio` 每次可处理 20 个视频、并行队列、API/webhook、ProRes 4444 和 90 天保留。相关 Product Video 页面还绝对保证反光或玻璃制品效果，与首页明确承认玻璃和透明物体仍然困难的说明冲突。
- 修改要求：逐页清理德语、西班牙语、法语和葡萄牙语中的旧商业模式、旧额度和未上线功能，只保留当前真实产品边界：每个登录账户每 24 小时最多完成 3 次免费去背景；每段最长 60 秒、最大 2 GB；输出为保持源尺寸的透明 VP9 WebM，无水印；源文件和结果保留 24 小时；换背景完全免费且不限次数；目前没有付费计划、订阅、积分包、批量上传、`Studio` 套餐、API、webhook、ProRes 4444、PNG 序列、单独蒙版、90 天保留或站内手动边缘精修。更新所有受影响的可见正文、FAQ、功能列表、CTA 附近说明、meta description 和 `FAQPage` JSON-LD；翻译必须自然，并与对应英语页面表达同一事实，不能只删除关键词后留下语义残缺的句子。对于反光、玻璃和透明包装，只能说明结果取决于边缘分离、反光和透明程度，并建议先测试代表性素材，不能承诺一定成功。
- 验收标准：抓取四种语言的全部公开页面，搜索 `Studio`、`20 clips` 及其本地化数字表达、`API`、`webhook`、`ProRes 4444`、`PNG`、`90 days` 及其翻译、付费计划、更高分辨率、更长时长、批量上传和精细边缘处理时，不再发现任何作为当前 BGRemove 能力的肯定承诺；当前额度、时长、大小、格式、保留时间和换背景规则在四种语言中一致。各语言可见 FAQ 与 JSON-LD 逐字一致，页面不再声称透明或反光产品必然成功，也不再出现互相冲突的免费与付费说明。
- 不要修改：英语页面已经准确的真实额度和功能、实际处理能力、认证、数据保留、输出格式或法务条款。不要新增定价、套餐、排队速度、质量等级、客户案例、成功率、性能指标或尚未上线的功能，也不要用自动直译覆盖已经准确且自然的本地化段落。

### 修正英语工具页的过期换背景说明和过度质量承诺

- 优先级：`P1`
- 页面或界面：`https://bgremove.video/tools/remove-background-from-video/` 和 `https://bgremove.video/tools/product-video-background-remover/`
- 当前问题与线上证据：`/tools/remove-background-from-video/` 仍写着背景只能稍后在外部编辑器决定，并明确声称 `We do not offer flattening as an export option`，但站内已经可以为透明视频添加颜色、模糊、图片或视频并导出 MP4。`/tools/product-video-background-remover/` 对 `Does it handle reflective products?` 直接回答 `Yes.`，并承诺玻璃表面和反光材质会保留高光；这与首页和 FAQ 对玻璃、透明物体及复杂边缘仍然困难的谨慎说明冲突，降低页面可信度。
- 修改要求：在 `/tools/remove-background-from-video/` 的 `Removed background` 段落中，用 `Nothing is behind your subject. You can add a color, blur, image, or video in Change Background and export an MP4, or keep the transparent WebM for an external editor.` 替换只允许外部编辑器的绝对说法，并把 `Change Background` 设为指向 `/change-background/` 的描述性链接。把 `Can I get an MP4 with a white background instead?` 的回答替换为 `Yes. Open the finished clip in Change Background, choose white under Colour, and export an MP4. Keep the transparent WebM if you may want another background later.`，同步可见 FAQ 与 `FAQPage` JSON-LD。把 Product Video 页反光产品答案替换为 `Reflective products can work, but results vary with transparency, glare, and how clearly the product separates from the background. Chrome and glazed surfaces may retain highlights; clear glass and transparent packaging remain difficult. Test one representative clip before processing a larger set.`，同步结构化数据。
- 验收标准：两个页面均不再出现 `We do not offer flattening as an export option`、只能在外部编辑器换背景或反光和玻璃材质必然成功的绝对说法；指定英文替换文案逐字出现，`Change Background` 链接返回 `200`。可见 FAQ 与各自 `FAQPage` JSON-LD 完全一致，页面对玻璃和透明物体的限制与首页及独立 FAQ 保持一致。
- 不要修改：透明 WebM 作为可复用主文件的推荐、VP9 alpha 说明、站内换背景支持的四种类型、MP4 导出能力或外部编辑器高级工作流。不要新增成功率、兼容性保证、自动光线匹配、批量处理、API、手动边缘精修或其他未上线能力。

### 补上首页功能区额度提示并修正移动端按钮排列

- 优先级：`P1`
- 页面或界面：英文首页 `https://bgremove.video/` 去背景处理完成后的左侧结果卡，以及右侧 `Your recent clips` 作品列表
- 当前问题与线上证据：`2026-09-02` 在生产环境登录状态下复查时，首页去背景功能模块没有显示已批准的完整额度句 `Remove up to 3 video backgrounds for free every 24 hours.`；在 `390px` 宽度下，处理完成卡中的 `Download` 和 `Run another` 仍上下排列，而不是用户要求的并排显示。
- 修改要求：首页去背景功能模块增加且只使用一句额度提示，文案精确为 `Remove up to 3 video backgrounds for free every 24 hours.`。提示靠近上传或剩余额度区域，使用可读但不抢过主操作的辅助文字样式，不添加标题、第二句、额度卡片或同一区域内的重复提示。保留已完成的左侧两个按钮和右侧逐作品换背景入口；只调整左侧结果卡的响应式布局，使 `Download` 和 `Run another` 在桌面端及 `390px` 宽移动端都位于同一行。移动端可缩小两者之间的间距并让按钮等宽，但不能缩小可点击高度、截断文字或改回上下排列。
- 验收标准：未登录上传状态、已登录上传状态、处理中和处理完成状态下，首页功能模块都只出现一次完整文案 `Remove up to 3 video backgrounds for free every 24 hours.`，且不被截断或拆成多句；页面其他位置现有且准确的简短免费额度说明无需删除。处理完成后，左侧仍只有 `Download` 和 `Run another`，在 `390px`、`768px` 和常见桌面宽度下始终同排、等高、完整可见且无横向滚动；两个按钮分别继续下载当前透明视频和开始另一次处理。右侧每条作品现有的下载、换背景和正确预选行为不得回退。
- 不要修改：右侧现有的逐作品操作、下载文件内容、再次处理流程、作品排序、缩略图、日期、时长、分辨率、过期规则、真实额度、认证、用户作品数据、去背景处理或换背景合成行为。不要删除页面其他位置准确的营销说明，也不要让两个左侧按钮在移动端变成难以点击的小按钮。

### 允许在换背景功能区选择任意已完成作品

- 优先级：`P1`
- 页面或界面：`https://bgremove.video/change-background/` 的换背景功能卡
- 当前问题与线上证据：`2026-09-02` 在生产环境登录状态下复查时，首页 `Your recent clips` 同时存在两条仍有效的已完成作品，但直接进入换背景页时只显示单个作品；页面正文中不存在 `Choose a Finished Clip` 或其他作品切换控件，用户无法在编辑器内改选另一条有效作品。
- 修改要求：在换背景功能卡顶部、预览和背景选项之前增加一个紧凑的作品选择区域，标题使用 `Choose a Finished Clip`。当存在两个或更多仍有效的已完成作品时，必须让用户从全部可用作品中明确选择一个再进行换背景；不能只加载最后一个，也不能把列表位置、日期或文件名当作作品身份。每个选项至少显示缩略图、完成日期和时间、时长、分辨率及过期时间，选择值必须使用作品的稳定唯一标识。当前选项要有明显的选中状态，并同步显示在主预览中。

  从首页某条作品的 `Change the background` 进入时，优先预选该条作品，但选择区域仍允许切换到其他可用作品；直接打开换背景页且存在多个作品时，不得悄悄固定为最后一个，应先显示选择区域并让用户确认选择。只有一个可用作品时可以自动选中，并保留简洁的当前作品信息；没有可用作品时继续显示 `Remove a Background First` 空状态。已过期、已删除、未完成、失败或不属于当前账户的作品不得出现在可选项中；深链接指向不可用作品时，显示安全空状态并允许选择其他可用作品，不能回退到另一条作品而不告知用户。

  选择另一条作品后，日期、时长、分辨率、预览源和最终 `Export MP4` 的导出对象必须同时切换到该作品。切换时把背景类型恢复为 `None`，清除上一条作品临时选择的颜色、模糊、图片或视频背景及其预览，避免把 A 作品的编辑状态误用于 B 作品；正在合成或导出时应阻止切换或安全结束当前操作，绝不能导出与当前选中状态不一致的视频。选择区域应是编辑器内部的紧凑控件、可展开列表或响应式卡片区，不得恢复占据半个首屏的右侧 `Your Finished Clips` 大栏；作品较多时必须仍能访问全部可用项，不能只显示最新一条，也不能造成页面横向滚动。
- 验收标准：准备至少三条不同日期和缩略图的可用作品，从换背景页依次选择 A、B、C，主预览、元信息和导出对象每次都与当前选项一致；为 A 选择自定义背景后切换到 B，B 不继承 A 的背景素材或设置；分别导出 A 和 B，得到的 MP4 对应各自选中的源作品。通过首页 A 的换背景按钮进入时预选 A，通过首页 B 的按钮进入时预选 B；刷新页面后不得无提示地改成最后一个作品。单作品自动选中，多作品可明确选择，零作品显示正确空状态，不可用深链接不会误选其他作品。选择器支持键盘操作并使用合适的 `radiogroup`、`listbox` 或等效语义表达选中状态；`390px`、`768px` 和常见桌面宽度下所有选项可访问、无截字、重叠或横向溢出。
- 不要修改：作品的排序规则、缩略图生成、保留期限、删除行为、用户权限、认证、去背景处理、换背景支持类型、本地合成、额度或 MP4 内容。不要重新加入换背景页右侧大作品列表，不要自动选择用户无权访问或已过期的作品，也不要把当前选择只保存在不稳定的数组索引中。

### 修正首页残留的换背景绝对表述

- 优先级：`P1`
- 页面或界面：英文首页 `https://bgremove.video/`
- 当前问题与线上证据：`2026-09-02` 复查生产环境时，英文首页 `A cleaner handoff from creator to editor` 模块末段仍写着 `BGRemove only creates the transparent video.`，与已上线的站内换背景和 MP4 导出功能冲突。
- 修改要求：把该模块末段完整替换为：`BGRemove creates the transparent video and can also add a color, blur, image, or video before exporting an MP4. It does not host team projects, manage versions, collect comments, or build every channel layout. Use an editor when you need text, complex layouts, or different frame sizes.` 保留透明 WebM 进入外部编辑器的高级工作流，不要删除或贬低该路径。
- 验收标准：首页不再出现 `BGRemove only creates the transparent video.`；指定替换段落逐字出现且无需执行 JavaScript即可读取。该模块同时准确表达站内简单换背景与外部编辑器高级工作流，不再与首页 FAQ、换背景页、独立 FAQ 或 Free Access 页面冲突。
- 不要修改：每 24 小时 3 次去背景的真实额度、失败任务是否计数、去背景输入限制、透明 WebM 输出、换背景支持的四种类型、浏览器本地合成、MP4 导出或保留期限。不要声称换背景包含自动光线匹配、复杂排版、文字、字幕、画幅转换、背景素材库或其他未上线功能，也不要把外部编辑器从高级工作流说明中完全删除。

### 保持换背景视频比例并自动播放预览

- 优先级：`P1`
- 页面或界面：`https://bgremove.video/change-background/` 的视频预览、背景合成和 `Export MP4`
- 当前问题与线上证据：`2026-09-02` 在生产环境登录状态下复查并选择 `Colour` 后，源透明视频固有尺寸为竖屏 `480×832`，合成画布的内部尺寸也为 `480×832`，但桌面端画布被直接渲染成约 `1188×405` 的横向区域，人物随之明显横向拉伸；说明问题发生在显示画布缩放层，而不是源文件尺寸。选择背景后，负责合成的隐藏视频停在开头且处于暂停状态，预览没有自动播放。用户此前提供的图片背景截图呈现相同拉伸问题；最终导出比例尚不能仅凭公开页面确认，因此也必须纳入修复和验收。
- 修改要求：无论选择 `Blur`、`Colour`、`Image` 还是 `Video`，前景透明视频和合成画布都必须始终保持源视频的固有宽高比，不得使用分别拉满宽度和高度的缩放方式。以当前视频显示区域可用高度为基准，根据源视频固有比例自动计算显示宽度，并在容器中水平居中；若计算后的宽度超过容器可用宽度，则等比缩小到容器宽度，并自动计算高度，任何屏幕尺寸下都不能裁切或拉伸前景视频。纯色背景铺满合成画布；图片或视频背景在不改变合成画布比例的前提下使用等比覆盖方式填满，必要时只裁切背景素材的边缘，不能通过压扁、拉长前景视频或让背景素材比例决定输出比例。`None` 状态、选择背景后的实时预览以及最终导出的 MP4 必须使用同一套源视频尺寸和比例计算，避免预览正常但导出变形，或预览和导出构图不一致。

  用户选择任一背景选项或完成纯色、图片、视频素材选择后，合成预览应自动开始播放；如果源视频已经播放结束，先回到开头再播放。预览使用 `muted` 和 `playsinline` 以满足常见浏览器自动播放限制，前景视频与视频背景的播放、暂停、跳转和循环状态必须同步，不能出现背景在动而人物静止或时间轴逐渐错位。若浏览器仍拒绝自动播放，保留明显可用的播放控件作为回退，不得隐藏错误或阻塞背景选择。自动播放只作用于编辑预览，不得改变导出视频原有的音频处理规则。
- 验收标准：分别使用至少一个横屏、一个竖屏和一个接近方形的透明视频，依次选择 `Colour`、`Image`、`Blur` 和 `Video`；每次切换后人物及其他前景内容的宽高比例均与 `None` 状态一致，没有横向拉宽、纵向压扁、裁掉前景或瞬间跳变。预览区域优先保持现有可用高度并自动适配宽度，空间不足时等比缩小；`390px`、`768px` 和常见桌面宽度下均无横向溢出。图片和视频背景可以为横屏、竖屏或方形，背景允许等比裁边但前景和输出画布比例不变。每次选择或更换背景后，合成结果无需再次点击播放即可从当前可播放位置开始；已结束的视频从头播放，视频背景与前景同步。导出各背景类型的 MP4 后，用播放器或媒体信息检查其宽高比与源透明视频一致，抽查首帧、中间帧和末帧均无拉伸且与预览构图一致。
- 不要修改：源透明视频文件、用户上传素材、现有背景类型、编辑区目标高度、前景透明度、主体位置、导出编码格式、帧率、时长、音频规则或浏览器本地处理方式。不要通过固定所有视频为 `16:9`、裁切前景、拉伸背景、降低清晰度或隐藏播放控件来规避问题，也不要让自动播放发出声音。

### 隐藏图片背景按钮的装饰图标语义

- 优先级：`P2`
- 页面或界面：`https://bgremove.video/change-background/` 的 `Image` 背景选择控件
- 当前问题与线上证据：`2026-09-02` 复查生产环境时，`Image` 背景选择标签内的装饰性 SVG 缺少 `aria-hidden="true"`，可能让辅助技术读取与可见文字重复的无意义图形内容。
- 修改要求：只给 `Image` 背景选择标签内的装饰性 SVG 增加 `aria-hidden="true"`，并确保该 SVG 本身不可聚焦。保留标签中可见的 `Image` 文字和关联的文件选择控件作为完整可访问名称。
- 验收标准：辅助技术读取该控件时只得到清晰的 `Image` 名称，装饰图标不进入可访问树且不能单独获得键盘焦点；图片文件选择仍可通过鼠标和键盘触发，现有焦点样式保持可见。
- 不要修改：其他背景控件、图标外观、文件选择行为、全站颜色、聊天按钮、页面布局或功能逻辑。

### 补充 Organization 的公开法定名称

- 优先级：`P2`
- 页面或界面：英文首页 `https://bgremove.video/` 的 `Organization` 结构化数据
- 当前问题与线上证据：首页当前公开的 `Organization` 已包含支持邮箱和 `contactPoint`，但仍没有把 About 页面公开显示的法定名称 `BGRemove d.o.o.` 表达为 `legalName`。
- 修改要求：继续使用 `https://bgremove.video/#organization` 作为唯一稳定的组织 `@id`，只增加 `legalName: "BGRemove d.o.o."`。其他页面继续通过同一 `@id` 引用该实体。
- 验收标准：首页 `Organization` JSON-LD 可解析，`legalName` 与 About 页面公开名称完全一致；全站不存在名称或 `@id` 冲突；Schema.org 验证没有关键错误。
- 不要修改：可见公司名称、地址、邮箱、现有 `contactPoint` 或其他法定信息。不要虚构电话、注册标识、税号、社交账号、评价、奖项或外部实体链接。

### 更新本次发布的公开更新日志

- 优先级：`P1`
- 页面或界面：`https://bgremove.video/changelog/`
- 当前问题与线上证据：`2026-09-02` 复查公开更新日志时，最新记录仍是 `2026-08-31` 的 `A page for changing a video background`。首页每条作品的换背景入口、全宽换背景编辑区、居中的 MP4 导出、完全免费且不限次数的提示以及全站页脚菜单已经上线但尚未记录；首页功能区额度提示和移动端按钮排列、编辑器内多作品选择、视频比例与自动播放、多语言失效链接和过期产品说明仍待完成，因此不能提前声称这些尚未上线的改进已经发布。
- 修改要求：本批次其余工作成功发布后只新增一条带日期的公开记录。只概括实际在线且用户可见的改进：可以从首页每条已完成作品进入换背景并在编辑器中切换其他有效作品；换背景编辑区更宽、MP4 导出更明显；预览和导出保持源视频比例，选择背景后自动播放；首页功能区清楚提示每 24 小时可免费去背景 3 次；相关页面区分有限的去背景额度与完全免费、不限次数的换背景；多语言页面不再链接到不存在的页面，产品说明与当前免费功能保持一致；页脚能分别找到两个产品功能和说明资源。若其中任何一项没有成功发布，就从记录中删除对应说法；如果没有任何新的用户可见改进成功发布，则不要新增记录。
- 验收标准：本批次恰好新增一条记录；内容简洁、脱敏、面向用户并与线上实际状态一致；`2026-08-31` 及更早的历史记录和日期保持不变。
- 不要修改：历史记录及其日期。不得提及文件名、组件名、代码架构、仓库、分支、提交、基础设施、服务商配置、成本、密钥、安全敏感实现、客户数据、内部指标、AI 提示词或内部工作流程。
