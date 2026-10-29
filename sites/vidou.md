---
site_id: "vidou"
name: "Vidou"
production_url: "https://vidou.ai/"
changelog_url: "not_established"
delivery_method: "not_established"
target_repository: "not_established"
default_branch: "not_established"
updated_at: "2026-10-29"
---

# Vidou 当前待办事项

## 已批准任务

### 统一 Product Image to Video Prompts 文章的真实发布日期

- 优先级：`P2`
- 页面或界面：文章 `https://vidou.ai/blog/product-image-to-video-prompts-ads-ecommerce/`、Blog 列表页 `https://vidou.ai/blog/`、XML Sitemap
- 当前问题与线上证据：2026-10-29 使用禁止缓存请求和实际浏览器渲染复核，文章已返回可索引的 200 页面，但文章可见日期、Blog 卡片、`article:published_time`、`article:modified_time`、`BlogPosting.datePublished`、`BlogPosting.dateModified` 和 Sitemap `lastmod` 仍统一写成 `October 19, 2026` 或 `2026-10-19`。本文在 2026-10-29 才可在线验证，当前日期与真实公开日期不一致。
- 修改要求：只把本文的文章可见发布日期及 `<time datetime>`、Blog 列表卡片日期、`article:published_time`、`article:modified_time`、`BlogPosting.datePublished`、`BlogPosting.dateModified` 和 Sitemap `lastmod` 统一改为真实发布日期；可见文案使用 `October 29, 2026`，机器可读值使用 `2026-10-29`。
- 验收标准：文章页显示 `October 29, 2026` 且对应机器可读时间为 `2026-10-29`；Blog 卡片显示 `October 29, 2026`；Open Graph 的发布与修改时间、`BlogPosting.datePublished` 与 `BlogPosting.dateModified`、Sitemap 中该 canonical 的 `lastmod` 均为 `2026-10-29`；页面继续返回 200、允许索引，结构化数据可解析且与可见日期一致。
- 不要修改：不要改动 SEO Title、Meta Description、H1、canonical、正文、12 个提示词、链接数量或目标、锚文本、CTA、图片、`srcset`、Alt、Caption、作者、阅读时长、分类、文章排序、反向内链、其他结构化数据、其他文章、导航、Footer、工具功能、登录逻辑或价格；不要新增 Changelog 条目。

### 发布博客文章 How to Keep Faces Consistent in AI Image to Video

