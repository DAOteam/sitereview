---
site_id: "fastimg"
name: "FastImg"
production_url: "https://fastimg.ai/"
changelog_url: "https://fastimg.ai/changelog/"
delivery_method: "not_established"
target_repository: "not_established"
default_branch: "not_established"
updated_at: "2026-09-26"
---

# FastImg 当前待办事项

## 已批准任务

### 补齐 www HTTPS 证书并完成主域重定向

- 优先级：`P0`
- 页面或界面：https://www.fastimg.ai/ 及该主机名下的任意路径与查询参数
- 当前问题与线上证据：2026-09-26 使用 1.1.1.1 和 8.8.8.8 查询时，`www.fastimg.ai` 均已解析到 `149.28.63.172`；`http://www.fastimg.ai/es/?utm_source=test` 和 `http://www.fastimg.ai/app/?utm_source=test` 也已分别通过一次 301 保留路径与查询参数跳转到非 www HTTPS URL。剩余问题是 443 端口返回的证书 Subject 为 `CN=fastimg.ai`，Subject Alternative Name 只有 `DNS:fastimg.ai`，不包含 `www.fastimg.ai`；标准 `curl` 访问 `https://www.fastimg.ai/` 时仍返回 `SSL: no alternative certificate subject name matches target host name 'www.fastimg.ai'`，浏览器因此无法在安全 TLS 连接中读取后续重定向。非 www 主域的 HSTS、Canonical、`hreflang` 和 Sitemap 已正确使用 `https://fastimg.ai/`。
- 修改要求：为现有 HTTPS 入口签发并部署一张公信、未过期且 Subject Alternative Name 同时包含 `fastimg.ai` 和 `www.fastimg.ai` 的证书，确保 SNI 为 `www.fastimg.ai` 时返回该证书。TLS 握手成功后，将 `https://www.fastimg.ai/*` 通过单次 `301` 永久重定向到保留原路径和查询参数的 `https://fastimg.ai/*`。保留现有 www DNS A 记录、www HTTP→非 www HTTPS 的单次 301、非 www 主域响应和 `Strict-Transport-Security: max-age=31536000`。
- 验收标准：普通浏览器和未使用 `-k` 或其他忽略证书错误选项的 `curl` 访问 `https://www.fastimg.ai/` 时均能完成 TLS 握手，证书链可信，证书有效期正常，Subject Alternative Name 包含 `www.fastimg.ai`。`https://www.fastimg.ai/es/?utm_source=test` 和 `https://www.fastimg.ai/app/?utm_source=test` 均只经过一次 301，分别到达 `https://fastimg.ai/es/?utm_source=test` 和 `https://fastimg.ai/app/?utm_source=test`；不出现证书、超时、重定向链或循环错误。现有两个 HTTP www 测试 URL 继续保持一次 301；最终 200 页面仍输出 `Strict-Transport-Security: max-age=31536000`，Canonical、`hreflang` 和 XML Sitemap 仍只使用非 www 主域。
- 不要修改：不要删除或改回已生效的 `www.fastimg.ai` DNS 解析和 HTTP 重定向，不要把 www 改成首选主域，不要将所有 www 路径重定向到首页，不要丢弃查询参数或增加第二次跳转；不要改动已正确的非 www HTTP→HTTPS 规则、Canonical、`hreflang`、Sitemap 或 HSTS，不要在未验证其他子域名前启用 HSTS `includeSubDomains` 或提交 preload。

### 修复生成与连续编辑的间歇性失败及重试行为

