---
site_id: "vidou"
name: "Vidou"
production_url: "https://vidou.ai/"
changelog_url: "not_established"
delivery_method: "not_established"
target_repository: "not_established"
default_branch: "not_established"
updated_at: "2026-10-19"
---

# Vidou 当前待办事项

## 已批准任务

### 统一 Camera Movements 文章的真实发布日期

- 优先级：`P2`
- 页面或界面：文章 `https://vidou.ai/blog/best-camera-movements-ai-image-to-video/`、Blog 列表页 `https://vidou.ai/blog/`、XML Sitemap
- 当前问题与线上证据：2026-10-18 线上复核确认文章、Blog 卡片、两张响应式图片、两篇旧文反向链接和 Sitemap 条目均已发布，原发布任务的其他要求已经完成。但该文章在 2026-10-18 才实际公开，当前文章可见日期、Blog 卡片日期、`BlogPosting.datePublished`、`BlogPosting.dateModified` 和 Sitemap `lastmod` 仍统一显示 `October 16, 2026` 或 `2026-10-16`，与真实公开日期不一致。
- 修改要求：只把文章可见发布日期和机器可读时间、Blog 列表卡片日期、`BlogPosting.datePublished`、`BlogPosting.dateModified`、Sitemap `lastmod` 统一改为真实发布日期：可见文案使用 `October 18, 2026`，机器可读值使用 `2026-10-18`。
- 验收标准：文章页可见日期与机器可读时间均为 2026-10-18；Blog 卡片显示 `October 18, 2026`；`BlogPosting.datePublished` 与 `BlogPosting.dateModified` 均为 `2026-10-18`；Sitemap 中该 canonical 的 `lastmod` 为 `2026-10-18`；页面保持可索引且结构化数据可解析。
- 不要修改：不要改动文章标题、Meta Description、H1、canonical、正文、链接、CTA、图片、Alt、Caption、作者、阅读时长、分类、其他结构化数据、Blog 排序、其他文章、导航、Footer、工具功能或价格；不要新增 Changelog 条目。

### 发布博客文章 Product Image to Video Prompts for Ads and Ecommerce

