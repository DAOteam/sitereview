---
site_id: "bgremove-video"
name: "BGRemove"
production_url: "https://bgremove.video/"
changelog_url: "https://bgremove.video/changelog/"
delivery_method: "direct_publish"
target_repository: "not_applicable"
default_branch: "not_applicable"
updated_at: "2026-09-10"
---

# BGRemove 当前待办事项

## 已批准任务

### 让 Remove Green Screen 首屏与首页使用同一套工作区布局

- 优先级：`P1`
- 页面或界面：`https://bgremove.video/green-screen-remover/` 的首屏标题区与功能工作区
- 当前问题与线上证据：2026-09-10 线上桌面端对比显示，首页 `https://bgremove.video/` 的首屏在标题和简介下方使用接近页面内容宽度的双栏工作区：左侧为上传、处理或结果卡片，右侧为 `Your recent clips`；去绿幕页目前把 `Upload a Green Screen Video`、格式说明和功能卡片放在居中的窄幅单列区域，右侧留有大片空白，功能模块的宽度、层级、间距和信息组织均与首页不一致。用户已明确要求去绿幕页首屏，尤其是功能模块，与首页保持一致。
- 修改要求：让去绿幕页首屏复用首页现有首屏工作区的布局体系和视觉样式：标题与简介之后直接进入同宽的工作区；桌面端采用与首页一致的双栏结构、列宽比例、卡片高度、边框、圆角、内边距和栏间距，左侧显示去绿幕上传、处理或结果状态，右侧显示与首页相同的 `Your recent clips` 列表；小屏断点、堆叠顺序和横向留白也与首页一致。保留去绿幕页现有 H1、介绍文案、`Upload a Green Screen Video`、格式限制及免费额度信息，但把这些内容放入与首页对应的信息层级中，不在工作区上方另设一套窄幅模块。优先复用首页同一工作区组件或布局规则，避免复制出两套后续会继续分叉的样式。
- 验收标准：在相同桌面视口下，首页与去绿幕页的标题区最大宽度、工作区起始位置、整体宽度、双栏比例、卡片样式和垂直节奏视觉一致；去绿幕页左侧功能卡片和右侧 `Your recent clips` 完整可见，不再以居中窄单列形式展示；登录前、上传中、处理中、完成、失败和额度用尽状态均不导致工作区跳出既定宽度或明显改变布局；移动端按首页现有顺序自然堆叠，无横向滚动、裁切或按钮溢出；绿幕专属文案和页面其余内容保持原样。
- 不要修改：`https://bgremove.video/change-background/` 的任何页面、功能或文案；首页现有布局和功能；去绿幕页的顶部菜单、页脚、登录规则、每日免费任务规则、处理能力和输出格式。除本文件单独批准的 SEO 内容与三阶段案例图修改外，不修改其他正文、元数据、结构化数据或配图；不得在本任务中增加或删除产品功能。

### 重新制作三阶段案例图并确保主体完全一致

