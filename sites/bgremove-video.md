---
site_id: "bgremove-video"
name: "BGRemove"
production_url: "https://bgremove.video/"
changelog_url: "https://bgremove.video/changelog/"
delivery_method: "direct_publish"
target_repository: "not_applicable"
default_branch: "not_applicable"
updated_at: "2026-08-31"
---

# BGRemove 当前待办事项

## 已批准任务

### 将换背景页面迁移到根目录并开放索引

- 优先级：`P1`
- 页面或界面：旧地址 `https://bgremove.video/app/change-background/`、新地址 `https://bgremove.video/change-background/`、全站导航、站内链接和 sitemap
- 当前问题与线上证据：当前换背景页位于 `/app/change-background/`，canonical 指向该应用路径，使用 `noindex, nofollow`，不在 sitemap 中，页面的 H1 和主体内容还依赖客户端组件加载。用户已经明确批准把页面迁移到根目录并允许搜索引擎索引。
- 修改要求：将完整换背景落地页和现有工具迁移到唯一正式地址 `https://bgremove.video/change-background/`。新页面使用自引用 canonical；删除 `noindex, nofollow`，允许正常 `index, follow`；加入正式 sitemap；把页头、页脚、首页、功能页、账户界面及其他公开页面中指向旧地址的站内链接全部更新到新地址。旧的 `/app/change-background` 和 `/app/change-background/` 使用永久重定向指向 `/change-background/`，保留必要的查询参数，不得继续返回重复页面。页面标题必须精确使用 `Change Video Background Online Free`，包含 `Free`，末尾不得添加 `| BGRemove` 或其他品牌后缀；meta description 使用 `Change a video background online for free. Add a color, blur, image, or video behind a finished transparent clip, then export as MP4.`。H1、简介、案例、步骤、FAQ 和 CTA 必须服务器渲染；个性化视频列表、账户状态和编辑器交互可以继续客户端加载。新地址必须继续承载登录状态、已完成视频选择、背景编辑及 MP4 导出，不得把工具留在旧地址。
- 验收标准：`https://bgremove.video/change-background/` 最终返回 200，title、meta description 和 canonical 与要求一致，robots 不含 `noindex` 或 `nofollow`；该 URL 出现在正式 sitemap 和站内导航中；未执行 JavaScript时仍能读取唯一 H1、主要落地页正文、FAQ 和 CTA；旧地址及其斜杠变体只经过一次永久重定向到新地址，不形成链式或循环重定向；全站不再存在指向旧地址的可见链接；已登录用户在新地址仍能看到自己的可用视频并完成换背景与 MP4 导出；未登录用户可以阅读完整落地页并获得明确的登录或先去背景入口。若尚无真实的非英文版本，不得输出指向不存在翻译页的 hreflang。
- 不要修改：现有用户视频、认证会话、背景合成行为、素材本地处理规则、额度规则、MP4 导出或其他 `/app/` 页面。不要让新旧两个地址同时返回可索引的 200 页面，不要用 JavaScript 跳转代替 HTTP 永久重定向，也不要创建未经批准的非英文路径。

### 把换背景功能页扩展为完整落地页

