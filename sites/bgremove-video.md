---
site_id: "bgremove-video"
name: "BGRemove"
production_url: "https://bgremove.video/"
changelog_url: "https://bgremove.video/changelog/"
delivery_method: "direct_publish"
target_repository: "not_applicable"
default_branch: "not_applicable"
updated_at: "2026-09-02"
---

# BGRemove 当前待办事项

## 已批准任务

### 调整首页额度提示、完成状态和作品列表入口

- 优先级：`P1`
- 页面或界面：英文首页 `https://bgremove.video/` 去背景处理完成后的左侧结果卡，以及右侧 `Your recent clips` 作品列表
- 当前问题与线上证据：用户提供的当前状态显示，每 24 小时免费去背景 3 次的新提示被错误放进了换背景功能模块，首页去背景功能模块仍显示旧提示。用户之前提供的首页截图还显示，左侧结果卡依次提供 `Download`、`Change the background` 和 `Run another` 三个操作；右侧作品列表的每条记录只有下载图标，没有可以直接针对该作品使用的换背景入口。
- 修改要求：首页去背景功能模块只使用一句精简额度提示，文案精确为 `Remove up to 3 video backgrounds for free every 24 hours.`；用它替换该功能模块内现有的旧额度提示，不再添加标题、第二句解释、额度卡片或重复文案。提示应靠近上传或剩余额度区域，使用可读但不抢过主操作的辅助文字样式。从左侧处理完成卡中完全移除 `Change the background` 按钮；保留 `Download` 和 `Run another`，并在同一行使用两个并排按钮展示，`Download` 继续使用绿色主按钮样式，`Run another` 使用现有次级按钮样式，两者宽度和高度协调，不再把 `Run another` 单独放在下一行。右侧 `Your recent clips` 中每一条已经完成、可以继续换背景的作品记录都增加一个可见文字按钮 `Change the background`，不能只使用含义不明确的图标；保留该记录原有的下载操作，把两个操作放在记录右侧的同一操作区。点击某条记录的 `Change the background` 后进入 `/change-background/`，并把当前这条作品作为换背景工具中已选择的视频；选择依据必须使用该作品稳定标识，不能根据列表位置、显示日期或文件名猜测。若作品不可用，显示现有安全错误或空状态，不得误选另一条作品。不要为此发明新的公开接口或查询参数，优先复用现有选择和跳转机制。
- 验收标准：首页功能模块只出现一次完整文案 `Remove up to 3 video backgrounds for free every 24 hours.`，旧提示和其他重复的每日额度说明不再出现；该句在未登录、已登录和处理完成状态下均不会被截断或改成多句。去背景完成后，左侧结果卡只有 `Download` 和 `Run another` 两个操作，桌面端及 `390px` 宽移动端均保持并排、无截字、无重叠和无横向滚动；两个按钮分别继续执行下载当前透明视频和开始另一次去背景处理。右侧列表中每一条符合条件的作品都同时具有下载和 `Change the background` 操作；点击任意一条后，`/change-background/` 中预选的是被点击的同一作品，连续测试至少两条不同作品不会串选。按钮支持键盘操作，具有清晰的 `focus-visible` 状态；窄屏中允许把右侧记录的操作区换行到作品信息下方，但两个操作必须完整可见且不会被聊天悬浮按钮遮挡。
- 不要修改：下载文件内容、再次处理流程、作品排序、缩略图、日期、时长、分辨率、过期规则、额度、认证、用户作品数据、去背景处理或换背景合成行为。不要删除右侧原有下载操作，不要让左侧按钮跳转到错误流程，也不要为历史作品增加未经支持的恢复、续期或永久保存能力。

### 扩大换背景编辑区并突出导出操作

