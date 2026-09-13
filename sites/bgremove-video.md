---
site_id: "bgremove-video"
name: "BGRemove"
production_url: "https://bgremove.video/"
changelog_url: "https://bgremove.video/changelog/"
delivery_method: "direct_publish"
target_repository: "not_applicable"
default_branch: "not_applicable"
updated_at: "2026-09-14"
---

# BGRemove 当前待办事项

## 已批准任务

### 把去绿幕页未登录对比示例的原视频改为绿幕背景

- 优先级：`P1`
- 页面或界面：英文及 `es`、`pt`、`de`、`fr` 五个 Remove Green Screen 页面在用户未登录时显示的首屏 Source / Alpha out 对比视频
- 当前问题与线上证据：2026-09-14 未登录状态线上复核显示，`https://bgremove.video/green-screen-remover/` 首屏对比区域仍加载与首页相同的普通室内背景原视频 `hero-source...mp4`，右侧则是透明结果 `hero-matte...webm`。页面主题是去除绿幕，但对比滑块左侧没有绿幕，无法直观看出“绿幕原片 → 透明结果”的对应关系。用户明确要求保留当前人物视频，只把原视频背景制作成绿色。
- 修改要求：保留当前透明示例中的同一人物、动作、服装、构图、时长、尺寸、帧率和播放节奏，使用当前透明人物素材合成一份背景为均匀纯绿色的原始示例视频，并用它替换五个去绿幕页面未登录首屏对比组件左侧的 Source 视频及对应 poster。绿色背景需要清楚呈现为拍摄用绿幕，不加入房间、道具、渐变、纹理、阴影或文字；人物本身不得染绿、变形、换脸、重绘、裁切或改变比例。右侧 Alpha out 继续使用当前已经确认的透明结果，不重新生成另一名人物。两段素材必须从同一帧开始、时长一致并共用当前播放、暂停、循环和拖动对比逻辑；五种语言复用同一对视频素材，只本地化已有界面文字。
- 验收标准：清除缓存后，以未登录状态分别打开英文、西班牙语、巴西葡萄牙语、德语和法语去绿幕页，首屏对比滑块左侧始终显示当前人物位于纯绿色背景前，右侧始终显示完全相同人物和动作的透明棋盘格结果；拖动滑块时人物轮廓、位置、比例和当前帧逐像素对齐，不出现两个人物、跳帧、时间偏移、黑帧、旧室内背景、绿边加重或画面拉伸。点击播放后两侧同步播放并同步循环，暂停后帧位置一致；poster 在视频载入前也显示同一人物和绿幕背景，不短暂闪现旧背景。桌面端和移动端均无溢出、裁切或布局变化；已登录后的上传、作品列表和处理流程不受影响。
- 不要修改：去绿幕页的 H1、正文、功能、额度、格式限制、透明输出、CTA、SEO 元数据、结构化数据、页面布局及已登录工作区；不替换人物、不使用首页普通背景示例、不修改首页对比视频。该修改属于页面示例素材修正，不新增或修改公开 Changelog。

### 修正 Blog 文章的 Meta description、署名链接与图片 alt

- 优先级：`P2`
- 页面或界面：`https://bgremove.video/es/blog/transparent-webm-background/`；五种语言的 15 个 Blog 文章页；英文 `/blog/choose-video-background/` 与 `/blog/transparent-webm-background/`
- 当前问题与线上证据：2026-09-14 线上复核确认，西班牙语文章 `/es/blog/transparent-webm-background/` 的 Meta description 为 164 个字符，超过本批批准的 155 字符上限。15 个文章页都可见显示本地化的 `By BGRemove` 或等效署名，`BlogPosting` JSON-LD 也正确引用 BGRemove 组织实体，但可见署名只是普通文本，没有链接到对应语言 About 页面。英文背景选择文章的主图实际是空白显示器，alt 却写成 `A desk with a monitor showing a video preview next to a notebook and a coffee cup`；英文透明 WebM 文章的主图实际是空白笔记本屏幕，alt 却写成 `A laptop on a desk showing a video editing timeline with a layered clip`，屏幕中没有可见预览或时间线。其他四种语言已经把这两张图片描述为空白屏幕，只有英文 alt 与图像不符。
- 修改要求：把西班牙语透明 WebM 文章的 Meta description 精确替换为 `Aprende por qué un WebM transparente puede seguir mostrando un fondo, cómo comprobar el canal alfa y qué hacer si tu reproductor no lo interpreta.`。在全部 15 个 Blog 文章页中，把可见的 BGRemove 组织署名改为可访问链接：英文指向 `/about/`，西班牙语指向 `/es/about/`，巴西葡萄牙语指向 `/pt/about/`，德语指向 `/de/about/`，法语指向 `/fr/about/`；保留当前语言已有的署名前缀、发布日期和版式。把英文背景选择文章主图 alt 改为 `A desk with a blank monitor beside a notebook and a coffee cup`，把英文透明 WebM 文章主图 alt 改为 `A laptop with a blank screen on a desk beside a notebook and a plant`。保持结构化数据中的 author 和 publisher 继续引用同一个 BGRemove Organization，不新增个人作者。
- 验收标准：西班牙语页面源代码和渲染后的 Meta description 与定稿逐字一致、长度不超过 155 个字符，Title、H1、正文和社交分享文案不变；15 个文章页的可见 BGRemove 署名均是可聚焦、可点击的链接，目标为当前语言 About 页面且直接返回 `200`，键盘焦点清楚，不造成日期换行或移动端溢出；两张英文主图的 alt 与定稿逐字一致，其他语言现有准确 alt 不变。15 个页面的 canonical、`hreflang`、`BlogPosting`、Breadcrumb、文章正文、发布日期、主图文件及内链保持可解析和正常显示。
- 不要修改：文章标题、H1/H2、正文、摘要、URL、主图文件、其他语言 Meta description、其他图片 alt、Blog 列表页、产品功能页、导航、页脚或 Sitemap；不增加个人姓名、职位、履历或虚构作者资质。该任务属于轻微 SEO 与可访问性修正，不新增或修改公开 Changelog。
