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

### 补充 Image to Video 完整 Prompt 实例并提高四页 FAQ 的信息密度

- 优先级：`P2`
- 页面或界面：`https://vidou.ai/image-to-video/`、`https://vidou.ai/text-to-video/`、`https://vidou.ai/text-to-image/`、`https://vidou.ai/image-edit/`
- 当前问题与线上证据：2026-10-04 线上正文统计显示，四页不含导航和工具表单的英文内容分别约为 524、463、427、467 词。现有内容已经覆盖页面用途、三步流程、参数或 Prompt 结构、适用场景、结果检查和 FAQ，字数与内容深度足以支撑工具落地页，不需要继续增加通用介绍或更多装饰图。当前明确缺口是 Image to Video 只有零散的 motion、camera、pace 和 stable details 建议，没有像另外三个页面一样给出一条可直接理解的完整 Prompt；四页 FAQ 中的比例、分辨率和 credits 问题大量复述表单及正文，页面专属的 Prompt 决策和排错问题偏少。
- 修改要求：不要整体扩写四页，也不要增加图片。仅完成以下内容改进：

  1. 在 Image to Video 页的三步工作流之后、`More Control for Image to Video Workflows` 之前增加一个原生 HTML 内容模块，使用以下完整英文内容：

     **H2:** `Build a Motion Prompt From the Source Image`

     **Intro:** `The source image already shows the subject, composition, lighting, and visual style. Use the prompt to explain what changes over time: the subject motion, the camera movement, the pace, and the details that must remain stable.`

     **Prompt parts:**

     - `Motion`：`The runner's jacket moves gently in the wind.`
     - `Camera`：`The camera makes a slow push in.`
     - `Pace`：`Keep the movement calm and continuous.`
     - `Preserve`：`Keep the face, logo, and background structure stable.`

     **Complete prompt:** `The runner's jacket moves gently in the wind as the camera makes a slow push in. Keep the movement calm and continuous, and preserve the face, logo, and background structure.`

     使用与现有 Prompt Builder 一致的可扫描 HTML 卡片或分组，不把文字制作进图片，不把静态内容伪装成输入框或按钮。

  2. Image to Video FAQ 保留账户、格式和 credits 三项，用以下两项替换现有比例与分辨率问题：

     - **Question:** `What should I describe in an image to video prompt?`
       **Answer:** `Describe what should move, how the camera should move, the pace of the shot, and any details that must remain stable. Avoid repeating everything already visible in the source image unless a detail needs special protection.`
     - **Question:** `How can I reduce unwanted movement?`
       **Answer:** `Ask for one clear action and one camera move. State which face, logo, product shape, or background detail must stay stable, then review the first and last frames for drift or sudden changes.`

  3. Text to Video FAQ 保留账户、5-second duration 和 credits 三项，用以下两项替换现有比例与分辨率问题：

     - **Question:** `What should a text to video prompt include?`
       **Answer:** `Include a clear subject, one main action, the setting, camera framing or movement, lighting and mood, and the desired pace. Keep every instruction focused on the same moment.`
     - **Question:** `Should I describe more than one scene in a prompt?`
       **Answer:** `Use one concise moment per generation. Several unrelated scenes can make the subject, motion, and camera direction harder to interpret. Generate separate shots when the idea needs multiple scenes.`

  4. Text to Image FAQ 保留账户、Prompt structure 和 credits 三项，用以下两项替换现有比例问题并新增结果检查问题：

     - **Question:** `How do I choose an aspect ratio?`
       **Answer:** `Choose 1:1 for square placements, 9:16 or 3:4 for vertical layouts, and 16:9 or 4:3 for horizontal scenes. Decide where the image will appear before generating so the subject has enough space.`
     - **Question:** `What should I review after generation?`
       **Answer:** `Check the subject, hands, faces, text, object edges, reflections, shadows, and background details. Revise one prompt element at a time when the result needs correction.`

  5. Image Editor FAQ 保留账户、格式、preserve 和 credits 四项，用以下问题替换现有比例问题：

     - **Question:** `Should I request several edits at once?`
       **Answer:** `Start with one main change. Add only the preservation and background constraints needed for that change, then make another edit separately if the image needs a second transformation.`