- 优先级：`P0`
- 页面或界面：https://fastimg.ai/app/ 的文生图、生成后继续编辑、失败状态和 `Retry` 操作
- 当前问题与线上证据：2026-09-24 使用无敏感内容提示词 `A solid blue circle centered on a plain white background` 实测时，第一次文生图请求返回 `The service is busy right now. Give it a moment and try again.`，重新提交后才成功生成无可见水印的图片。随后提交 `Change the blue circle to red and keep the white background` 进行连续编辑，第一次请求再次返回相同 busy 错误。失败界面的 `Retry` 按钮只清理失败占位并回到可编辑输入状态，虽然保留了原提示词，但没有重新提交请求。这会让新用户在核心生成和编辑流程中反复遇到可恢复失败，且按钮行为与 `Retry` 文案不一致。
- 修改要求：将上游返回的可恢复 busy、429、502、503 和 504 失败统一视为临时错误；每次用户提交后在同一任务内最多自动重试 2 次，两次重试前分别等待 1 秒和 3 秒，且不向时间线新增重复步骤。两次自动重试仍失败时，保留现有错误文案 `The service is busy right now. Give it a moment and try again.` 和按钮文案 `Retry`。点击 `Retry` 后必须立即重新提交失败任务原有的同一张输入图、同一条提示词和同一分支起点，并直接进入生成中状态；不得只清理失败占位、把提示词放回输入框或要求用户再点击底部 Generate。Retry 发起请求后立即禁用重复提交并显示生成中状态，保留上一个成功版本、原提示词和时间线分支位置；重试成功后只用真实结果替换当前失败占位。
- 验收标准：添加自动化测试，模拟第一次请求返回 503、第二次成功时，界面在 1 秒后自动重试并只产生一个成功时间线步骤；模拟连续三次返回 429 时，依次等待 1 秒和 3 秒后显示指定错误文案与 `Retry`，时间线不出现三个失败版本。在最终失败状态点击 `Retry` 一次后，无需与提示词输入框或 Generate 交互就立即发起且只发起一次新请求，界面进入生成中状态；请求载荷中的输入图片、提示词和分支起点与失败任务完全一致。生产环境冒烟测试从纯文字完成一次生成，再在同一时间线完成一次后续编辑，分别制造一次可恢复失败并点击 Retry；两次均可直接完成，最终 Download 可用，时间线只包含成功生成图和成功编辑图两个真实版本，不包含空白画布或重复失败版本。
- 不要修改：不要把无限免费生成改成额度、排队、登录或付费解锁，不要隐藏最终失败或无限循环重试，不要对认证、参数错误、不支持输入或其他不可恢复的 4xx 错误自动重试；不要删除取消、回退、分支、比较、下载或多语言功能，不要在请求、错误文案或日志中包含用户图片、提示词或生成结果。

### 优化 Generate from text 的初始输入流程

- 优先级：`P1`
- 页面或界面：https://fastimg.ai/app/ 的初始引导、Generate from text、提示词输入区、主预览区和时间线
- 当前问题与线上证据：2026-09-26 在线点击 `Generate from text` 后，页面仍会立即创建一张标为 `Blank canvas` 的黑色空白图片，在时间线新增编号 0 的 `Blank canvas` 版本，并启用 Download；浏览器焦点仍停留在页面根节点，没有进入提示词输入框。用户尚未输入或生成任何内容，却先看到一个可下载的虚假作品版本，且还要再次找到输入框才能开始文生图。
- 修改要求：点击 `Generate from text` 后进入纯提示词初始状态，不创建、渲染或下载任何黑色空白图片，不向时间线写入 `Blank canvas` 或其他占位版本，也不启用 Download。主区域不显示图片框中的黑色占位作品，改为无图片的轻量引导状态；底部提示词输入框使用当前语言既有的“描述想要生成的图片”提示文案。由于焦点移动由用户主动点击入口触发，点击后立即将键盘焦点和文本光标放入提示词输入框；桌面端可直接输入，移动端允许系统软键盘随之打开，并将输入框和 Generate 按钮滚动到可见区域。首次页面加载时不要自动聚焦。只输入空白字符时 Generate 保持禁用；第一次生成请求开始后显示临时生成状态，但只有第一张图片真实生成成功后才创建首个时间线版本并启用 Download，后续连续编辑按现有顺序追加版本。首次生成失败时保留提示词并显示 Retry，不创建永久失败缩略图；点击 Retry 按上一任务直接重发。
- 验收标准：添加自动化测试，从初始页点击 `Generate from text` 后，`document.activeElement` 是提示词输入框，DOM 和可访问性树中不存在名为 `Blank canvas` 的图片或时间线按钮，时间线项目数为 0，Download 不可见，且没有为占位图片创建 Blob URL、Canvas 导出或下载对象。桌面端可在点击入口后不再点击其他元素直接键入提示词；在 iOS Safari 和 Android Chrome 的 320×568、375×667 与 390×844 视口中，点击入口会聚焦输入框并打开软键盘，输入框和 Generate 仍完整可见且页面无横向滚动。提交只包含空白字符时不发请求；输入有效提示词并成功生成后，页面只新增一个真实图片版本，该版本成为首个时间线项目并启用 Download。模拟首次请求失败时，时间线仍没有图片版本，提示词保持不变；点击 Retry 直接重发，成功后只新增一个真实版本。
- 不要修改：不要删除初始页的 Choose image 或 Generate from text 两种入口，不要让首次页面加载自动弹出软键盘，不要用透明、纯黑、纯白、data URL 或隐藏图片替代 `Blank canvas`，不要把占位状态计入时间线或设为可下载版本；不要改变图片上传流程、提示词实际内容、生成参数、无限免费、无需登录、无水印、多语言、连续编辑、回退、分支、比较或取消功能。