- 优先级：`P1`
- 页面或界面：`https://bgremove.video/change-background/`
- 当前问题与线上证据：页面当前只有约 `92` 个可见英文单词。登录后的公开可见结构是一个标题、一句简介、没有可用透明视频时的空状态、额度卡片和浏览器本地合成说明；操作区之后立即进入页脚。页面没有效果案例、操作流程、背景类型、适用场景、FAQ 或底部 CTA，首屏也没有展示换背景后的实际结果。无可用视频时，额度卡片的 `3/3 videos left` 容易让用户误以为换背景也受 3 次额度限制，而页面另一处又说明换背景不使用额外额度。当前主体内容由客户端组件加载，首次 DOM 状态只有导航和页脚；现有页面使用 `noindex, nofollow`，且不在 sitemap 中。
- 修改要求：保留现有换背景工具、已完成视频选择逻辑、颜色、模糊、自定义图片、自定义视频、浏览器本地合成和 MP4 导出行为，把页面改成“先理解价值，再直接使用工具，继续阅读案例与说明”的完整落地页。视觉沿用首页的深色背景、绿色主按钮、宽内容容器、真实感案例图、清晰分区和充足留白。首屏必须复用首页当前的信息结构和空间关系；首屏之后的内容针对换背景功能重新设计，不能把首页其他模块原样复制过来。除个性化的视频列表、账户状态和编辑器交互外，落地页标题、说明、案例、步骤、FAQ 和 CTA 必须由服务器返回或在首屏 HTML 中可读取。

  按以下顺序组织页面，并使用给定英文标题和核心文案：

  1. 首屏：严格采用首页当前结构。使用一个全宽 `shell`，顶部放服务器渲染、水平居中的 H1 `Change Your Video Background Online for Free`；副标题居中并限制在约 `58ch`，使用 `Choose a video you have already processed with BGRemove. Add a color, blur, image, or video behind it, then export an MP4 for free.`。标题区下方使用与首页相同层级的双栏大卡片布局，桌面端比例接近首页的 `1fr 1.05fr`，卡片等高，间距和圆角沿用首页。左栏是主要换背景工具或没有视频时的引导状态；右栏标题使用 `Your Finished Clips`，显示可以继续换背景的已处理视频及 `See All` 链接，没有视频时显示清晰空状态。不要在首屏继续使用当前“主内容加窄额度侧栏”的布局，也不要把单独的宣传案例图放在双栏工具区之前。左侧卡片底部增加和首页上传卡片类似的事实摘要栏，使用 `Runs in Your Browser`、`No Extra Allowance`、`MP4 Export`，不得显示会让人误解为换背景次数限制的 `3/3` 主视觉。移动端顺序固定为“居中标题与副标题 → 左侧工具卡 → 右侧 Finished Clips 卡”，两张卡片满宽且没有横向滚动。
  2. 工具区：把现有功能区放在首屏价值说明之后，并给它稳定的页内锚点。存在已处理视频时，主操作是选择视频并换背景；没有视频时，标题改为 `Remove a Background First`，说明改为 `This tool starts with a transparent video. Remove the original background, wait for the clip to finish, then come back here to add a new scene.`，CTA 使用 `Remove a Background`。删除未经稳定验证的 `It takes about a minute`，保留 `Changing the background does not use another video allowance.`。不要让额度卡片成为换背景页的主要卖点；将其改成辅助说明或移到空状态附近，并明确它只用于第一次移除背景。
  3. 效果案例：新增 H2 `See the Same Cutout on 4 Backgrounds`。先用约 `40–60` 个英文单词解释：主体不变，只替换它后面的场景；用户可以先尝试纯色或模糊，再根据用途换成自己的图片或视频。首段必须使用原句 `Keep the person or product exactly as it is. Try a solid color, soften the scene with blur, add your own image, or place another video behind the cutout.`，随后再补充一句浅显说明。使用同一位虚构人物制作 4 张真实感案例图，分别标注 `Solid Color`、`Blur`、`Image`、`Video`；四张图的脸、发型、服装、姿态、机位、主体尺寸和主体光线必须一致，只改变背景。图片下方加可见说明 `Demonstration images. No customer footage is shown.`，不得暗示为真实客户素材或未经修饰的产品实测结果。不得使用流程简图、抽象图形、单纯色块、通用图标或伪造产品界面代替案例图。
  4. 操作步骤：新增 H2 `Change a Video Background in 3 Steps`。用约 `160–220` 个英文单词完成该模块；先用一句话说明必须从已经去除原背景的视频开始，再用三个带真实案例图的步骤解释完整流程。三个步骤依次使用：`1. Remove the Original Background`，说明 `Upload a video to BGRemove and wait until the transparent version is ready. Your finished clip will appear on this page.`；`2. Choose a New Background`，说明 `Select a color, blur, image, or video. BGRemove combines it with your transparent clip in this browser.`；`3. Export the Finished MP4`，说明 `Download the result as an MP4. You can return to the same transparent clip and try another background without using another allowance.`。每一步可再补充 `1–2` 句新手能直接理解的操作结果，但不得增加未验证功能。步骤采用首页同类模块的数字、标题和短段落结构；编号、标题和说明使用 HTML 排版，不能烘焙进图片。
  5. 背景选择：新增 H2 `Choose the Background That Fits the Job`，用约 `180–240` 个英文单词说明不同背景分别适合什么目的，而不是只罗列功能。设置 4 个带真实案例缩略图的内容项：`Solid Color` 说明可减少干扰，适合产品展示、头像和已有品牌色；`Blur` 说明能保留原场景的感觉，同时让人物或产品更突出；`Image` 说明用户可以加入自己的品牌场景、活动视觉、产品环境或演示背景；`Video` 说明移动背景适合教程、社交内容和创意合成。每项使用一句“适合什么”加一句“用户会看到什么”，避免生硬术语。可以复用上一模块的同组四张案例图或其裁切版本，不再生成一套外观不一致的主体。只描述当前工具真实支持的行为，不承诺自动匹配光线、透视、颜色或音频。
  6. 用途区：新增 H2 `Make More Versions From One Cutout`，用约 `160–220` 个英文单词和 3 张真实案例图说明：电商可把同一件无品牌产品放入不同活动场景；创作者可把同一位虚构讲解者放到整洁的教程或演示背景前；代理商可从同一素材准备不同画幅和场景的交付版本。每项要有具体标题、`2–3` 句浅显说明和描述性链接，分别连接到 `/use-cases/ecommerce/`、`/use-cases/creators/`、`/use-cases/agencies/`，模块结尾再链接 `/use-cases/`。不得声称工具会自动完成画幅转换，也不得与用途详情页重复大段正文。
  7. 隐私与额度：将现有标题 `Composited here, not on a server` 改为更易懂的 H2 `Your Background Stays on Your Device`，正文使用 `Your transparent clip and the background you choose are combined in this browser. The image or video you use as a background is not uploaded to BGRemove.`。补充独立短句 `Changing a background does not use another video allowance because the original background has already been removed.`。这两项必须靠近工具区和 FAQ，而不是只放在弱化的小字中。
  8. FAQ：新增可见 FAQ，并同步输出逐项一致的 `FAQPage` JSON-LD。至少包含：`Does this page remove the original background?`，回答必须说明要先使用 BGRemove 完成去背景；`What can I use as a new background?`，回答只列颜色、模糊、自己的图片或视频；`Does changing a background use another allowance?`，回答为不使用额外额度；`Are my background images or videos uploaded?`，回答为背景素材在浏览器中使用且不会上传到 BGRemove；`What format do I download?`，回答为最终结果导出为 MP4；`Why do I not see any clips here?`，回答必须说明只有已经完成去背景的视频才会出现在这里。
  9. 底部 CTA：新增 H2 `Ready to Put Your Subject Somewhere New?`，正文使用 `Choose a finished cutout, add the background you want, and export a video that is ready to share.`。有可用视频时，主按钮使用 `Choose a Clip` 并回到工具锚点；没有可用视频时，主按钮使用 `Remove a Background First` 并指向首页去背景入口；次级链接使用 `See How It Works` 并指向 `/how-it-works/`。

  图文内容统一要求：正文面向第一次使用视频换背景工具的人，使用常用词、短句和直接的操作结果，每段只说明一个重点。不要使用未解释的 `compositing`、`alpha channel`、`matte`、`plate`、`render pipeline` 或 `keying` 等专业词。自然使用 `change video background`、`replace video background`、`add a background to video`、`blur video background`、`free` 和 `online` 等表达，但不得堆砌关键词。主要可见正文控制在约 `850–1050` 个自然英文单词；不能用重复 FAQ、隐藏文字、结构化数据或图片中文字补足。所有生成图统一采用写实商业视频画面风格、`16:9` 横图、至少 `1200×675`；在保持画面比例的前提下输出优化后的 WebP 或 AVIF，声明宽高，首屏外延迟加载。图片内不得出现标题、步骤编号、按钮、品牌标志、水印或说明文字；这些信息全部使用可访问的 HTML 文本。移动端裁切必须保留完整主体，不能拉伸图片。真实产品界面只能从实际页面截取，不能让 AI 伪造。

  配图生成和验收按以下提示词执行。先生成“主体基准图”，再把它作为图像参考生成同组变体；若所用生成工具无法锁定参考主体，就停止并更换支持参考图的生成方式，不能接受四张身份不同的近似人物：

  **A. 四种背景效果的主体基准图**

  ```text
  Create a photorealistic commercial video still of one fictional adult woman, waist-up, facing the camera with a relaxed natural expression. She wears a dark emerald overshirt over a plain charcoal top. Use an eye-level 50 mm camera, soft three-point studio lighting, realistic skin texture, natural hands, a centered composition, and generous space around the subject for responsive cropping. Place her against a simple neutral studio background for this master reference. This is a fictional demonstration subject, not a real customer. 16:9 landscape, 1200x675 or larger. No text, logos, watermark, interface, icons, borders, split screen, checkerboard, exaggerated bokeh, beauty-filter skin, or cutout halo.
  ```

  **A1–A4. 同一人物的四个背景变体**

  ```text
  Using the supplied master reference, preserve the exact same fictional woman, face, hair, expression, clothing, pose, camera angle, crop, subject scale, lighting, and clean subject edges. Change only the area behind her. Generate four separate 16:9 landscape images: (1) a restrained solid emerald-green studio background; (2) a believable home-office scene with strong optical background blur; (3) a bright modern presentation studio with a blank display area and realistic depth; (4) a believable single frame from moving city-light footage, with natural motion blur only in the background. Keep the subject sharp and unchanged in every image. No text, logos, watermark, UI, arrows, comparison labels, checkerboard, extra people, edge halo, altered clothing, changed facial features, or changed body position.
  ```

  **B. 三步流程案例图**

  ```text
  Create a consistent three-image photorealistic workflow set featuring the exact same unbranded matte-white reusable bottle with a small emerald cap, viewed from the exact same camera angle and at the same scale. Image 1: the bottle in front of a visually busy but realistic home-kitchen background, representing the original video. Image 2: the identical bottle cleanly isolated, shown over a subtle neutral transparency-checker preview, representing the finished transparent clip. Image 3: the identical bottle placed in a polished warm commercial studio scene with a tasteful new background, representing the exported MP4. Preserve the bottle geometry, cap, angle, lighting direction, and edge quality across all three images. Each image is a separate 16:9 landscape frame, 1200x675 or larger. No text, step numbers, logos, watermark, interface, buttons, arrows, hands, extra products, warped bottle, or fake software screen.
  ```

  **C. 三个用途案例图**

  ```text
  Create three separate photorealistic commercial video stills with one cohesive premium color grade. Scene 1, ecommerce: an unbranded skincare bottle cleanly placed in a tasteful seasonal campaign setting, with realistic contact shadow and space for an HTML caption. Scene 2, creator tutorial: one fictional adult presenter in front of a clean home-studio background beside a blank presentation screen, with no writing on the screen. Scene 3, agency delivery: a realistic desk with a laptop and a phone displaying the same fictional presenter against two different clean backgrounds, suggesting multiple deliverable versions without showing any branded software interface. All people and products are fictional demonstration subjects. Each output must be a separate 16:9 landscape image, 1200x675 or larger, composed for safe mobile cropping. No text, logos, watermark, customer brands, platform UI, metrics, testimonial styling, distorted screens, duplicated limbs, or cutout halo.
  ```

  配图验收：同组素材逐张对比主体的脸、服装、产品形状、姿态、机位、比例和边缘；有任何不一致就重新生成。四背景案例与“背景选择”模块应复用同一组素材，避免重复下载和视觉冲突。三步图必须让用户不读说明也能看出“原视频 → 透明主体 → 新背景成片”的顺序。用途图只展示可实现的结果，不得出现客户身份、虚构产品界面、虚构数据或未经支持的功能。每张图提供具体、简洁的英文 `alt`，描述主体和替换后的背景；装饰性裁切图使用空 `alt`，不能重复朗读相邻标题。