- 验收标准：Image to Video 页出现一条由 Motion、Camera、Pace、Preserve 组成的完整实例，用户无需阅读其他页面即可理解 Prompt 的组合方法；四页 FAQ 均优先回答各工具专属的 Prompt、场景拆分、比例选择、结果检查或编辑范围问题，不再用比例与分辨率问题重复可见表单。新增或替换内容全部使用上述英文原文，FAQ 第一项默认展开、其余收起，现有 `aria-expanded`、关联面板 ID、键盘操作和结构化数据内容同步一致。四页正文仍保持紧凑，不新增通用 AI 定义、重复功能介绍、关键词堆砌、额外图片或未经验证的效果声明。
- 不要修改：不要改变工具表单、API、账户、credits、格式、比例、分辨率、时长、Audio、生成逻辑、现有主视觉、Title、Meta、canonical 或其他已上线正文；不要新增模型、质量、速度、免费额度、保存期限、版权或商业使用保证；不要给可见功能名称增加连字符。

### 发布第二篇 Blog：Image to Video Prompt Guide

- 优先级：`P1`
- 页面或界面：新文章 `https://vidou.ai/blog/image-to-video-prompt-guide/`；文章列表 `https://vidou.ai/blog/`；反向内链来源 `https://vidou.ai/blog/how-to-animate-a-photo-with-ai/`；Sitemap `https://vidou.ai/sitemap.xml`
- 当前问题与线上证据：2026-10-05 线上 Blog 只有《How to Animate a Photo With AI: Step-by-Step Guide》和旧版 Complete Guide，既定 90 天计划中的第二篇 Prompt Engineering 父文章尚未发布。第一篇已经覆盖选图、上传、比例、生成和检查等完整操作流程，因此第二篇必须专门回答如何把 subject motion、camera movement、pace、environmental motion 和 preservation constraints 组织成清晰的 motion prompt，不能重新写一遍操作教程。线上首页 `https://vidou.ai/#image-to-video` 当前承担免费、无需登录、快速开始的 Image to Video 意图，适合作为本篇初学者 Prompt 教程的唯一转化目标。
- 修改要求：在现有 Blog 模板中发布以下完整内容。下列标题、元数据、署名、正文、链接、CTA、FAQ 和图片 alt 均为最终发布文案，不得改写、扩写、删减或替换。

  **内容定位与发布字段**

  - Primary intent：帮助读者写出结构清晰、动作可执行、便于逐项修改的 Image to Video motion prompt。
  - Target reader：已经有一张源图，但不知道如何描述主体动作、镜头、节奏和稳定约束的初学者与内容创作者。
  - 与现有页面的区别：不重复首页的免费工具定位，不覆盖 `/image-to-video/` 的登录、credits、分辨率、Audio 和保存功能，不重复第一篇从选图到导出的完整流程，也不重复 Complete Guide 的技术原理和宽泛用途。
  - Content type：How-to / Prompt Engineering；Cluster：Prompt Engineering；本篇作为后续 Prompt 文章的父文章。
  - Slug：`image-to-video-prompt-guide`
  - Canonical：`https://vidou.ai/blog/image-to-video-prompt-guide/`
  - Title：`Image to Video Prompt Guide: Write Better Motion Prompts | Vidou`
  - Meta Description：`Learn how to write Image to Video prompts with clear subject motion, camera direction, pace, and preservation constraints, plus practical examples.`
  - H1：`Image to Video Prompt Guide: How to Write Better Motion Prompts`
  - Category：`Guide`
  - Visible publication date：`October 5, 2026`
  - `datePublished`：`2026-10-05`
  - `dateModified`：`2026-10-05`
  - Visible byline：`By Vidou`，其中 `Vidou` 链接到 `https://vidou.ai/about/`
  - Estimated reading time：`9 min read`
  - 唯一转化目标：`https://vidou.ai/#image-to-video`
  - 唯一正文工具锚文本：`free AI image to video generator`
  - 最终 CTA 按钮文案：`Write Your First Motion Prompt With Vidou`
  - Open Graph：`og:type=article`；`og:title` 使用上述 H1；`og:description` 使用上述 Meta Description；`og:url` 使用上述 Canonical；`og:image=https://vidou.ai/images/blog/image-to-video-prompt-guide-hero.jpg`；`og:image:width=1536`；`og:image:height=864`；`og:image:alt=A coastal still image unfolding into controlled motion frames`
  - Twitter：`twitter:card=summary_large_image`；title、description 和 image 分别与 Open Graph 对应字段一致。

  **Article JSON-LD**

  ```json
  {
    "@context": "https://schema.org",
    "@type": "Article",
    "headline": "Image to Video Prompt Guide: How to Write Better Motion Prompts",
    "description": "Learn how to write Image to Video prompts with clear subject motion, camera direction, pace, and preservation constraints, plus practical examples.",
    "image": "https://vidou.ai/images/blog/image-to-video-prompt-guide-hero.jpg",
    "datePublished": "2026-10-05",
    "dateModified": "2026-10-05",
    "author": {
      "@type": "Organization",
      "name": "Vidou",
      "url": "https://vidou.ai/about/"
    },
    "publisher": {
      "@type": "Organization",
      "name": "Vidou",
      "logo": {
        "@type": "ImageObject",
        "url": "https://vidou.ai/logo.png"
      }
    },
    "mainEntityOfPage": {
      "@type": "WebPage",
      "@id": "https://vidou.ai/blog/image-to-video-prompt-guide/"
    }
  }
  ```

  **最终图片包**

  1. Hero image
     - 源文件：`assets/vidou-blog/image-to-video-prompt-guide/image-to-video-prompt-guide-hero.jpg`
     - 最终文件名：`image-to-video-prompt-guide-hero.jpg`
     - 格式与尺寸：JPEG，1536×864，16:9
     - 发布 URL：`https://vidou.ai/images/blog/image-to-video-prompt-guide-hero.jpg`
     - 位置：H1、署名信息之后，正文导语之前；同时用于 Open Graph、Twitter 和 Article JSON-LD `image`
     - Editorial purpose：用同一海岸场景的连续画面和克制运动轨迹表示静态图像、时间推进与镜头运动之间的关系，不表示真实 Vidou 输出。
     - Alt：`A coastal still image unfolding into controlled motion frames`
     - 加载：写入 `width="1536"`、`height="864"`，使用响应式 `srcset` 与 `sizes`；作为 LCP 候选图不得默认 lazy-load。

  2. In-article image
     - 源文件：`assets/vidou-blog/image-to-video-prompt-guide/motion-prompt-anatomy.jpg`
     - 最终文件名：`motion-prompt-anatomy.jpg`
     - 格式与尺寸：JPEG，1536×864，16:9
     - 发布 URL：`https://vidou.ai/images/blog/motion-prompt-anatomy.jpg`
     - 位置：`The Five Decisions Inside a Useful Motion Prompt` 小节五项列表之后、`Build a Prompt in Five Passes` 之前
     - Editorial purpose：用骑行场景中的主体运动、镜头方向、节奏线和稳定构图区域辅助解释 Prompt 的四类可控信息，不表示真实 Vidou 输出。
     - Alt：`Visual guide to subject motion, camera direction, pace, and preserved details`
     - 加载：写入 `width="1536"`、`height="864"`、响应式 `srcset` 与 `sizes`，并使用 `loading="lazy"` 和 `decoding="async"`。

  图片只能使用上述两个最终文件。不得重新生成、搜索、下载、重画或替换素材；不得把图片描述成 Vidou 的真实生成结果。执行端可以在不改变构图、内容和颜色关系的前提下生成响应式尺寸，但不得用其他图替代原图。

  **完整英文文章正文（精确发布文案）**

  A useful Image to Video prompt tells the system what should change over time and what should remain stable. Start with one visible subject action, add one camera instruction only when it helps, describe the pace in plain language, and protect any face, product, logo, or background detail that must not drift. A focused prompt is usually easier to interpret and revise than a long list of cinematic adjectives.

  This guide explains how to build that prompt deliberately. It focuses on motion language rather than the full creation workflow. If you need the complete process from choosing a source image through reviewing the finished clip, read [how to animate a photo with AI](https://vidou.ai/blog/how-to-animate-a-photo-with-ai/). For a broader introduction to the technology and its common uses, see the [complete guide to AI image to video generation](https://vidou.ai/blog/ai-image-to-video-guide/).

  ## What an Image to Video Prompt Actually Controls

  The source image already contains the subject, composition, colors, lighting, and visible background. Your prompt should not spend most of its space describing what the image already shows. Its main job is to explain what happens next.

  In practice, a motion prompt can guide five decisions:

  1. What the main subject does.
  2. Whether and how the camera moves.
  3. What moves in the environment.
  4. How fast or intense the movement feels.
  5. Which visible details should remain stable.

  Think of the prompt as direction for a short shot, not a description for creating a new image. The clearer the hierarchy, the easier it is to identify which instruction needs revision when the result is not what you expected.

  ## The Five Decisions Inside a Useful Motion Prompt

  ### 1. Subject Motion

  Begin with one action that can be seen. “Make it dynamic” is an intention, not an action. “The runner looks toward the road while her jacket moves in the wind” gives the system visible changes to interpret.

  Useful subject motion verbs include:

  - turns
  - looks
  - blinks
  - walks
  - sways
  - rises
  - drifts
  - ripples
  - rotates slowly

  Keep the action compatible with the source image. A close portrait can support blinking, a slight head turn, or moving hair more naturally than a request for the person to run out of frame. A single product photo can support a slow reveal or moving light, but a complete rotation asks the system to invent surfaces that are not visible.

  ### 2. Camera Movement

  Add camera movement only when it improves the shot. A slow push in can direct attention toward a face or product. A pull back can reveal more context. A gentle pan can follow a wide landscape. A static camera can be the best choice when the subject already has enough movement.

  Use one clear camera instruction:

  - `Slow camera push in.`
  - `Gentle pan from left to right.`
  - `Camera remains static.`
  - `Smooth tracking movement beside the subject.`

  Avoid combining a push, orbit, tilt, pan, and zoom in the same short prompt. Competing camera directions make the intended framing less clear and may require the system to invent too much unseen space.

  ### 3. Environmental Motion

  Environmental movement can make a shot feel alive without forcing the main subject to perform a large action. Water can ripple, clouds can drift, leaves can move in a breeze, steam can rise, and light can shift subtly across a surface.

  Treat atmosphere as support. If the subject turns, the camera moves, rain begins, lights flash, fog rolls in, and objects enter the scene at once, the prompt no longer has a clear priority. Choose the environmental motion that best supports the main action.

  ### 4. Pace and Intensity

  Words such as `slow`, `gentle`, `subtle`, `steady`, and `calm` help define restrained movement. Words such as `rapid`, `sharp`, or `energetic` ask for greater intensity, but they can also increase the chance of abrupt motion or visible distortion.

  Pace should match the source. A quiet portrait often benefits from minimal movement. A sports image may support stronger motion if the pose, framing, and background provide enough visual information. Describe the speed you want instead of relying on broad words such as “epic” or “cinematic.”

  ### 5. Details to Preserve

  Use preservation language for details that matter to the final use. Examples include a face, hairstyle, product silhouette, logo, label, clothing pattern, building geometry, or background layout.

  Write constraints as direct instructions:

  - `Keep the face and hairstyle consistent.`
  - `Preserve the product shape, logo, label, and colors.`
  - `Keep the buildings and background layout stable.`
  - `Do not add new objects to the scene.`

  Do not list every pixel in the image. Protect the few details whose change would make the clip unusable.

  ![Visual guide to subject motion, camera direction, pace, and preserved details](https://vidou.ai/images/blog/motion-prompt-anatomy.jpg)

  ## Build a Prompt in Five Passes

  A reliable way to write a motion prompt is to add one decision at a time.

  Start with the subject:

  > The cyclist looks toward the road.

  Add one visible secondary movement:

  > The cyclist looks toward the road while her jacket moves slightly in the wind.

  Add the camera:

  > The cyclist looks toward the road while her jacket moves slightly in the wind. Slow camera push in.

  Define the pace and environment:

  > The cyclist looks toward the road while her jacket moves slightly in the wind. Slow camera push in. Trees move gently in the background with a natural, calm pace.

  Finish with the important constraints:

  > The cyclist looks toward the road while her jacket moves slightly in the wind. Slow camera push in. Trees move gently in the background with a natural, calm pace. Keep her face, bicycle, clothing, and the street layout consistent.

  Each sentence has a job. If the first version is too busy, remove the environmental motion. If the framing changes too much, replace the push in with a static camera. If the subject drifts, strengthen the preservation instruction. This structure makes revision more controlled than rewriting everything at once.

  ## Weak Prompts and Better Rewrites

  ### Portrait

  **Weak:**

  > Make this portrait cinematic and beautiful.

  **Better:**

  > The woman blinks naturally and turns her gaze slightly toward the camera. Her hair moves in a light breeze. Slow camera push in, soft movement, and a calm pace. Keep her face, clothing, and background consistent.

  The rewrite replaces abstract praise with visible actions, a camera direction, a pace, and specific details to preserve.

  ### Product

  **Weak:**

  > Create an exciting advertisement for this sneaker.

  **Better:**

  > The camera moves slowly toward the sneaker as a soft highlight travels across the side. Keep the shoe shape, logo, materials, colors, and studio background unchanged.

  The prompt stays within what a single product image can support. It does not request a hidden side of the shoe or an entirely new scene.

  Ready to test a prompt? Begin with the better version, review the full frame, and change only one instruction before generating another variation.

  ## Revise One Variable at a Time

  When a result needs improvement, keep the source image and the rest of the prompt unchanged while testing one adjustment.

  If motion is too strong, replace `energetic` with `gentle` or remove a secondary action. If the background changes, reduce the camera movement and add a stability constraint. If a face changes, request smaller facial motion and preserve facial proportions. If the result feels still, replace an abstract instruction with one visible verb.

  Use this revision order:

  1. Confirm the main action.
  2. Reduce or remove secondary movement.
  3. Simplify the camera direction.
  4. Clarify the pace.
  5. Strengthen one preservation constraint.

  This process does not guarantee an identical result on every attempt. It makes your tests easier to compare because each revision has a clear purpose.

  ## A Reusable Motion Prompt Template

  Use this structure as a starting point:

  > [Main subject] [one visible action]. [One camera instruction]. [One supporting environmental movement]. [Pace and mood]. Keep [important visible details] consistent.

  Short version:

  > The subject moves gently. Slow camera push in. Keep the face and background stable.

  Detailed version:

  > The chef places the finished dish on the counter as steam rises slowly. Gentle camera push in, warm kitchen light, and a natural pace. Keep the chef's face, hands, plate shape, food arrangement, and background consistent.

  Use the short version when the image and action are simple. Add detail only when it removes ambiguity or protects something important. You can try the structure in Vidou's [free AI image to video generator](https://vidou.ai/#image-to-video), then revise one line at a time after reviewing the result.

  ## Motion Prompt Checklist

  Before generating, confirm that your prompt:

  - Names one main subject action.
  - Uses no more than one camera direction.
  - Adds environmental motion only when it supports the subject.
  - States the intended pace in plain language.
  - Protects the few details that must remain stable.
  - Avoids asking for several scenes in one generation.
  - Does not depend on hidden visual information.
  - Gives each sentence a clear purpose.

  ## Frequently Asked Questions

  ### How long should an Image to Video prompt be?

  Use enough words to define the main action, camera, pace, and essential constraints. A few focused sentences are often more useful than a long paragraph filled with mood words and competing actions.

  ### Should I describe everything visible in the image?

  No. The image already supplies the subject and visual setting. Describe what should move and call out only the visible details that must remain stable.

  ### Should every prompt include camera movement?

  No. A static camera is often better when the subject or environment already has meaningful motion. Add camera movement only when it supports the composition and the purpose of the shot.

  ### How do I keep a face, logo, or product stable?

  Start with a clear source image, request restrained movement, and name the important detail directly in a preservation sentence. Avoid camera moves or rotations that require the system to invent hidden views.

  ## Write a Clearer Motion Prompt

  A strong motion prompt does not need to sound technical. It needs a clear priority. Name one visible action, choose a camera direction only when it helps, control the pace, and protect the details that matter. Then review the full frame and revise one variable at a time.

  [Write Your First Motion Prompt With Vidou](https://vidou.ai/#image-to-video)

  **Editorial note:** This guide was prepared from Vidou's current public interface, its published educational pages, and general prompt design principles. The prompt examples are instructional and are not presented as benchmarked Vidou outputs. The two editorial illustrations were created with generative AI and reviewed for relevance; they do not depict actual Vidou results.

  **发布与反向内链要求**

  - 把新文章加入 `/blog/` 列表，显示 `Guide`、`October 5, 2026`、`9 min read` 和上述 Meta Description；列表卡片使用 Hero image 与对应 alt。
  - 在 `https://vidou.ai/blog/how-to-animate-a-photo-with-ai/` 的 `Step 4: Write a Clear Motion Prompt` 小节末尾增加一句：`For a deeper explanation of prompt structure and revision, read the [Image to Video prompt guide](https://vidou.ai/blog/image-to-video-prompt-guide/).` 不改写该文章其他内容。
  - 将 Canonical 加入 Sitemap，`lastmod` 使用真实发布日期 `2026-10-05`；不要修改其他 URL 的 `lastmod`。
  - 正文中的 Hero 由文章模板呈现；正文第二张图按上述精确位置插入。图片不得包裹链接。

- 验收标准：新文章线上返回 200，Canonical、Title、Meta Description、H1、Open Graph、Twitter 和 Article JSON-LD 与任务完全一致；可见作者为 `By Vidou` 并链接 About，日期为 October 5, 2026。英文正文不含图片说明和 Editorial note 时达到 1,200–1,800 词且无关键词堆砌；所有可见功能名称均写作 `Image to Video`，不写 `Image-to-Video`。正文恰好只有一个指向 `https://vidou.ai/#image-to-video` 的上下文锚文本 `free AI image to video generator`，结尾 CTA 按钮是第二个且最后一个指向同一目标的链接；正文、图片、FAQ 和新增文章导航中没有第三个工具链接。两条已有文章内链有效，第一篇旧文章出现一条指向新文章的反向内链。两个最终图片文件均成功加载、无文字水印、无虚构 Vidou 输出，图片尺寸、alt、加载策略和社交预览正确；新 URL 出现在 Blog 列表和 Sitemap 中，Sitemap `lastmod` 与发布日期一致；桌面与移动端无溢出、裁切、布局跳动或不可见 CTA。
- 不要修改：不要改写任务提供的英文文章、SEO 字段、JSON-LD、图片、alt 或 CTA；不要添加年份标题、第三个工具链接、其他工具页链接、竞品链接、未经验证的性能或效果声明、虚构测试、虚构作者、用户案例、排名、流量或转化数据；不要把 `/image-to-video/` 的登录、credits、分辨率、Audio 或保存能力写进本篇；不要修改第一篇除指定反向内链以外的内容，也不要修改 Complete Guide、工具表单、API、账户、定价或生成逻辑。