### 将 Download 移到当前作品的上下文操作区

- 优先级：`P1`
- 页面或界面：https://fastimg.ai/app/ 的英语、西班牙语、葡萄牙语、法语、德语和日语状态，以及上传、文生图、连续编辑、时间线切换和比较状态
- 当前问题与线上证据：2026-09-26 在 1280×720 视口进入空白画布并完成生成后，Download 仍位于页面全局顶栏右上角，而不是用户指定的画布内部、作品右侧黑色留白区靠下位置。按钮与作品所在的编辑上下文分离，用户查看或切换时间线版本后仍要把视线和指针移到页面右上角，且当前位置不能直观说明将下载哪个版本。
- 修改要求：从全局顶栏移除 Download。1024px 及以上桌面视口保持当前作品水平居中，在画布框内部使用“左侧留白、作品、右侧留白操作区”的三列布局；将 Download 放在作品右侧黑色留白操作区的左下方，按钮左边缘距作品实际渲染右边缘 24px，按钮底边距画布框内侧底边 24px，与用户截图红箭头指向的位置一致。右侧操作区必须为按钮预留完整宽度，必要时等比缩小作品预览，但不得裁切作品或让按钮覆盖图片、边框装饰、提示文字和 Compare 控件。481–1023px 及 480px 以下没有足够右侧留白时，将 Download 放在作品下方、时间线上方；480px 以下左右各保留 12px，按钮占满作品区域可用宽度且高度至少 44px。用户切换时间线、回退、分支或进入比较状态时，Download 始终绑定当前选中的单个版本；比较状态下载当前选中版本，不下载比较界面的拼接截图。没有任何可下载版本的初始上传状态或初始文字输入状态不显示 Download，也不预留空白位置；一旦当前版本可下载，显示使用当前语言既有文案和下载图标的按钮。按钮使用原生 `button`，保留可见 `:focus-visible` 状态，并在下载准备期间显示不可重复触发的加载状态。
- 验收标准：在 1280×720、1440×900 和 1920×1080 桌面视口中，上传或生成结果后，Download 只出现一次，并位于画布内部的作品右侧黑色留白区靠下位置；按钮左边缘与作品右边缘的距离为 24±2px，按钮底边与画布框内侧底边的距离为 24±2px，按钮矩形不与作品、画布边框装饰、提示文字或 Compare 控件相交，作品保持完整显示且水平中心位置不发生肉眼可见偏移。桌面端作品下方与时间线上方不新增操作行或额外高度。768×1024、390×844、375×667 和 320×568 视口中，右侧空间不足时按钮自动使用作品下方布局；移动端按钮完整位于 12px 页面内边距之间且触控高度至少 44px。页面顶栏和图片表面不再出现 Download。连续产生至少两个版本并分别选中后，每次点击都下载当前选中版本的 PNG，不会下载先前版本或比较界面截图；下载期间不能因连点产生重复文件，完成或失败后按钮恢复可操作并提供可感知状态。使用键盘可到达 Download，焦点轮廓不被画布、时间线、固定输入区或客服遮挡。六种语言均保留各自现有 Download 文案，不新增横向滚动、布局跳动或被底部编辑区遮挡的问题。
- 不要修改：不要把 Download 放回全局顶栏；不要在 1024px 及以上桌面端把按钮放到作品下方、时间线上方、覆盖在作品上、移到提示词提交按钮旁或做成仅图标按钮；不要新增自动下载、格式选择、分享、登录、额度或付费流程，不要改变 PNG 输出、文件内容、文件名规则、当前版本选择逻辑、时间线、比较、回退、分支或多语言文案；不要改动页面 Logo、Compare 和顶栏中的编辑快捷键说明。

