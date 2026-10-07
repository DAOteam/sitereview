---
site_id: "vidou"
name: "Vidou"
production_url: "https://vidou.ai/"
changelog_url: "not_established"
delivery_method: "not_established"
target_repository: "not_established"
default_branch: "not_established"
updated_at: "2026-10-07"
---

# Vidou 当前待办事项

## 已批准任务

### 将工具页导航中的 Credits 改为 Pricing

- 优先级：`P2`
- 页面或界面：`https://vidou.ai/image-to-video/`、`https://vidou.ai/text-to-video/`、`https://vidou.ai/text-to-image/`、`https://vidou.ai/image-edit/` 的桌面左侧导航和移动端导航
- 当前问题与线上证据：2026-10-05 使用禁止缓存请求复核，四个工具页的导航均把指向 `https://vidou.ai/pricing/` 的入口显示为 `Credits`。目标页面实际是完整 Pricing 页面，包含 credits 套餐与购买信息，因此导航名称使用 `Pricing` 更准确，也与 Blog 页脚和工具页新 Footer 中的 `Pricing` 保持一致。
- 修改要求：将四个工具页桌面左侧导航和移动端导航中指向 `https://vidou.ai/pricing/` 的可见名称从 `Credits` 精确替换为 `Pricing`。若桌面和移动端复用同一导航配置，只修改共享配置一次；同时把该链接的 `aria-label`、title、屏幕阅读器专用文本或其他可访问名称中的 `Credits` 同步改为 `Pricing`。保持现有图标、位置、样式、链接目标、点击行为和激活状态不变。
- 验收标准：四个工具页的桌面左侧导航和移动端导航都只显示 `Pricing`，不再出现作为菜单名称的 `Credits`；对应链接仍为 `https://vidou.ai/pricing/`，可通过鼠标、触摸和键盘正常打开；可访问名称与可见名称均为 `Pricing`；页面 Footer 中现有 `Pricing` 链接继续正常。桌面与 390px 移动端无文字截断、换行、重叠或导航宽度异常。
- 不要修改：不要修改 Pricing 页面内容、credits 数量、套餐、价格、支付流程、URL、图标、菜单顺序、其他导航名称、工具表单、API、账户逻辑、Title、Meta、canonical、正文、CTA、Footer 或结构化数据；不要把正文和产品界面中表示计费单位的普通名词 `credits` 改为 `pricing`；不要给可见功能名称增加连字符。

### 发布博客文章 How to Turn Product Photos Into Videos With AI