- 优先级：`P1`
- 页面或界面：`https://bgremove.video/change-background/` 的首屏功能区域
- 当前问题与线上证据：根目录换背景页、SEO 标题、正文、案例图、步骤、FAQ 和公开更新日志已经上线。用户提供的当前功能区截图显示，桌面端仍把近一半宽度分配给 `Your Finished Clips`，右侧只有少量缩略图和大片空白，导致真正需要操作的预览、背景类型和导出区域被压缩在左栏；`Export MP4` 仍贴在控制区右下角，不像页面的主要完成动作。用户进一步确认，每 24 小时免费去背景 3 次的新提示被错误放进了这个换背景功能模块；换背景实际完全免费且不限次数，因此这里应该显示与换背景本身有关的简短承诺。
- 修改要求：保留当前已经上线的标题、说明、案例、步骤、用途、隐私、FAQ 和 CTA，只重做首屏功能卡。删除功能区右侧的 `Your Finished Clips`、`See All`、作品缩略图及其空白栏，让换背景编辑器横跨整个内容宽度；不要在编辑器内部重新创建另一份作品列表。用户从首页某条作品的 `Change the background` 按钮进入时，直接加载对应作品。存在已选视频时，保留日期、时长和分辨率等必要信息，主体预览尽量使用可用宽度并保持视频比例，`None`、`Blur`、`Colour`、`Image`、`Video` 五种现有背景选项保持清晰可见。没有已选视频时，标题使用 `Remove a Background First`，说明使用 `This tool starts with a transparent video. Remove the original background, wait for the clip to finish, then come back here to add a new scene.`，CTA 使用 `Remove a Background`。

  从换背景功能卡中删除 `3 Free Background Removals Every 24 Hours`、`Remove the background from up to 3 videos every 24 hours.` 以及其他每日 3 次提示，不得把首页额度文案复制到这里。功能卡只显示一句与换背景相关的精简提示，文案精确为 `Change backgrounds as many times as you like, completely free.`；不添加标题、第二句解释、额度卡片或重复文案。页面下方现有的隐私和额度说明可以继续解释为什么不扣额度，但不能与这句核心承诺冲突。

  把 `Export MP4` 设为功能卡内唯一最突出的完成动作：位于背景选项和预览结果之后的独立操作行，桌面端水平居中，使用绿色主按钮、清晰下载图标和不小于约 `240px` 的可点击宽度；不能继续贴在控制项最右侧，也不能与隐私小字挤在同一行。移动端按钮使用容器全宽或接近全宽，最小高度 `48px`，上下留出明确间距。无可导出结果、正在合成或导出期间沿用真实禁用和进度状态，不能为了突出视觉而绕过现有状态判断。
- 验收标准：桌面端首屏采用“全宽居中标题区 + 单个全宽换背景功能卡”，不再出现 `Your Finished Clips`、`See All` 或右侧作品列表空栏；工具区准确加载从首页所选的作品，五种现有背景选项和 MP4 导出继续正常工作。换背景功能卡只出现一次完整文案 `Change backgrounds as many times as you like, completely free.`，不存在 `3 Free Background Removals Every 24 Hours`、首页的额度句或其他每日次数提示。`Export MP4` 位于独立操作行的视觉中心，桌面端明显居中，移动端接近全宽，并在禁用、处理中和可导出状态下行为正确。`390px`、`768px` 和常见桌面宽度下均无截字、重叠或横向溢出；当前已上线的正文、案例图、FAQ、SEO 元数据和结构化数据保持完整。
- 不要修改：实际支持的背景类型、浏览器本地合成、用户素材传输方式、24 小时额度规则、透明视频生成流程、MP4 导出内容、认证、用户视频、正文模块、案例图或非英文页面。不要重新加入换背景页作品列表，也不要把“3 次免费去背景”错误表述成“3 次免费换背景”。

### 统一换背景完全免费且不限次数的公开文案