### 修复 Compare 前后图层尺寸不一致导致的错位

- 优先级：`P1`
- 页面或界面：https://fastimg.ai/app/ 的 Compare 模式、对比滑块、窗口缩放与横竖屏切换
- 当前问题与线上证据：2026-09-26 在 1280px 宽视口重新实测 Compare 时，比较容器和 before 图片的边界均为 x=26、y=126、宽 1228px、高约 362.3px，但 after 图片边界仍为 x=26、y=126、宽 1280px、高约 362.3px；after 比容器和 before 宽 52px。本次 before 原图为 1024×768、after 原图为 960×720，两者同为 4:3，仍使用相同的居中 contain 规则，因此错位来自 after 图层继续按视口宽度布局。滑块改变 after 的可见区域时，两层仍不能按相同坐标完全重合。
- 修改要求：让 Compare 根容器成为 before 与 after 唯一的定位和尺寸参照。before 和 after 图片都使用同一个绝对定位边界 `inset: 0; width: 100%; height: 100%`，并共享完全相同的 `object-fit: contain`、`object-position: 50% 50%` 和变换原点；禁止任何一层使用 `100vw`、页面宽度或滑块百分比作为图片自身宽度。滑块只通过 Compare 根容器上的一个百分比 CSS 变量改变 after 图层的可见裁剪范围，使用 `clip-path: inset(0 calc(100% - var(--compare-position)) 0 0)` 或等效遮罩；不得通过缩放图片、改变 after 图片宽度或让半宽裁剪容器重新计算其子图片百分比宽度实现对比。Compare 根容器使用 `overflow: hidden`，滑块线和手柄独立叠加，不参与两张图片的尺寸计算。窗口缩放、横竖屏切换和时间线版本切换时，两层必须在同一帧布局中更新，不出现一帧跳位。当前后版本原始尺寸或比例不同时，以当前选中版本的显示画布为统一比较框，两张图均保持比例、居中并使用同一套 contain 规则，允许出现对称留白，但不得拉伸或分别使用不同定位。
- 验收标准：添加自动化布局测试，在 Compare 根容器宽度为 320、375、390、768、1024、1228 和 1920 CSS px 时，将滑块分别置于 0%、25%、50%、75% 和 100%；每个位置下 before 与 after 图片的 `getBoundingClientRect()` 的 x、y、width 和 height 差值均不超过 0.5 CSS px，且 after 图片宽度始终等于 Compare 根容器宽度，不等于浏览器视口宽度或裁剪区域宽度。使用两张同为 960×720 且仅颜色不同的测试图时，在 50% 位置以边缘特征点比对，分隔线两侧对应像素的垂直位置差不超过 1 个设备像素；拖动滑块全过程不发生缩放、漂移、闪烁、露边或跳动。再使用一组不同宽高比图片验证两层保持比例并在同一画布中心对齐，没有拉伸。生产环境在桌面、390px 移动端、浏览器缩放 80%、100%、125% 以及横竖屏切换后重复测试；滑块、BEFORE/AFTER 标签和图片边界始终对齐，键盘方向键仍能调整滑块并正确更新 `aria-valuenow`。
- 不要修改：不要通过裁切掉共同有效内容、强制拉伸不同宽高比图片、固定写死某个视口尺寸、隐藏 Compare、移除滑块或降低图片清晰度来掩盖错位；不要改变前后版本选择规则、时间线、回退、分支、生成结果、下载内容、Compare 文案或六种语言；不要在渲染过程中反复读取布局并逐帧写入内联宽度。

