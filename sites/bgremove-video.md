---
site_id: "bgremove-video"
name: "BGRemove"
production_url: "https://bgremove.video/"
changelog_url: "https://bgremove.video/changelog/"
delivery_method: "direct_publish"
target_repository: "not_applicable"
default_branch: "not_applicable"
updated_at: "2026-09-09"
---

# BGRemove 当前待办事项

## 已批准任务

### 修正竖屏视频在换背景工作区仍被旋转的问题

- 优先级：`P1`
- 页面或界面：`https://bgremove.video/change-background/` 的视频预览与 MP4 导出
- 当前问题与线上证据：用户于 2026-09-08 使用真实账号和竖屏素材在线上生产环境复测，确认视频进入换背景功能区域后仍会被旋转 90 度，以横屏方向播放。线上 `Sep 6, 2026 · Fix · 2.0` 更新日志声称竖屏方向已经修复，但该声明与实际行为不一致。用户同时确认 `Colour`、`Blur` 的选择顺序和处理状态提示等其他换背景问题已经解决。
- 修改要求：正确识别进入换背景工作区的透明成品视频的实际显示方向、方向元数据、显示矩阵和固有宽高，在读取、预览、背景合成与 MP4 导出流程中只执行一次必要的方向归一化。浏览器或解码器已经应用方向信息时不得再次旋转；不得用固定旋转角度或盲目互换宽高处理全部竖屏素材。至少覆盖手机拍摄且携带方向元数据的 MP4/MOV 经过去背景后生成的透明作品，以及已经按像素方向归一化的竖屏 WebM。
- 验收标准：使用真实竖屏、横屏和方形视频逐一验证 `None`、`Colour`、`Blur`、`Image`、`Video` 五种背景状态；竖屏视频始终保持竖屏且没有 90、180 或 270 度误旋转，横屏与方形视频方向不变；预览与导出的 MP4 方向、画面比例和宽高关系一致；手机和桌面端结果一致。
- 不要修改：已经解决的 `Colour`、`Blur` 选择流程和处理状态反馈；主体的原始宽高比、主体在画布中的既定缩放与位置、视频时长、帧率、音频、透明边缘质量及现有背景类型。

### 新增 Remove Green Screen SEO 功能页并改造顶部 Remove 菜单

- 优先级：`P1`
- 页面或界面：新增 `https://bgremove.video/green-screen-remover/`；全站桌面端和移动端顶部导航的 `Remove` 菜单
- 当前问题与线上证据：用户于 2026-09-09 已批准新增 `Remove Green Screen` 专营页，并确认 URL、内链和全部产品规则。当前线上顶部导航的 `Remove` 仍是直接指向首页的单一链接，尚无 `/green-screen-remover/` 页面。搜索结果调研显示，同类排名页普遍采用工具首屏、差异化优势、三步流程、原理说明和 FAQ；部分页面存在关键词堆砌、绝对效果承诺或未经核实的编辑器兼容性声明，因此新页面需要以低权重新站能够可信支撑的窄主题和真实产品边界切入。
- 修改要求：按下方两段定稿新增英文页面并复用站内现有 AI 视频上传处理组件，不得另造处理引擎或参数。把全站顶部 `Remove` 改成可访问的下拉菜单，菜单内只有两个视觉上呈按钮式的语义链接：`Remove Video Background` 指向 `/`，`Remove Green Screen` 指向 `/green-screen-remover/`；支持键盘、触屏、鼠标、焦点管理、展开状态和菜单外关闭。新页必须可索引、自引用 canonical、加入 XML sitemap，并使用一个 H1、清晰的 H2/H3、可解析 FAQ 与同步的 `FAQPage` JSON-LD。生成并人工检查两张真实摄影风格配图，替换 HTML 中的图片路径变量；不得把 AI 图描述为真实客户素材。
- 验收标准：`/green-screen-remover/` 返回 `200`，没有 `noindex`，canonical 为自身且出现在 sitemap；Title 为 `Remove Green Screen from Video Online Free`（42 字符），meta description 为下方 152 字符定稿，页面只有一个 H1 且包含核心关键词。顶部菜单在桌面端和移动端均可操作，两个链接目标正确且无 404，当前页状态明确。既有上传组件完成登录、上传、处理、透明 WebM 下载和转到换背景流程；页面文案、可见 FAQ 与 JSON-LD 使用下方相同事实；两张图片无人物或设备畸形、无文字水印并具备准确 alt；`390px`、`768px` 和常见桌面宽度无横向滚动或内容裁切。
- 不要修改：首页现有 H1 与定位、AI 处理能力、额度计算、认证、数据保留、现有 `/tools/green-screen-alternative/` 内容、换背景功能、页脚 Product 列或其他顶部菜单项。不要新增手动 chroma key 控件、本地处理、实时预览、速度、成功率、客户评价、付费套餐、商业使用授权、编辑器兼容保证或其他未确认能力；本次不创建多语言版本。

