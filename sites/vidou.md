---
site_id: "vidou"
name: "Vidou"
production_url: "https://vidou.ai/"
changelog_url: "not_established"
delivery_method: "not_established"
target_repository: "not_established"
default_branch: "not_established"
updated_at: "2026-10-02"
---

# Vidou 当前待办事项

## 已批准任务

### 将首篇 Blog 的唯一转化目标改为首页免费工具区

- 优先级：`P1`
- 页面或界面：`https://vidou.ai/blog/how-to-animate-a-photo-with-ai/`
- 当前问题与线上证据：2026-10-02 线上正文中的工具锚文本和文末 CTA 均指向 `https://vidou.ai/image-to-video/`。该文章服务于初次尝试和基础照片动画意图，而首页已明确承接免费、无需登录的 Image to Video 使用场景；专用工具页需要改为承接登录后的高级设置意图。线上文章还在导读链接、定义段、上传步骤和 FAQ 中使用了带连字符的功能名称，与 Vidou 统一使用 `Image to Video`、`Text to Video`、`Text to Image` 和 `Image Editor` 的可见命名规范不一致。
- 修改要求：修改文章中的两个转化链接，并统一正文中的功能名称。把上传步骤的现有句子替换为以下精确英文文案：`Open Vidou's [free AI image to video generator](https://vidou.ai/#image-to-video) and choose the photo you want to animate. The current interface accepts JPEG, PNG, and WebP images.`；把文末现有 `Animate Your Photo With Vidou` CTA 按钮的目标地址改为 `https://vidou.ai/#image-to-video`，按钮文字保持不变。正文锚文本和 CTA 必须使用同一个绝对 URL，正文只出现这一个工具锚文本，CTA 是第二次且最后一次出现该 URL。同时执行以下精确文本替换：`complete guide to AI image-to-video generation` 改为 `complete guide to AI image to video generation`；`An image-to-video system` 改为 `An image to video system`；`Image-to-video generation can interpret` 改为 `Image to video generation can interpret`。检查该文章的 Title、Meta、Open Graph、Twitter、H1、H2、H3、正文、FAQ、CTA、图片 alt 和 Article JSON-LD 中的用户可见字符串；如果还存在作为功能名称使用的 `Image-to-Video`、`image-to-video`、`Text-to-Video`、`text-to-video`、`Text-to-Image` 或 `text-to-image`，统一删除功能名称中的连字符。URL、slug、canonical、fragment、资源文件名和代码标识保持原样。
- 验收标准：线上文章正文可见且可点击的 `free AI image to video generator` 只出现一次并准确跳到首页 `#image-to-video` 工具区；文末 `Animate Your Photo With Vidou` 按钮也跳到同一地址；文章主内容、FAQ 和文章专属导航中不再出现指向 `/image-to-video/` 或其他工具页的链接；整篇文章合计只有这两个指向所选转化目标的链接；文章全部用户可见内容和结构化数据可见字符串均不再使用带连字符的 Vidou 功能名称，技术 URL 与资源路径继续有效；桌面端与移动端均能正确定位到首页工具表单。
- 不要修改：除本任务列出的链接与功能名称拼写外，不要修改文章其余正文、标题含义、Meta 含义、H1、发布日期、作者 `By Vidou`、Article JSON-LD 字段结构、现有配图、父子文章链接或页面布局；不要重命名 URL、slug、canonical、fragment、资源文件名或代码标识；不要把普通导航和页脚中的全站链接计入或删除。

### 为 Image to Video 高级工具页增加差异化图文内容