- 优先级：`P1`
- 页面或界面：新文章 `https://vidou.ai/blog/keep-faces-consistent-ai-image-to-video/`、Blog 列表页 `https://vidou.ai/blog/`、旧文章 `https://vidou.ai/blog/image-to-video-prompt-guide/` 与 `https://vidou.ai/blog/image-to-video-problems-fixes/`、XML Sitemap
- 当前问题与线上证据：2026-10-29 线上复核确认目标 URL 返回 Vidou 的软 404 页面，带 `noindex` 且 canonical 指向首页，Blog 列表和 Sitemap 均没有本文。现有 `Image to Video Prompt Guide` 负责通用动作提示词结构，`Image to Video Problems: 9 Common Failures and Fixes` 只用一个小节概述面部身份漂移；当前缺少一篇专门帮助单张人像来源的读者从源图、动作幅度、身份约束和逐帧审核四个环节降低面部漂移的完整文章。本文只解决单个短片中的人脸一致性，不扩写为 Week 11 的跨场景角色一致性主题，也不宣称任何方法能够保证结果。
- 修改要求：
  1. 新建并发布下方已定稿英文文章，不得让发布执行方改写、缩写、扩写或另行生成正文。精确使用以下字段：
     - URL：`https://vidou.ai/blog/keep-faces-consistent-ai-image-to-video/`
     - Slug：`keep-faces-consistent-ai-image-to-video`
     - SEO Title：`How to Keep Faces Consistent in AI Image to Video | Vidou`
     - Meta Description：`Learn how to keep faces consistent in AI Image to Video with a clear source image, restrained motion, identity constraints, and a frame review workflow.`
     - H1：`How to Keep Faces Consistent in AI Image to Video`
     - Category：`Guide`
     - Author：可见署名为 `Vidou`，链接到 `https://vidou.ai/about/`
     - Publish date：`October 29, 2026`；机器可读值为 `2026-10-29`
     - Reading time：`9 min read`
     - Canonical：`https://vidou.ai/blog/keep-faces-consistent-ai-image-to-video/`
     - Open Graph：`og:type=article`；`og:title` 与 H1 一致；`og:description` 与 Meta Description 一致；`og:url` 与 canonical 一致；`og:image=https://vidou.ai/images/blog/keep-faces-consistent-ai-image-to-video-hero.jpg`；图片尺寸为 1536×864。
     - Twitter：使用 `summary_large_image`；title、description 和 image 分别与 Open Graph 对应字段一致。
  2. 使用以下已经完成的最终图片文件，不得重新生成、下载或替换：
     - Hero 原图：`assets/vidou-blog/keep-faces-consistent-ai-image-to-video/keep-faces-consistent-ai-image-to-video-hero.jpg`；发布 URL：`https://vidou.ai/images/blog/keep-faces-consistent-ai-image-to-video-hero.jpg`；JPEG，1536×864；作为文章 Hero、Open Graph 图和 Blog 卡片图；Alt：`Three portrait frames showing the same face with restrained expression changes`；Hero 不得 lazy-load，并设置明确的 `width=1536`、`height=864`。
     - Hero 响应式图：`assets/vidou-blog/keep-faces-consistent-ai-image-to-video/keep-faces-consistent-ai-image-to-video-hero-768w.jpg`；发布 URL：`https://vidou.ai/images/blog/keep-faces-consistent-ai-image-to-video-hero-768w.jpg`；JPEG，768×432。
     - 正文原图：`assets/vidou-blog/keep-faces-consistent-ai-image-to-video/face-consistency-frame-review.jpg`；发布 URL：`https://vidou.ai/images/blog/face-consistency-frame-review.jpg`；JPEG，1536×864；放在 `Match the Motion to the Source` 表格之后；Alt：`Five portrait frames used to review facial identity through a video`；Caption：`Compare the same facial landmarks at the beginning, middle, and end instead of judging only during playback.`；设置明确的 `width=1536`、`height=864` 并 lazy-load。
     - 正文响应式图：`assets/vidou-blog/keep-faces-consistent-ai-image-to-video/face-consistency-frame-review-768w.jpg`；发布 URL：`https://vidou.ai/images/blog/face-consistency-frame-review-768w.jpg`；JPEG，768×432。
     - 两组图片均使用 `srcset` 提供 768w 与 1536w 候选，并设置与现有文章一致的 `sizes`。图片由 OpenAI ImageGen 于 2026-10-29 为本文生成。Hero 最终提示词：`Use case: photorealistic-natural. Asset type: wide 16:9 editorial blog hero for an article about keeping faces consistent in AI Image to Video. Primary request: create a sophisticated cinematic portrait concept showing the same adult woman's facial identity remaining visually stable across a short sequence of motion frames. Scene/backdrop: dark charcoal portrait studio with subtle depth, three restrained translucent photographic frame planes aligned behind and around one central portrait, suggesting consecutive moments without becoming a software interface. Subject: one fictional adult woman, natural face with realistic pores and fine skin texture, calm expression, direct three-quarter gaze; the exact same facial proportions, eye shape, nose, mouth, jawline, hairstyle, skin tone, clothing, and lighting remain consistent in every visible frame; only a slight blink, tiny gaze shift, and a few gently moving hair strands are implied. Style/medium: premium photorealistic editorial portrait photography, cinematic but natural, realistic lens rendering, not glossy beauty advertising. Composition/framing: landscape 16:9, head-and-shoulders portrait centered, readable visual sequence from left to right, generous margins, no cropped facial features. Lighting/mood: soft directional key light, restrained emerald edge light and warm amber fill, calm precise mood. Color palette: charcoal, muted emerald, warm amber, natural skin tones. Materials/textures: real skin texture, matte fabric, translucent acrylic frame planes, subtle film grain. Constraints: one identity only; adult subject; no second person; no face morphing; no asymmetrical or duplicated facial features; no exaggerated smile; no text; no letters; no numbers; no logos; no trademarks; no watermark; no UI; no app screenshot; no charts; no face-recognition boxes; no before-and-after claim; do not imply this is a Vidou output; avoid generic neon cyberpunk styling.` 正文图最终提示词：`Use case: scientific-educational. Asset type: wide 16:9 in-article editorial illustration for a guide to reviewing facial consistency in AI Image to Video. Primary request: create a clear physical film-review contact sheet showing the same fictional adult man's face across five consecutive portrait frames, with only a subtle blink and tiny gaze shift while identity remains stable. Scene/backdrop: refined dark creative-review table with one horizontal strip of five evenly spaced photographic portrait frames, small unlabeled translucent crop guides and simple circular markers made from physical acrylic, no computer interface. Subject: the identical adult man in every frame, natural realistic face with visible skin texture, short dark hair, calm neutral expression; exact same eye spacing, nose, mouth, jawline, ears, hairstyle, skin tone, clothing, camera angle, and background in all five frames; motion progresses only through a natural blink and minimal gaze change. Style/medium: photorealistic overhead three-quarter editorial photography of a physical contact sheet, educational and precise, not a software screenshot. Composition/framing: landscape 16:9, left-to-right five-frame sequence with generous spacing, each head-and-shoulders portrait fully visible and the same scale, room for a short caption below in webpage layout but no text inside the image. Lighting/mood: soft neutral studio light with restrained warm amber and muted emerald accents, analytical calm mood, consistent lighting across all frames. Color palette: charcoal tabletop, natural skin tones, muted emerald, warm amber, pale gray acrylic. Materials/textures: matte photographic paper, translucent acrylic, brushed metal, realistic skin and fabric texture. Constraints: one identity only; adult subject; exact facial consistency across all five frames; no face morphing; no extra people; no altered age; no changing hair or clothes; no dramatic expression; no text; no letters; no numbers; no labels; no logos; no trademarks; no watermark; no app interface; no fake screenshot; no facial recognition boxes; no before-and-after claim; do not imply this is a Vidou result.` 不得宣称图片是 Vidou 的真实生成结果、客户素材、测试输出或前后对比证据；保留正文末尾 Editorial note 披露。
  3. 正文转化链接必须严格只有两个，且都指向同一 URL `https://vidou.ai/#image-to-video`：第一处是正文唯一工具锚文本 `free portrait Image to Video generator`，第二处是末尾按钮 `Animate a Portrait Carefully`。不要给图片、标题、其他关键词或中段过渡 CTA 添加工具链接，不要链接到任何其他工具页。正文内 `Image to Video` 等可见功能名称不得添加连字符；URL、slug 和图片文件名中的技术连字符保持不变。
  4. 按照现有 Blog 文章视觉与组件样式发布以下定稿正文：