- 验收标准：页面在未登录、已登录但没有可用视频、已登录且有可用视频三种状态下都具有完整落地页内容，只有工具区的操作和账户信息随状态变化；SEO title 精确为 `Change Video Background Online Free` 且不含 `| BGRemove`，页面有且只有一个 H1 `Change Your Video Background Online for Free`，H2 顺序与上述结构一致；桌面首屏与首页一致采用“全宽居中标题区 + 双栏等高大卡片”，左侧是主操作、右侧是 Finished Clips，不能退化为窄侧栏；工具区仍可正常选择已经完成的视频、切换当前支持的背景类型并导出 MP4；四背景、三步流程和三个用途模块均使用符合提示词的真实感案例图，同组主体保持一致，图片包含准确的 `alt`、显式宽高或宽高比，首屏之外使用延迟加载；桌面端内容宽度、视觉层级和留白接近首页质量，移动端按规定顺序单列显示且没有横向溢出；首屏之后不再直接进入页脚；主要可见正文达到约 `850–1050` 个自然英文单词，不靠隐藏文字、JSON-LD 或图片中文字凑数；所有站内链接返回成功并使用描述性锚文本；FAQ 可见答案与 `FAQPage` 完全一致；不得因落地页改造破坏工具状态、浏览器本地合成、用户视频列表、额度或导出行为。
- 不要修改：实际支持的背景类型、处理位置、用户素材传输方式、额度规则、透明视频生成流程、MP4 导出行为、认证逻辑、用户视频或非英文页面。不要虚构自动光线匹配、智能构图、模板库、音乐、字幕、团队协作、处理速度、客户评价、效果数据或第三方软件兼容性。