- 优先级：`P1`
- 页面或界面：`https://vidou.ai/image-to-video/`
- 当前问题与线上证据：2026-10-02 线上页面主要是登录后的生成表单和 `My Creations`，缺少可索引的功能说明、设置选择指导、输入建议和 FAQ；现有页面可见上传格式为 JPEG、PNG、WebP，可选 9:16、4:3、3:4、1:1、16:9，时长显示为 5s，可选 480p、720p、1080p，并提供 Audio 开关和生成前的 credits 提示。首页已经完整承接免费、无需登录的快速体验，专用页不能重复该定位。
- 修改要求：保持现有表单和 `My Creations` 的顺序与功能不变，在其下方新增以下精确英文内容。SEO Title 改为 `Advanced AI Image to Video Generator | Vidou`；Meta Description 改为 `Use Vidou's signed-in image to video workspace with five aspect ratios, 480p to 1080p output, optional audio, and visible credit requirements.`；页面 H1 改为 `Advanced AI Image to Video Generator`。在 H1 与表单之间加入导语：`Use the signed-in Vidou workspace when you need more control than the free homepage tool. Upload a JPEG, PNG, or WebP image, describe one clear motion, then choose an aspect ratio, resolution, and optional audio before generating. The required credits are shown before you start.`。在表单与 `My Creations` 之后按以下顺序加入内容：

  1. H2 `More Control for Image to Video Workflows`

     `The homepage is the quickest way to try image to video without signing in. This workspace is designed for projects that need selectable output settings, saved creations, and clear credit requirements.`

  2. H2 `How to Use the Advanced Workspace`

     - `Sign in and upload a JPEG, PNG, or WebP image.`
     - `Describe the subject motion, camera movement, pace, and details that should remain stable.`
     - `Choose 9:16, 4:3, 3:4, 1:1, or 16:9; select 480p, 720p, or 1080p; decide whether to enable audio; then review the displayed credit requirement before generating.`

  3. H2 `Choose Settings for the Final Destination`

     H3 `Aspect ratio`

     `Use 9:16 for vertical mobile viewing, 16:9 for widescreen layouts, 1:1 for square placements, and 4:3 or 3:4 when the composition needs a less extreme horizontal or vertical frame. Choose the destination before generating so important subjects are not forced into a later crop.`

     H3 `Resolution`

     `Choose 480p for lightweight drafts, 720p for a balanced review file, or 1080p when the destination calls for the largest available output. A higher output setting cannot restore detail that is missing from the source image.`

     H3 `Audio`

     `Enable audio only when the project needs a generated soundtrack. Review sound and visuals together before using the result in a final edit.`

  4. H2 `Prepare a Better Source Image`

     `Start with a sharp image that has a clear subject, enough space for the intended movement, and no important details cut off at the frame edge. Small faces, unreadable labels, heavy compression, and overlapping hands can become harder to evaluate once motion is added. If a logo, product shape, or facial feature must remain stable, name that constraint directly in the prompt.`

  5. H2 `What to Review Before You Use the Video`

     `Watch the full clip at normal speed and inspect faces, hands, text, logos, product shape, background edges, and the first and last frames. Look for sudden jumps, flicker, unwanted objects, or camera motion that conflicts with the prompt. Regenerate or revise the prompt when a visible error affects the intended use.`

  6. H2 `Advanced Image to Video FAQ`，使用以下精确问答：

     - H3 `Does this workspace require an account?` 答案：`Yes. The advanced workspace requires you to sign in before uploading and generating.`
     - H3 `Which image formats are supported?` 答案：`The current upload control accepts JPEG, PNG, and WebP images.`
     - H3 `Which aspect ratios are available?` 答案：`The current workspace offers 9:16, 4:3, 3:4, 1:1, and 16:9.`
     - H3 `Which resolutions are available?` 答案：`The current workspace offers 480p, 720p, and 1080p output settings.`
     - H3 `How are credits handled?` 答案：`The interface shows the required credits before generation. Review the displayed amount before starting, and visit the Pricing page when you need to compare available credit packages.`，其中 `Pricing page` 链接到 `https://vidou.ai/pricing/`。

  同时制作并使用两张符合现有品牌视觉、无第三方素材和虚构生成结果的原创 WebP 说明图：`advanced-image-to-video-workflow.webp`，1400×788，放在导语之后，内容为 Upload → Prompt → Ratio / Resolution / Audio → Review 的界面化流程图，alt 为 `Advanced image to video workflow from upload and prompt to output review`；`image-to-video-settings-guide.webp`，1200×800，放在 `Choose Settings for the Final Destination` 小节之后，以五种比例框、三档分辨率和 Audio 开关组成设置说明图，alt 为 `Image to video aspect ratio, resolution, and audio settings guide`。图片必须输出响应式尺寸，声明固有 width/height；首张图按首屏位置合理处理加载优先级，第二张图使用 lazy loading。同步 canonical、Open Graph 和 Twitter 标题、描述与分享图，canonical 保持 `https://vidou.ai/image-to-video/`。
