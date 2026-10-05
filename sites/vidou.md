---
site_id: "vidou"
name: "Vidou"
production_url: "https://vidou.ai/"
changelog_url: "not_established"
delivery_method: "not_established"
target_repository: "not_established"
default_branch: "not_established"
updated_at: "2026-10-05"
---

# Vidou 当前待办事项

## 已批准任务

### 为四个工具页补充与可见 FAQ 同步的 FAQPage 结构化数据

- 优先级：`P2`
- 页面或界面：`https://vidou.ai/image-to-video/`、`https://vidou.ai/text-to-video/`、`https://vidou.ai/text-to-image/`、`https://vidou.ai/image-edit/`
- 当前问题与线上证据：2026-10-05 线上复核确认，四页新的 Prompt 和 FAQ 文案均已显示，FAQ 使用按钮、`aria-expanded` 和关联面板 ID，默认只展开第一项；但每页当前唯一的 JSON-LD `@graph` 都只有 `WebPage` 与 `SoftwareApplication`，没有 `FAQPage`，因此可见问答尚未进入结构化数据。
- 修改要求：在每页现有 JSON-LD `@graph` 中各增加一个 `FAQPage` 节点，不新增第二套互相重复的 FAQ 数据。`FAQPage` 使用该页 canonical 加 `#faq` 作为 `@id`，`mainEntity` 按可见手风琴顺序包含以下五个 `Question`；每个问题只包含一个 `acceptedAnswer`，答案使用纯文本并与页面完全一致：

  1. `https://vidou.ai/image-to-video/`
     - `Does this workspace require an account?` → `Yes. The advanced workspace requires you to sign in before uploading and generating.`
     - `Which image formats are supported?` → `The current upload control accepts JPEG, PNG, and WebP images.`
     - `What should I describe in an image to video prompt?` → `Describe what should move, how the camera should move, the pace of the shot, and any details that must remain stable. Avoid repeating everything already visible in the source image unless a detail needs special protection.`
     - `How can I reduce unwanted movement?` → `Ask for one clear action and one camera move. State which face, logo, product shape, or background detail must stay stable, then review the first and last frames for drift or sudden changes.`
     - `How are credits handled?` → `The interface shows the required credits before generation. Review the displayed amount before starting, and visit the Pricing page when you need to compare available credit packages.`

  2. `https://vidou.ai/text-to-video/`
     - `Does text to video require an account?` → `Yes. You need to sign in before generating in this workspace.`
     - `How long is the current output?` → `The current duration shown in the workspace is 5 seconds.`
     - `What should a text to video prompt include?` → `Include a clear subject, one main action, the setting, camera framing or movement, lighting and mood, and the desired pace. Keep every instruction focused on the same moment.`
     - `Should I describe more than one scene in a prompt?` → `Use one concise moment per generation. Several unrelated scenes can make the subject, motion, and camera direction harder to interpret. Generate separate shots when the idea needs multiple scenes.`
     - `How do I check the credit cost?` → `Review the credit requirement displayed in the interface before you generate.`

  3. `https://vidou.ai/text-to-image/`
     - `Does text to image require an account?` → `Yes. You need to sign in before generating in this workspace.`
     - `How do I choose an aspect ratio?` → `Choose 1:1 for square placements, 9:16 or 3:4 for vertical layouts, and 16:9 or 4:3 for horizontal scenes. Decide where the image will appear before generating so the subject has enough space.`
     - `How should I structure a prompt?` → `Start with the subject, then add the setting, composition, lighting, visual mood, and important details.`
     - `What should I review after generation?` → `Check the subject, hands, faces, text, object edges, reflections, shadows, and background details. Revise one prompt element at a time when the result needs correction.`
     - `How are credits handled?` → `The interface shows the required credits before generation. Review that amount before you start.`

  4. `https://vidou.ai/image-edit/`
     - `Does the image editor require an account?` → `Yes. You need to sign in before uploading and generating an edit.`
     - `Which image formats are supported?` → `The current upload control accepts JPEG, PNG, and WebP images.`
     - `Should I request several edits at once?` → `Start with one main change. Add only the preservation and background constraints needed for that change, then make another edit separately if the image needs a second transformation.`
     - `How do I tell the editor what to preserve?` → `Name the subject features, object shapes, background elements, camera angle, or lighting that should remain unchanged.`
     - `How are credits handled?` → `Review the credit requirement displayed in the interface before you generate the edit.`

  结构化数据与可见 FAQ 必须由同一份页面数据生成，避免以后只更新其中一处。保留当前 `WebPage` 和 `SoftwareApplication` 节点，不改变它们的字段。