### 修复换背景页的小字对比度和移动端遮挡

- 优先级：`P1`
- 页面或界面：`https://bgremove.video/change-background/` 桌面端和移动端
- 当前问题与线上证据：现有 `text-ink-faint` 小字在卡片背景上的实测对比度约为 `3.49:1`，包括 `videos left in this window`、额度重置时间、`Changing a background costs nothing...` 等正常字号文本，低于 WCAG AA 对普通文本的 `4.5:1` 要求。`390×844` 移动端中，右下角聊天悬浮按钮覆盖在额度卡片区域上方；当前虽然未遮住主要 CTA，但新增内容后仍可能遮挡按钮、FAQ 或文字。空状态中的装饰性 SVG 没有明确从辅助技术中隐藏。
- 修改要求：提高所有承载实际信息的小字颜色对比度，使普通文本达到至少 `4.5:1`；不能仅增加字体粗细而保留不足的颜色。装饰性 SVG 增加 `aria-hidden="true"` 且不可聚焦。为固定聊天按钮预留移动端安全空间，确保它不会覆盖主按钮、表单控件、FAQ 展开按钮、文字或页脚链接；同时保留清晰的键盘焦点样式，并遵循 `prefers-reduced-motion`。
- 验收标准：使用对比度工具复测所有正文和辅助说明，普通文本不低于 `4.5:1`，大号文本不低于 `3:1`；`390×844`、`768×1024` 和常见桌面宽度均无横向溢出，聊天按钮不覆盖任何可交互元素或重要文字；装饰图不进入可访问名称；所有链接和按钮可通过键盘到达并具有可见的 `focus-visible` 状态。
- 不要修改：全站品牌色方向、深色主题、聊天服务本身、功能行为或其他页面的版式。不要通过缩小内容、隐藏说明或禁用页面缩放来解决遮挡。