### 修复 App 在手机窄屏下的横向溢出与操作遮挡

- 优先级：`P0`
- 页面或界面：https://fastimg.ai/app/ 的英语、西班牙语、葡萄牙语、法语、德语和日语状态，以及初始提示词、生成中、成功、失败和客服展开状态
- 当前问题与线上证据：2026-09-26 在已有生成结果的状态下复测，390×844 视口的 `documentElement.clientWidth` 为 390px、`scrollWidth` 为 401px；320×568 视口的 `clientWidth` 为 320px、`scrollWidth` 仍为 401px。两种视口下 Generate 按钮均位于 x=305–401，右侧分别超出 11px 和 81px；390px 下客服按钮位于 x=316–370、y=770–824，320px 下位于 x=246–300、y=494–548，均与 x=96–282 的提示词输入区及 Generate 操作区域发生覆盖。顶部 Download 高 36px、Compare 高 30px、底部 Generate 高 36px，也低于移动端 44px 触控目标。
- 修改要求：在 480px 及以下采用专用移动布局。底部编辑区使用两行布局：第一行的提示词输入区域占满容器可用宽度并允许内部文本收缩或换行，第二行的 Generate、Cancel、Retry 或对应当前状态的主要操作按钮占满同一可用宽度；容器左右各保留 12px 间距，所有子项使用 `min-width: 0` 和 `box-sizing: border-box`，不得依靠裁切或页面级 `overflow-x: hidden` 掩盖溢出。底部编辑区使用 `100dvh` 对应的可见布局高度，并在底部加入 `env(safe-area-inset-bottom)`；主画布或初始提示词引导区可纵向滚动，并预留等于底部编辑区实际高度的空间，不能被固定输入区覆盖。将客服悬浮按钮放到完整底部编辑区上方，保持至少 12px 间距；客服展开层在手机上继续使用全屏显示，关闭后焦点返回打开客服的按钮。移动端 Download、Choose image、Generate from text、Generate、Cancel、Retry、客服打开/隐藏/关闭以及其他图标操作的实际可点击区域均至少为 44×44 CSS px，图标视觉尺寸可以保持不变。首次加载页面时不要自动聚焦；只有用户明确点击 `Generate from text` 后，才立即聚焦提示词输入框并允许系统软键盘打开，聚焦后的输入框、当前主要操作按钮和最新结果须可滚动到可见区域。
- 验收标准：在真实或等效的 iOS Safari 与 Android Chrome 中，以 320×568、375×667 和 390×844 三组视口分别测试六种语言；初始提示词、输入长达 500 个字符、生成中、成功、失败与 Retry、客服关闭和客服展开各状态下，`document.documentElement.scrollWidth` 始终等于 `clientWidth`，页面没有横向滚动，所有文字可换行且没有被裁切。底部输入区与主要操作按钮完整位于视口内，客服按钮不与任何输入框、按钮、结果操作或系统安全区相交，任意两个独立触控目标的可点击矩形不重叠；所有主要触控目标至少为 44×44 CSS px。点击 `Generate from text` 后提示词输入框获得焦点并打开软键盘，输入框与 Generate 仍完整可见；打开再关闭客服后，焦点返回客服按钮。弹出和收起软键盘、横竖屏切换及地址栏伸缩后，提示词内容不丢失，页面高度重新适配，用户可以继续 Generate、Cancel、Retry 和 Download。桌面宽度 1024px 及以上保留现有单行编辑器布局和视觉样式。
- 不要修改：不要删除或隐藏客服、Download、Choose image、Generate from text、Generate、Cancel、Retry、时间线、回退、分支、比较或下载功能；不要用禁用页面缩放、缩小字体或触控目标、截断按钮文案、固定 320px 以上最小宽度或全局隐藏横向溢出来掩盖布局问题；不要改变生成参数、免费无限、无需登录、无水印、多语言文案或桌面工作流。