```markdown
# How to Keep Faces Consistent in AI Image to Video

To keep a face consistent in AI Image to Video, begin with a source image that defines the face clearly, request a small movement the visible angle can support, and name the identity details that must remain stable. Then compare the beginning, middle, and final frames. If the face changes, reduce one variable instead of adding more prompt language.

This guide focuses on one person in one short clip. It does not cover maintaining a character across several scenes, outfits, or camera setups. For the broader writing framework, use the [Image to Video prompt guide](https://vidou.ai/blog/image-to-video-prompt-guide/). If the face is only one of several failures, start with the [common Image to Video problems and fixes](https://vidou.ai/blog/image-to-video-problems-fixes/). When framing is the main issue, choose a safer move with the [camera movement guide](https://vidou.ai/blog/best-camera-movements-ai-image-to-video/).

## Why Faces Change During Motion

A source image defines only one visible moment. When a prompt asks for a large head turn, a wide smile, a fast camera move, or a new viewing angle, the result must fill in facial information that the source does not show clearly. Heavy filters, blur, deep shadows, hair across the face, glasses glare, and a very small face can make the stable details harder to read.

Stacking facial, camera, lighting, and background changes also makes it difficult to identify which instruction caused the identity to drift.

Consistency is therefore a workflow, not one magic phrase. Improve the source, limit the requested change, protect a few defining details, and review the full sequence before increasing motion.

## Start With a Source That Defines the Face

Choose a portrait in which the face is large enough to inspect and important features are not hidden. A clean source does not need to look like an identification photo, but the eyes, eyebrows, nose, mouth, jawline, hairline, and skin tone should be readable at the intended crop.

Check these details before generating:

- **Focus:** The eyes and facial edges are sharp.
- **Angle:** The motion stays close to the visible head angle.
- **Lighting:** Important features remain visible without deep shadow or blown highlights.
- **Occlusion:** Hair, hands, or accessories do not cover details you need to preserve.
- **Expression:** The starting expression is close to the requested change.
- **Scale:** The face is large enough to review.
- **People:** In a group, the prompt identifies who moves and who stays still.

Avoid heavy smoothing, reshaping, sharpening halos, or filters before animation. Use the version closest to the appearance you want to preserve.

## Match the Motion to the Source

Begin with the smallest visible action that serves the clip. The safer choice depends on what the portrait already shows.

| Source condition | Motion to try first | Main risk to avoid |
| --- | --- | --- |
| Front-facing close portrait | One blink or a slight gaze shift | Large expression change |
| Three-quarter portrait | Gentle blink with minimal head movement | Turning toward an unseen angle |
| Side profile | Small eye or hair movement | Asking for a front view |
| Face partly covered by hair | Subtle hair movement away from key features | Hair repeatedly crossing the eyes or mouth |
| Person in a wider scene | Breathing or environmental motion | Fast camera move that makes the face too small |
| Two or more people | One named subject moves while others remain still | Simultaneous expressions and head turns |

![Five portrait frames used to review facial identity through a video](https://vidou.ai/images/blog/face-consistency-frame-review.jpg)

*Compare the same facial landmarks at the beginning, middle, and end instead of judging only during playback.*

A static camera is often the best first test for a close portrait because it separates facial motion from reframing. If the face remains stable, try a very short push in. Avoid beginning with an orbit, a long pan, or a pull back that reveals large areas outside the source.

## Write a Prompt That Protects Identity

Give the prompt four jobs: name one facial action, set its intensity, control the camera, and protect the defining details.

> [Person] performs [one small visible action] at a [gentle or controlled pace]. [One camera instruction]. Keep facial identity, facial proportions, eye shape, nose, mouth, jawline, hairstyle, skin tone, clothing, lighting, and background consistent. Do not add new accessories or change the person's age.

You do not need every item in every prompt. Choose the details that would make the result unusable if they changed.

For a direct portrait:

> The subject blinks once and makes a very small gaze shift toward the camera. Keep the head near its original angle. Static camera, soft natural movement. Preserve facial identity, eye shape, eyebrows, nose, mouth, jawline, hairstyle, skin tone, clothing, lighting, and background.

For a portrait with environmental motion:

> A few loose strands of hair move gently in a light breeze while the subject remains relaxed. The face and head stay nearly still. Static camera. Preserve facial identity, facial proportions, hairstyle, skin tone, clothing, and the original background.

For a three-quarter portrait:

> The subject blinks naturally and turns the gaze slightly without rotating the head. Slow, restrained movement. The camera remains fixed. Keep the original face angle, identity, eye spacing, nose, lips, jawline, hair, skin tone, and lighting consistent.

Test the smallest useful version in Vidou's [free portrait Image to Video generator](https://vidou.ai/#image-to-video). Keep the source unchanged while revising the prompt so each comparison answers one question.

## Protect the Face Without Freezing the Entire Shot

Protect the face and a few connected details, then allow motion somewhere else.

- If the face must remain nearly still, let hair tips, clothing, light, or the background carry subtle motion.
- If the expression changes, keep the camera and lighting fixed.
- If the camera moves, reduce facial action to a blink or small gaze shift.
- If a hand is close to the face, keep the hand still or remove that interaction from the first test.

Before adding more motion, save the clearest source and one minimal prompt as your baseline. Every later version should change one decision from that baseline.

## Separate Face, Camera, and Environment

Treat the face, camera, and environment as three motion layers. Give one layer priority and keep the others restrained. A portrait-led clip may use one blink with a static camera. An atmosphere-led clip may keep the person still while curtains or soft light move. A camera-led clip may use a small push in while the expression remains unchanged.

If the face changes during a static-camera test, reduce the facial action. If it changes only after a push in, shorten the camera move. If moving hair crosses the eyes, limit the hair rather than rewriting the whole prompt.

## Review the Beginning, Middle, and End

Normal playback can hide small changes. Pause at three moments and compare them with the source.

1. **Beginning:** Does the first generated frame already match the source identity, crop, head angle, and lighting?
2. **Middle:** Do the eyes, nose, mouth, jawline, hairline, and skin tone remain coherent during the action?
3. **End:** Does the person still look like the same individual after the blink, gaze shift, camera move, or environmental motion finishes?

Compare relationships: eye spacing, eyebrow shape, the nose and mouth position, jaw width, and hair outline. Also watch for sudden changes in age, makeup, facial hair, accessories, or skin tone.

If one frame looks wrong, identify the first moment of drift. The timing often points to the instruction that needs adjustment. A change during a smile suggests reducing the expression. A change as the camera moves suggests shortening the move. A change when hair crosses the face suggests keeping key features unobstructed.

## Fix One Failure at a Time

Use the first visible failure to choose the next revision.

- **The face becomes a different person:** Reduce the head turn or expression and strengthen the identity and proportion constraints.
- **The eyes or mouth change shape:** Replace a broad instruction such as “smiles brightly” with one smaller action such as “forms a slight closed-mouth smile.”
- **The jaw or head shape shifts:** Keep the original head angle and remove an orbit, profile reveal, or large turn.
- **The face looks stable but lifeless:** Add one blink, breath, or slight gaze change instead of several expression instructions.
- **The skin tone or age changes:** Keep lighting fixed and explicitly preserve skin tone, age, and facial texture.
- **One person changes into another in a group:** Name the moving subject by position or clothing and tell the other people to remain still.

Keep the source image, baseline prompt, and accepted clip together. If you change several variables at once, you lose the ability to tell which correction helped.

## Know When to Choose a Different Source

Start with another image when the face is very small, blurred, compressed, hidden, covered by glare, or divided by extreme light and shadow. Choose another angle when the motion would reveal a side of the face absent from the source.

For a group portrait, consider a tighter crop when only one person needs to move. For a strong expression change, use a source whose expression is already close to the intended result. A better source usually gives you a clearer baseline than adding a longer list of constraints to a weak image.

## Use Portraits Responsibly

Animate only images you have the right and permission to use. Do not use a real person's portrait to impersonate them, misrepresent what they said or did, or create deceptive endorsements. When a generated clip could reasonably be mistaken for real footage, label or disclose its synthetic nature in the final context where it appears.

## A Repeatable Face Consistency Workflow

Use one clear portrait, choose one small action, keep the camera restrained, and protect the facial details that define the person. Generate a baseline, compare the beginning, middle, and end, and revise only the first visible failure. Increase motion only after the face remains coherent through the simpler version.

[Animate a Portrait Carefully](https://vidou.ai/#image-to-video)

*Editorial note: This guide was prepared from Vidou's current public interface, its published educational articles, and general portrait review and prompt-design principles. The prompt examples are instructional and are not presented as benchmarked Vidou outputs. The two editorial images were created with generative AI and reviewed for relevance; they do not depict a real customer, a real person, or actual Vidou generation results.*
```

  5. 在 Blog 列表页添加该文章卡片，使用 Hero 图、Category `Guide`、标题、摘要 `Use a clear portrait, restrained motion, identity constraints, and a three-frame review to reduce face drift in Image to Video.`、日期 `October 29, 2026`，点击卡片进入 canonical URL；保持现有列表排序规则，并将本文作为最新文章显示。
  6. 为两篇既有文章添加反向内链，只执行以下两处，不改写其他句子：
     - 在 `https://vidou.ai/blog/image-to-video-prompt-guide/` 的 `Portrait` 示例中，现有句子 `The rewrite replaces abstract praise with visible actions, a camera direction, a pace, and specific details to preserve.` 之后追加：`For a focused source-image, motion, and review workflow, read [how to keep faces consistent in AI Image to Video](https://vidou.ai/blog/keep-faces-consistent-ai-image-to-video/).`
     - 在 `https://vidou.ai/blog/image-to-video-problems-fixes/` 的 `2. The Face Loses Its Identity` 小节中，现有提示词示例之后追加：`For a complete portrait workflow, use the guide to [keeping faces consistent in AI Image to Video](https://vidou.ai/blog/keep-faces-consistent-ai-image-to-video/).`
  7. 加入与现有文章一致的面包屑和 `BlogPosting` 结构化数据。字段至少包括：`headline` 为 H1；`description` 为 Meta Description；`image` 为 Hero 绝对 URL；`datePublished` 与 `dateModified` 均为 `2026-10-29`；`mainEntityOfPage` 与 canonical 一致；`author` 与 `publisher` 均为 `Organization`、名称 `Vidou`、URL `https://vidou.ai/about/`。保留站点现有 `WebSite`、`Organization` 或 `BreadcrumbList` 数据，避免重复冲突。
  8. 将 canonical URL 加入线上 XML Sitemap，`lastmod` 使用实际发布日期 `2026-10-29`。确保页面可索引、不含 `noindex`，并返回正确的 200 状态。