- 验收标准：四个 URL 各只有一个有效的 `FAQPage` 节点，`@id` 分别为对应 canonical 加 `#faq`；每个节点恰好包含五个 `Question`，顺序、问题和答案均与线上可见手风琴逐字一致；Schema.org validator 能解析全部节点且无 JSON 语法错误、重复 `@id` 或空答案。现有 `WebPage`、`SoftwareApplication`、canonical、Title 和 Meta 保持有效；FAQ 第一项仍默认展开，其余收起，所有按钮继续具备正确的 `aria-expanded`、`aria-controls`、可见键盘焦点和关联面板。
- 不要修改：不要修改 FAQ 可见文案、顺序、展开行为、工具表单、API、账户、credits、格式、比例、分辨率、时长、Audio、图片、Title、Meta 或 canonical；页面正文与导航只允许执行本文件下一项已批准任务规定的修改，除此之外不要改动；不要新增虚构的价格、评分、评论、Offer、HowTo、测试结果或 Google 富媒体展示保证；不要给可见功能名称增加连字符。

### 为四个工具页增加相关工具推荐、结尾 CTA 和全站页脚

- 优先级：`P1`
- 页面或界面：`https://vidou.ai/image-to-video/`、`https://vidou.ai/text-to-video/`、`https://vidou.ai/text-to-image/`、`https://vidou.ai/image-edit/`
- 当前问题与线上证据：2026-10-05 线上四页的主内容均在 FAQ 手风琴后直接结束；没有正文内的相关工具推荐、没有引导用户返回当前工具表单的结尾 CTA，也没有 Blog 页面已经使用的全站页脚。桌面端虽然有工具侧边栏，但它只承担主导航；移动端用户读到页面底部后缺少清晰的下一步和法律、公司、资源入口。现有正文内链也不均衡：Text to Video 只有一条指向 Image to Video 的上下文链接，Text to Image 与 Image Editor 没有正文工具内链。
- 修改要求：四页统一按 `FAQ → Explore More AI Tools → 当前工具 CTA → 全站页脚` 的顺序补充页面末尾结构。使用现有黑色、石墨灰和品牌绿色设计语言，不增加新图片，不复制侧边栏样式。具体执行如下：

  1. 在每页 FAQ 后增加 `Explore More AI Tools` 区块，区块导语统一使用：`Continue your workflow with another Vidou tool.` 每页只显示以下两个相关工具，不显示当前页面自身，也不增加第三张卡片：

     - Image to Video：
       - `Text to Video` → `https://vidou.ai/text-to-video/`；说明：`Create a short video from a scene description when you do not have a source image.`
       - `Image Editor` → `https://vidou.ai/image-edit/`；说明：`Make one focused change to an image while naming the details that should stay consistent.`
     - Text to Video：
       - `Image to Video` → `https://vidou.ai/image-to-video/`；说明：`Animate a source image with a motion prompt and selectable output settings.`
       - `Text to Image` → `https://vidou.ai/text-to-image/`；说明：`Create a new image from a clear description, composition, lighting, and visual mood.`
     - Text to Image：
       - `Image Editor` → `https://vidou.ai/image-edit/`；说明：`Make one focused change to an image while naming the details that should stay consistent.`
       - `Image to Video` → `https://vidou.ai/image-to-video/`；说明：`Animate a source image with a motion prompt and selectable output settings.`
     - Image Editor：
       - `Text to Image` → `https://vidou.ai/text-to-image/`；说明：`Create a new image from a clear description, composition, lighting, and visual mood.`
       - `Image to Video` → `https://vidou.ai/image-to-video/`；说明：`Animate a source image with a motion prompt and selectable output settings.`

     每张卡片整体使用一个真实 `<a>` 元素，工具名称位于该链接内部并作为主要可见锚文本；不要给名称和按钮再创建嵌套或重复链接。卡片尾部可以显示非独立链接的方向箭头，但不得使用 `Learn More`、`Click Here` 或只有图标的可访问名称。桌面端两列、移动端单列；整卡具有可见 hover 与 `focus-visible` 状态，键盘 Tab 顺序与视觉顺序一致。

  2. 在相关工具区块之后增加当前页面专属的结尾 CTA。CTA 是独立区块，包含以下精确英文文案：

     - Image to Video：
       - Heading：`Ready to Create Your Video?`
       - Body：`Upload an image, describe one clear motion, and choose the output settings that fit your project.`
       - Button：`Create Your Video From an Image`
     - Text to Video：
       - Heading：`Ready to Turn Your Idea Into a Video?`
       - Body：`Describe one scene, choose the format, and generate a short video from your prompt.`
       - Button：`Create a Video From Text`
     - Text to Image：
       - Heading：`Ready to Create an Image From Text?`
       - Body：`Describe the subject, composition, lighting, and visual mood you want to explore.`
       - Button：`Create Your Image From Text`
     - Image Editor：
       - Heading：`Ready to Edit Your Image?`
       - Body：`Upload an image, describe one focused change, and preserve the details that matter.`
       - Button：`Edit Your Image`

     给每页现有工具表单外层增加稳定的 `id="tool"`，CTA 按钮使用同页 `href="#tool"`，不跳转首页或其他工具页。点击后滚动到当前工具表单；使用 `scroll-margin-top` 避免标题被固定导航遮挡。不得在 CTA 中增加 `Free`、`No Login`、无限生成、速度、质量或结果保证。CTA 链接必须是可键盘操作的真实链接，并具有可见焦点状态。

  3. 在 CTA 后为四页增加与现有 Blog 页一致的全站页脚布局，但使用以下精确结构与文案：

     - 品牌区：Vidou Logo 链接 `https://vidou.ai/`；说明 `AI tools for creating videos, images, and focused image edits.`
     - `Product`：`Image to Video`、`Text to Video`、`Text to Image`、`Image Editor`，分别链接现有四个 canonical URL。
     - `Resources`：`Blog` → `https://vidou.ai/blog/`；`FAQ` → `https://vidou.ai/#faq`；`Pricing` → `https://vidou.ai/pricing/`。
     - `Company`：`About` → `https://vidou.ai/about/`。
     - `Legal`：`Privacy Policy` → `https://vidou.ai/privacy-policy/`；`Terms of Service` → `https://vidou.ai/terms-of-service/`；`Cookie Policy` → `https://vidou.ai/cookie-policy/`。
     - 底部版权：`© 2026 Vidou. All rights reserved.`

     页脚应复用一个共享组件和同一份链接配置，不为四页复制四套独立实现。当前页面对应的 Product 链接可使用 `aria-current="page"`，但仍保持正常可访问链接。桌面端使用紧凑多列布局，移动端按品牌、Product、Resources、Company、Legal 的顺序折叠为单列或双列；不得做成第二套固定侧边栏，也不得遮挡现有客服按钮。