- 优先级：`P1`
- 页面或界面：`https://bgremove.video/green-screen-remover/` 的三阶段操作说明案例图
- 当前问题与线上证据：用户于 2026-09-10 提供的线上截图显示，绿幕原片、透明背景和办公室成品三个画面中的男性在脸型、五官、发型、胡须、衬衫颜色、姿势、身体比例和画面裁切上均不一致，看起来像三名相似但不同的人。这无法正确表达“同一段素材只替换背景”的产品流程，也会削弱案例可信度。
- 修改要求：重新制作整张三阶段案例图。先生成或选定一张唯一的源人物画面，再从该源画面提取同一个人物主体图层，并将这一个完全相同的主体图层分别用于三个面板：左侧保留绿幕原片，中间把背景替换为透明棋盘格，右侧把背景替换为真实办公室场景。三个面板不得分别生成不同人物；人物前景像素、脸、发型、胡须、服装、姿势、表情、身体比例、大小、方向和裁切位置必须一致，只允许背景发生变化。推荐制作提示词：`Create one photorealistic source frame of a seated adult male presenter in an olive button-up shirt against a wrinkled green screen. Use that exact same source frame and exact same foreground cutout in all three panels of one 16:9 triptych: left shows the original green-screen frame, center shows the identical cutout over a neutral transparency checkerboard, and right shows the identical cutout over a realistic home-office background. Preserve identical face, hair, beard, clothing color and folds, pose, expression, anatomy, scale, orientation, lighting on the subject, and crop in every panel. Only the background may change. No text, labels, logos, watermarks, extra limbs, facial drift, wardrobe changes, or independently regenerated subjects.` 实际制作时必须采用同一源图抠图后合成三个背景，不得仅依赖提示词生成三个人像。
- 验收标准：将三个面板并排对比时，人物轮廓和所有前景细节能够逐像素对齐；三处人物可明确判断为同一个源帧，而不只是外貌相近；左侧仅有绿幕背景，中间仅有透明棋盘格，右侧仅有办公室背景；没有人物变形、多余肢体、面部漂移、衣服变化、文字、标志或水印；图片在桌面端与移动端无拉伸、裁切错误或失真；保留准确的英文 alt：`The same presenter shown on a green screen, transparent background, and finished scene`。
- 不要修改：除本文件单独批准的 SEO 标题和内链调整外，该模块的三步文案、CTA、alt 含义及其他页面配图保持不变；不得把生成图描述为真实客户素材或未经处理的真实产品截图。

### 提升 Remove Green Screen 页的 SEO 内容可引用性和主题区分