- 优先级：`P1`
- 页面或界面：`https://bgremove.video/change-background/`、英文首页 `https://bgremove.video/`、`https://bgremove.video/faq/` 和 `https://bgremove.video/pricing/`
- 当前问题与线上证据：换背景页的 title、H1 和副标题已经说明免费，三步说明写着重新尝试不使用额外额度，页面 FAQ 也写着可以反复更换，但核心区域没有直接说“完全免费且不限次数”。同时，英文首页 FAQ 仍写着 `Not inside BGRemove — there is no background library here.`，首页部分图文仍把外部编辑器描述成添加背景的唯一方式；独立 FAQ 的 `What exactly do I get back?` 仍写着 `Nothing is composited onto a colour for you, because that step belongs in your editor`。这些说法已经与当前可在 BGRemove 内添加颜色、模糊、图片或视频并导出 MP4 的功能冲突。Free Access 页面只解释去背景的 3 次额度，没有明确区分不限次数的换背景。
- 修改要求：全站统一使用以下产品边界：每个账户每 24 小时最多完成 3 次免费去背景；已经完成去背景的视频可以在 BGRemove 内不限次数、完全免费地更换背景，换背景不消耗去背景额度。按以下要求修改英文文案：

  - 换背景功能卡使用唯一一句核心提示 `Change backgrounds as many times as you like, completely free.`。
  - 换背景页 FAQ 的 `Does changing a background use another allowance?` 回答改为 `No. Background changes are completely free and unlimited. The allowance is used only when removing the original background.`；可见答案与 `FAQPage` JSON-LD 必须逐字一致。
  - 英文首页 FAQ 的 `Can I replace the background after removing it?` 回答改为 `Yes. Open a finished clip in Change Background, add a color, blur, image, or video, and export the result as an MP4. Background changes are completely free and unlimited.`，并把 `Change Background` 设为指向 `/change-background/` 的描述性链接。
  - 英文首页图文中凡是声称必须使用外部编辑器、BGRemove 只生成透明视频或 BGRemove 不能添加背景的绝对说法，都改为同时说明两种真实路径：可以在 BGRemove 中添加颜色、模糊、图片或视频并导出 MP4；需要文字、复杂排版、画幅调整或更多控制时，仍可把透明 WebM 放入外部编辑器。不得删除仍然准确的高级编辑工作流说明。
  - 独立 FAQ 的 `What exactly do I get back?` 删除 `Nothing is composited onto a colour for you, because that step belongs in your editor where it is reversible.`，改为 `You can download the transparent WebM, or open the finished clip in Change Background to add a color, blur, image, or video and export an MP4.`。
  - 独立 FAQ 新增 `Is changing a background free?`，回答使用 `Yes. Background changes are completely free and unlimited. The 3-video allowance applies only when removing an original background.`；同时增加指向 `/change-background/` 的描述性入口，并同步 FAQ 结构化数据。
  - Free Access 页面在解释 3 次去背景额度的区域增加一句 `Changing the background of a finished clip is completely free and unlimited.`，并把 `Change Background` 的描述性链接指向 `/change-background/`。

- 验收标准：换背景功能卡、换背景页 FAQ、首页 FAQ、首页相关图文、独立 FAQ 和 Free Access 页面对产品规则的表达一致；任何页面都不再声称 BGRemove 不能换背景、没有换背景功能或只能在外部编辑器中添加背景。所有“3 次”表达都明确只指每 24 小时的去背景成功任务；所有换背景表达都明确为完全免费、不限次数且不消耗去背景额度。指定英文文案逐字出现，页面中的相关链接返回成功；两个 FAQ 页面的可见问答与各自 `FAQPage` JSON-LD 一致；未执行 JavaScript 时仍能读取这些说明。
- 不要修改：每 24 小时 3 次去背景的真实额度、失败任务是否计数、去背景输入限制、透明 WebM 输出、换背景支持的四种类型、浏览器本地合成、MP4 导出或保留期限。不要声称换背景包含自动光线匹配、复杂排版、文字、字幕、画幅转换、背景素材库或其他未上线功能，也不要把外部编辑器从高级工作流说明中完全删除。

### 重新整理全站页脚菜单

- 优先级：`P1`
- 页面或界面：英文站所有公开页面的公共页脚
- 当前问题与线上证据：公开页面的页脚目前不一致。`https://bgremove.video/changelog/` 已经显示新的 `Product`、`Resources` 和带 `Changelog` 的 `Company` 分组，但首页抓取结果仍显示旧的五栏结构，`Product` 下仍放置 `How it works`、`Free Access`、`FAQ` 和 `Changelog`。说明菜单重组只在部分页面生效，尚未统一覆盖所有使用公共页脚的英文页面。
- 修改要求：按以下信息架构调整公共页脚，链接文案、顺序和地址必须一致：

  - `Product`：`Remove Video Background` → `/`；`Change Video Background` → `/change-background/`。
  - 新增 `Resources`：`How it works` → `/how-it-works/`；`Free Access` → `/pricing/`；`FAQ` → `/faq/`。
  - `Company`：保留 `About` → `/about/`、`Contact` → `/contact/`、`Status` → `/status/`，并在其后加入 `Changelog` → `/changelog/`。
  - `Use cases`、`Compare` 和 `Legal` 的现有栏目名称、链接、顺序保持不变。

  `How it works`、`Free Access`、`FAQ` 和 `Changelog` 必须从 `Product` 移除，但仍各保留一个清晰的页脚入口；不得为了兼容旧结构在多个栏目重复同一链接。桌面端为新增的第六栏重新分配合理列宽，移动端继续使用清晰的两列或单列排列。