- 验收标准：线上 Title、Meta、H1、导语、六个内容区块、FAQ 和两张说明图均与任务一致；现有上传、Prompt、比例、时长、分辨率、Audio、credits、Generate、登录和 `My Creations` 行为不变；页面不使用 `free`、`no login`、`unlimited`、`instant`、`in seconds` 或无法验证的效果保证来描述专用工具页，只有差异说明中的 `free homepage tool` 和 `without signing in` 用于明确区分首页；所有文案在桌面与移动端可读，标题层级连续，图片无布局偏移，Pricing 链接有效，结构化数据和社交元数据不声明未验证能力。
- 不要修改：不要复制首页的免费/免登录主标题、首页长文内容或首页 FAQ；不要改变 credits 数量、价格、生成参数、账户逻辑或 API；不要展示伪造的前后对比、用户结果、评价、排名或性能数据；不要使用竞品或未授权素材。

### 为 Text to Video 工具页增加完整图文内容

- 优先级：`P2`
- 页面或界面：`https://vidou.ai/text-to-video/`
- 当前问题与线上证据：2026-10-02 线上页面主要是登录后的 Prompt 表单和 `My Creations`，缺少对提示词结构、输出比例、检查方法和账户/credits 的可索引说明；当前界面可见五种比例、5s、480p/720p/1080p 和生成前 credits 提示。
- 修改要求：保持现有工具功能不变，在 H1 与表单之间增加导语，并在表单与 `My Creations` 之后加入以下精确英文内容。SEO Title 使用 `AI Text to Video Generator | Vidou`；Meta Description 使用 `Turn a written scene description into a short AI video with five aspect ratios, 480p to 1080p output, and visible credit requirements.`；H1 使用 `AI Text to Video Generator`；导语使用 `Describe the scene you want to create, then choose an aspect ratio and resolution before generating a short video in Vidou's signed-in workspace. The required credits are shown before generation.`。正文顺序如下：

  1. H2 `Turn a Scene Description Into a Video`

     `Text to video begins with the description rather than a source image. A useful prompt gives the model a clear subject, one main action, a setting, a camera choice, and a visual mood without packing several unrelated scenes into one request.`

  2. H2 `How to Write the Prompt`

     `Build the prompt in this order: subject + action + setting + camera movement or framing + lighting and mood + pace. For example: “A paper boat drifts through a shallow rain puddle, close low-angle framing, soft overcast light, gentle forward camera movement, calm pace.” Keep the central action easy to recognize and state important constraints plainly.`

  3. H2 `Choose the Output Format`

     `Select 9:16 for vertical mobile placements, 16:9 for widescreen scenes, 1:1 for square layouts, or 4:3 and 3:4 for intermediate horizontal and vertical compositions. Choose 480p, 720p, or 1080p according to the review or delivery need. The current workspace creates a 5-second clip, so frame the prompt around one concise moment rather than a long sequence.`

  4. H2 `Review the Generated Scene`

     `Check whether the main subject remains recognizable, the requested action is visible, the background stays coherent, and no unwanted objects appear. Review camera direction, motion speed, lighting continuity, and the transition between the first and last frames before using the clip elsewhere.`

  5. H2 `When Text to Video Fits the Workflow`

     `Use text to video when you need to explore a scene without a fixed source image, such as a concept shot, an establishing shot, or a short social visual. If an exact person, product, logo, or composition must be preserved, start from an appropriate reference image and use the image to video workflow instead.`，其中 `image to video workflow` 链接到 `https://vidou.ai/image-to-video/`。

  6. H2 `Text to Video FAQ`，使用以下精确问答：

     - H3 `Does text to video require an account?` 答案：`Yes. You need to sign in before generating in this workspace.`
     - H3 `How long is the current output?` 答案：`The current duration shown in the workspace is 5 seconds.`
     - H3 `Which aspect ratios are available?` 答案：`The current workspace offers 9:16, 4:3, 3:4, 1:1, and 16:9.`
     - H3 `Which resolutions are available?` 答案：`The current workspace offers 480p, 720p, and 1080p output settings.`
     - H3 `How do I check the credit cost?` 答案：`Review the credit requirement displayed in the interface before you generate.`

  制作两张原创 WebP 说明图：`text-to-video-prompt-structure.webp`，1400×788，放在 `How to Write the Prompt` 之后，以六个连续模块展示 Subject、Action、Setting、Camera、Lighting & Mood、Pace，alt 为 `Text to video prompt structure with subject, action, setting, camera, lighting, and pace`；`text-to-video-format-guide.webp`，1200×800，放在 `Choose the Output Format` 之后，展示五种比例及其适用构图，并标注 5-second clip 和 480p/720p/1080p，alt 为 `Text to video aspect ratio and resolution guide`。两图不得呈现虚构成片。设置响应式图片、固有尺寸和非首屏 lazy loading。同步 canonical、Open Graph 和 Twitter 字段，canonical 保持 `https://vidou.ai/text-to-video/`。
