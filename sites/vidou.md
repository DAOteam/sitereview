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

### 归并旧版 `/pro/` 并将 About 纳入当前站点结构

- 优先级：`P1`
- 页面或界面：`https://vidou.ai/pro/`、`https://vidou.ai/about/`、全站导航、页脚、`https://vidou.ai/sitemap.xml`
- 当前问题与线上证据：`/pro/` 仍公开返回 200，并展示旧版 Image to Video 界面、固定 `10` Credits、720p 和 7 天保留；当前导航的 `Pro Version` 却指向 `/image-to-video/`，该页提供 480p、720p、1080p 等另一套界面。`/about/` 同样使用旧视觉，Logo 还链接回 `/pro/`，宣称 `15+ creative video effects` 等未在当前主导航呈现的能力。两个页面均未列入 sitemap，却仍可被搜索引擎发现，形成重复索引、产品能力和积分规则冲突。
- 修改要求：将 `/pro/` 永久 301 重定向到当前规范页 `https://vidou.ai/image-to-video/`，删除旧页面的独立可索引输出和所有指向 `/pro/` 的站内链接。使用当前站点的 Header、Footer、字体、颜色和响应式布局重建 `/about/`，只介绍当前四个公开工具与首页免费工具，不保留无法在线验证的 `15+ creative video effects` 等数量承诺；Logo 必须回到 `/`，并在页脚 Company 区加入 About 链接。把 `/about/` 以带尾斜杠的 Canonical URL 加入 sitemap；把 sitemap 中 `/blog`、文章和三个法律页的无尾斜杠 URL 全部改成对应自引用 Canonical URL，并把所有 `lastmod` 更新为各页面实际内容发布日期。
- 验收标准：请求 `/pro/` 只发生一次 301 并最终到达 `/image-to-video/`；站内抓取不到任何指向 `/pro/` 的链接；`/about/` 与当前站点视觉和导航一致，Title、Meta Description、H1、自引用 Canonical、Open Graph 和 Twitter 卡片齐全；sitemap 仅列最终返回 200 的 Canonical URL，不依赖 301，且 `lastmod` 与实际发布记录一致；Google 等现有旧链接访问者不会进入旧版生成器。
- 不要修改：不要把旧版积分数、分辨率或效果数量迁移到当前工作区；不要重定向其他四个工具页；不要删除 `/about/`。

### 修复博客文章的年份冲突与正文格式

- 优先级：`P2`
- 页面或界面：`https://vidou.ai/blog/`、`https://vidou.ai/blog/ai-image-to-video-guide/`
- 当前问题与线上证据：博客列表卡片标题仍为 `Complete Guide to AI Image to Video Generation in 2025`，详情页 Title 与 H1 却改成 `2026`，同时可见发布日期仍为 `January 15, 2025`。正文 `Key Benefits` 段落直接显示 `**Speed and Efficiency**` 等 Markdown 标记，而不是语义化的加粗列表；文章还继续使用 `completely free`、`in just seconds` 等已与积分工作区冲突的绝对承诺。
- 修改要求：列表卡片、详情页 Title、H1、Open Graph、Twitter 卡片和 Article JSON-LD 统一使用不带年份的标题 `Complete Guide to AI Image to Video Generation`；保留真实首次发布日期 `January 15, 2025`，只有在正文确有实质更新时才增加真实的 `dateModified`。将 `Key Benefits` 的五项内容改为语义化有序列表，每项使用 `<strong>` 标题，不在可见正文中输出 Markdown 符号。按当前免费首页工具与积分工作区的边界重写文章中的 `completely free`、`in just seconds` 和无限试用表述，并让结尾 CTA 明确指向对应的免费首页工具。
- 验收标准：博客列表、浏览器 Title、H1、社交分享元数据和 JSON-LD 使用完全相同的无年份标题；页面只显示真实发布日期，`datePublished` 与可见日期一致；正文不再出现原样 `**` 标记，五项 Benefits 对屏幕阅读器呈现为包含五项的列表；文章不再承诺全站完全免费、无限使用或固定秒级生成。
- 不要修改：不要伪造新的发布日期、作者、测试结果、性能数据或搜索排名；不要为消除年份冲突而把旧文章冒充成新发布内容。