- 优先级：`P1`
- 页面或界面：新文章 `https://vidou.ai/blog/product-image-to-video-prompts-ads-ecommerce/`、Blog 列表页 `https://vidou.ai/blog/`、旧文章 `https://vidou.ai/blog/turn-product-photos-into-videos-with-ai/` 与 `https://vidou.ai/blog/image-to-video-prompt-guide/`、XML Sitemap
- 当前问题与线上证据：2026-10-19 使用禁止缓存请求复核，目标 URL 当前显示 Vidou 404 页面并带 `noindex`，canonical 指向首页；Blog 列表与 XML Sitemap 均没有该文章。现有 `How to Turn Product Photos Into Videos With AI` 负责从素材选择到生成、审核的完整工作流，`Image to Video Prompt Guide` 负责通用提示词结构，当前仍缺少一篇帮助电商和广告制作人员按广告目标选择并修改产品视频提示词的独立文章。本文必须保持为广告与电商提示词库，不重复现有产品图工作流文章，也不扩写成后续 `AI Product Video Ads: Turn One Product Photo Into an Ad` 的完整广告制作流程。
- 修改要求：
  1. 新建并发布下方已定稿英文文章，不得让发布执行方改写、缩写、扩写或另行生成正文。精确使用以下字段：
     - URL：`https://vidou.ai/blog/product-image-to-video-prompts-ads-ecommerce/`
     - Slug：`product-image-to-video-prompts-ads-ecommerce`
     - SEO Title：`Product Image to Video Prompts for Ecommerce | Vidou`
     - Meta Description：`Use 12 Product Image to Video prompts for ecommerce ads, product reveals, material shots, social creative, website heroes, and controlled variations.`
     - H1：`Product Image to Video Prompts for Ads and Ecommerce`
     - Category：`Ecommerce`
     - Author：可见署名为 `Vidou`，链接到 `https://vidou.ai/about/`
     - Publish date：`October 19, 2026`；机器可读值为 `2026-10-19`
     - Reading time：`10 min read`
     - Canonical：`https://vidou.ai/blog/product-image-to-video-prompts-ads-ecommerce/`
     - Open Graph：`og:type=article`；`og:title` 与 H1 一致；`og:description` 与 Meta Description 一致；`og:url` 与 canonical 一致；`og:image=https://vidou.ai/images/blog/product-image-to-video-prompts-ads-ecommerce-hero.jpg`；图片尺寸为 1536×864。
     - Twitter：使用 `summary_large_image`；title、description 和 image 分别与 Open Graph 对应字段一致。
  2. 使用以下已经完成的最终图片文件，不得重新生成、下载或替换：
     - Hero 原图：`assets/vidou-blog/product-image-to-video-prompts-ads-ecommerce/product-image-to-video-prompts-ads-ecommerce-hero.jpg`；发布 URL：`https://vidou.ai/images/blog/product-image-to-video-prompts-ads-ecommerce-hero.jpg`；JPEG，1536×864；作为文章 Hero、Open Graph 图和 Blog 卡片图；Alt：`Blue skincare bottle surrounded by frames showing controlled product ad motion concepts`；Hero 不得 lazy-load，并设置明确的 `width=1536`、`height=864`。
     - Hero 响应式图：`assets/vidou-blog/product-image-to-video-prompts-ads-ecommerce/product-image-to-video-prompts-ads-ecommerce-hero-768w.jpg`；发布 URL：`https://vidou.ai/images/blog/product-image-to-video-prompts-ads-ecommerce-hero-768w.jpg`；JPEG，768×432。
     - 正文原图：`assets/vidou-blog/product-image-to-video-prompts-ads-ecommerce/product-ad-motion-prompt-storyboard.jpg`；发布 URL：`https://vidou.ai/images/blog/product-ad-motion-prompt-storyboard.jpg`；JPEG，1536×864；放在 `Match the Prompt to the Ad Job` 表格之后；Alt：`Four storyboard frames of an amber product jar with different controlled ad motion ideas`；Caption：`Plan one controlled change at a time: camera emphasis, moving light, background atmosphere, or a tighter product reveal.`；设置明确的 `width=1536`、`height=864` 并 lazy-load。
     - 正文响应式图：`assets/vidou-blog/product-image-to-video-prompts-ads-ecommerce/product-ad-motion-prompt-storyboard-768w.jpg`；发布 URL：`https://vidou.ai/images/blog/product-ad-motion-prompt-storyboard-768w.jpg`；JPEG，768×432。
     - 两组图片均使用 `srcset` 提供 768w 与 1536w 候选，并设置与现有文章一致的 `sizes`。图片由 OpenAI ImageGen 于 2026-10-19 为本文生成。Hero 最终提示词：`Use case: ads-marketing. Asset type: premium editorial blog hero image for an article about Product Image to Video prompts for ads and ecommerce. Primary request: create a sophisticated conceptual product advertising studio that communicates turning one product photo into several controlled motion directions. Scene/backdrop: deep charcoal studio with a sculptural stone pedestal, restrained curved translucent panels, and subtle atmospheric depth. Subject: one elegant unbranded cobalt-blue glass skincare pump bottle centered and fully visible, with exact stable silhouette, no label and no text. Style/medium: photorealistic luxury product campaign photography, editorial technology aesthetic, realistic materials. Composition/framing: wide 16:9 composition, centered visual hierarchy, bottle remains the anchor while three subtle ghosted framing planes and controlled light trails imply a push in, light sweep, and background drift; generous clean margins. Lighting/mood: controlled emerald edge light with warm amber highlights, dark premium mood, crisp product reflections, no excessive glow. Color palette: charcoal, cobalt blue, restrained emerald, warm amber. Materials/textures: real glass, brushed stone, translucent acrylic, fine studio haze. Constraints: no people, no hands, no text, no letters, no numbers, no labels, no logos, no trademarks, no watermarks, no app interface, no fake screenshots, no charts, no visible brand marks; do not distort the bottle; avoid generic neon cyberpunk styling.` 正文图最终提示词：`Use case: scientific-educational. Asset type: in-article editorial illustration for a guide to choosing Product Image to Video prompts for ads and ecommerce. Primary request: show a coherent physical tabletop storyboard for planning four restrained product ad motion ideas from one source photo. Scene/backdrop: refined dark creative-director table with four evenly spaced physical photographic frames of the same unbranded amber cosmetic jar on the same pale stone pedestal. Subject: the identical jar and pedestal remain consistent across all four frames; each frame visually suggests one concept through physical lighting and composition only: stable hero shot, soft light sweep, gentle fabric movement in the background, and slow camera push in. Style/medium: photorealistic overhead three-quarter editorial photography, educational but not a software interface. Composition/framing: wide 16:9 layout, four clear frames in a left-to-right sequence with generous spacing; subtle unlabelled motion trails and crop guides made from real translucent acrylic strips. Lighting/mood: soft studio illumination, controlled shadows, warm amber and muted emerald accents. Color palette: charcoal tabletop, warm amber glass, pale stone, restrained emerald accents. Materials/textures: glass jar, matte paper, stone, brushed metal, translucent acrylic. Constraints: no people, no hands, no text, no letters, no numbers, no labels, no logos, no trademarks, no watermarks, no UI, no charts, no fake Vidou output, no before-and-after claim; keep the product geometry identical across every frame.` 不得宣称图片是 Vidou 的真实生成结果、客户素材、测试输出或前后对比证据；保留正文末尾 Editorial note 披露。
  3. 正文转化链接必须严格只有两个，且都指向同一 URL `https://vidou.ai/#image-to-video`：第一处是正文唯一工具锚文本 `free product Image to Video generator`，第二处是末尾按钮 `Create a Product Video Prompt`。不要给图片、标题、其他关键词或中段过渡 CTA 添加工具链接，不要链接到任何其他工具页。正文内 `Image to Video` 等可见功能名称不得添加连字符；URL、slug 和图片文件名中的技术连字符保持不变。
  4. 按照现有 Blog 文章视觉与组件样式发布以下定稿正文：