- 验收标准：线上元数据、H1、导语、六个正文区块、FAQ 和两张说明图准确呈现；内部链接有效；表单现有行为和可选项不变；页面没有虚构生成质量、速度、模型、免费额度或结果；桌面与移动端无横向溢出，图片 alt、width、height、响应式资源和加载方式正确。
- 不要修改：不要改变登录、credits、时长、分辨率、比例、生成接口或 `My Creations`；不要添加未经验证的 negative prompt、镜头控制、模型选择或编辑能力；不要使用第三方成片冒充 Vidou 输出。

### 为 Text to Image 工具页增加完整图文内容

- 优先级：`P2`
- 页面或界面：`https://vidou.ai/text-to-image/`
- 当前问题与线上证据：2026-10-02 线上页面主要是登录后的 Prompt 表单和 `My Creations`，仅展示五种比例和 credits，缺少提示词方法、比例选择、结果检查和适用场景内容。
- 修改要求：保持现有工具不变，使用以下精确英文内容。SEO Title 使用 `AI Text to Image Generator | Vidou`；Meta Description 使用 `Create an image from a written prompt in Vidou's signed-in workspace, choose from five aspect ratios, and review the credit requirement before generating.`；H1 使用 `AI Text to Image Generator`；H1 与表单之间的导语使用 `Describe the image you want to create, choose an aspect ratio, and review the displayed credit requirement before generating in Vidou's signed-in workspace.`。在表单与 `My Creations` 后加入：

  1. H2 `Build the Image From Clear Visual Details`

     `A useful text to image prompt describes what should be visible and how the scene should be composed. Start with the main subject, then add the setting, framing, lighting, visual mood, and the details that must remain prominent.`

  2. H2 `How to Write a More Useful Image Prompt`

     `Use this order: subject + setting + composition + lighting + style or mood + important details. For example: “A ceramic teapot on a pale stone table, centered product composition, soft window light from the left, warm editorial mood, clean background, handle and spout fully visible.” Prefer concrete visual language over broad praise such as “amazing” or “perfect.”`

  3. H2 `Choose an Aspect Ratio Before You Generate`

     `Use 1:1 for square compositions, 9:16 or 3:4 for vertical layouts, and 16:9 or 4:3 for horizontal scenes. Decide where the image will appear before generating so the subject has appropriate space and is less likely to require a damaging crop.`

  4. H2 `Review the Whole Image`

     `Inspect the subject first, then check hands, faces, text, object edges, reflections, shadows, background details, and lighting direction. Look for repeated objects, warped geometry, unreadable lettering, or elements that conflict with the prompt. Revise one part of the prompt at a time so the effect of each change is easier to judge.`

  5. H2 `Where Text to Image Can Help`

     `Text to image can support early concept exploration, social visual drafts, mood boards, and composition studies. Treat the generated image as material to review rather than proof that brand, legal, product, or factual details are correct.`

  6. H2 `Text to Image FAQ`，使用以下精确问答：

     - H3 `Does text to image require an account?` 答案：`Yes. You need to sign in before generating in this workspace.`
     - H3 `Which aspect ratios are available?` 答案：`The current workspace offers 9:16, 4:3, 3:4, 1:1, and 16:9.`
     - H3 `How should I structure a prompt?` 答案：`Start with the subject, then add the setting, composition, lighting, visual mood, and important details.`
     - H3 `How are credits handled?` 答案：`The interface shows the required credits before generation. Review that amount before you start.`

  制作两张原创 WebP 说明图：`text-to-image-prompt-structure.webp`，1400×788，放在 `How to Write a More Useful Image Prompt` 之后，展示 Subject、Setting、Composition、Lighting、Style / Mood、Details 六段提示词结构，alt 为 `Text to image prompt structure from subject to important visual details`；`text-to-image-aspect-ratio-guide.webp`，1200×800，放在比例小节之后，用五种比例框展示横向、方形和纵向构图差异，alt 为 `Text to image aspect ratio guide for horizontal, square, and vertical layouts`。不得使用虚构生成图作为效果证明。设置响应式资源、固有尺寸和非首屏 lazy loading。同步 canonical、Open Graph 和 Twitter 字段，canonical 保持 `https://vidou.ai/text-to-image/`。