### 为六个功能落地页建立五种完整本地化版本

- 优先级：`P1`
- 页面或界面：新建 `/es/`、`/pt/`、`/fr/`、`/de/`、`/ja/` 下的 `ai-image-generator/`、`change-background/`、`remove-object/`、`add-object/`、`change-clothes/` 和 `product-photo-editor/`，共 30 个 URL
- 当前问题与线上证据：2026-09-26 线上六个功能落地页只有英语版本，初始 HTML 均为 `lang="en"`、只有英语自引用 Canonical，未输出任何 `hreflang`；XML Sitemap 也只收录这六个英语功能页。按现有语言目录检查的 30 个候选 URL 当前全部返回 404。网站已有西班牙语、葡萄牙语、法语、德语和日语首页，但这些首页的用户和搜索引擎进入具体生图或编辑功能时只能落到英语页，无法形成对应语言的功能搜索入口。
- 修改要求：使用现有语言目录和固定英语 slug 创建以下页面矩阵：`/{es|pt|fr|de|ja}/ai-image-generator/`、`/{es|pt|fr|de|ja}/change-background/`、`/{es|pt|fr|de|ja}/remove-object/`、`/{es|pt|fr|de|ja}/add-object/`、`/{es|pt|fr|de|ja}/change-clothes/`、`/{es|pt|fr|de|ja}/product-photo-editor/`。每页以对应英语功能页为事实来源，完整本地化 Title、Meta Description、Open Graph、Twitter Description、H1、正文、步骤、适用场景、输入输出限制、FAQ、CTA、Before/After 标题与图片 alt、面包屑、WebApplication、FAQPage 和 BreadcrumbList JSON-LD；不得只翻译关键词或元数据。保留 FastImg、AI、PNG 等通用产品或格式词，并由目标语言自然表达相同搜索意图。首屏利益点固定使用：西班牙语 `Gratis para siempre · Uso ilimitado · Sin registro · Sin marca de agua`，葡萄牙语 `Grátis para sempre · Uso ilimitado · Sem cadastro · Sem marca-d’água`，法语 `Gratuit pour toujours · Utilisation illimitée · Sans inscription · Sans filigrane`，德语 `Für immer kostenlos · Unbegrenzte Nutzung · Keine Anmeldung · Kein Wasserzeichen`，日语 `永久無料 · 無制限 · 登録不要 · 透かしなし`。每个语言版本设置正确的 `html lang` 和 JSON-LD `inLanguage`，使用自引用 Canonical、`index, follow, max-image-preview:large`，并与该功能的英语及其他四种本地化页面组成包含 `en`、`es`、`pt`、`fr`、`de`、`ja` 和 `x-default` 的完整双向 `hreflang` 集合；`x-default` 指向英语功能页。语言切换器必须从当前功能页跳到同一功能的目标语言页。五个本地化首页的功能入口改为指向同语言功能页，每个本地化功能页的首页、生成器和相关工具内链也只指向同语言 URL。将 30 个新 URL 加入 XML Sitemap，使用真实发布日期的 `lastmod` 和与 HTML 完全一致的 `hreflang` 集合；现有图片可复用，不复制或改名资源。
- 验收标准：30 个 URL 全部直接返回 200，不经过重定向，允许索引且 Canonical 自引用；`html lang`、可见正文、控件、图片 alt、Meta、Open Graph、Twitter 和 JSON-LD 使用目标语言，除 FastImg、AI、PNG 等通用词外不残留整段英语。每个功能的六语言页面与 `x-default` 互相返回完全一致且可解析的 `hreflang` 集合，不存在缺失回链、错误区域代码、相对 URL、404 或 Canonical 冲突。语言切换器从任意一个功能页切换六种语言后始终保持相同功能，不退回首页。五个本地化首页可通过普通 `<a>` 链接到六个同语言功能页，每个新页面在三次普通链接点击内可从同语言首页到达。Sitemap 在现有 13 个 URL 基础上新增且只新增这 30 个 Canonical 页面，总数为 43，不包含 `/app/`、参数 URL、重定向或 `noindex` 页面。每页 WebApplication、FAQPage 和 BreadcrumbList JSON-LD 可解析，内容与页面可见事实一致；同一语言内六个页面的 Title、H1、主要正文和任务专属 FAQ 不重复。桌面端和 390px 移动端无裁切、重叠或横向滚动，所有功能入口继续进入对应的现有编辑流程。
- 不要修改：不要翻译 URL slug、创建国家地区变体、子域或额外语言，不要把本地化页面 Canonical 到英语页，不要使用客户端运行时翻译、IP 强制跳转或仅搜索引擎可见的文字；不要批量复制同一正文只替换功能关键词，不要添加模型、速度、质量、分辨率、商业授权、数据保留、评分、评论或其他未经确认的承诺；不要改变英语功能页 URL、`/app/` 的 `noindex`、现有图片、实际生成参数、无限免费、无需登录、无水印和 PNG 下载规则，也不要在本任务中创建本地化 Changelog 页面。

