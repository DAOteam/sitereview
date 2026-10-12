---
site_id: "vidou"
name: "Vidou"
production_url: "https://vidou.ai/"
changelog_url: "not_established"
delivery_method: "not_established"
target_repository: "not_established"
default_branch: "not_established"
updated_at: "2026-10-12"
---

# Vidou 当前待办事项

## 已批准任务

### 发布博客文章 50 Image to Video Prompt Examples for Realistic Motion

- 优先级：`P1`
- 页面或界面：新文章 `https://vidou.ai/blog/image-to-video-prompt-examples/`、Blog 列表页 `https://vidou.ai/blog/`、旧文章 `https://vidou.ai/blog/image-to-video-prompt-guide/` 与 `https://vidou.ai/blog/how-to-animate-a-photo-with-ai/`、XML Sitemap
- 当前问题与线上证据：2026-10-12 使用禁止缓存请求复核，目标 URL 当前显示 Vidou 的 404 页面，Blog 列表页尚无博客计划 Week 2 的第一篇文章。线上已有 Prompt Guide 解释提示词结构与逐项修改方法，但尚无覆盖人像、产品、风景、生活方式、建筑、插画和镜头运动的可直接改写示例库。首页 `https://vidou.ai/#image-to-video` 当前公开主打免费、无需登录的 Image to Video 快速试用，适合作为本文唯一转化目的地；高级工具页保持其登录后可选设置意图，不在本文增加链接。
- 修改要求：
  1. 新建并发布下方已定稿的英文文章，不得让发布执行方改写、缩写、扩写或另行生成正文。文章 URL、SEO 字段和页面信息精确使用：
     - URL：`https://vidou.ai/blog/image-to-video-prompt-examples/`
     - Slug：`image-to-video-prompt-examples`
     - SEO Title：`50 Image to Video Prompt Examples for Realistic Motion | Vidou`
     - Meta Description：`Explore 50 Image to Video prompt examples for realistic portraits, products, landscapes, food, illustrations, and cinematic camera motion.`
     - H1：`50 Image to Video Prompt Examples for Realistic Motion`
     - Category：`Prompts`
     - Author：可见署名为 `Vidou`，链接到 `https://vidou.ai/about/`
     - Publish date：`October 12, 2026`；机器可读值为 `2026-10-12`
     - Reading time：`11 min read`
     - Canonical：`https://vidou.ai/blog/image-to-video-prompt-examples/`
     - Open Graph：`og:type=article`；`og:title` 与 H1 一致；`og:description` 与 Meta Description 一致；`og:url` 与 canonical 一致；`og:image=https://vidou.ai/images/blog/image-to-video-prompt-examples-realistic-motion-hero.jpg`；图片尺寸为 1536×864。
     - Twitter：使用 `summary_large_image`；title、description 和 image 分别与 Open Graph 对应字段一致。
  2. 文章顶部使用主图，正文在 `How to Adapt These Prompt Examples` 小节的三个步骤之后使用第二张图。把仓库内已生成的最终图片集成到站点静态资源体系，并生成现有图片组件所需的 768px 宽响应式版本；不得重新生成或用占位图替换：
     - 本地源文件：`assets/vidou-blog/image-to-video-prompt-examples-realistic-motion/image-to-video-prompt-examples-realistic-motion-hero.jpg`；发布 URL：`https://vidou.ai/images/blog/image-to-video-prompt-examples-realistic-motion-hero.jpg`；尺寸：1536×864；Alt：`Five visual scenes connected by motion trails for an Image to Video prompt example library`；作为文章 Hero、Open Graph 图和 Blog 列表卡片图。
     - 本地源文件：`assets/vidou-blog/image-to-video-prompt-examples-realistic-motion/realistic-motion-prompt-layers.jpg`；发布 URL：`https://vidou.ai/images/blog/realistic-motion-prompt-layers.jpg`；尺寸：1536×864；Alt：`Portrait beside a sunlit window with subtle hair curtain and atmosphere motion`；Caption：`Realistic motion usually comes from one restrained subject action, one supporting environmental movement, and a stable composition.`
     - 两张图片均由 OpenAI ImageGen 于 2026-10-12 为本文生成。不得宣称它们是 Vidou 的真实生成结果、客户素材、测试输出或前后对比证据。文章末尾保留定稿中的 Editorial note 披露。
  3. 正文中的转化链接必须严格只有两个，且都指向同一 URL `https://vidou.ai/#image-to-video`：第一处是正文唯一工具锚文本 `free Image to Video generator`，第二处是末尾按钮 `Try an Image to Video Prompt`。不要给图片、标题、其他关键词或中段过渡 CTA 添加工具链接，不要链接到任何其他工具页。正文内 `Image to Video` 等可见功能名称不得添加连字符；URL、slug 和图片文件名中的技术连字符保持不变。
  4. 按照现有 Blog 文章视觉与组件样式发布以下定稿正文：