### 发布第一篇 Blog `How to Animate a Photo With AI`

- 优先级：`P1`
- 页面或界面：`https://vidou.ai/blog/`、新增页面 `https://vidou.ai/blog/how-to-animate-a-photo-with-ai/`、`https://vidou.ai/sitemap.xml`
- 当前问题与线上证据：当前线上 Blog 尚无专门回答 `how to animate a photo with AI` 操作意图的文章；现有 Complete Guide 主要覆盖 Image-to-Video 的定义、原理、优势和通用场景，不能替代一篇从选择照片到生成、检查和修正结果的分步教程。
- 修改要求：使用现有 Blog 模板逐字发布下面提供的 SEO 字段和英文文章定稿；执行 AI 只负责集成、发布和线上验证，不得研究、扩写、缩写、改写、润色或替换标题、段落、示例、链接、FAQ 与 CTA。若代码或线上产品事实与定稿冲突，停止发布并将冲突返回推荐 AI，不得自行修改内容。`datePublished`、Article JSON-LD 中的发布日期和 sitemap `lastmod` 使用实际发布日期；除这些发布日期字段外，其余内容保持逐字一致。

  **SEO 与发布字段**

  - Slug：`/blog/how-to-animate-a-photo-with-ai/`
  - SEO Title：`How to Animate a Photo With AI: Step-by-Step Guide`
  - Meta Description：`Learn how to animate a photo with AI, write a clear motion prompt, choose the right format, fix common problems, and export your video.`
  - H1：`How to Animate a Photo With AI: Step-by-Step Guide`
  - Canonical：`https://vidou.ai/blog/how-to-animate-a-photo-with-ai/`
  - Open Graph Title：`How to Animate a Photo With AI: Step-by-Step Guide`
  - Open Graph Description：与 Meta Description 逐字一致
  - Twitter Title：与 SEO Title 逐字一致
  - Twitter Description：与 Meta Description 逐字一致
  - Article JSON-LD `headline`：与 H1 逐字一致
  - Article JSON-LD `description`：与 Meta Description 逐字一致
  - 结尾 CTA 链接：`https://vidou.ai/image-to-video/`

  **配图定稿要求**

  本文必须随文章正文一起发布 3 张最终配图。推荐 AI 必须在任务交付执行前提供下列最终图片文件，并让文件与本清单完全一致；执行 AI 只负责放置、发布和验证，不得自行搜索、下载、生成、重绘、替换或改变图片表达。任一最终文件缺失、无法读取或与清单不符时，停止发布并将任务退回推荐 AI。

  1. Hero 图片
     - 文件名：`how-to-animate-a-photo-with-ai-hero.webp`
     - 格式与尺寸：WebP，`1600 × 900`，`16:9`
     - 放置位置：H1 后、第一段正文前
     - 画面用途：原创编辑插画，以一个静态人物或物体照片向短视频运动序列过渡的画面表达“用 AI 让照片动起来”；不嵌入文字、产品界面或第三方 Logo，不把虚构结果冒充真实 Vidou 生成结果。
     - Alt：`Still photo transitioning into an AI-animated video sequence`
  2. 正文图片一
     - 文件名：`best-source-photo-for-ai-animation.webp`
     - 格式与尺寸：WebP，`1200 × 800`，`3:2`
     - 放置位置：`Step 1: Choose a Photo That Is Easy to Animate` 的检查清单之后
     - 画面用途：原创并排教学图，左侧展示主体清楚、背景分离良好的易用照片，右侧展示拥挤、模糊或主体被遮挡的困难照片；只解释源图选择，不声称是实际 Vidou 输出对比。
     - Alt：`Comparison of a clear source photo and a difficult photo for AI animation`
  3. 正文图片二
     - 文件名：`ai-photo-animation-prompt-formula.webp`
     - 格式与尺寸：WebP，`1200 × 675`，`16:9`
     - 放置位置：`Step 4: Write a Clear Motion Prompt` 中三个 Prompt 示例之后
     - 画面用途：原创流程图，清晰呈现 `subject + movement + camera + environment + pace + details to preserve` 六个 Prompt 组成部分；图中文字只能使用这六个英文标签，不加入工具链接或额外 CTA。
     - Alt：`AI photo animation prompt formula with six prompt components`

  三张图片必须为原创或已取得发布权，不得复制竞品图片、使用含隐私信息的账户截图，或使用无法证实的产品效果。输出响应式图片，声明固有宽高以避免布局偏移；Hero 作为潜在 LCP 图片默认不得懒加载，正文图片必须懒加载；压缩后不得出现明显画质损失。发布后将 Hero 的绝对 URL 写入 Article JSON-LD `image`，并在现有模板支持时用于 Open Graph 与 Twitter 图片。

  **英文文章定稿（从 H1 开始逐字发布）**

  ```markdown
  # How to Animate a Photo With AI: Step-by-Step Guide

  You can animate a photo with AI by uploading a still image, describing the movement you want, choosing a suitable output format, and generating a short video. You do not need to draw individual frames or learn traditional animation software. The result depends mainly on the source photo, the clarity of the motion prompt, and how carefully you review the generated video.

  This guide covers the complete workflow: choosing an image, planning one clear movement, writing a useful prompt, selecting a format, reviewing the result, and fixing common problems. If you want a broader explanation of the technology first, read the [complete guide to AI image-to-video generation](https://vidou.ai/blog/ai-image-to-video-guide/).

  ## What Does It Mean to Animate a Photo With AI?

  Animating a photo means turning a still image into a short moving sequence. An image-to-video system examines the subjects, background, composition, lighting, and visual depth of the image. It then uses a written prompt to decide what should move, how quickly it should move, and whether the camera should remain still or move through the scene.

  The generated motion might include a slow camera push toward a subject, hair moving in the wind, water flowing, clouds drifting, lights flickering, or a product receiving a subtle camera reveal. The goal is not to make every part of the image move. One clear subject motion combined with restrained camera movement often creates a more controlled result.

  ## Step 1: Choose a Photo That Is Easy to Animate

  AI can work with many kinds of images, but a clear source photo gives the system fewer details to guess.

  Look for an image with:

  - One obvious main subject
  - Sharp, visible facial or product details
  - Clear separation between the subject and background
  - Enough space around the subject for the intended movement
  - Consistent lighting
  - Limited motion blur
  - Few overlapping hands, objects, or facial features

  Portraits, product photos, landscapes, illustrations, and AI-generated artwork can all be animated. More difficult inputs include crowded group photos, tiny faces, cropped limbs, heavy blur, detailed text, and products partly hidden behind other objects.

  Before uploading, identify the most important part of the photo. If you cannot quickly tell what the video should focus on, choose a clearer crop or a simpler image.

  ## Step 2: Decide on One Main Motion

  Start with one primary action instead of a long list of effects.

  For example:

  - A woman turns her head slightly toward the camera.
  - Ocean waves move gently toward the shore.
  - The camera slowly pushes toward a product.
  - Steam rises from a cup while the background remains still.
  - Clouds drift across the sky.
  - A character's hair moves in a light breeze.

  A focused request gives the system a clear priority. You can add atmosphere or a small camera movement after defining the main action.

  A vague instruction such as "make this photo exciting and cinematic" does not explain what should move. A clearer direction would be:

  > The camera slowly pushes toward the subject while her hair moves gently in the wind. Keep her face and the background stable.

  This version identifies the subject, motion, camera behavior, pace, and the details that should remain unchanged.

  ## Step 3: Upload the Image

  Open Vidou's Image-to-Video workspace and choose the photo you want to animate. The current interface accepts JPEG, PNG, and WebP images.

  Use the original image when possible instead of a compressed screenshot or a file repeatedly downloaded from social media. Before continuing, check that:

  - The image appears in the correct orientation.
  - The main subject is not accidentally cropped.
  - Important faces, logos, labels, and product details remain visible.
  - The image has a similar shape to the planned video format.

  A horizontal photo usually adapts more naturally to a horizontal video. Turning a tightly framed horizontal image into a vertical video may require cropping or the generation of background areas that were not present in the original.

  ## Step 4: Write a Clear Motion Prompt

  A useful prompt can follow this formula:

  **Subject + movement + camera + environment + pace + details to preserve**

  Portrait example:

  > The woman looks toward the camera and blinks naturally. Her hair moves in a light breeze. Slow camera push-in, soft daylight, and subtle motion. Keep her face and the background consistent.

  Product example:

  > Slow camera movement around the sneaker. Gentle studio light moves across the surface. Keep the shoe shape, logo, colors, and background unchanged.

  Landscape example:

  > Clouds drift slowly above the mountains while the lake shows subtle movement. Static camera, calm atmosphere, and a natural pace.

  Avoid combining several unrelated actions in one prompt. A request to rotate the camera, transform the subject, replace the weather, move the background, and add new objects forces the system to make too many decisions at once. Begin with the most important motion and add complexity only after reviewing a simpler result.

  **Ready to try the workflow? Keep the prompt focused on one visible action, then use the review checklist below before making another version.**

  ## Step 5: Choose the Right Aspect Ratio and Output

  Choose an aspect ratio based on where the finished video will appear:

  - **9:16** for TikTok, Instagram Reels, and YouTube Shorts
  - **16:9** for YouTube, presentations, and website banners
  - **1:1** for square social posts and product grids
  - **4:3** for traditional presentation and editorial layouts
  - **3:4** for portrait-oriented posts and product content

  The signed-in workspace currently displays 480p, 720p, and 1080p resolution choices. Select an output appropriate for its destination, but remember that a higher output setting cannot restore details missing from the original photo.

  Whenever possible, begin with an image whose orientation already resembles the intended video. This reduces the need for aggressive cropping or generated areas around the frame.

  ## Step 6: Generate and Review the Entire Frame

  Generate the video and watch it more than once. Do not look only at the main subject.

  Check:

  - Facial features
  - Hands and fingers
  - Product shape
  - Logos and labels
  - Edges of clothing or hair
  - Background objects
  - Reflections and shadows
  - The first and final frames
  - Sudden flicker or color changes

  A convincing main movement can still be accompanied by a distracting error near the edge of the frame. Review the video at full size before publishing or placing it in a campaign.

  ## Step 7: Improve One Variable at a Time

  If the first result is not right, avoid rewriting the entire prompt immediately. Change one element so you can see what affected the output.

  Useful adjustments include:

  - Reduce the amount of movement.
  - Remove a secondary action.
  - Replace words such as "dramatic" with a specific camera direction.
  - Ask for a static background.
  - Use "subtle," "slow," or "gentle" to control intensity.
  - Name the details that must remain unchanged.
  - Choose a source image with clearer subject separation.
  - Select an aspect ratio closer to the original image.

  Changing one variable at a time turns each generation into a controlled revision rather than a random restart.

  ## Common Problems and How to Fix Them

  ### The Face Changes or Becomes Distorted

  Use smaller facial movements. Replace a full head turn or a large expression change with blinking, a slight smile, or a subtle shift in gaze.

  Add a constraint such as:

  > Preserve facial identity and proportions. Use minimal head movement.

  A clear, front-facing portrait usually gives the system more usable facial information than a small, blurred, or partly hidden face.

  ### The Background Keeps Changing

  State what should remain still:

  > Static background. Keep all buildings, signs, and background objects unchanged.

  You can also reduce camera movement. A large orbit or pan requires the system to create areas that are not visible in the original photo.

  ### The Product Shape, Logo, or Label Changes

  Use a sharp source image and request restrained movement:

  > Slow camera push-in. Keep the product shape, logo, label, colors, and packaging unchanged.

  Avoid requesting a complete product rotation when the source image only shows one side. The system does not have reliable visual information for hidden surfaces.

  ### The Motion Is Too Weak

  Replace broad instructions with a visible action. Instead of "bring the image to life," write:

  > Leaves move gently from left to right while sunlight flickers through the branches.

  One precise action is usually easier to interpret than several abstract adjectives.

  ### The Result Feels Too Busy

  Remove secondary effects. Keep either the subject motion or the camera motion simple. Use a static camera while the subject moves, or use a slow camera push while the subject remains mostly still.

  ## A Reusable Prompt Template

  Use this structure as a starting point:

  > [Main subject] [specific movement]. [Camera direction]. [Environmental movement]. [Pace and mood]. Keep [important details] unchanged.

  Example:

  > The cyclist looks toward the road while her jacket moves slightly in the wind. Slow camera push-in. Trees move gently in the background. Natural pace and soft morning light. Keep her face, bicycle, and clothing consistent.

  This template is not a guarantee of a perfect result. It gives the system a clearer hierarchy: what should move, how the scene should be filmed, and what must remain stable.

  ## Frequently Asked Questions

  ### Can I animate an old family photo?

  Yes, provided you have permission to use the image. Begin with subtle movements such as blinking, breathing, a small smile, or a gentle camera push. Large facial or body movements are more likely to alter identity or introduce visible artifacts.

  ### What types of photos are easiest to animate?

  Photos with one clear subject, visible edges, good lighting, and an uncluttered background are usually easier to control. Portraits, products, landscapes, and illustrations can all work when the intended motion is specific.

  ### Do I need to write a long prompt?

  No. A short prompt with one precise action is often more useful than a long prompt containing competing instructions. Add camera movement, atmosphere, and preservation constraints only when they support the main action.

  ### Which image formats can I upload to Vidou?

  The current Vidou interface supports JPEG, PNG, and WebP images.

  ### Why can the result look different between attempts?

  Image-to-video generation can interpret the same image and prompt differently between attempts. Keep the source image and settings unchanged while adjusting one prompt element at a time. This makes it easier to identify which instruction changed the result.

  ### Can I animate a product photo?

  Yes. Use a sharp image, keep the requested movement restrained, and explicitly ask the system to preserve the product's shape, logo, label, colors, and packaging.

  ## Animate Your First Photo

  A successful photo animation starts with three decisions: choose a clear image, describe one visible movement, and identify the details that must remain unchanged.

  Start simple. Review the entire frame. Then refine one instruction at a time.

  [**Animate Your Photo With Vidou**](https://vidou.ai/image-to-video/)
  ```