### 修正产品图页的操作说明标题

- 优先级：`P2`
- 页面或界面：https://fastimg.ai/product-photo-editor/
- 当前问题与线上证据：2026-09-26 产品图页的操作说明 H2 仍是语法和大小写错误的 `How to aI product photo editor`。
- 修改要求：将产品图页 H2 `How to aI product photo editor` 逐字替换为 `How to edit product photos with AI`。
- 验收标准：产品图页只出现一个 `How to edit product photos with AI` H2，初始 HTML、DOM、可访问性树和纯文本提取中都不再出现 `How to aI product photo editor`；页面的 Title、Meta Description、Canonical、robots、JSON-LD、其他标题和布局保持不变。
- 不要修改：不要改写产品图页的其他文案，不要更换该 H2 的搜索意图，不要改动英语首页、任何多语言页面、图片 alt、结构化数据、内链、工具入口或页面布局。

### 发布移动端与多语言功能页更新的公开变更日志

- 优先级：`P1`
- 页面或界面：https://fastimg.ai/changelog/
- 当前问题与线上证据：`/app/` 当前在手机窄屏下存在横向溢出和客服按钮遮挡核心操作的问题，六个功能落地页也只有英语版本。本批工作包含重要的移动端兼容性修复和 30 个用户可访问的本地化功能页，属于用户可发现的显著更新；现有公开 Changelog 尚未记录这些仍未上线的改进。
- 修改要求：仅在“修复 App 在手机窄屏下的横向溢出与操作遮挡”和“为六个功能落地页建立五种完整本地化版本”两项任务均通过生产环境验收后，使用真实发布日期在现有 Changelog 顶部新增标题 `Mobile editor improvements and localized tool pages`，正文逐字使用 `FastImg now offers its image generator and editing tool pages in Spanish, Portuguese, French, German, and Japanese. We also improved the mobile editor so the prompt field, Generate button, and support chat stay accessible without overlap, with larger touch targets and safe-area spacing.`。保持现有条目、日期、页面 Title、Meta Description、Canonical 和结构化数据不变，并同步该页面在 XML Sitemap 中的真实 `lastmod`。
- 验收标准：两项指定任务均已在生产环境通过各自全部验收标准后，Changelog 才显示使用实际上线日期的新条目；标题和正文与指定文案逐字一致，条目位于旧条目之前。页面返回 200、允许索引、自引用 Canonical，XML Sitemap 中的 Changelog `lastmod` 与该条目发布日期一致；条目描述的五种语言功能页以及输入区、Generate、客服、触控目标和安全区改进均可在线复现。
- 不要修改：不要在任一指定任务上线前发布条目，不要预填或虚构发布日期，不要为每种语言或每个功能拆分多条记录，不要改写或删除已有历史条目与日期；不要在公开变更日志中提及文件、组件、CSS 类、代码、仓库、分支、提交、部署、测试设备、内部指标、翻译流程或客服供应商。