- 优先级：`P1`
- 页面或界面：新文章 `https://vidou.ai/blog/turn-product-photos-into-videos-with-ai/`、Blog 列表页 `https://vidou.ai/blog/`、旧文章 `https://vidou.ai/blog/how-to-animate-a-photo-with-ai/`、XML Sitemap
- 当前问题与线上证据：2026-10-07 使用禁止缓存请求复核，目标文章 URL 当前显示 Vidou 的 404 页面，Blog 列表页尚无这篇计划中的第三篇文章。线上已有入门流程文 `How to Animate a Photo With AI` 和提示词文章 `Image to Video Prompt Guide`，但缺少面向产品照片、覆盖素材准备、保真运动、输出选择和成片检查的商业场景文章。高级工具页 `https://vidou.ai/image-to-video/` 当前公开提供 9:16、4:3、3:4、1:1、16:9 比例，480p、720p、1080p 分辨率，5 秒时长、可选音频、credits 提示和登录后保存创作记录，适合作为本文唯一工具目的地。
- 修改要求：
  1. 新建并发布下方已定稿的英文文章，不得让发布执行方改写、缩写、扩写或另行生成正文。文章 URL、SEO 字段和页面信息精确使用：
     - URL：`https://vidou.ai/blog/turn-product-photos-into-videos-with-ai/`
     - Slug：`turn-product-photos-into-videos-with-ai`
     - SEO Title：`How to Turn Product Photos Into Videos With AI | Vidou`
     - Meta Description：`Learn how to turn product photos into short AI videos with controlled motion, clear prompts, suitable formats, and a practical review checklist.`
     - H1：`How to Turn Product Photos Into Videos With AI`
     - Category：`Guide`
     - Author：可见署名为 `Vidou`，链接到 `https://vidou.ai/about/`
     - Publish date：`October 7, 2026`；机器可读值为 `2026-10-07`
     - Reading time：`9 min read`
     - Canonical：`https://vidou.ai/blog/turn-product-photos-into-videos-with-ai/`
     - Open Graph：`og:type=article`；`og:title` 与 H1 一致；`og:description` 与 Meta Description 一致；`og:url` 与 canonical 一致；`og:image=https://vidou.ai/images/blog/turn-product-photos-into-videos-with-ai-hero.jpg`；图片尺寸为 1536×864。
  2. 文章顶部使用主图，正文在 `Start With a Product Photo That Leaves Room for Motion` 小节两段正文之后使用第二张图。把仓库内已生成的最终图片集成到站点静态资源体系，并生成现有图片组件所需的 768px 宽响应式版本；不得重新生成或用占位图替换：
     - 本地源文件：`assets/vidou-blog/turn-product-photos-into-videos-with-ai/turn-product-photos-into-videos-with-ai-hero.jpg`；发布 URL：`https://vidou.ai/images/blog/turn-product-photos-into-videos-with-ai-hero.jpg`；尺寸：1536×864；Alt：`Olive running shoe with subtle motion trails illustrating a product photo becoming a video`；作为文章 Hero、Open Graph 图和 Blog 列表卡片图。
     - 本地源文件：`assets/vidou-blog/turn-product-photos-into-videos-with-ai/product-photo-motion-planning.jpg`；发布 URL：`https://vidou.ai/images/blog/product-photo-motion-planning.jpg`；尺寸：1536×864；Alt：`Unbranded amber bottle photographed with clear edges and space for AI video motion`；Caption：`A clean silhouette, stable reflections, and space around the subject give the motion model fewer details to reinterpret.`
     - 两张图片均由 OpenAI ImageGen 于 2026-10-07 为本文生成。不得宣称它们是 Vidou 的真实生成结果、客户素材或产品测试结果。文章末尾保留正文中的 Editorial note 披露。
  3. 正文中的工具链接必须严格只有两个，且都指向同一 URL `https://vidou.ai/image-to-video/`：第一处是正文唯一锚文本 `advanced Image to Video workspace`，第二处是末尾按钮 `Turn Your Product Photo Into a Video`。不要给图片、标题、其他关键词或中段过渡 CTA 添加工具链接。正文内 `Image to Video` 等可见功能名称不得添加连字符；URL slug 中的技术连字符保持不变。
  4. 按照现有 Blog 文章视觉与组件样式发布以下定稿正文：