- 验收标准：新增 URL 直接返回 200；Title、H1、Meta Description、Canonical、社交元数据和 Article JSON-LD 与指定内容一致；正文为 1,200–1,800 个英文词，完整呈现可执行步骤、示例、限制、失败情形和 FAQ；页面只有 1 个工具页内链且位于结尾 CTA，Complete Guide 内链可访问，没有虚构的后续文章链接；三张指定图片均在准确位置正常显示，文件名、格式、尺寸、画面用途和 Alt 与清单一致，Hero URL 已写入 Article JSON-LD `image`，图片具有响应式候选与明确宽高，Hero 未默认懒加载且正文图片已懒加载，桌面与移动端无明显布局偏移；sitemap 包含该 Canonical URL，`datePublished` 和 `lastmod` 为真实发布日期；文章不与主页、`/image-to-video/` 或现有 Complete Guide 争夺相同主要意图。
- 不要修改：不要修改主页、现有 Complete Guide 或工具页正文；不要增加第二个工具页内链；不要让执行 AI 自行找图、生成图或替换配图，不要复制竞品图片、使用未授权第三方素材、隐私截图、文字堆叠的通用 AI 图或虚假前后对比；不要声称 Vidou 具备未在线验证的功能，不要承诺无限免费、固定生成速度、结果质量、排名、流量或转化提升；不要伪造作者、测试、用户结果或发布日期；不要为本篇普通 Blog 发布添加公开产品更新日志。