```markdown
# Product Image to Video Prompts for Ads and Ecommerce

A useful product Image to Video prompt starts with the advertisement's job, not a list of effects. Decide whether the clip should reveal the product, emphasize a material, create atmosphere, hold attention in a social feed, or support a website hero. Then choose one controlled movement and state exactly which product details must remain unchanged.

The 12 prompts below are designed for ecommerce and advertising concepts made from a single product photo. They protect the product as the visual anchor while the camera, light, or background supplies motion. For the complete source-image and review workflow, read [how to turn product photos into videos with AI](https://vidou.ai/blog/turn-product-photos-into-videos-with-ai/). For the underlying prompt structure, use the [Image to Video prompt guide](https://vidou.ai/blog/image-to-video-prompt-guide/). If the result bends the product or changes the background, consult the [common Image to Video problems and fixes](https://vidou.ai/blog/image-to-video-problems-fixes/).

## Match the Prompt to the Ad Job

Choose the simplest visual change that supports the placement. A product page may need clarity and material detail. A paid social concept may need a faster hook. A website hero usually needs restrained, repeatable movement that does not compete with nearby copy.

| Ad job | Motion to try first | Detail to protect |
| --- | --- | --- |
| Clean product reveal | Slow push in or soft light sweep | Silhouette, color, label position |
| Material emphasis | One moving highlight | Texture, finish, reflections |
| Lifestyle atmosphere | Gentle background movement | Product geometry and placement |
| Social feed hook | One clear action in the first moment | Crop and product recognition |
| Website hero | Static camera with subtle environment | Negative space and stable framing |
| Product detail | Small focus change or restrained push in | Feature shape and surrounding context |

![Four storyboard frames of an amber product jar with different controlled ad motion ideas](https://vidou.ai/images/blog/product-ad-motion-prompt-storyboard.jpg)

*Plan one controlled change at a time: camera emphasis, moving light, background atmosphere, or a tighter product reveal.*

## Use a Product Safe Prompt Structure

Build each prompt from four parts:

> Keep [product identity details] unchanged. [One visible motion] happens at [pace]. [One camera or environmental instruction]. Preserve [shape, color, material, label position, and background details]. Do not add [unwanted objects, text, or structural changes].

The constraints should match the product. A shoe prompt may protect its sole, laces, logo area, and mesh. A bottle prompt may protect its cap, label position, liquid level, glass color, and reflections. A watch prompt may protect the case, dial, hands, crown, strap, and metal finish.

Test one controlled version in Vidou's [free product Image to Video generator](https://vidou.ai/#image-to-video), then compare the beginning, middle, and final frames with the source photo. Keep the source unchanged while revising the prompt so you can identify which instruction helped.

## 1. Clean Studio Product Reveal

Use this when the product is centered against a simple background and the goal is to make a static catalog image feel more deliberate without changing the scene.

> Keep the product centered and fully visible. The camera makes a slow, smooth push in while the studio light remains soft and stable. Preserve the exact silhouette, proportions, colors, material, label placement, pedestal, and background. No rotation, no new objects, no text changes, and no sudden camera movement.

## 2. Soft Light Sweep for Material Detail

Use a moving highlight when the material is part of the selling point, such as glass, metal, leather, satin, polished plastic, or glazed ceramic.

> Keep the product and camera completely still. One soft highlight travels slowly from left to right across the visible surface. Preserve the exact shape, finish, color, edges, logo area, label placement, and background. No flicker, no second light source, no rotation, and no surface deformation.

## 3. Packaging Hero With Moving Shadows

Use this for skincare, fragrance, food packaging, or other upright products when a subtle environment can add mood without moving the package.

> Keep the package upright, centered, and unchanged. Soft window shadows move slowly across the background while the camera remains static. Preserve the package geometry, cap, edges, colors, label position, visible text area, surface, and pedestal. No added props, no moving product, and no changes to the packaging.

## 4. Gentle Fabric Background Motion

This prompt suits cosmetics, accessories, jewelry, or premium objects already photographed with fabric in the scene.

> Keep the product fixed in its original position. The fabric in the background moves gently in a light breeze while the foreground remains still. Preserve the product silhouette, color, material, label or logo area, shadows, pedestal, and original composition. No new folds in front of the product, no camera movement, and no added objects.

## 5. Footwear Detail Push In

Use a restrained move to direct attention toward one visible construction detail without asking the shoe to turn or reveal an unseen side.

> Keep the shoe in the same position and angle. The camera pushes in slowly toward the visible side panel as a soft highlight moves across the material. Preserve the exact silhouette, sole, laces, stitching, mesh, colors, logo area, and background. No foot, no rotation, no new branding, and no shape changes.

## 6. Watch or Jewelry Reflection Pass

Reflective products need a single controlled lighting idea and a stable camera.

> Keep the watch completely still on its stand. A narrow soft reflection moves once across the bezel and crystal. Preserve the case, dial, hands, markers, crown, strap, metal finish, proportions, and dark background. No rotation, no sparkling particles, no extra jewelry, and no changes to the dial.

## 7. Food or Beverage Atmosphere

Use environmental movement that is already plausible in the source, such as steam above a warm drink or a small condensation highlight on a cold container.

> Keep the cup, handle, liquid level, saucer, and table setting unchanged. A thin stream of steam rises slowly and drifts slightly to the right. The camera remains static and the morning light stays consistent. No spilling liquid, no changing container shape, no new ingredients, and no added text.

Do not use motion to imply temperature, ingredients, freshness, or performance that the real product cannot support. Treat the clip as a creative concept until the claim and product presentation are reviewed.

## 8. Controlled Background Color Shift

A restrained background transition can create a campaign variation while leaving the product presentation stable.

> Keep the product, pedestal, and camera fixed. The background light changes gradually from warm amber to muted green while the product lighting remains neutral. Preserve the exact product shape, color, material, label placement, shadows, and composition. No color change on the product, no new objects, and no pulsing light.

The product color must remain accurate throughout. Reject a result if the background treatment contaminates the product hue or changes the apparent material.

## 9. Vertical Social Ad Hook

Use this when the source already has enough space above and below the product for a vertical crop. The opening action should be clear without becoming chaotic.

> Keep the product centered inside the vertical frame. Begin with a soft shadow moving behind it, followed by one slow camera push in. Preserve the product shape, proportions, color, material, label position, and safe space around every edge. No rotation, no extra objects, no text changes, and no abrupt zoom.

Check the actual placement before approval. Interface overlays, captions, or buttons may cover areas that look empty in a clean preview.

## 10. Square Ecommerce Feed Creative

For a square post, protect the edges and keep the motion readable at a smaller display size.

> Keep the product large, centered, and fully inside the square composition. A soft pool of light expands slowly behind the product while the camera stays still. Preserve the product silhouette, colors, material, label area, pedestal, and background texture. No crop changes, no new props, no rotation, and no fast effects.

The product should remain recognizable even when the clip is viewed without sound or reduced to a feed thumbnail.

## 11. Website Hero With Negative Space

Use this for a wide composition that already leaves room for real webpage copy. Do not ask the generated video to create or animate the headline itself.

> Keep the product anchored on its original side of the frame and preserve the clean negative space. The camera remains static while a faint background shadow moves slowly and one soft highlight crosses the product. Preserve the exact product geometry, colors, material, label position, background, and empty copy area. No added text, no reframing, and no new objects.

Review the loop point and the page layout together. Motion should support the page hierarchy, not pull attention away from the actual headline and button.

## 12. Product Detail Focus Transition

Use a subtle focus change only when the source contains a clear foreground detail and a complete product behind it.

> Begin with the visible foreground material detail in focus, then shift focus slowly to the complete product. Keep the camera fixed. Preserve the product silhouette, proportions, colors, label position, foreground object, background, and lighting. No object movement, no new details, no crop change, and no sudden blur.

If the transition hides the product for too long or makes the detail look different, replace it with a simple push in.

## Adapt a Prompt Without Rewriting Everything

Start with the closest template and change only the variables that belong to your source:

1. Replace the generic product name with the visible item.
2. Name three to six identity details that would make the result unusable if they changed.
3. Choose one camera, lighting, or environmental movement.
4. Match the pace to the placement: restrained for product pages and website heroes, clearer and earlier for short social concepts.
5. Remove instructions that require hidden sides, new props, or a different environment.

Do not stack a push in, orbit, light sweep, fabric movement, particles, and background transition into one prompt. Generate one controlled idea first. If it works, create a second variation by changing one production choice while keeping the source and preservation language constant.

## Review the Result as an Advertisement

An attractive clip can still be unsuitable for commercial use. Check the result against the original product photo and the intended placement.

- **Product accuracy:** Are shape, color, finish, packaging, and visible features consistent?
- **Text and branding:** Did any label, logo area, or small character change?
- **Claim risk:** Does the motion imply a feature, ingredient effect, durability, result, or performance that has not been approved?
- **Composition:** Is the product fully visible inside the final crop and interface safe areas?
- **Continuity:** Do the background, shadows, reflections, and product position remain coherent from beginning to end?
- **Purpose:** Does the movement support the ad job, or is it simply decorative?

Keep the original still, the approved prompt, and the final clip together during review. If the product becomes inaccurate, shorten the movement, simplify the lighting, or return to a clearer source image. Do not publish a generated variation merely because the motion looks polished.

## Build a Controlled Prompt Set

Choose one prompt that matches the placement, protect the details that define the product, and test a single motion idea. Once that version remains accurate from beginning to end, create variations one change at a time. A small set of controlled prompts is more useful than one overloaded instruction because each result has a clear purpose and a clear reason to revise it.

[Create a Product Video Prompt](https://vidou.ai/#image-to-video)

*Editorial note: These prompts are instructional templates based on Vidou's current public interface, its published educational articles, and general product-advertising review principles. They are not presented as benchmarked Vidou outputs. The two editorial images were created with generative AI and reviewed for relevance; they do not depict customer assets, actual advertisements, or Vidou generation results.*
```

  5. 在 Blog 列表页添加该文章卡片，使用 Hero 图、Category `Ecommerce`、标题、摘要 `Use 12 controlled prompts to turn one product photo into focused ecommerce and advertising video concepts.`、日期 `October 19, 2026`，点击卡片进入 canonical URL；保持现有列表排序规则，并将本文作为最新文章显示。
  6. 为两篇既有文章添加反向内链，只执行以下两处，不改写其他句子：
     - 在 `https://vidou.ai/blog/turn-product-photos-into-videos-with-ai/` 的 `Write a Prompt That Protects Product Identity` 小节中，现有句子 `If you want a deeper explanation of subject, motion, camera, environment, and constraints, use the Image to Video prompt guide.` 之后追加：`For ad-ready templates organized by creative goal, use these [Product Image to Video prompts for ads and ecommerce](https://vidou.ai/blog/product-image-to-video-prompts-ads-ecommerce/).`
     - 在 `https://vidou.ai/blog/image-to-video-prompt-guide/` 的 `Product` 示例中，现有句子 `The prompt stays within what a single product image can support. It does not request a hidden side of the shoe or an entirely new scene.` 之后追加：`For more product-specific templates, explore these [Product Image to Video prompts for ads and ecommerce](https://vidou.ai/blog/product-image-to-video-prompts-ads-ecommerce/).`
  7. 加入与现有文章一致的面包屑和 `BlogPosting` 结构化数据。字段至少包括：`headline` 为 H1；`description` 为 Meta Description；`image` 为 Hero 绝对 URL；`datePublished` 与 `dateModified` 均为 `2026-10-19`；`mainEntityOfPage` 与 canonical 一致；`author` 与 `publisher` 均为 `Organization`、名称 `Vidou`、URL `https://vidou.ai/about/`。保留站点现有 `WebSite`、`Organization` 或 `BreadcrumbList` 数据，避免重复冲突。
  8. 将 canonical URL 加入线上 XML Sitemap，`lastmod` 使用实际发布日期 `2026-10-19`。确保页面可索引、不含 `noindex`，并返回正确的 200 状态。