```markdown
# How to Turn Product Photos Into Videos With AI

One strong product photo can become a short video without a full reshoot. The practical method is to begin with a clean source image, choose one believable motion idea, describe what should move and what must remain unchanged, then review the result for product accuracy before using it in a campaign.

This workflow is useful for product pages, social posts, launch teasers, marketplace creative, and concept testing. It does not replace careful product photography, and an AI video should not be treated as an exact simulation of how a product works. Its value is speed: a still asset can gain camera movement, light, atmosphere, or subtle environmental motion while the product remains the visual anchor.

If you are new to the format, start with the broader [guide to AI image to video generation](https://vidou.ai/blog/ai-image-to-video-guide/). The steps below focus specifically on product imagery, where shape, color, packaging, and readable details matter more than dramatic motion.

## Decide Where the Video Will Be Used

Choose the placement before you animate the image. A vertical social story, a square marketplace post, and a wide website banner need different framing. Making that decision first helps you choose a source photo with enough space around the product and prevents an important detail from being cropped later.

Write down three constraints before you begin:

- **Placement:** product page, paid social concept, organic post, email, or presentation.
- **Frame:** vertical, square, portrait, or landscape.
- **Single purpose:** reveal the product, show its material, create atmosphere, or draw attention to one feature.

Keep the first version simple. A five second clip with one clear visual purpose is easier to control than a scene that tries to rotate the product, change the background, add particles, move the camera, and reveal text at the same time.

## Start With a Product Photo That Leaves Room for Motion

The source image determines how much the model must invent. Use a sharp image in which the complete product is visible, the silhouette is easy to separate from the background, and important details are not hidden by props. The product should occupy enough of the frame to remain recognizable without touching every edge.

Leave breathing room in the direction of the intended movement. A slow push in needs space around the subject for reframing. A lateral camera move benefits from background detail on both sides. For a vertical output, begin with a composition that can survive a tall crop rather than forcing a wide hero image into a narrow frame.

![Unbranded amber bottle photographed with clear edges and space for AI video motion](https://vidou.ai/images/blog/product-photo-motion-planning.jpg)

*A clean silhouette, stable reflections, and space around the subject give the motion model fewer details to reinterpret.*

Packaging deserves extra care. Small type, logos, repeating patterns, transparent materials, and mirror-like surfaces are easy to reinterpret. Verify critical label or legal copy against the original still. If text must remain exact, composite it after generation instead of asking the model to recreate it through motion.

## Choose One Product Safe Motion Idea

The most dependable concepts let the product stay structurally stable while the camera, light, or environment provides movement. Start with one of these approaches:

| Motion idea | What moves | Best suited to |
| --- | --- | --- |
| Slow push in | The camera moves gently toward the product | Packaging, footwear, accessories, hero shots |
| Subtle orbit | The camera shifts slightly around a stable subject | Products with a clear three dimensional form |
| Light sweep | Highlights travel across the surface | Metal, glass, watches, cosmetics |
| Background drift | Shadows, fabric, steam, or particles move behind the product | Lifestyle and atmospheric creative |
| Focus transition | Attention shifts from a foreground detail to the product | Detail led reveals and premium compositions |

Avoid asking for a complete spin when the source photo shows only one side. The unseen back and side must be invented, so packaging geometry, soles, clasps, ports, and labels may change. If a full rotation is essential, use real multiview product assets or a controlled 3D workflow.

Natural motion is usually restrained. Ask for a slow camera move rather than a fast sweep. Let reflections slide across a bottle rather than changing the bottle itself. The product should remain the fixed reference point.

## Write a Prompt That Protects Product Identity

A useful product prompt separates four things: the subject, the motion, the camera, and the constraints. Put the product first, describe one primary action, state the pace and framing, then say what must stay consistent.

Use this reusable pattern:

> Keep the [product, color, material, and position] unchanged. [One camera or environmental motion] happens slowly. [Lighting and atmosphere]. Maintain the original shape, proportions, colors, label placement, and background style. No new objects, no deformation, no text changes, and no sudden camera movement.

Here are two examples you can adapt.

### Running shoe

> Keep the olive running shoe centered on the pedestal. The camera makes a slow push in while a soft highlight travels across the mesh and sole. Maintain the exact silhouette, laces, material texture, colors, and proportions. No foot, no new branding, no rotation, and no shape changes.

### Skincare bottle

> Keep the amber glass bottle upright and unchanged. Warm window shadows drift slowly across the background while the camera remains steady. Preserve the bottle geometry, cap, label position, glass color, reflections, and surface. No added text, no liquid movement, and no new props.

Notice that each prompt says more about restraint than spectacle. Product video prompts work best when they reduce ambiguity. If you want a deeper explanation of subject, motion, camera, environment, and constraints, use the [Image to Video prompt guide](https://vidou.ai/blog/image-to-video-prompt-guide/).

## Generate a Controlled First Version

Upload the chosen still to Vidou's [advanced Image to Video workspace](https://vidou.ai/image-to-video/). Choose the aspect ratio that matches the planned placement, select an available resolution, decide whether the clip needs audio, and paste the prompt. The workspace currently offers 9:16, 4:3, 3:4, 1:1, and 16:9 formats, 480p, 720p, and 1080p output options, and a five second duration. It also shows the credit requirement before generation and keeps creations available in a signed in account.

Treat the first result as a controlled draft. Change only one variable per revision. If the product bends, strengthen the identity constraints. If the scene feels static, add one subtle camera or lighting action. If motion becomes chaotic, remove secondary effects rather than stacking more instructions onto the prompt.

## Review the Entire Clip, Not Just the First Frame

Watch the video several times and pause at the beginning, middle, and end. A result can look convincing at first and still drift near the final frames. Review it against the original product photo, not from memory.

Check the following:

- **Silhouette:** Does the outer shape remain stable throughout the clip?
- **Color and material:** Do the finish, transparency, texture, and reflections stay believable?
- **Packaging:** Do the cap, seams, edges, logo area, and label placement remain consistent?
- **Text:** Has any visible copy changed, blurred, or turned into different characters?
- **Motion:** Does the camera move smoothly without sudden speed or direction changes?
- **Background:** Do shadows and props remain coherent without appearing or disappearing?
- **Crop:** Is the full product visible in the final placement, including interface safe areas?
- **Claims:** Could the motion imply a feature, effect, ingredient behavior, or performance the product does not actually have?

Reject a clip if it misrepresents a material detail or product function, even when the overall motion looks attractive. For commercial use, accuracy is part of creative quality. Keep the original still available wherever a customer needs to inspect precise details.

## Fix Common Product Video Problems

### The packaging changes shape

Reduce camera movement and explicitly preserve the product's geometry, proportions, cap, edges, and label position. A slow push in is usually safer than an orbit when the packaging has strong straight lines.

### The label becomes unreadable

Use a cleaner source with a larger label area and ask the model to keep the label placement unchanged. Do not rely on generated frames for mandatory copy. Add exact typography in post production when perfect readability is required.

### Reflections flicker on glass or metal

Simplify the lighting instruction. Request one soft, controlled light sweep and a stable camera. Multiple moving lights create competing changes and can make the surface appear to reshape.

## Build Variations Without Losing Consistency

Once one version passes review, create variations by changing a single production choice: aspect ratio, camera direction, lighting mood, or background motion. Keep the source photo and identity constraints constant. This produces a coherent family of assets while making differences easy to evaluate.

For example, a wide version might use a slow lateral move for a website banner, while a vertical version uses a gentle push in with more space above and below the product. Both can share the same color, material, label, and geometry constraints. Do not assume one crop will work everywhere; review each format in its actual placement.

## A Practical Product Photo to Video Checklist

Before generation:

1. Confirm the placement and aspect ratio.
2. Choose a sharp source with a clear, complete product.
3. Leave room around the subject for the planned movement.
4. Pick one product safe motion idea.
5. Write explicit identity and text constraints.

Before publishing:

1. Compare the beginning, middle, and end with the source photo.
2. Verify shape, color, material, label placement, and visible text.
3. Check the crop inside the real destination layout.
4. Remove any motion that suggests an unsupported product claim.
5. Keep the original still and approved generation details with the asset.

## Frequently Asked Questions

### What product photos work best for AI video?

Use a sharp, well lit photo with a complete product, a clean silhouette, and space around the subject. Simple backgrounds and stable lighting give the model fewer details to reinterpret. Highly reflective surfaces, tiny text, and overlapping props require closer review.

### Can AI keep a product label perfectly readable?

It may preserve the general label area, but small text can change between frames. If wording must be exact, add it during post production or use the original still for close inspection. Always review generated frames against the source image.

### Which motion is safest for a single product photo?

A slow push in, restrained light sweep, or gentle background movement is usually safer than a full rotation. These choices create motion without requiring the model to invent unseen sides of the product.

### Can I use the result in an advertisement?

You can evaluate it for your campaign, but approval depends on your rights to the source image, brand rules, advertising requirements, and the accuracy of the generated result. Review every frame and do not publish a clip that changes the product or implies unsupported performance.

## Turn One Strong Product Photo Into a Focused Video

The most effective workflow is controlled rather than complicated: choose the destination, prepare a clean source, use one believable motion, protect product identity in the prompt, and inspect the full clip before publishing. Once that foundation works, create channel specific variations one change at a time.

[Turn Your Product Photo Into a Video](https://vidou.ai/image-to-video/)

*Editorial note: The illustrative images in this article were created with AI for editorial explanation. They are not customer assets, product test results, or examples generated by Vidou.*
```

  5. 在 Blog 列表页添加该文章卡片，使用主图、Category `Guide`、标题、Meta Description 的首句摘要、日期 `October 7, 2026`，点击卡片进入 canonical URL；保持现有列表顺序规则，并将本文作为最新文章显示。
  6. 在旧文章 `https://vidou.ai/blog/how-to-animate-a-photo-with-ai/` 的 FAQ 问题 `Can I animate a product photo?` 现有回答末尾追加一句：`For a product focused workflow, read [how to turn product photos into videos with AI](https://vidou.ai/blog/turn-product-photos-into-videos-with-ai/).` 链接文字保持全小写；不要改写该 FAQ 的其他句子。
  7. 加入与现有文章一致的面包屑和结构化数据。使用 `BlogPosting`，字段至少包括：`headline` 为 H1；`description` 为 Meta Description；`image` 为主图绝对 URL；`datePublished` 和 `dateModified` 均为 `2026-10-07`；`mainEntityOfPage` 与 canonical 一致；`author` 与 `publisher` 均为 `Organization`、名称 `Vidou`、URL `https://vidou.ai/about/`。保留站点现有 `WebSite`、`Organization` 或 `BreadcrumbList` 数据，避免重复冲突。
  8. 将 canonical URL 加入线上 XML Sitemap，`lastmod` 使用实际发布日期 `2026-10-07`。确保页面可索引，不添加 `noindex`，并保持正确的 200 状态。