### 补全四个工具表单的可访问名称与状态反馈

- 优先级：`P2`
- 页面或界面：`https://vidou.ai/image-to-video/`、`https://vidou.ai/text-to-video/`、`https://vidou.ai/text-to-image/`、`https://vidou.ai/image-edit/`
- 当前问题与线上证据：公开无障碍树中，四页的 Prompt 输入均只暴露为无名称的 `text entry area`；Image to Video 的 Audio 控件暴露为无名称按钮，上传区、登录要求、积分变化和禁用生成按钮之间也缺少程序化关联。工具名称还在同一页连续重复为 H1 和 H2，降低标题层级的可读性。
- 修改要求：为每个 Prompt 使用可见 `<label>` 并通过 `for`/`id` 关联输入框；为上传控件提供可聚焦按钮、支持格式说明和可访问的错误反馈；为 Audio、Aspect Ratio、Duration、Resolution 提供明确的控件名称、选中状态和分组说明。使用 `aria-describedby` 将登录要求、积分消耗、格式限制和错误信息关联到相关输入或生成按钮，并用 `aria-live="polite"` 宣布积分和校验状态变化。每页只保留一个描述当前工具的 H1，把表单卡片内的重复标题降为非标题文本或改成描述具体步骤的 H2；补全可见键盘焦点样式，确保 Tab 顺序与视觉顺序一致。
- 验收标准：浏览器无障碍树中每个输入、上传按钮、Audio 开关、参数组和生成按钮都有唯一且可理解的名称；只用键盘即可完成所有非文件内容输入、设置切换和登录跳转；错误、积分变化和禁用原因会被屏幕阅读器宣布；每页恰好一个 H1，标题层级不跳级；桌面和移动布局中焦点不被遮挡。
- 不要修改：不要改变生成参数的可选值、默认值、计费、模型或上传格式；不要用仅靠 placeholder 的方式替代 label。