- 验收标准：所有使用公共页脚的英文页面都呈现相同菜单结构；`Product` 恰好只有两个功能，`Resources` 恰好包含三个说明和帮助入口，`Company` 在原有三项后显示 `Changelog`；所有地址返回成功，不存在指向旧 `/app/change-background/` 的页脚链接，也不存在丢失或重复的四个迁移链接。所有链接支持键盘访问并具有可见焦点状态；`390px` 宽度下栏目不溢出、不截字，桌面端六栏不拥挤，页脚品牌、联系邮箱、版权和法务信息保持完整。
- 不要修改：对应页面内容、主导航、功能行为、页脚品牌说明、邮箱、版权、语言选择器或未列出的链接。不要删除说明、FAQ 或 changelog 页面，也不要增加尚未上线的产品功能。

### 修复换背景页的小字对比度和移动端遮挡

- 优先级：`P1`
- 页面或界面：`https://bgremove.video/change-background/` 桌面端和移动端
- 当前问题与线上证据：现有 `text-ink-faint` 小字在卡片背景上的实测对比度约为 `3.49:1`，低于 WCAG AA 对普通文本的 `4.5:1` 要求。`390×844` 移动端中，右下角聊天悬浮按钮可能覆盖按钮、FAQ 或文字；空状态中的装饰性 SVG 没有明确从辅助技术中隐藏。
- 修改要求：提高所有承载实际信息的小字颜色对比度，使普通文本达到至少 `4.5:1`；不能仅增加字体粗细而保留不足的颜色。装饰性 SVG 增加 `aria-hidden="true"` 且不可聚焦。为固定聊天按钮预留移动端安全空间，确保它不会覆盖主按钮、表单控件、FAQ 展开按钮、文字或页脚链接；同时保留清晰的键盘焦点样式，并遵循 `prefers-reduced-motion`。
- 验收标准：使用对比度工具复测所有正文和辅助说明，普通文本不低于 `4.5:1`，大号文本不低于 `3:1`；`390×844`、`768×1024` 和常见桌面宽度均无横向溢出，聊天按钮不覆盖任何可交互元素或重要文字；装饰图不进入可访问名称；所有链接和按钮可通过键盘到达并具有可见的 `focus-visible` 状态。
- 不要修改：全站品牌色方向、深色主题、聊天服务本身、功能行为或其他页面的版式。不要通过缩小内容、隐藏说明或禁用页面缩放来解决遮挡。

### 补充 Organization 的公开法定名称

- 优先级：`P2`
- 页面或界面：英文首页 `https://bgremove.video/` 的 `Organization` 结构化数据
- 当前问题与线上证据：首页当前公开的 `Organization` 已包含支持邮箱和 `contactPoint`，但仍没有把 About 页面公开显示的法定名称 `BGRemove d.o.o.` 表达为 `legalName`。
- 修改要求：继续使用 `https://bgremove.video/#organization` 作为唯一稳定的组织 `@id`，只增加 `legalName: "BGRemove d.o.o."`。其他页面继续通过同一 `@id` 引用该实体。
- 验收标准：首页 `Organization` JSON-LD 可解析，`legalName` 与 About 页面公开名称完全一致；全站不存在名称或 `@id` 冲突；Schema.org 验证没有关键错误。
- 不要修改：可见公司名称、地址、邮箱、现有 `contactPoint` 或其他法定信息。不要虚构电话、注册标识、税号、社交账号、评价、奖项或外部实体链接。

### 更新本次发布的公开更新日志

- 优先级：`P1`
- 页面或界面：`https://bgremove.video/changelog/`
- 当前问题与线上证据：公开更新日志已经包含 `2026-08-31` 的 `A page for changing a video background`，该记录对应已经上线的根目录页面、图文内容、FAQ、隐私和额度说明；尚未记录本文件中仍待发布的首页作品入口、全宽换背景编辑区、突出导出按钮、免费不限次数文案统一和页脚菜单调整。
- 修改要求：本批次成功发布后只新增一条带日期的公开记录。只概括实际发布且用户可见的改进：首页用一句简短文字说明每 24 小时可免费去背景 3 次；可以从首页每条已完成作品直接进入换背景；换背景编辑区更宽且 MP4 导出更明显；相关页面现在清楚区分有限的去背景额度与完全免费、不限次数的换背景；页脚能分别找到两个产品功能和说明资源。若某项没有成功发布，不得在记录中声称已经完成；如果没有任何可见改进成功发布，则不要新增记录。
- 验收标准：本批次恰好新增一条记录；内容简洁、脱敏、面向用户并与线上实际状态一致；`2026-08-31` 及更早的历史记录和日期保持不变。
- 不要修改：历史记录及其日期。不得提及文件名、组件名、代码架构、仓库、分支、提交、基础设施、服务商配置、成本、密钥、安全敏感实现、客户数据、内部指标、AI 提示词或内部工作流程。