- 验收标准：目标 URL 返回 200 且不再是软 404；SEO Title、Meta Description、H1、canonical、Open Graph、Twitter、作者、发布日期、阅读时长、分类和 `BlogPosting` 数据与要求一致；可见英文正文为上述定稿，正文词数在 1,200–1,800 词范围内；源图检查、动作匹配表、三组完整提示词、运动分层、三帧审核、逐项修复、换源条件、肖像责任提示和 Editorial note 完整；Hero 与正文图在桌面及 390px 移动端清晰显示、比例稳定、无拉伸或页面横向溢出，四个指定文件全部发布且 `srcset` 正确；两图 Alt 和 Caption 精确；正文到 `https://vidou.ai/#image-to-video` 恰好两个链接，其中一个为指定关键词锚文本、一个为末尾 CTA 按钮，不存在第三个首页工具链接或其他工具页链接；正文恰好包含三条指向既有 Vidou Blog 文章的上下文内链；可见文案中的 `Image to Video` 不含连字符；两篇旧文章均有指定反向链接；Blog 列表有最新文章卡片；Sitemap 包含 canonical；结构化数据可解析且与页面可见信息一致；键盘可操作、焦点清晰，表格和正文在移动端可扫描。
- 不要修改：不要改写定稿文章、SEO 字段、提示词示例、指定锚文本、CTA、Alt、Caption 或披露；不要把 `Image to Video`、`Text to Video`、`Text to Image`、`Image Editor` 等可见功能名称写成带连字符形式；不要增加第二个正文工具锚文本、第三个工具转化链接、其他工具页链接、外部竞品链接、结果保证、虚构测试数据、真人客户案例、身份识别能力或未经验证的产品能力；不要把生成图描述成 Vidou 输出；不要扩写为跨场景、跨服装、跨镜头的角色一致性文章；不要改动首页工具功能、高级工具、pricing、登录逻辑、账户数据、API、价格、旧文章正文（除指定的两句反向链接）、其他 Blog 卡片、全站导航、Footer 或无关页面；不要新增 Changelog 条目。