### 增加公开页面的基础安全响应头

- 优先级：`P2`
- 页面或界面：`https://vidou.ai/` 及所有同域公开 HTML 页面
- 当前问题与线上证据：当前 HTTPS 响应已包含 HSTS，但首页、工具页、Pricing 和法律页均未返回 `Content-Security-Policy`、`X-Content-Type-Options`、`Referrer-Policy`、`Permissions-Policy` 或 `X-Frame-Options`；全站同时加载同域资源和 `https://hepo.ai/w/g3np5gzd.js`，缺少资源来源与嵌入边界会放大第三方脚本或注入问题的影响范围。
- 修改要求：先以 `Content-Security-Policy-Report-Only` 覆盖首页、四个工具页、Pricing、Blog、About 和法律页，按实际资源逐项收敛到 `'self'` 与经过核验的必要来源；清除违规后切换为强制 `Content-Security-Policy`。至少设置 `default-src 'self'`、禁止对象资源、限制 `base-uri`、限制表单提交目标，并使用 `frame-ancestors 'none'`；为客服脚本只开放其实际需要的最小来源。同步返回 `X-Content-Type-Options: nosniff`、`Referrer-Policy: strict-origin-when-cross-origin` 和禁止未使用摄像头、麦克风、地理位置能力的 `Permissions-Policy`；继续保留现有 HSTS。
- 验收标准：所有公开 HTML 的 200 响应均返回强制 CSP、`nosniff`、`strict-origin-when-cross-origin` 和预期 Permissions Policy；CSP 不包含 `*`，不为解决问题而新增宽泛的 `unsafe-eval`，且 `frame-ancestors 'none'` 生效；首页视频、图片、四个工具页、登录入口、Pricing、Blog 和 Hepo 客服在桌面与移动端无 CSP 阻断错误；现有 HSTS 仍为 `max-age=31536000` 或更严格值。
- 不要修改：不要禁用 HTTPS、HSTS、客服或现有核心资源；不要把开发域、localhost、未使用第三方域或通配符加入生产策略。