#### 第一段：完整英文文案稿

```text
=== 1. TOP TOOL AREA ===

Eyebrow: AI Green Screen Remover

H1: Remove Green Screen from Video Online Free

Intro: Upload footage shot against green. BGRemove finds the subject with AI instead of asking you to pick a key color or tune tolerance sliders. It can work through folds, shadows, uneven light, and mild green spill, then give you a transparent result or let you add a different background.

Tool heading: Upload a Green Screen Video

Tool helper: MP4, MOV, WebM, M4V, and GIF · Up to 60 seconds · Maximum 2 GB

Primary action: Remove Green Screen

Processing state: Removing the green screen…

Complete state: Your subject is ready. Download the transparent video or choose a new background.

Allowance line: 3 free background removals per 24-hour window, shared with Remove Video Background · No watermark

=== 2. CORE DIFFERENTIATORS ===

H2: A Green Screen Remover That Does Not Need a Perfect Screen

Intro: A clean screen still helps, but it should not have to be a studio-perfect wall. BGRemove uses AI subject detection rather than a single color threshold, so common shooting flaws do not force you into a long manual keying session.

Card 1
H3: Skip the chroma key controls
Body: You do not need to sample a shade of green, balance tolerance, or chase the edge frame by frame. Upload the clip and let AI identify the person or product.

Card 2
H3: Work with wrinkles, shadows, and light spill
Body: A folded cloth, a darker patch, or a little reflected green can confuse a color-only key. AI looks for the subject, not one exact background color. Review difficult edges before you publish, especially around fast motion, loose hair, glass, or reflective objects.

Card 3
H3: Use it in your browser
Body: There is no software to install and no timeline to configure. The green screen remover video workflow stays focused: upload, review the cutout, then download it or choose another background.

Card 4
H3: Try your footage before changing your workflow
Body: Each signed-in account gets up to 3 successful background removals per 24-hour window, shared with Remove Video Background. There are no paid plans. Test a representative clip first so you can judge the edges on the footage you actually shoot.

AI image prompt: Photorealistic 16:9 commercial video-production still. A real adult creator standing several feet in front of an imperfect green fabric backdrop in a small home studio. The green cloth has visible soft folds, one natural shadow, and slight green spill along one shoulder, while the subject remains sharply lit and anatomically correct. Show honest practical conditions, not a perfect soundstage. Natural skin, realistic hair and hands, restrained lighting, no text, no logos, no watermark, no UI, no split-screen labels, no distorted body parts. Leave clear negative space on the right for webpage copy.

Image alt: A creator filming in front of a wrinkled green screen with a soft shadow

=== 3. NO GREEN SCREEN TRANSITION ===

H2: No Green Screen? Remove Any Background With AI.

Body: Your footage does not need a colored backdrop. Use BGRemove to remove video background from a room, street, store, classroom, or wherever you recorded.

CTA: Remove Video Background
Link: /

=== 4. HOW IT WORKS ===

H2: How to Remove a Green Background From Video

Step 1
H3: Upload your green screen footage
Body: Choose the clip you want to cut out. Use clear footage where the subject stays visible, and start with a short representative section if the full video contains difficult motion.

Step 2
H3: Let AI separate the subject
Body: BGRemove follows the subject across the video and removes the green background without asking you to choose a key color or adjust chroma key sliders.

Step 3
H3: Download transparency or add a new scene
Body: Review the edges, download a transparent WebM using VP9 with alpha, or use the background tool to place a color, blur, image, or video behind the subject and export an MP4.

Primary CTA: Remove Green Screen

Secondary link: Learn how BGRemove works
Link: /tools/green-screen-alternative/

AI image prompt: Photorealistic wide 16:9 three-stage production workflow in one coherent image, with the exact same adult presenter repeated from the exact same source frame in all three stages. Left: presenter in front of a wrinkled green cloth. Center: identical presenter with the background removed over a neutral transparency checkerboard. Right: identical presenter placed in a realistic home-office scene. Preserve the same face, pose, clothing, hair, body proportions, scale, and orientation in every stage. Accurate anatomy and edges, no text, no numbers, no arrows, no logos, no watermark, no interface chrome, no mismatched identity, no warped shoulders or hands.

Image alt: The same presenter shown on a green screen, transparent background, and finished scene

=== 5. GREEN SCREEN REMOVAL EXPLAINED ===

H2: What Is Green Screen Removal—and How Does AI Make It Easier?

Green screen removal, also called chroma keying, separates a filmed subject from a colored backdrop so the background can become transparent or be replaced. A traditional chroma key remover looks for a selected shade of green. You choose the color, adjust tolerance and edge controls, then suppress green reflected onto skin, hair, or clothing. That works well in a controlled studio, but a wrinkled cloth, a hard shadow, or uneven lighting can create several shades of green and leave holes or halos.

BGRemove takes a different route. Its AI looks for the subject rather than relying on one background color. Green footage is still useful because it creates strong visual separation, but the screen does not have to be perfectly flat or evenly lit. The model can treat folds, shadows, and mild spill as background while keeping the person or product in view across the clip. That makes it a practical green screen remover for gaming clips, lessons, product demos, social videos, and school projects when you do not want to tune chroma key controls by hand.

AI does not make every shot perfect. Fast motion, heavy blur, flyaway hair, transparent objects, reflective surfaces, or green clothing close to the backdrop can still produce difficult edges. If you need frame-by-frame matte control for professional compositing, use a full editor. For a straightforward green screen video remover workflow, upload the clip, review the result, and either keep the transparent output or choose a new background.

=== 6. FAQ ===

H2: Green Screen Remover FAQ

Q: Can BGRemove handle a wrinkled or shadowy green screen?
A: Yes, AI subject detection can handle folds, uneven shades, shadows, and mild green spill because it is not removing one exact color. A cleaner recording can still produce a better edge. Review hair, motion blur, transparent objects, and reflective surfaces before you publish.

Q: How is this different from a manual chroma key remover?
A: A manual chroma key removes a selected color and usually gives you controls for tolerance, edge softness, and spill suppression. BGRemove identifies the subject with AI instead, so you do not have to pick the green shade or tune those controls. Use a professional editor when you need frame-by-frame matte adjustments.

Q: What video formats and limits are supported?
A: BGRemove accepts MP4, MOV, WebM, M4V, and GIF. Each file can be up to 2 GB and 60 seconds long. The transparent output is WebM using VP9 with alpha.

Q: Can I use the transparent video in CapCut or Premiere Pro?
A: BGRemove exports transparent WebM using VP9 with alpha. Whether transparency imports correctly depends on the editor, version, platform, and codec support. Check the current CapCut or Premiere Pro documentation before you start. If your editor does not accept WebM alpha, use BGRemove to add the final background and export an MP4. Renaming a file extension does not change its codec.

Q: Can I remove green screen from video for free?
A: Yes. Each signed-in account can complete up to 3 successful background removals per 24-hour window. The allowance is shared with Remove Video Background. There are no paid plans.

Q: Do I need to sign in?
A: Yes. You must sign in before processing a video.

Q: Will the downloaded video have a watermark?
A: No. Downloads do not include a watermark.

Q: Can I replace the green screen with my own background?
A: Yes. After the green background is removed, you can keep the result transparent or place a color, blur, image, or video behind the subject. The finished background-replaced video is exported as an MP4.

Q: When should I use manual chroma key software instead?
A: Use a full editor when the shot needs frame-by-frame masks, precise spill correction, detailed work around transparent or reflective objects, or exact control over hair and heavy motion blur. BGRemove is intended for automatic subject separation without manual key settings.

=== SEO METADATA ===

Title: Remove Green Screen from Video Online Free
Character count: 42

Meta description: Remove green screen from video with AI, even with wrinkles, shadows, or spill. Try it online, then download a transparent video or add a new background.
Character count: 152
```