```markdown
# 50 Image to Video Prompt Examples for Realistic Motion

A useful Image to Video prompt describes what moves, whether the camera moves, how fast the action feels, and which details stay consistent. Below are 50 prompts to adapt for portraits, products, landscapes, food, architecture, illustrations, and camera movements.

These are starting points, not guaranteed recipes. Match the prompt to the source, keep motion plausible, and review the full clip for changes in faces, hands, text, product shape, or background geometry.

For the reasoning behind motion, camera direction, pace, and constraints, read the [Image to Video prompt guide](https://vidou.ai/blog/image-to-video-prompt-guide/). For the complete workflow, start with [how to animate a photo with AI](https://vidou.ai/blog/how-to-animate-a-photo-with-ai/).

## How to Adapt These Prompt Examples

Adapt each example in three passes:

1. **Match the subject.** Replace the subject, environment, colors, and details with what appears in your image.
2. **Choose one priority.** Keep the subject, camera, or environmental motion dominant. Remove secondary action if it feels busy.
3. **Protect important details.** Name the face, hands, product shape, label, clothing, architecture, or background that must remain stable.

![Portrait beside a sunlit window with subtle hair curtain and atmosphere motion](https://vidou.ai/images/blog/realistic-motion-prompt-layers.jpg)

*Realistic motion usually comes from one restrained subject action, one supporting environmental movement, and a stable composition.*

Paste one adapted example into Vidou's [free Image to Video generator](https://vidou.ai/#image-to-video), review the full result, and change one instruction per revision. This reveals which variable caused the difference.

## Portrait Prompts

Use restrained movement. Large turns can require features that are not visible in the portrait.

1. **Natural blink and gaze**
   > The subject blinks naturally and shifts their gaze slightly toward the camera. Keep the face, hairstyle, clothing, skin tone, and background consistent. Static camera and calm movement.

2. **Hair in a light breeze**
   > A few strands of hair move gently in a light breeze while the subject remains relaxed. Slow camera push in. Preserve facial identity, body position, clothing, and lighting.

3. **Subtle smile**
   > The subject forms a slight natural smile and breathes gently. Keep the eyes, facial proportions, hair, shoulders, clothing, and background unchanged. Camera remains steady.

4. **Small profile turn**
   > The subject turns their head a few degrees toward the window and pauses. Use slow, controlled motion. Preserve facial features, hairstyle, jewelry, clothing, and the original composition.

5. **Reading by a window**
   > The reader lowers their gaze toward the open book as the curtain moves softly. Static camera, quiet pace. Keep the face, hands, book shape, room, and daylight consistent.

6. **Musician at rest**
   > The musician takes a calm breath and adjusts their gaze toward the instrument. A soft highlight shifts across the scene. Preserve the face, hands, instrument, clothing, and background.

7. **Athlete before movement**
   > The athlete breathes steadily while loose fabric moves slightly in the air. Gentle camera push in. Keep facial identity, body proportions, pose, uniform, and setting stable.

8. **Warm side light**
   > The subject remains still as warm window light moves subtly across the face. Minimal hair movement, static camera, natural pace. Preserve identity, skin texture, clothing, and room layout.

## Product Prompts

Keep product geometry and visible details stable. Avoid a full rotation when only one side is visible. For the full workflow, see [how to turn product photos into videos with AI](https://vidou.ai/blog/turn-product-photos-into-videos-with-ai/).

9. **Sneaker light sweep**
   > A soft studio highlight travels slowly across the sneaker while the camera pushes in slightly. Preserve the exact shape, sole, laces, materials, colors, logo area, and background.

10. **Skincare bottle shadows**
   > The bottle remains upright as warm window shadows drift across the background. Static camera and gentle movement. Keep the bottle geometry, cap, label placement, glass color, and reflections consistent.

11. **Watch detail reveal**
   > A narrow light moves slowly across the watch case and dial. Gentle camera push in. Preserve the hands, markings, case shape, strap texture, colors, and original position.

12. **Headphones on a pedestal**
   > The camera makes a small, smooth arc around the headphones without revealing the back. Keep the headband, ear cups, controls, materials, proportions, and studio background unchanged.

13. **Handbag material focus**
   > Soft light glides across the handbag texture while the camera remains steady. Preserve the silhouette, handles, stitching, hardware, color, logo area, and surface beneath the product.

14. **Coffee package atmosphere**
   > A faint ribbon of steam rises behind the coffee package as the camera slowly pushes in. Keep the package shape, printed design, label placement, colors, edges, and tabletop stable.

15. **Ceramic object reveal**
   > The camera moves gently from left to right while a soft reflection changes across the ceramic surface. Preserve the object shape, glaze texture, color, base, and background composition.

16. **Furniture in natural light**
   > Sunlight and leaf shadows shift slowly across the chair while the camera stays fixed. Keep the chair geometry, fabric, legs, room perspective, floor, and surrounding objects unchanged.

## Landscape and Nature Prompts

Let the environment move while landforms and the horizon stay stable.

17. **Mountain lake**
   > Clouds drift slowly above the mountains while small ripples move across the lake. Static camera and calm pace. Keep the shoreline, peaks, trees, reflections, and horizon consistent.

18. **Ocean at sunrise**
   > Gentle waves roll toward the shore as the sunrise brightens gradually. Slow camera push in. Preserve the coastline, rock shapes, horizon, sky colors, and overall composition.

19. **Forest morning**
   > Leaves move lightly in the breeze while thin mist drifts between the trees. Camera remains steady. Keep trunks, paths, plants, depth, and the direction of the morning light stable.

20. **Waterfall detail**
   > Water flows steadily over the rocks as fine spray moves through the air. Use a subtle push in. Preserve rock geometry, surrounding plants, pool shape, colors, and framing.

21. **Desert wind**
   > A thin layer of sand moves gently along the dune surface while distant heat haze shifts. Static camera. Keep dune contours, footprints, horizon, shadows, and sky unchanged.

22. **Snowy cabin**
   > Light snow falls slowly as a small amount of chimney smoke rises. Keep the camera fixed and the mood quiet. Preserve cabin structure, windows, trees, snowbanks, and landscape.

23. **Meadow in a breeze**
   > Tall grass and wildflowers sway gently from left to right while clouds move slowly overhead. Preserve the path, tree line, horizon, flower colors, and natural daylight.

24. **Canyon light change**
   > Soft sunlight moves gradually across the canyon wall while a small amount of dust drifts near the ground. Static camera. Preserve rock formations, scale, shadows, and sky.

## Food and Everyday Scene Prompts

Use small movements such as steam, flame, condensation, fabric, or shifting light. Keep object shapes unchanged.

25. **Fresh coffee**
   > Steam rises slowly from the coffee while morning light shifts across the table. Gentle camera push in. Preserve the cup shape, handle, liquid level, saucer, and background objects.

26. **Birthday cake candles**
   > Candle flames flicker softly above the cake while the camera remains steady. Keep the frosting, decorations, candle positions, plate, table, colors, and background consistent.

27. **Pasta on a table**
   > A small amount of steam rises from the pasta as light moves subtly across the sauce. Static camera. Preserve the food arrangement, plate shape, garnish, cutlery, and table setting.

28. **Cold drink**
   > Condensation moves slowly down the glass while ice shifts only slightly. Use a gentle push in. Keep the glass, garnish, liquid color, reflections, tabletop, and background stable.

29. **Open book and curtain**
   > The curtain moves softly in the breeze and one page lifts slightly before settling. Keep the camera fixed. Preserve the book position, visible page layout, furniture, and room light.

30. **Vinyl listening scene**
   > The record rotates steadily while a warm lamp flickers almost imperceptibly. Slow camera move toward the turntable. Keep the tonearm, controls, furniture, and room layout consistent.

31. **Candle on a shelf**
   > The candle flame moves gently and creates subtle shifting shadows on the wall. Static camera and calm pace. Preserve the candle shape, shelf, nearby objects, and composition.

32. **Flowers in a vase**
   > A few flower stems sway slightly while sunlight moves across the table. Gentle camera push in. Keep the petals, vase shape, water level, arrangement, colors, and background unchanged.

## Architecture and Travel Prompts

Protect straight lines, signs, and horizon placement. Avoid camera moves that demand large unseen areas.

33. **Quiet old street**
   > Morning light shifts slowly along the building facades while a few tree leaves move. Gentle forward camera movement. Preserve windows, doors, signs, pavement lines, and street perspective.

34. **Modern tower**
   > Clouds move behind the tower as reflections change subtly across the glass. Camera remains fixed. Keep every building edge, floor line, neighboring structure, and the vertical perspective stable.

35. **Sunlit interior**
   > Sheer curtains move gently while sunlight and shadows shift across the floor. Static camera. Preserve walls, windows, furniture geometry, decor placement, and room perspective.

36. **Train platform**
   > A light breeze moves clothing and a distant train approaches slowly without changing the platform. Keep the camera steady. Preserve faces, signs, tracks, architecture, and perspective.

37. **Bridge over water**
   > Water and reflected light move beneath the bridge while clouds drift slowly. Gentle lateral camera movement. Preserve the bridge structure, cables, skyline, shoreline, and horizon.

38. **Temple courtyard**
   > Tree branches and hanging fabric move slightly in a breeze as sunlight changes softly. Static camera. Preserve columns, roof lines, stonework, steps, ornaments, and courtyard layout.

39. **Coastal town**
   > The sea moves gently beyond the buildings while laundry shifts in the breeze. Slow camera push in. Keep building shapes, balconies, streets, colors, coastline, and horizon stable.

40. **Night market atmosphere**
   > Steam rises from one food stall while hanging lights sway slightly. Camera moves forward slowly. Preserve faces, hands, stall structures, signs, objects, and the street layout.

## Illustration and AI Art Prompts

Name the medium and protect its line work, palette, character design, and composition.

41. **Watercolor animal**
   > The fox blinks once while nearby grass and fabric move gently. Static camera. Preserve the watercolor texture, line work, character proportions, colors, paper grain, and composition.

42. **Anime portrait**
   > The character blinks naturally as a few strands of hair move in a soft breeze. Gentle push in. Keep facial design, eye shape, outfit, color palette, line art, and background stable.

43. **Fantasy castle painting**
   > Thin clouds drift around the castle towers while flags move slowly. Camera remains steady. Preserve the painted architecture, mountain shapes, lighting, brush texture, palette, and composition.

44. **Science fiction scene**
   > Small navigation lights pulse gently as mist moves beneath the spacecraft. Slow camera push in. Keep the ship design, panels, landing gear, environment, scale, and art style consistent.

45. **Paper cut forest**
   > Layered leaves sway slightly and soft shadows shift between the paper layers. Static camera. Preserve every cut edge, character shape, color layer, texture, and depth arrangement.

46. **Clay character**
   > The clay character blinks and tilts its head slightly while the background remains still. Preserve facial features, fingerprints, body proportions, clothing, colors, lighting, and handcrafted texture.

## Reusable Camera Movement Prompts

These templates make the camera primary. Replace the brackets and keep subject movement minimal.

47. **Slow push in**
   > Slow camera push in toward [main subject]. Keep the subject almost still while [one subtle environmental detail] moves gently. Preserve [identity or shape details], background geometry, lighting, and composition.

48. **Gentle pull back**
   > The camera pulls back slowly to reveal more of [visible surrounding area]. Keep [main subject] stable and centered. Preserve proportions, edges, background objects, perspective, and the original visual style.

49. **Short lateral pan**
   > Gentle camera pan from left to right across [scene]. [One visible detail] moves subtly. Keep the movement slow and preserve the subject, horizon, architecture, object positions, and lighting.

50. **Controlled tracking move**
   > The camera tracks smoothly beside [moving subject] at a matching pace. Keep the subject's face or shape consistent. Preserve clothing or materials, background direction, scale, and natural motion.

## How to Fix a Prompt That Looks Unrealistic

If a face or object bends, reduce subject motion and strengthen the preservation sentence. If the background changes, replace an orbit or large pan with a static camera or short push in. If everything moves, remove one environmental action. If the clip feels still, replace `dynamic` with a visible verb such as `blinks`, `sways`, `drifts`, or `ripples`. Keep the source image unchanged, adjust one variable, and compare the beginning, middle, and end.

## Start With One Clear Motion

Choose the example closest to your image, replace the visible details, and remove any action the source cannot support. Generate a controlled first version, review the whole clip, and revise one variable at a time.

[Try an Image to Video Prompt](https://vidou.ai/#image-to-video)

*Editorial note: The prompts in this article are instructional starting points and are not presented as benchmarked Vidou outputs. The two editorial images were created with generative AI and reviewed for relevance; they do not depict actual Vidou results.*
```

  5. 在 Blog 列表页添加该文章卡片，使用主图、Category `Prompts`、标题、Meta Description 的首句摘要、日期 `October 12, 2026`，点击卡片进入 canonical URL；保持现有列表顺序规则，并将本文作为最新文章显示。
  6. 为旧文添加反向内链，精确执行以下两处，不改写其他句子：
     - 在 `https://vidou.ai/blog/image-to-video-prompt-guide/` 的 `A Reusable Motion Prompt Template` 小节、详细示例后的解释段末尾追加：`For more starting points across different subjects, browse [50 Image to Video prompt examples for realistic motion](https://vidou.ai/blog/image-to-video-prompt-examples/).`
     - 在 `https://vidou.ai/blog/how-to-animate-a-photo-with-ai/` 的 `Step 4: Write a Clear Motion Prompt` 小节、现有 Portrait、Product、Landscape 三个示例之后追加：`For more starting points, browse [50 Image to Video prompt examples for realistic motion](https://vidou.ai/blog/image-to-video-prompt-examples/).`
  7. 加入与现有文章一致的面包屑和结构化数据。使用 `BlogPosting`，字段至少包括：`headline` 为 H1；`description` 为 Meta Description；`image` 为主图绝对 URL；`datePublished` 和 `dateModified` 均为 `2026-10-12`；`mainEntityOfPage` 与 canonical 一致；`author` 与 `publisher` 均为 `Organization`、名称 `Vidou`、URL `https://vidou.ai/about/`。保留站点现有 `WebSite`、`Organization` 或 `BreadcrumbList` 数据，避免重复冲突。
  8. 将 canonical URL 加入线上 XML Sitemap，`lastmod` 使用实际发布日期 `2026-10-12`。确保页面可索引，不添加 `noindex`，并保持正确的 200 状态。