- 验收标准：线上元数据、H1、导语、六个内容区块、FAQ、两张说明图和 alt 均与任务一致；页面清晰解释提示词与比例选择但不暗示未验证能力；表单行为不变；桌面与移动端层级、间距、图片加载和可读性正常。
- 不要修改：不要改变登录、credits、比例、生成接口或 `My Creations`；不要新增未在界面验证的分辨率、模型、negative prompt 或编辑功能；不要声称图片可直接满足品牌、法律、产品或事实准确性要求。

### 为 AI Image Editor 工具页增加完整图文内容

- 优先级：`P2`
- 页面或界面：`https://vidou.ai/image-edit/`
- 当前问题与线上证据：2026-10-02 线上页面主要是登录后的图片上传、Prompt、比例和 credits 表单，上传支持 JPEG、PNG、WebP，但缺少对单一编辑目标、保留约束、源图选择和结果检查的可索引说明。
- 修改要求：保持现有工具功能不变，使用以下精确英文内容。SEO Title 使用 `AI Image Editor | Vidou`；Meta Description 使用 `Upload a JPEG, PNG, or WebP image, describe the change you want, choose an aspect ratio, and review the credit requirement before editing.`；H1 使用 `AI Image Editor`；H1 与表单之间加入导语：`Upload a JPEG, PNG, or WebP image, describe one clear change, choose an aspect ratio, and review the displayed credit requirement before editing in Vidou's signed-in workspace.`。在表单与 `My Creations` 后加入：

  1. H2 `Describe One Clear Edit`

     `Image editing works best when the request identifies the element to change and the details that should stay intact. Begin with one main edit, then add preservation or background constraints instead of combining several unrelated transformations.`

  2. H2 `How to Edit an Image`

     - `Sign in and upload a JPEG, PNG, or WebP image.`
     - `Describe the target, the requested change, and the details that must remain unchanged.`
     - `Choose 9:16, 4:3, 3:4, 1:1, or 16:9, review the displayed credit requirement, and generate the edit.`

  3. H2 `Write an Edit Prompt That Preserves Important Details`

     `Use this order: target element + requested change + elements to preserve + background or composition constraints. For example: “Change the chair upholstery to deep green velvet; keep the chair shape, wooden legs, room layout, camera angle, and window lighting unchanged.” Name exact colors, materials, or areas only when they matter to the result.`

  4. H2 `Choose the Right Source Image`

     `Use a sharp source image where the target area is visible and separated from similar objects. Avoid heavy compression, extreme blur, or a crop that removes details you want to preserve. Choose the output ratio deliberately because a different frame can change the composition as well as the edited subject.`

  5. H2 `Review the Edited Image`

     `Compare the result with the source at the same size. Check the requested change, subject identity, object shape, edges, hands, faces, text, logos, lighting direction, shadows, reflections, and background continuity. Reject an edit when it changes protected details or introduces visible artifacts.`

  6. H2 `Common Editing Uses`

     `Use the editor to explore a style variation, a background adjustment, a color or lighting direction, or a revised composition. Keep each request focused and verify the output before using it in a public or commercial context.`

  7. H2 `AI Image Editor FAQ`，使用以下精确问答：

     - H3 `Does the image editor require an account?` 答案：`Yes. You need to sign in before uploading and generating an edit.`
     - H3 `Which image formats are supported?` 答案：`The current upload control accepts JPEG, PNG, and WebP images.`
     - H3 `Which aspect ratios are available?` 答案：`The current workspace offers 9:16, 4:3, 3:4, 1:1, and 16:9.`
     - H3 `How do I tell the editor what to preserve?` 答案：`Name the subject features, object shapes, background elements, camera angle, or lighting that should remain unchanged.`
     - H3 `How are credits handled?` 答案：`Review the credit requirement displayed in the interface before you generate the edit.`

  制作两张原创 WebP 说明图：`ai-image-edit-workflow.webp`，1400×788，放在 `How to Edit an Image` 之后，展示 Upload → Describe One Change → Choose Ratio → Review 的流程，不展示虚构前后对比，alt 为 `AI image editing workflow from source upload to result review`；`image-edit-prompt-anatomy.webp`，1200×800，放在提示词小节之后，展示 Target、Change、Preserve、Constraints 四段结构，alt 为 `AI image edit prompt structure for target, change, preserved details, and constraints`。设置响应式资源、固有尺寸和非首屏 lazy loading。同步 canonical、Open Graph 和 Twitter 字段，canonical 保持 `https://vidou.ai/image-edit/`。