- 验收标准：目标 URL 返回 200 且不是软 404；SEO Title、Meta Description、H1、canonical、Open Graph、作者、发布日期、阅读时长、分类和 `BlogPosting` 数据与要求一致；可见英文正文为上述定稿且正文词数在 1,300–2,000 词范围内；Hero 和正文图在桌面及 390px 移动端清晰显示、比例稳定、无拉伸、无布局偏移，并输出 768px 响应式候选；两图 Alt 和 Caption 精确；正文到 `https://vidou.ai/image-to-video/` 恰好两个链接，其中一个为指定关键词锚文本、一个为末尾 CTA 按钮，不存在第三个工具页或首页转化链接；可见文案中的 `Image to Video` 不含连字符；三条 Blog 内链可点击且无 404；旧文章新增反向链接；Blog 列表有最新文章卡片；Sitemap 包含 canonical；结构化数据通过解析且字段与页面可见信息一致；页面键盘可操作、焦点清晰，图片不会遮挡正文或 CTA。
- 不要修改：不要改写定稿文章、SEO 字段、指定锚文本、CTA、Alt、Caption 或披露；不要把 `Image to Video`、`Text to Video`、`Text to Image`、`Image Edit` 等可见功能名称写成带连字符形式；不要增加第二个正文工具锚文本、首页链接、第三个工具转化链接、外部竞品链接、效果承诺、虚构测试数据、客户案例、品牌或法律结论；不要把生成图描述成 Vidou 输出；不要改动高级工具的功能、选项、credits、登录逻辑、账户数据、API、价格、现有文章正文（除指定的一句反向链接）、其他 Blog 卡片、全站导航、Footer 或无关页面；不要新增 Changelog 条目。