#### 第二段：语义化 HTML 页面骨架

```html
<!doctype html>
<html lang="en">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>Remove Green Screen from Video Online Free</title>
  <meta name="description" content="Remove green screen from video with AI, even with wrinkles, shadows, or spill. Try it online, then download a transparent video or add a new background.">
  <link rel="canonical" href="https://bgremove.video/green-screen-remover/">

  <script type="application/ld+json">
  {
    "@context": "https://schema.org",
    "@type": "FAQPage",
    "mainEntity": [
      {
        "@type": "Question",
        "name": "Can BGRemove handle a wrinkled or shadowy green screen?",
        "acceptedAnswer": {"@type": "Answer", "text": "Yes, AI subject detection can handle folds, uneven shades, shadows, and mild green spill because it is not removing one exact color. A cleaner recording can still produce a better edge. Review hair, motion blur, transparent objects, and reflective surfaces before you publish."}
      },
      {
        "@type": "Question",
        "name": "How is this different from a manual chroma key remover?",
        "acceptedAnswer": {"@type": "Answer", "text": "A manual chroma key removes a selected color and usually gives you controls for tolerance, edge softness, and spill suppression. BGRemove identifies the subject with AI instead, so you do not have to pick the green shade or tune those controls. Use a professional editor when you need frame-by-frame matte adjustments."}
      },
      {
        "@type": "Question",
        "name": "What video formats and limits are supported?",
        "acceptedAnswer": {"@type": "Answer", "text": "BGRemove accepts MP4, MOV, WebM, M4V, and GIF. Each file can be up to 2 GB and 60 seconds long. The transparent output is WebM using VP9 with alpha."}
      },
      {
        "@type": "Question",
        "name": "Can I use the transparent video in CapCut or Premiere Pro?",
        "acceptedAnswer": {"@type": "Answer", "text": "BGRemove exports transparent WebM using VP9 with alpha. Whether transparency imports correctly depends on the editor, version, platform, and codec support. Check the current CapCut or Premiere Pro documentation before you start. If your editor does not accept WebM alpha, use BGRemove to add the final background and export an MP4. Renaming a file extension does not change its codec."}
      },
      {
        "@type": "Question",
        "name": "Can I remove green screen from video for free?",
        "acceptedAnswer": {"@type": "Answer", "text": "Yes. Each signed-in account can complete up to 3 successful background removals per 24-hour window. The allowance is shared with Remove Video Background. There are no paid plans."}
      },
      {
        "@type": "Question",
        "name": "Do I need to sign in?",
        "acceptedAnswer": {"@type": "Answer", "text": "Yes. You must sign in before processing a video."}
      },
      {
        "@type": "Question",
        "name": "Will the downloaded video have a watermark?",
        "acceptedAnswer": {"@type": "Answer", "text": "No. Downloads do not include a watermark."}
      },
      {
        "@type": "Question",
        "name": "Can I replace the green screen with my own background?",
        "acceptedAnswer": {"@type": "Answer", "text": "Yes. After the green background is removed, you can keep the result transparent or place a color, blur, image, or video behind the subject. The finished background-replaced video is exported as an MP4."}
      },
      {
        "@type": "Question",
        "name": "When should I use manual chroma key software instead?",
        "acceptedAnswer": {"@type": "Answer", "text": "Use a full editor when the shot needs frame-by-frame masks, precise spill correction, detailed work around transparent or reflective objects, or exact control over hair and heavy motion blur. BGRemove is intended for automatic subject separation without manual key settings."}
      }
    ]
  }
  </script>
</head>
<body>
  <header class="site-header">
    <a class="site-logo" href="/" aria-label="BGRemove home">BGRemove</a>
    <nav class="primary-navigation" aria-label="Primary navigation">
      <details class="navigation-dropdown">
        <summary>Remove</summary>
        <ul class="navigation-dropdown__menu">
          <li><a href="/">Remove Video Background</a></li>
          <li><a href="/green-screen-remover/" aria-current="page">Remove Green Screen</a></li>
        </ul>
      </details>
      <a href="/change-background/">Change background</a>
      <a href="/how-it-works/">How it works</a>
      <a href="/use-cases/">Use cases</a>
      <a href="/pricing/">Free Access</a>
      <a href="/faq/">FAQ</a>
    </nav>
  </header>

  <main id="main-content">
    <section class="green-screen-hero" aria-labelledby="green-screen-title">
      <p class="eyebrow">AI Green Screen Remover</p>
      <h1 id="green-screen-title">Remove Green Screen from Video Online Free</h1>
      <p>Upload footage shot against green. BGRemove finds the subject with AI instead of asking you to pick a key color or tune tolerance sliders. It can work through folds, shadows, uneven light, and mild green spill, then give you a transparent result or let you add a different background.</p>
      <p class="tool-heading">Upload a Green Screen Video</p>
      <p class="tool-helper">MP4, MOV, WebM, M4V, and GIF · Up to 60 seconds · Maximum 2 GB</p>
      <!-- 此处嵌入站内现有 AI 视频上传处理组件 -->
      <!-- 使用现有组件状态映射以下文案：Remove Green Screen；Removing the green screen…；Your subject is ready. Download the transparent video or choose a new background. -->
      <p class="allowance-line">3 free background removals per 24-hour window, shared with Remove Video Background · No watermark</p>
    </section>

    <section class="green-screen-features" aria-labelledby="features-title">
      <div class="section-copy">
        <h2 id="features-title">A Green Screen Remover That Does Not Need a Perfect Screen</h2>
        <p>A clean screen still helps, but it should not have to be a studio-perfect wall. BGRemove uses AI subject detection rather than a single color threshold, so common shooting flaws do not force you into a long manual keying session.</p>
      </div>
      <div class="feature-grid">
        <article><h3>Skip the chroma key controls</h3><p>You do not need to sample a shade of green, balance tolerance, or chase the edge frame by frame. Upload the clip and let AI identify the person or product.</p></article>
        <article><h3>Work with wrinkles, shadows, and light spill</h3><p>A folded cloth, a darker patch, or a little reflected green can confuse a color-only key. AI looks for the subject, not one exact background color. Review difficult edges before you publish, especially around fast motion, loose hair, glass, or reflective objects.</p></article>
        <article><h3>Use it in your browser</h3><p>There is no software to install and no timeline to configure. The green screen remover video workflow stays focused: upload, review the cutout, then download it or choose another background.</p></article>
        <article><h3>Try your footage before changing your workflow</h3><p>Each signed-in account gets up to 3 successful background removals per 24-hour window, shared with Remove Video Background. There are no paid plans. Test a representative clip first so you can judge the edges on the footage you actually shoot.</p></article>
      </div>
      <!-- AI IMAGE PROMPT: Photorealistic 16:9 commercial video-production still. A real adult creator standing several feet in front of an imperfect green fabric backdrop in a small home studio. The green cloth has visible soft folds, one natural shadow, and slight green spill along one shoulder, while the subject remains sharply lit and anatomically correct. Show honest practical conditions, not a perfect soundstage. Natural skin, realistic hair and hands, restrained lighting, no text, no logos, no watermark, no UI, no split-screen labels, no distorted body parts. Leave clear negative space on the right for webpage copy. -->
      <img src="{{imperfect-green-screen-image-src}}" alt="A creator filming in front of a wrinkled green screen with a soft shadow" width="1600" height="900" loading="lazy">
    </section>

    <section class="any-background-cta" aria-labelledby="any-background-title">
      <h2 id="any-background-title">No Green Screen? Remove Any Background With AI.</h2>
      <p>Your footage does not need a colored backdrop. Use BGRemove to remove video background from a room, street, store, classroom, or wherever you recorded.</p>
      <a class="button" href="/">Remove Video Background</a>
    </section>

    <section class="green-screen-steps" aria-labelledby="steps-title">
      <h2 id="steps-title">How to Remove a Green Background From Video</h2>
      <ol class="step-list">
        <li><article><h3>Upload your green screen footage</h3><p>Choose the clip you want to cut out. Use clear footage where the subject stays visible, and start with a short representative section if the full video contains difficult motion.</p></article></li>
        <li><article><h3>Let AI separate the subject</h3><p>BGRemove follows the subject across the video and removes the green background without asking you to choose a key color or adjust chroma key sliders.</p></article></li>
        <li><article><h3>Download transparency or add a new scene</h3><p>Review the edges, download a transparent WebM using VP9 with alpha, or use the background tool to place a color, blur, image, or video behind the subject and export an MP4.</p></article></li>
      </ol>
      <!-- AI IMAGE PROMPT: Photorealistic wide 16:9 three-stage production workflow in one coherent image, with the exact same adult presenter repeated from the exact same source frame in all three stages. Left: presenter in front of a wrinkled green cloth. Center: identical presenter with the background removed over a neutral transparency checkerboard. Right: identical presenter placed in a realistic home-office scene. Preserve the same face, pose, clothing, hair, body proportions, scale, and orientation in every stage. Accurate anatomy and edges, no text, no numbers, no arrows, no logos, no watermark, no interface chrome, no mismatched identity, no warped shoulders or hands. -->
      <img src="{{three-stage-workflow-image-src}}" alt="The same presenter shown on a green screen, transparent background, and finished scene" width="1600" height="900" loading="lazy">
      <a class="button" href="#green-screen-title">Remove Green Screen</a>
      <a href="/tools/green-screen-alternative/">Learn how BGRemove works</a>
    </section>

    <section class="green-screen-explainer" aria-labelledby="explainer-title">
      <h2 id="explainer-title">What Is Green Screen Removal—and How Does AI Make It Easier?</h2>
      <p>Green screen removal, also called chroma keying, separates a filmed subject from a colored backdrop so the background can become transparent or be replaced. A traditional chroma key remover looks for a selected shade of green. You choose the color, adjust tolerance and edge controls, then suppress green reflected onto skin, hair, or clothing. That works well in a controlled studio, but a wrinkled cloth, a hard shadow, or uneven lighting can create several shades of green and leave holes or halos.</p>
      <p>BGRemove takes a different route. Its AI looks for the subject rather than relying on one background color. Green footage is still useful because it creates strong visual separation, but the screen does not have to be perfectly flat or evenly lit. The model can treat folds, shadows, and mild spill as background while keeping the person or product in view across the clip. That makes it a practical green screen remover for gaming clips, lessons, product demos, social videos, and school projects when you do not want to tune chroma key controls by hand.</p>
      <p>AI does not make every shot perfect. Fast motion, heavy blur, flyaway hair, transparent objects, reflective surfaces, or green clothing close to the backdrop can still produce difficult edges. If you need frame-by-frame matte control for professional compositing, use a full editor. For a straightforward green screen video remover workflow, upload the clip, review the result, and either keep the transparent output or choose a new background.</p>
    </section>

    <section class="green-screen-faq" aria-labelledby="faq-title">
      <h2 id="faq-title">Green Screen Remover FAQ</h2>
      <details><summary>Can BGRemove handle a wrinkled or shadowy green screen?</summary><p>Yes, AI subject detection can handle folds, uneven shades, shadows, and mild green spill because it is not removing one exact color. A cleaner recording can still produce a better edge. Review hair, motion blur, transparent objects, and reflective surfaces before you publish.</p></details>
      <details><summary>How is this different from a manual chroma key remover?</summary><p>A manual chroma key removes a selected color and usually gives you controls for tolerance, edge softness, and spill suppression. BGRemove identifies the subject with AI instead, so you do not have to pick the green shade or tune those controls. Use a professional editor when you need frame-by-frame matte adjustments.</p></details>
      <details><summary>What video formats and limits are supported?</summary><p>BGRemove accepts MP4, MOV, WebM, M4V, and GIF. Each file can be up to 2 GB and 60 seconds long. The transparent output is WebM using VP9 with alpha.</p></details>
      <details><summary>Can I use the transparent video in CapCut or Premiere Pro?</summary><p>BGRemove exports transparent WebM using VP9 with alpha. Whether transparency imports correctly depends on the editor, version, platform, and codec support. Check the current CapCut or Premiere Pro documentation before you start. If your editor does not accept WebM alpha, use BGRemove to add the final background and export an MP4. Renaming a file extension does not change its codec.</p></details>
      <details><summary>Can I remove green screen from video for free?</summary><p>Yes. Each signed-in account can complete up to 3 successful background removals per 24-hour window. The allowance is shared with Remove Video Background. There are no paid plans.</p></details>
      <details><summary>Do I need to sign in?</summary><p>Yes. You must sign in before processing a video.</p></details>
      <details><summary>Will the downloaded video have a watermark?</summary><p>No. Downloads do not include a watermark.</p></details>
      <details><summary>Can I replace the green screen with my own background?</summary><p>Yes. After the green background is removed, you can keep the result transparent or place a color, blur, image, or video behind the subject. The finished background-replaced video is exported as an MP4.</p></details>
      <details><summary>When should I use manual chroma key software instead?</summary><p>Use a full editor when the shot needs frame-by-frame masks, precise spill correction, detailed work around transparent or reflective objects, or exact control over hair and heavy motion blur. BGRemove is intended for automatic subject separation without manual key settings.</p></details>
    </section>
  </main>

  <footer class="site-footer">
    <!-- 复用现有全站页脚；Product 列继续只显示 Remove Video Background 与 Change Video Background。 -->
  </footer>

  <!--
    GENERATED ASSET PATHS TO REPLACE DURING IMPLEMENTATION:
    {{imperfect-green-screen-image-src}}
    {{three-stage-workflow-image-src}}
  -->
</body>
</html>
```