- 优先级：`P1`
- 页面或界面：`https://bgremove.video/green-screen-remover/` 的正文、FAQ、内部链接和社交分享元数据；`https://bgremove.video/tools/green-screen-alternative/` 的一条上下文内链
- 当前问题与线上证据：2026-09-10 线上检查确认目标页返回 `200`，`lang="en"`、Title、Meta description、自引用 canonical、Open Graph、Twitter Card、XML sitemap、单一 H1、可见 FAQ 与 `FAQPage` JSON-LD 均已配置；Title 为 `Remove Green Screen from Video Online Free`，核心词位于 H1 和首屏，现有页面连导航与页脚约 1320 个英文词，主要关键词没有明显堆砌。当前不足不是字数，而是内容仍缺少便于用户和答案引擎直接提取的 AI 与传统 chroma key 决策对比、提高源素材成功率的实用检查清单，以及让游戏、社交视频、产品视频和教学素材用户快速判断适用方式的场景说明；现有正文只在长段落中罗列这些用途，缺少可扫描的具体建议。FAQ 中 `How is this different from a manual chroma key remover?` 与 `When should I use manual chroma key software instead?` 信息重复，却没有回答蓝幕或其他纯色背景能否处理，也缺少“透明 WebM 单独播放仍显示绿色”的关键解释。三步区标题使用 `How to Remove a Green Background From Video`，没有自然覆盖已批准的变体 `remove green background from video`；指向 `/tools/green-screen-alternative/` 的锚文本 `Learn how BGRemove works` 与目标页的真实主题不一致。目标页与 Green Screen Alternative 页意图接近，但目前缺少一条明确说明分工并回链到专营工具页的上下文链接。搜索结果抽查显示，当前竞争页普遍把操作工具、方式对比、源素材建议、导出说明、使用场景和具体 FAQ 作为核心信息架构；部分竞品依赖未经证实的速度、客户数字和绝对效果承诺，BGRemove 应以真实产品边界、明确格式限制和可操作建议形成差异化。
- 修改要求：保留现有 URL、Title、Meta description、H1、canonical 和已正确的主体文案，不为增加长度而重复关键词。按下方英文定稿完成这些修改：
  1. 将三步区 H2 从 `How to Remove a Green Background From Video` 改为 `Remove Green Background From Video in 3 Steps`，以简洁自然的标题覆盖已批准的关键词变体。三个步骤分别在现有 H3 标题上方显示可见标签 `Step 1`、`Step 2`、`Step 3`，标签与对应标题组成同一张步骤卡片；保留现有三个 H3 和正文，不用单独的 `1`、`2`、`3` 或仅靠 CSS 计数器代替文字标签。辅助技术读取每个 `Step` 标签一次，不产生重复朗读。
  2. 在现有差异化卖点区之后、`No Green Screen?` 转折模块之前新增 `AI Green Screen Remover vs. Chroma Key` 对比模块，使用语义化 `<section>`、一个 H2、简介和带表头的 `<table>`；移动端不得截断表格信息，可转为逐项对比卡片，但阅读和 DOM 顺序必须保持一致。
  3. 在三步操作区之后新增 `How to Get a Cleaner Green Screen Cutout` 实用建议模块，使用一个 H2、直接回答式引言和四个 H3，不新增产品没有的调节工具或效果保证。
  4. 在实用建议模块之后、现有 `What Is Green Screen Removal (Chroma Key)?` 说明正文之前，新增 `Remove Green Screen for the Videos You Already Make` 使用场景模块。使用一个 H2、直接引言和四张文本卡片；不增加配图、轮播、虚构案例或效果保证。可在创作者卡片中自然链接 `/use-cases/creators/`，在产品卡片中自然链接 `/use-cases/ecommerce/`，每张卡片最多一个上下文链接。
  5. 删除现有重复 FAQ `When should I use manual chroma key software instead?`，保留前面的 `How is this different from a manual chroma key remover?`；新增下方“蓝幕或其他纯色背景”和“透明 WebM 单独播放仍显示绿色”两问两答。把两条新增问答和删除同步到 `FAQPage` JSON-LD，可见文字与结构化数据必须逐字一致，完成后页面 FAQ 总数为 10。
  6. 将 `/tools/green-screen-alternative/` 的现有锚文本从 `Learn how BGRemove works` 改为 `Compare AI removal with chroma key`；在同一附近增加 `See how AI video matting works` 指向 `/how-it-works/`。在 `/tools/green-screen-alternative/` 首段之后增加下方回链句，其中仅锚文本 `remove green screen from video` 指向 `/green-screen-remover/`。不要把 Alternative 页的 Title 或 H1 改成专营页核心词。
  7. 将目标页通用的 `/og/default.png` 替换为该页面专属的 `1200 × 630` 社交分享图，可从已通过人工检查的绿幕拍摄案例图制作安全裁切；同步用于 `og:image` 与 `twitter:image`，增加 `og:image:alt` 和 `twitter:image:alt`，值为 `A presenter filming in front of an imperfect green screen`。图片不得包含文字、标志、水印、畸形人物或未经验证的产品结果。
  8. 在 FAQ 之后、页脚之前增加最终 CTA 模块。使用与现有暗色页面一致但视觉上可区分的宽幅卡片，内容居中，只有一个主按钮和一行辅助说明，不增加配图、第二按钮、注册弹窗或新处理流程。为首屏工具工作区设置稳定锚点 `green-screen-tool`，CTA 按钮指向 `#green-screen-tool`，点击后回到当前页面的上传或任务状态区域。

#### AI 与 chroma key 对比模块英文定稿