- 验收标准：线上元数据、H1、导语、七个正文区块、FAQ 和两张说明图准确呈现；支持格式和比例说明与当前界面一致；现有上传、Prompt、比例、credits、登录、Generate 和 `My Creations` 不变；页面没有伪造结果、效果保证或未经验证的编辑能力；桌面与移动端无布局或可访问性回退。
- 不要修改：不要改变 credits、账户逻辑、API、现有编辑参数或支持格式；不要加入第三方素材、虚构 before/after、用户案例或效果数据；不要承诺能精确保留商标、人物身份、文字或其他细节。

### 将 CSP 从 Report-Only 切换为强制策略

- 优先级：`P2`
- 页面或界面：`https://vidou.ai/` 及所有同域公开 HTML 页面
- 当前问题与线上证据：2026-10-02 复核首页、当前工具页、About、Blog、新文章和法律页时，所有公开 HTML 已返回 `X-Content-Type-Options: nosniff`、`Referrer-Policy: strict-origin-when-cross-origin`、`Permissions-Policy: camera=(), microphone=(), geolocation=()`、`X-Frame-Options: DENY` 和原有 HSTS；`/pro/` 也已单次 301 到当前 Image to Video 工作区。但 CSP 仍只通过 `Content-Security-Policy-Report-Only` 返回，没有强制 `Content-Security-Policy`，所以资源来源与 `frame-ancestors 'none'` 尚未由浏览器实际阻止。
- 修改要求：检查当前 Report-Only 策略的真实违规报告，在首页、四个工具页、登录入口、Pricing、Blog、About、法律页和 Hepo 客服均无必要资源被阻断后，把当前已验证策略以 `Content-Security-Policy` 强制响应头覆盖所有公开 HTML。强制策略至少保留 `default-src 'self'`、`object-src 'none'`、`base-uri 'self'`、受限的 `form-action` 和 `frame-ancestors 'none'`，并继续只允许已经核验的同域、API、Google 登录、Hepo 客服及现有图片来源；Report-Only 可以删除，或仅用于测试比强制策略更严格的后续规则，不能替代强制策略。
- 验收标准：所有公开 HTML 的 200 响应和 `/pro/` 的 301 响应均返回强制 `Content-Security-Policy`；策略不包含 `*`，不新增 `unsafe-eval`、开发域、localhost 或未使用第三方域，且 `frame-ancestors 'none'` 生效；首页视频、图片、四个工具页、登录入口、Pricing、Blog、About、法律页和 Hepo 客服在桌面与移动端无 CSP 阻断错误；现有 `nosniff`、Referrer Policy、Permissions Policy、`X-Frame-Options: DENY` 和 `Strict-Transport-Security: max-age=31536000` 继续存在。
- 不要修改：不要禁用 HTTPS、HSTS、Google 登录、Hepo 客服或现有核心资源；不要为消除违规而使用通配符、增加 `unsafe-eval` 或开放未核验来源；不要在公开文件中记录 CSP 违规报告里的用户数据、完整查询参数或其他敏感信息。