### 补充 Organization 的公开法定名称

- 优先级：`P2`
- 页面或界面：英文首页 `https://bgremove.video/` 的 `Organization` 结构化数据
- 当前问题与线上证据：首页 `Organization` 已经包含支持邮箱和 `contactPoint`，但仍没有把 About 页面公开显示的法定名称 `BGRemove d.o.o.` 表达为 `legalName`。
- 修改要求：继续使用 `https://bgremove.video/#organization` 作为唯一稳定的组织 `@id`，只增加 `legalName: "BGRemove d.o.o."`。其他页面继续通过同一 `@id` 引用该实体。
- 验收标准：首页 `Organization` JSON-LD 可解析，`legalName` 与 About 页面公开名称完全一致；全站不存在名称或 `@id` 冲突；Schema.org 验证没有关键错误。
- 不要修改：可见公司名称、地址、邮箱、现有 `contactPoint` 或其他法定信息。不要虚构电话、注册标识、税号、社交账号、评价、奖项或外部实体链接。

### 更新本次发布的公开更新日志

- 优先级：`P1`
- 页面或界面：`https://bgremove.video/changelog/`
- 当前问题与线上证据：当前公开更新日志最新记录为 `2026-08-15` 的 `Plainer language on the homepage`，尚未记录新的根目录换背景页面及本批次实际上线的可见改进。
- 修改要求：本批次成功发布后只新增一条带日期的公开记录。文案面向用户说明换背景功能现在有独立公开页面，并通过与首页一致的清晰操作首屏、真实案例、3 步说明、背景选择、常见问题及更明确的隐私和额度解释，帮助用户在已去背景视频后继续加入颜色、模糊、图片或视频背景并导出 MP4。只描述本批次实际上线的内容；如果没有任何可见改进成功发布，则不要新增记录。
- 验收标准：本批次恰好新增一条记录；内容简洁、脱敏、面向用户且与线上页面一致；`2026-08-15` 及更早的历史记录和日期保持不变。
- 不要修改：历史记录及其日期。不得提及文件名、组件名、代码架构、仓库、分支、提交、基础设施、服务商配置、成本、密钥、安全敏感实现、客户数据、内部指标、AI 提示词或内部工作流程。
