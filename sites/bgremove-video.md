---
site_id: "bgremove-video"
name: "BGRemove"
production_url: "https://bgremove.video/"
changelog_url: "https://bgremove.video/changelog/"
delivery_method: "direct_publish"
target_repository: "not_applicable"
default_branch: "not_applicable"
updated_at: "2026-08-15"
---

# BGRemove 当前待办事项

## 已批准任务

### 用浅显英文重写首页三个图文模块

- 优先级：`P1`
- 页面或界面：英文首页 `https://bgremove.video/` 中的 `One transparent master, many finished scenes`、`One cutout, every aspect ratio` 和 `A cleaner handoff from creator to editor` 三个图文模块
- 当前问题与线上证据：三个主题、真实感案例图和对应 FAQ 已经上线，但正文使用了大量新手难以理解的抽象表达和编辑术语，例如 `a stack of layers stays editable`、`baked in`、`lower third`、`grading`、`flattened`、`opaque`、`downstream` 和 `the split falls in the same place every time`。句子较长，一个句子经常同时解释多个概念，用户需要先理解专业剪辑流程才能看懂产品价值。三个模块的主题不需要改变，只需要把正文改成常用词、短句、明确步骤和具体例子。
- 修改要求：保留三个现有标题、案例图、图片说明、HTML 结构和排列顺序，只替换三个模块的正文。以下英文文案已经批准，必须逐段使用；可以按现有组件拆成 `<p>`，但不得重新润色、增加专业术语、改写产品能力或恢复原文中的抽象比喻。

  `One transparent master, many finished scenes` 正文：

  > A transparent master is a video of your subject with the background removed. Think of it as a reusable top layer. You can place a color, photo, product scene, slide, or another video underneath it. The person or product stays the same while the scene changes.
  >
  > This is useful when you need more than one version of a video. Start with a clean room for your website. Use the same subject over a product display for an ad. Place the subject beside a presentation screen for a tutorial. You do not need to upload the clip again or remove the background again. Add the transparent video to your editor, choose a new background, and export the next version.
  >
  > Keeping the subject and background separate also makes small edits easier. Move the subject left to make space for a headline. Crop the scene without changing the subject. Replace a photo, update a background color, or change the text while keeping the same performance. This also helps you test different scenes before you decide which version to publish.
  >
  > Save the transparent WebM as your master file. When you need a new campaign, language, or layout, start with that file instead of the original recording. You will still need an editor to add the background and export the finished video, but the difficult step of separating the subject is already done.
  >
  > See how this works for [product videos](/use-cases/ecommerce/), [creator content](/use-cases/creators/), and [agency projects](/use-cases/agencies/), or compare all common workflows in [the use-case overview](/use-cases/).

  `One cutout, every aspect ratio` 正文：

  > One recording may need to fit several screen shapes. A video on a website is often wide. A square post uses a 1:1 frame. A short video for a phone usually uses a tall 9:16 frame. If the background is already part of the video, a quick crop can cut off the subject or leave no space for text.
  >
  > A transparent video gives you more control. In a 16:9 layout, place the subject on one side and use the open space for a product, slide, or screen recording. In a 1:1 layout, make the subject larger so the frame does not feel empty. In a 9:16 layout, move the subject lower or to one side so captions can stay clear of the face.
  >
  > This is not the same as stretching one finished video into three shapes. Create a separate canvas for each size in your editor. Add the same transparent WebM to each canvas, then choose its size and position. Add a background that fits the new frame and check that important details are not covered by text or interface buttons. You can also use the open space differently for each channel and message.
  >
  > BGRemove removes the background and gives you the transparent file. It does not build the final layouts automatically. You make those layouts in your editor. The benefit is that you can use the same recording for a product page, a tutorial, a presentation, a square post, and a vertical social video without filming the subject again.

  `A cleaner handoff from creator to editor` 正文：

  > A transparent master makes it easier for one person to record a video and another person to finish it. The creator can focus on the performance. The editor can choose the background, text, and layout later.
  >
  > The handoff is simple. First, the creator records the clip and uses BGRemove to create a transparent WebM. Next, the editor imports that file into an editing tool and places a color, photo, slide, or video underneath it. The editor can then move or resize the subject without changing the original performance.
  >
  > If someone asks for a different background, more space for a logo, or a vertical version, the editor can update the layout instead of asking the creator to record the clip again. The subject stays the same. Only the parts around it change.
  >
  > When the work is approved, the editor exports a normal finished video for each website, presentation, or social channel. Keep three things: the original clip, the transparent WebM, and the final exports. The transparent file is the useful middle step because it can be reused when another version is needed.
  >
  > BGRemove only creates the transparent video. It does not host team projects, manage versions, collect comments, or export every channel layout for you. Those steps happen in the editing tools your team already uses. The value is a clean, reusable subject that gives the editor more choices and reduces the need to film the same take again.

- 验收标准：三个标题和主题保持不变；线上正文与上述批准文案逐段一致；第一段共约 `249` 个英文单词，第二段约 `245` 个，第三段约 `238` 个；使用普通用户能理解的 `background`、`subject`、`video`、`editor`、`layout`、`file` 和 `export` 等常用词；不再出现 `baked in`、`lower third`、`grading`、`flattened`、`opaque`、`downstream`、`plate`、`layer stack` 或其他没有立即解释的剪辑术语；句子以单一信息为主，没有连续多个破折号或需要回读的长句；四个用途链接保持为可点击的描述性链接；桌面端和移动端的现有图文布局、图片、替代文本和图片说明不变；页面仍只有一个 H1，FAQ 可见内容与 `FAQPage` JSON-LD 保持一致。
- 不要修改：三个模块的标题、主题、案例图、图片文件、图片顺序、替代文本、图片说明、模块布局、FAQ、SEO 标题、H1、meta description、canonical、hreflang、首屏、三步流程、产品能力、格式、额度、保留规则、认证、处理流程或非英文页面。不得加入未经证实的节省时间、成本、转化率、效果保证、客户评价或第三方软件兼容性声明。

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
- 当前问题与线上证据：`2026-08-14` 的 `Seeing what a transparent master is for` 已经记录三个图文模块和 FAQ 上线；本轮浅显文案尚未发布，因此没有对应的新记录。
- 修改要求：浅显文案成功上线后，只新增一条带日期的公开记录。文案只需说明首页三个案例说明现在使用更直接、容易理解的语言，并帮助新手理解如何复用透明视频、适配不同画幅及交给编辑者继续处理。如果文案没有成功上线，则不要新增记录。纯结构化数据补充不必单独描述。
- 验收标准：本批次恰好新增一条记录；只描述实际上线且用户可见的文案改进；内容简洁、脱敏并与线上页面一致；`2026-08-14` 及更早的历史记录和日期保持不变。
- 不要修改：历史记录及其日期。不得提及文件名、组件名、代码架构、仓库、分支、提交、基础设施、服务商配置、成本、密钥、安全敏感实现、客户数据、内部指标、AI 提示词或内部工作流程。