- 验收标准：四个工具页均按 `FAQ → Explore More AI Tools → 当前工具 CTA → Footer` 显示，且每页恰好有两张指定的相关工具卡片；每张卡片只有一个链接元素，整卡可点击，工具名称是清晰锚文本，键盘焦点可见。四个 CTA 使用指定文案，均只滚动到当前页面 `#tool` 表单，不跳转首页、不打开新标签，也不宣称免费或无需登录。四页均出现相同信息架构的全站页脚，所有 Product、Resources、Company 和 Legal 链接返回 200 或正确锚点；当前页可用 `aria-current="page"` 识别。桌面端 1280px、平板端 768px 和移动端 390px 均无横向滚动、卡片裁切、文字重叠或客服按钮遮挡；现有侧边栏、移动导航、工具表单和 FAQ 键盘操作继续正常。
- 不要修改：不要改变工具表单字段、登录流程、API、credits、格式、比例、分辨率、时长、Audio、生成逻辑、`My Creations`、现有正文、图片、FAQ 文案、Title、Meta 或 canonical；结构化数据只允许执行本文件上一项已批准任务规定的修改，除此之外不要改动；除本任务列出的八张相关工具卡片、四个同页 CTA 和页脚链接外，不要新增其他工具内链、外链、弹窗、自动滚动、追踪代码、动画背景或第三方内容；不要给可见功能名称增加连字符。