### 纠正 Sep 6 的错误竖屏声明并更新本次公开 Changelog

- 优先级：`P1`
- 页面或界面：`https://bgremove.video/changelog/`
- 当前问题与线上证据：线上 `Sep 6, 2026 · Fix · 2.0` 条目当前声称竖屏视频会在预览、所有背景和导出文件中保持正确方向，但用户于 2026-09-08 的生产复测确认竖屏预览仍会横向播放。该条目同时包含方向元数据、高帧率和“其他副作用”等实现诊断，既不真实也不符合简洁、脱敏的用户向更新日志要求；其中 `Colour`、`Blur` 选择流程和更清晰的处理反馈已由用户确认上线。
- 修改要求：立即把 `Sep 6, 2026` 条目的标题改为 `Background controls now wait for your choice`，正文完整替换为：`Colour and Blur controls now wait for your choice before updating, with clearer progress and retry feedback while the preview is being prepared.` 保留该条目的日期、版本和类型。本批次竖屏方向修复和 `Remove Green Screen` 页面实际发布并经过生产验证后，再新增恰好一条带真实发布日期的记录，只概括实际上线的用户可见变化。竖屏方向可使用：`Vertical videos now keep the correct orientation in previews and exported MP4 files.`；新页面可概括为：`A new Remove Green Screen page helps you process imperfect green-screen footage with AI, without manual chroma key controls.` 未上线或未验证的内容必须省略；如果没有任何修改成功上线，则不要新增记录。
- 验收标准：`Sep 6, 2026` 条目不再声称竖屏方向已经修复，不再出现方向元数据、高帧率、副作用或其他实现诊断，只描述已经确认上线的控件和处理反馈。本批次恰好新增一条真实日期的简洁记录，且只包含生产环境已经验证的竖屏修复和/或 `Remove Green Screen` 新页面。
- 不要修改：`Sep 6, 2026` 条目的原日期、版本和类型，以及其他历史记录及其日期。不得提及文件名、组件名、代码架构、仓库、分支、提交、基础设施或服务商配置、成本、密钥、安全敏感实现、客户数据、内部指标、AI 提示词或内部工作流程。