- 验收标准：目标 URL 返回 200 且不是软 404；SEO Title、Meta Description、H1、canonical、Open Graph、Twitter、作者、发布日期、阅读时长、分类和 `BlogPosting` 数据与要求一致；可见英文正文为上述定稿，包含连续编号且不重不漏的 50 条提示词，正文词数在 1,500–2,200 词范围内；Hero 和正文图在桌面及 390px 移动端清晰显示、比例稳定、无拉伸、无布局偏移，并输出 768px 响应式候选；两图 Alt 和 Caption 精确；正文到 `https://vidou.ai/#image-to-video` 恰好两个链接，其中一个为指定关键词锚文本、一个为末尾 CTA 按钮，不存在第三个首页工具链接或其他工具页链接；可见文案中的 `Image to Video` 不含连字符；三条 Blog 内链可点击且无 404；两篇旧文章均有指定反向链接；Blog 列表有最新文章卡片；Sitemap 包含 canonical；结构化数据可解析且字段与页面可见信息一致；页面键盘可操作、焦点清晰，50 条提示词层级可扫描，移动端无横向滚动。
- 不要修改：不要改写定稿文章、SEO 字段、50 条提示词、指定锚文本、CTA、Alt、Caption 或披露；不要把 `Image to Video`、`Text to Video`、`Text to Image`、`Image Editor` 等可见功能名称写成带连字符形式；不要增加第二个正文工具锚文本、第三个工具转化链接、其他工具页链接、外部竞品链接、效果承诺、虚构测试数据、客户案例或未经验证的技术结论；不要把生成图描述成 Vidou 输出；不要改动首页工具功能、高级工具、credits、登录逻辑、账户数据、API、价格、旧文章正文（除指定的两句反向链接）、其他 Blog 卡片、全站导航、Footer 或无关页面；不要新增 Changelog 条目。