- 验收标准：目标 URL 返回 200 且不再是软 404；SEO Title、Meta Description、H1、canonical、Open Graph、Twitter、作者、发布日期、阅读时长、分类和 `BlogPosting` 数据与要求一致；可见英文正文为上述定稿，正文词数在 1,300–2,000 词范围内；广告目标表格、提示词结构、12 个产品广告提示词、修改规则、广告审核清单和 Editorial note 完整；Hero 与正文图在桌面及 390px 移动端清晰显示、比例稳定、无拉伸或布局偏移，四个指定文件全部发布且 `srcset` 正确；两图 Alt 和 Caption 精确；正文到 `https://vidou.ai/#image-to-video` 恰好两个链接，其中一个为指定关键词锚文本、一个为末尾 CTA 按钮，不存在第三个首页工具链接或其他工具页链接；正文恰好包含三条指向既有 Vidou Blog 文章的上下文内链；可见文案中的 `Image to Video` 不含连字符；两篇旧文章均有指定反向链接；Blog 列表有最新文章卡片；Sitemap 包含 canonical；结构化数据可解析且与页面可见信息一致；键盘可操作、焦点清晰，表格和正文在移动端可扫描且无横向滚动。
- 不要修改：不要改写定稿文章、SEO 字段、12 个提示词、指定锚文本、CTA、Alt、Caption 或披露；不要把 `Image to Video`、`Text to Video`、`Text to Image`、`Image Editor` 等可见功能名称写成带连字符形式；不要增加第二个正文工具锚文本、第三个工具转化链接、其他工具页链接、外部竞品链接、效果承诺、虚构测试数据、客户案例、广告效果指标或未经验证的产品能力；不要把生成图描述成 Vidou 输出；不要把本文改写成完整产品图工作流或完整广告制作流程；不要改动首页工具功能、高级工具、pricing、登录逻辑、账户数据、API、价格、旧文章正文（除指定的两句反向链接）、其他 Blog 卡片、全站导航、Footer 或无关页面；不要新增 Changelog 条目。