```text
H2: AI Green Screen Remover vs. Chroma Key

Intro: An AI green screen remover identifies the subject across the frame. A chroma key remover removes pixels close to a selected color. AI avoids manual key-color setup when the screen has folds, shadows, or mild spill. Chroma key gives an editor more manual control when the screen is evenly lit.

Table caption for screen readers: Comparison of AI green screen removal and manual chroma key

Row 1
Criteria: What it detects
AI green screen removal: The person or product in the scene
Manual chroma key: Pixels close to a selected screen color

Row 2
Criteria: What you adjust
AI green screen removal: No key color or tolerance controls
Manual chroma key: Key color, tolerance, edge softness, and spill suppression

Row 3
Criteria: Imperfect screens
AI green screen removal: Can work through folds, shadows, uneven light, and mild spill; review difficult edges
Manual chroma key: Often needs more cleanup when the screen contains several shades of green

Row 4
Criteria: Best fit
AI green screen removal: A quick automatic cutout in your browser
Manual chroma key: Controlled footage that needs precise, frame-level adjustment in an editor

Row 5
Criteria: Output here
AI green screen removal: Transparent VP9 WebM, or an MP4 after you add a background
Manual chroma key: Depends on the editor and export settings you choose

Closing: Use BGRemove when you want the subject separated automatically. Use a full editor when you need to adjust the matte frame by frame.

CTA: Remove Green Screen
CTA target: #green-screen-title
```

#### 实用建议模块英文定稿

```text
H2: How to Get a Cleaner Green Screen Cutout

Intro: AI can work with an imperfect screen, but clear source footage still makes the subject easier to separate. Check these four things before you upload.

H3: Keep the full subject inside the frame
Body: Leave room around moving hands, hair, clothing, and props. Anything cut off by the camera cannot be restored during background removal.

H3: Leave space between the subject and the screen
Body: More distance can reduce hard shadows and reflected green around the subject. You do not need a perfect studio, but avoid pressing the subject directly against the backdrop when you can.

H3: Test the hardest section first
Body: Choose a short section that includes fast motion, loose hair, or the most uneven part of the screen. A representative test tells you more than an easy frame from the start of the clip.

H3: Review the edge before you download
Body: Check hair, motion blur, glass, reflective objects, and green clothing against the intended background. Use a full editor when the shot needs frame-by-frame matte control.
```

#### 使用场景模块英文定稿

```text
H2: Remove Green Screen for the Videos You Already Make

Intro: Start with the clip you already recorded. BGRemove removes the green backdrop automatically, then gives you a transparent file or a finished scene with a new background.

H3: Gaming Clips and Streams
Body: Separate a player, host, or reaction shot from the green screen, then place the transparent WebM over gameplay in an editor that supports VP9 alpha. Review fast hand movement, hair, and motion blur before publishing.

H3: YouTube and TikTok Videos
Body: Use one cutout with different backgrounds for tutorials, reactions, short videos, and channel updates. Add the final background in BGRemove for an MP4, or keep the transparent WebM when the edit still needs captions and layout work.

H3: Product Videos
Body: Remove a green backdrop behind a product or presenter, then place the subject over a product page image, campaign scene, or brand color. Check glass, reflective surfaces, and transparent packaging carefully.

H3: Lessons and School Projects
Body: Replace a classroom green screen without learning key-color and tolerance controls. Use a slide, image, or recorded scene as the new background, then export an MP4 for a presentation or assignment.
```

#### 新增 FAQ 英文定稿

```text
Q: Can I use BGRemove with a blue screen or another solid-color background?

A: Yes. BGRemove identifies the subject instead of removing one selected key color, so the source background does not have to be green. It can process blue screens, other solid-color backdrops, and ordinary scenes. If the footage was not shot against green, use Remove Video Background for the general workflow.

Q: Why does my transparent WebM still look green when I play it by itself?

A: That can be normal. Some local players and browser tabs do not composite the VP9 alpha channel, so transparent pixels may show the source green even though the alpha data is present. Test the file above a solid color, image, or video in an editor that supports VP9 WebM alpha. If the lower layer appears around the subject, transparency is working. Renaming `.webm` to `.mp4` does not convert the codec or preserve transparency.
```

#### Alternative 页回链英文定稿

```text
Already have footage shot against green? Use our remove green screen from video tool for the dedicated upload workflow.
```

#### 页面底部 CTA 英文定稿

```text
H2: Ready to Remove Your Green Screen?

Body: Upload your clip and let AI separate the subject without key-color or tolerance controls. Download a transparent WebM with no watermark, or add a background and export an MP4.

Primary CTA: Remove My Green Screen
CTA target: #green-screen-tool

Supporting line: 3 free background removals per 24-hour window, shared with Remove Video Background.
```

- 验收标准：目标页继续返回 `200` 且保持可索引，自引用 canonical、Title、Meta description 和唯一 H1 不变；三步区依次清楚显示 `Step 1`、`Step 2`、`Step 3`，每个标签与对应的 H3 和正文匹配，桌面端与移动端均无错序、重叠、遗漏或重复编号；新增比较、实用建议和使用场景三个正文模块位于指定位置，桌面端和移动端清晰可读，比较表的行列关系不会在窄屏丢失，四张场景卡片的标题和正文与定稿一致；删除指定重复 FAQ 后新增两条 FAQ，页面与 `FAQPage` JSON-LD 均恰好保留 10 条问答，可见内容和结构化数据逐字一致且可解析；`Remove Video Background` 在蓝幕 FAQ 中自然链接到 `/`；页面出现指向 `/tools/green-screen-alternative/`、`/how-it-works/` 和 `/` 的自然上下文链接，所有目标返回 `200`；Alternative 页增加一条指向 `/green-screen-remover/` 的上下文回链且不改变其 Title、H1 和核心比较意图；页面源代码中自然覆盖 `remove green screen from video`、`green screen remover`、`green screen remover video`、`remove green background from video`、`chroma key remover`、`green screen video remover` 和 `remove green screen from video online free`，不得用隐藏文本、重复标题或机械重复句子补词；专属社交图返回 `200`、尺寸为 `1200 × 630`，Open Graph 与 Twitter 标签引用相同绝对 HTTPS URL，并包含准确 alt；底部 CTA 位于 FAQ 和页脚之间，文案与定稿一致，按钮是模块内唯一主操作，点击后 URL 更新为 `#green-screen-tool` 并将首屏工具区带入视口，键盘操作、固定导航偏移和移动端滚动位置正常；不得新增无法证实的速度、成功率、客户数量、评价、商业授权、编辑器兼容保证或绝对效果承诺。
- 不要修改：首页的 H1、正文、工具定位或索引信号；`/tools/green-screen-alternative/` 除指定回链外的内容与关键词定位；目标页现有产品事实、价格与免费额度、登录要求、格式和限制、无水印声明、数据规则、处理能力、除明确删除与新增外的其他 FAQ 答案、配图说明及已正确的结构化数据实体。不要新增 `HowTo`、评分、评价、VideoObject 或 SoftwareApplication 结构化数据，除非页面同时出现符合相应规范且可公开验证的真实内容。

### 更新本次公开 Changelog

- 优先级：`P1`
- 页面或界面：`https://bgremove.video/changelog/`
- 当前问题与线上证据：2026-09-10 线上页面的最新记录仍为 `Sep 5, 2026`，尚未记录 Remove Green Screen 专营页及其重要的首屏工作区更新。三阶段案例图更换、SEO 内容补充和底部 CTA 属于普通页面优化，不需要写入 Changelog。
- 修改要求：上述首屏布局上线并通过生产复测后，在 Changelog 顶部新增且只新增一条按实际发布日期记录的用户可见更新。正文使用：`Remove Green Screen now has a dedicated page with the same upload and recent-clips workspace as Remove Video Background.` 不得提及三阶段案例图、SEO 文案或底部 CTA，也不得写入尚未发布或与本批次无关的功能。
- 验收标准：线上 Changelog 顶部出现一条日期正确、可公开阅读的新记录；内容只描述实际发布的用户可见能力，不出现仓库、文件、组件、提交、供应商、成本、内部指标、提示词或实现细节；不恢复已删除的错误 `Sep 6, 2026` 条目；本批次不新增第二条记录。
- 不要修改：`Sep 5, 2026` 及更早的真实历史记录；其他页面文案、产品规则和功能行为；不得加入换背景页面的修复或验证内容。
