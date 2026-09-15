---
site_id: "imagehub"
name: "ImageHub"
production_url: "https://imagehub.ai/"
changelog_url: "https://imagehub.ai/changelog/"
delivery_method: "not_established"
target_repository: "not_established"
default_branch: "not_established"
updated_at: "2026-09-15"
---

# ImageHub 当前待办事项

## 已批准任务

### 为登录用户新增可复用的个人素材库

- 优先级：P1
- 页面或界面：首页集合 Workspace、登录后的完整 Workspace、全部具有图片输入的独立功能落地页、纯文本生成工具的任务提交入口，以及登录用户的图片来源选择弹窗和素材库管理界面；覆盖桌面端与移动端
- 当前问题与线上证据：当前图片输入只允许用户重新从本地设备选择文件，登录用户不能直接复用自己之前上传的图片或已经生成、编辑、增强、移除处理得到的结果。线上也没有供用户查看存储占用、删除素材或处理容量不足的个人素材库。
- 修改要求：为每个登录账户建立私有 Library。登录用户以后上传的每张原图，以及成功生成、编辑、增强、移除或以其他 ImageHub 功能处理得到的每张结果图，都自动作为独立素材长期保存到该用户的 Library，直到用户主动永久删除或删除账户；失败、取消或未产生结果的任务不得创建结果素材。上线时将该账户当前仍可访问的历史上传图片和历史生成或处理结果纳入 Library，不尝试恢复已经过期、删除或无法访问的历史文件。每项素材至少保存稳定唯一标识、所属用户、来源类型 Uploaded 或 Generated、原始文件名（如存在）、MIME 类型、实际文件字节数、像素宽高、创建时间、可用缩略图和原图访问引用；所有读取、选择、下载和删除操作必须在服务端校验素材所有权，任何账户不得通过修改 URL、素材标识或请求参数访问其他用户的素材。
  登录用户点击任何图片输入槽位时，不再立即打开系统文件选择器，而是先打开标题为 Add an image 的站内模态弹窗，显示两个同级入口：Upload from device 和 Choose from Library。Upload from device 打开现有本地文件选择流程；Choose from Library 在同一弹窗中进入该用户的素材网格。未登录用户继续直接使用现有本地上传流程，不显示素材库入口，也不得因此被要求登录。多图功能必须针对当前输入槽位打开选择器，并只允许选择符合该槽位实际格式、数量和用途要求的素材；选择现有素材后直接引用该素材完成预览和任务提交，不重新上传文件，不在 Library 中创建重复副本。关闭弹窗不得清空已选择的图片、提示词或参数。
  素材网格按创建时间从新到旧排列，展示缩略图、来源类型、创建时间和文件大小；提供空状态 No images in your Library yet.、加载状态、失败重试、分页或渐进加载，并在移动端保持可用。网格顶部持续显示 Storage used 和可见格式 {used} MB of {limit} MB，数值来自服务端，不由客户端推算。素材库管理必须支持单张删除和多选批量删除。用户第一次点击任何删除操作时只能打开二次确认弹窗，不得立即调用删除接口或改变素材状态；确认标题为 Permanently delete selected items?，正文动态显示 This will permanently delete {count} item(s) and free {size}. This can’t be undone.，主按钮为 Delete permanently，次按钮为 Cancel。只有用户在二次确认弹窗中点击 Delete permanently 后才执行永久删除；点击 Cancel、关闭按钮、遮罩或 Escape 均不得删除任何素材。服务端删除成功后才从网格移除素材并刷新占用；删除没有回收站、撤销或恢复入口，重复请求必须幂等。删除 Library 素材不得取消、损坏或改变已经提交的任务；任务运行需要的输入快照按现有任务生命周期独立处理。
  存储额度必须是账户套餐级的服务端配置能力，不得只在客户端写死。免费账户的额度固定为 100 MiB，即 104,857,600 bytes；界面显示为 100 MB。额度计算只累计 Library 中原始上传文件和生成或处理结果文件的实际存储字节数，缩略图和数据库元数据不计入用户额度。数据模型和额度接口必须允许未来不同付费套餐配置不同 storage_limit_bytes，但本批次不得创建、展示、销售或承诺任何付费套餐。选择 Library 中已有素材不增加占用；删除成功后按实际删除文件大小立即释放额度。
  本地上传文件的字节数在传输或持久化前与服务端当前占用相加；如果会超过账户额度，则不得上传、创建素材、启动任务或扣减每日免费次数。纯文本生成或任何无法提前确定结果大小的任务在当前占用小于额度时允许正常开始；成功结果必须保存，即使该结果使总占用超过额度，随后立即阻止该账户继续上传或启动任何新生成、编辑、增强、移除任务，直到实际占用重新低于该账户额度。当前占用已经达到或超过额度时，所有新上传和新任务提交都显示同一 Storage limit reached 弹窗，正文为 Your Library is full. Delete items to upload or generate new images.，并提供 Free up 10 MB、Manage Library 和 Cancel。因存储额度被阻止的尝试不得上传任务数据、调用处理服务、创建任务、加入队列、扣减每日免费次数或清空当前输入。
  Storage limit reached 弹窗中的 Free up 10 MB 是固定操作，每次固定以释放 10 MiB（10,485,760 bytes）为目标，不提供 5 MB、20 MB、自定义数值或其他释放量选项。第一次点击 Free up 10 MB 只能打开二次确认，不得立即删除；确认标题为 Permanently delete oldest items?，正文为 This will permanently delete your oldest Library items until at least 10 MB is freed. This can’t be undone.，主按钮为 Delete and free space，次按钮为 Cancel。只有点击 Delete and free space 后才执行删除；取消或关闭确认弹窗不改变任何素材。服务端按创建时间从早到晚选择素材；创建时间相同则按稳定素材标识排序；删除累计达到 10 MiB 所需的最少完整素材数量后立即停止。素材必须整张永久删除，不得截断文件；当最后一张完整素材使实际释放量略高于 10 MiB 时允许超过，但该次操作的目标值始终固定为 10 MiB，不得继续删除下一张素材。正在被已提交且未结束任务使用的素材不得删除，自动跳过并继续选择下一项。操作成功后显示 Storage space freed. 并立即刷新网格和占用；如果本次清理后总占用仍达到或超过额度，继续保持上传和生成禁用，并允许用户再次执行同一个 Free up 10 MB 操作或进入 Manage Library 手动删除。服务端必须防止重复点击、并发删除或重放请求导致超出已确认范围的重复删除。
- 验收标准：登录账户从任一单图和多图功能点击图片槽位时先看到 Add an image，并能分别完成本地上传和 Library 选择；未登录状态仍直接打开原有本地文件选择器。登录用户上传原图或成功得到任一功能结果后，该素材在刷新、退出并重新登录后仍出现在自己的 Library；当前仍可访问的历史素材在上线后出现，已删除或已过期素材不被虚构恢复。选择已有素材能够正常提交任务，网络记录中不重新上传同一文件，Library 占用和素材数量不增加。跨账户访问测试无法读取、选择、下载或删除其他账户素材。
  免费账户额度接口返回 104,857,600 bytes，界面显示 100 MB；上传已知大小文件时，used_bytes + file_bytes 大于额度即在文件上传和每日次数扣减前被阻止。当前占用低于额度时允许开始无法预知输出大小的任务；结果导致超限时结果仍保存并可查看，之后所有新上传和新任务均被阻止。存储限制和每日 3 次免费任务限制相互独立，存储失败不消耗免费次数。未来测试套餐可以仅通过套餐级配置获得不同额度，不修改客户端功能逻辑，也不在本批次公开任何付费方案。
  单张删除、批量删除和 Free up 10 MB 均需两步操作：第一次点击只打开确认弹窗，第二次点击确认主按钮才永久删除；取消、关闭或按 Escape 后素材数量、文件状态和存储占用完全不变。删除成功后文件不可访问、素材记录不再展示、占用按实际字节数减少，且没有回收站或恢复入口。每次 Free up 10 MB 的目标固定为 10,485,760 bytes，界面不存在其他可选释放量；服务端按最旧优先删除达到目标所需的最少完整素材数量，最后一张导致释放量略高于目标时不再继续删除下一张。操作不会删除正在被活动任务使用的素材，不会因重复点击或并发请求多删，完成后立即显示新占用。1440px、1280px、1024px 和 390px 视口下，来源选择、素材网格、存储提示、删除确认和快捷清理弹窗均无裁切、重叠或横向滚动；所有弹窗具有 dialog 语义、aria-modal、可访问标题、焦点锁定、Escape 关闭和关闭后的焦点返回，网格、选择、删除及确认可用键盘和触摸完成。
- 不要修改：不要改变全站共享的每用户每日 3 次免费任务额度、不同标签页可同时运行任务的现有规则、独立功能页无需登录的规则、无水印规则、图片格式和大小校验、任务处理参数、结果质量或下载行为；不要把 100 MiB 实现成每个工具各 100 MiB；不要把删除改成软删除、回收站或可恢复状态；不要自动删除最新素材，不要在未获得用户二次确认时执行 Free up 10 MB；不要在本批次加入价格、购买、升级入口或具体付费套餐权益。

### 为 Workspace 作品卡片新增完整预览、下载和删除

- 优先级：P1
- 页面或界面：登录后的完整 Workspace 及首页集合 Workspace 中所有已完成的作品卡片、作品预览弹窗；覆盖桌面端与移动端
- 当前问题与线上证据：Workspace 当前以裁切后的作品卡片展示生成或处理结果，用户不能点击卡片查看完整作品，也没有从完整预览直接下载、永久删除或将既有作品直接选入任务创建区继续处理的统一流程。
- 修改要求：所有已完成且仍可访问的作品卡片本体必须可点击，点击后打开站内模态弹窗，不跳转页面、不启动任务且不扣减每日免费次数。弹窗使用该作品的稳定标识重新向服务端读取当前账户有权访问的素材，不得只放大卡片缩略图；服务端必须校验作品和底层 Library 素材均属于当前登录账户。加载期间显示稳定骨架，读取失败显示 Unable to load this image.、Retry 和 Close，素材已被删除时显示 This image is no longer available.，不得泄露其他账户是否存在同一素材标识。
  弹窗以不裁切的 contain 方式在可用视口内显示完整作品，保持原始宽高比；透明图片使用可辨识透明区域的棋盘格背景。弹窗顶部提供可访问标题 Image preview 和 Close，底部操作区按主要操作、次要操作和危险操作的层级依次提供 Use this image、Download 和 Delete。
  Use this image 是主要按钮。点击后再次校验当前登录账户对该作品及底层 Library 素材的所有权，并使用与 Choose from Library 相同的素材引用和输入校验流程，将该作品直接选入当前 Workspace 底部任务创建模块的图片输入位，不重新上传文件，也不在 Library 创建副本。多图工具优先填入用户当前激活的图片输入位；没有激活位置时填入第一个空输入位；单图工具已有图片时，以该作品替换当前图片。选择成功后关闭作品预览，保持当前工具、模型、提示词和其他参数不变，并在固定功能模块中立即显示已选图片预览；不得自动提交任务、调用图片处理服务或扣减每日次数。作品不符合当前工具输入格式、数量或用途限制时不得选入、不得自动切换工具，弹窗保持打开并显示 This image can’t be used with the selected tool.。选择期间按钮显示加载状态并防止重复点击，失败显示 Unable to use this image. Try again.，原任务输入保持不变。
  Download 必须下载底层 Library 中的原始完整结果文件，不得下载缩略图、浏览器截图或重新压缩版本；使用素材原始文件名，缺少原始文件名时使用 imagehub-{asset_id}.{extension}，extension 必须与真实 MIME 类型一致。下载前再次校验登录状态和素材所有权，下载失败显示 Download failed. Try again.，不得关闭弹窗或删除作品。
  Delete 使用危险操作样式并复用 Library 单张永久删除的同一服务端流程和二次确认规则。第一次点击 Delete 只能打开确认弹窗，不得立即改变卡片、文件或容量；确认标题为 Permanently delete selected items?，正文按单张素材显示 This will permanently delete 1 item and free {size}. This can’t be undone.，主按钮为 Delete permanently，次按钮为 Cancel。只有用户再次确认且服务端删除成功后，才关闭预览、从首页及完整 Workspace 的作品列表移除对应卡片、从 Library 所有入口移除底层素材并按实际文件大小刷新存储占用；删除后原预览与下载 URL 立即失效且不可恢复。Cancel、关闭确认弹窗、点击遮罩或按 Escape 不得删除任何内容。删除请求必须幂等；已删除素材的重复请求按成功处理但不得重复扣减容量或影响其他素材。
  卡片中的其他独立操作按钮继续执行自身功能并阻止点击事件冒泡，不得因点击 Download、Delete、选择框或其他控件意外重复打开预览。预览弹窗打开时锁定页面背景滚动，焦点进入弹窗；Escape 先关闭最上层删除确认，再关闭作品预览；关闭后焦点返回原作品卡片。移动端图片区域在按钮之外支持双指缩放和拖动查看细节，按钮点击不得触发图片拖动。
- 验收标准：从首页集合 Workspace 和完整 Workspace 点击任一已完成作品卡片均打开同一完整预览，竖图、横图、方图和透明 PNG 均完整显示且不被裁切；打开、关闭或查看预览不创建任务、不调用处理服务且不消耗每日次数。点击 Use this image 后，弹窗关闭，当前功能模块立即显示该作品，底层素材标识与原 Library 素材一致，网络记录中没有重新上传或复制素材，Library 数量和存储占用不增加，工具、模型、提示词和参数不变。分别验证单图空输入、单图已有输入、多图当前激活位置和多图第一个空位置，素材均进入规定位置；不兼容素材保持弹窗和原输入不变并显示指定错误。重复点击只产生一次选择结果，查看和选择均不消耗每日次数。
  Download 得到的文件字节数、像素尺寸和 MIME 类型与 Library 原始结果一致，不是卡片缩略图；下载失败不关闭预览。Delete 第一次点击只出现确认，取消、关闭、遮罩或 Escape 后卡片、Library 文件和容量不变；确认成功后卡片从两个 Workspace 入口消失、Library 同一素材消失、占用按实际大小减少，旧预览和下载地址不可访问。修改素材标识或请求参数不能选择、查看、下载或删除其他账户作品。1440px、1280px、1024px 和 390px 视口及 200% 缩放下，图片、标题和 Use this image、Download、Delete 操作无裁切、重叠或横向页面滚动；弹窗具有 dialog、aria-modal、可访问标题、焦点锁定和焦点返回，全部操作可用键盘、鼠标和触摸完成。
- 不要修改：不要把按钮命名为 Edit、Reuse、Select 或其他文案，使用精确文案 Use this image；不要在选择作品时自动切换工具、提交任务、消耗免费次数、重新上传或复制素材；不要把预览改成新页面或浏览器新标签；不要下载缩略图或降低原始结果质量；不要新增公开分享链接；不要把永久删除改成仅隐藏 Workspace 卡片、软删除、回收站或可恢复状态；不要删除生成该作品所使用的其他输入素材或其他结果；不要改变 Library 删除规则、100 MiB 存储额度、每日 3 次免费任务、并发、登录、无水印或任务处理规则。

### 完成 Workspace 的移动端响应式适配

- 优先级：P1
- 页面或界面：首页集合 Workspace、登录后的完整 Workspace，以及 Workspace 内的 Header、导航、工具选择器、任务输入区、上传与 Library 选择、参数控件、任务状态、作品列表、作品卡片、空状态、限额提示和全部弹窗；覆盖手机竖屏、手机横屏及移动浏览器软键盘场景
- 当前问题与线上证据：用户确认当前 Workspace 在移动端没有完成适配。用户于 2026-09-15 提供的手机截图显示，在任务创建区选择名称较长的 Generate Background 工具后，工具选择器仍与 ImageHub Flash 模型选择器及右侧提交按钮保持桌面端横向排列；控件总宽度超过可视区域，模型名称和提交按钮被屏幕右侧裁切，页面产生横向溢出。用户同时明确要求删除 Workspace 顶部重复的功能分类菜单，并缩小 Workspace 顶部导航栏和 Logo，把释放的高度用于展示更多作品；工具选择统一由任务创建模块完成。其他桌面布局也可能使任务输入、作品卡片或操作控件无法在当前屏幕内稳定显示和操作，移动端不能作为完整可用的 Workspace 使用。登录后的完整 Workspace 无法在不使用真实账户的公开审计中核验，因此除截图所示问题外的登录后范围以用户提供的产品现状为依据。
- 修改要求：为 Workspace 建立移动优先的响应式布局，不得依赖桌面固定宽度、固定高度或页面级横向滚动。仅在登录后的完整 Workspace 页面中，桌面端与移动端均删除顶部 Header 内全部功能分类菜单及其下拉入口，包括 AI Generate、AI Enhance、AI Remove、AI Edit、AI Beauty 和同类工具分类；不得在移动端汉堡菜单、更多菜单或其他 Header 入口中重复保留这些分类。Workspace Header 只保留品牌首页入口、清晰的 Workspace 页面标识，以及当前已批准的 Library 和账户相关入口；主内容占满移除菜单后释放的可用宽度。
  将完整 Workspace 的 Header 做成紧凑单行：768px 及以上总高度固定为 56px，左右内边距为 16px；小于 768px 总高度固定为 48px，左右内边距为 12px。品牌 Logo 保持原始宽高比，桌面端可见高度不超过 28px，移动端不超过 24px，不得使用 CSS 非等比挤压；如果品牌标志与 ImageHub 字标为独立元素，二者同步按比例缩小并保持清晰。Workspace 标识、Library 和账户入口使用紧凑视觉尺寸，但每个交互入口仍保留至少 44×44 CSS px 的实际点击区域；点击区域可以大于图标或文字的可见尺寸，不得通过缩小触控范围换取高度。Header 下方不得保留已删除菜单的空白、占位容器或额外上边距，作品滚动区域的顶部边界必须紧接 Header，释放出的全部垂直空间归还作品展示区域。
  工具选择统一通过底部任务创建模块中的工具选择器完成，删除顶部菜单和缩小 Header 不得重置当前工具、任务输入、已选素材、参数、运行状态或列表滚动位置。本项不得删除首页或独立功能落地页的全站功能导航，也不得删除任何工具页面、链接目标或 Sitemap 条目。
  小于 768px 时，将包含图片输入、提示词、工具选择、模型选择、参数和提交按钮的整个任务创建模块作为一个整体固定在可视窗口底部，而不是随作品列表滚动离开屏幕。底部模块始终贴合当前 visual viewport，宽度不得超过页面可用宽度，底部内边距包含 `safe-area-inset-bottom`，层级高于作品列表但低于弹窗、菜单和抽屉。模块高度随当前内容变化，但在未打开软键盘的手机竖屏下不得超过 `55dvh`；超过时只允许模块内部正文区域纵向滚动，提示词输入框及底部控制栏仍可到达，不得让整个页面产生横向滚动。作品滚动区域必须动态增加至少等于底部模块实际高度加 16px 的底部留白，图片选择、参数展开或错误提示使模块高度变化时同步更新，确保最后一张作品可以完整滚到模块上方，不被固定模块遮挡。桌面端继续沿用现有非固定布局。
  任务创建区内部按内容顺序排列。图片预览、上传入口、提示词、工具选择器、参数和提交按钮均不得超出模块；并列参数在空间不足时换行或改为单列。小于 768px 时，提示词输入框下方的工具选择器、模型选择器和提交按钮必须保持为一条高度紧凑的单行控制栏，不得改成三行或让该区域因选中长名称而增高。控制栏使用可收缩布局并占满容器宽度：工具选择器和模型选择器共同使用提交按钮之外的剩余空间，工具选择器获得约 60% 的可用选择器宽度，模型选择器获得约 40%；两者都必须设置可收缩的 `min-width: 0`，提交按钮使用固定 44×44 CSS px 且不得被压缩或移出屏幕，控件间距计入容器宽度。不得为任一选择器保留由完整名称决定的固有最小宽度。
  工具和模型触发按钮必须使用 `width: 100%` 与 `max-width: 100%`，图标和下拉箭头不得压缩，名称文本区域以单行省略号处理且不得撑宽父级；按钮的可访问名称和 `title` 保留完整选中名称。小于 360px 时允许隐藏拖拽点阵和闪光等纯装饰性前置图标以增加文本空间，但不得隐藏工具名称、模型名称或下拉箭头。下拉菜单作为浮层展开，宽度不超过 `calc(100vw - 24px)`，不得参与撑宽控制栏；菜单项中的长名称允许自然换行并完整显示。菜单打开时默认定位并滚动到当前选中工具，用户切换后只更新原 Tools 位置的名称，不重新显示右侧功能标签。必须使用 Generate Background 以及站内实际字符数最长的工具名称作为边界测试，不得只用短名称验证。
  主要提交按钮在可操作状态下始终完整可见，加载、成功、失败、每日限额和存储限额状态不得遮挡输入或互相重叠。打开系统软键盘时，底部模块跟随 visual viewport 上移并保持贴在键盘上方，当前输入框和主要操作保持可见；不得使用固定 `100vh` 造成模块或操作被浏览器工具栏、键盘或安全区覆盖。关闭键盘后模块必须返回视口底部，不发生跳位、残留空白或页面滚动位置重置。
  作品列表在 320–767px 始终使用每行两张作品卡片的双列网格，列宽使用可收缩的等分布局，列间距与页面左右留白计入容器宽度，不得因卡片内容设置固有最小宽度而溢出。卡片图片使用统一比例的稳定预览区域；标题、状态和时间最多显示规定行数并以省略号收尾，完整信息保留在可访问名称或作品预览内。下载、删除、多选等操作必须采用不撑宽卡片的紧凑菜单或覆盖式控件，但仍保留至少 44×44 CSS px 的触控区域并阻止事件冒泡。卡片点击预览、下载、删除、多选及批量操作继续遵循各自已批准任务。选择模式下的批量操作栏保持可见，但不得覆盖底部固定任务模块或最后一行作品；长列表继续使用现有分页或渐进加载，不得一次渲染全部历史作品导致滚动卡顿。
  Workspace 内所有弹窗、抽屉和菜单必须适应当前可视区域：宽度不超过 `calc(100vw - 24px)`，高度不超过 `calc(100dvh - 24px)`，正文区域在需要时纵向滚动，标题和主要操作保持可达；不得出现弹窗整体超出屏幕、页面与弹窗双重横向滚动或关闭按钮不可见。上传与 Library 选择、作品完整预览、永久删除确认、每日 3 次限额和 Storage limit reached 等嵌套流程必须一次只让最上层界面接收焦点和触摸。所有布局变化使用现有设计系统的字号、颜色、圆角和间距，不建立与桌面端不同的功能版本。
- 验收标准：分别在 320×568、360×800、390×844、430×932 竖屏视口和 844×390 横屏视口中，从登录进入 Workspace 开始，能够完整完成选择工具、从本地或 Library 选图、填写提示词、修改参数、提交任务、查看运行状态、打开作品、下载、删除和多选操作；全流程没有页面级横向滚动、内容裁切、控件重叠、不可见关闭按钮或被固定区域覆盖的最后一项。手机视口中整个任务创建模块始终固定在当前可视窗口底部，滚动作品、选择图片、展开参数、出现错误、打开和关闭软键盘后均不离开底部、不超过宽度且不遮住最后一张作品；竖屏未打开键盘时模块高度不超过 55% 的动态视口。320–767px 下作品始终每行显示两张，连续加载至少 20 张作品后仍保持等宽双列、稳定间距和平滑纵向滚动。
  逐一选择 Generate Background 和站内实际名称最长的工具，已选工具、ImageHub Flash 模型选择器和 44×44 CSS px 提交按钮必须始终处于提示词下方的同一行并完整位于视口内，控制栏高度不得因名称长度发生变化；触发按钮可用省略号保持单行，但下拉菜单内能读取完整名称，打开菜单时当前工具处于可见选中状态，切换工具后不出现额外的右侧功能标签。首页集合 Workspace 与完整 Workspace 使用相同的移动端组件行为，切换视口方向或从 390px 扩大到桌面宽度后，已有输入、选择、任务状态和作品列表不丢失。
  在 iOS Safari 和 Android Chrome 的当前稳定版中打开和关闭地址栏、唤起软键盘、切换横竖屏、打开两层确认流程及滚动长作品列表，当前焦点和主要操作始终可见，背景滚动锁定正确，安全区内没有按钮被遮挡。320px 视口和 200% 浏览器缩放下仍可读取并操作全部核心控件；正文可重排，不通过页面横向滚动查看内容。所有交互控件具有至少 44×44 CSS px 触控目标、可见焦点和可访问名称；抽屉与弹窗具有正确语义、焦点锁定、Escape 关闭和关闭后的焦点返回。完整 Workspace 的 Header 在 320px、390px、768px、1024px 和 1440px 下均不显示、聚焦或展开 AI Generate、AI Enhance、AI Remove、AI Edit、AI Beauty 等功能分类菜单；小于 768px 时实测总高度为 48px、Logo 高度不超过 24px，768px 及以上总高度为 56px、Logo 高度不超过 28px。Header 下方不存在菜单空白或额外占位，作品区域从 Header 下一像素开始获得剩余可视高度；品牌、Workspace 标识、Library 和账户入口完整可用且触控区域不小于 44×44 CSS px。首页及独立工具页的顶部导航保持原样，桌面端 Workspace 其他布局与功能无回归。
- 不要修改：不要删除或隐藏移动端的 Workspace 核心任务功能、任务状态、作品操作、素材库入口、账户入口或品牌首页入口；不要把本次 Workspace Header 精简扩展到首页或独立功能落地页；不要删除工具页面、Sitemap URL 或底部任务创建模块中的工具选择器；不要把底部任务创建模块改成需要用户滚动页面才能找到的普通区块，也不要让它覆盖作品列表的可滚动终点；不要把移动端作品恢复为单列或一次只显示一张；不要创建只在移动端存在的另一套任务数据或接口；不要以整体页面缩放、强制横屏、固定桌面最小宽度或横向滚动代替响应式适配；不要改变工具参数、结果质量、每日 3 次免费任务、并发规则、100 MiB 存储额度、登录边界、无水印规则或素材永久删除规则。

### 在 Account 中新增密码与账户管理设置

- 优先级：P1
- 页面或界面：登录后的 Account 弹窗及其左侧导航，覆盖桌面端与移动端
- 当前问题与线上证据：当前 Account 弹窗没有独立的 Settings 入口，用户无法在站内修改 ImageHub 密码或永久删除自己的账户。用户已明确要求账户删除后立即清除该账户的全部数据，并要求通过输入确认文案防止误删。
- 修改要求：在 Account 弹窗左侧导航新增 Settings，点击后在弹窗主区域打开设置页，依次显示 Password 和 Delete account 两个清晰分区。Settings 必须沿用现有 Account 弹窗的视觉语言、关闭方式和响应式布局；切换左侧选项不得整页刷新，关闭后再次打开默认保持现有 Account 首屏，不把危险操作设为默认内容。
  Password 分区仅对已经拥有 ImageHub 本地密码凭据的账户显示修改表单，包含 Current password、New password 和 Confirm new password，以及 Change password 按钮。新密码必须使用现有注册密码的同一套强度和格式规则，不得另设冲突规则；两次新密码不一致、当前密码错误或新密码不合规时，在对应字段附近显示可理解的错误且不得更改密码。修改成功后显示 Password updated.，撤销除当前会话外的其他已登录会话，并继续保留当前设备登录状态。仅通过 Google 登录且从未建立本地密码的账户不显示密码输入框或 Change password 按钮，改为显示 Password is managed by Google.；不得为 Google 登录账户静默创建 ImageHub 密码。若一个账户同时拥有 Google 与本地密码两种登录方式，则正常显示修改密码表单，修改只影响本地密码，不解除 Google 登录。
  Delete account 分区必须使用危险操作样式，先说明删除会立即且永久删除账户及其全部数据，包括 Library 中的上传与生成素材、Workspace 内容、任务记录、账户设置和登录会话，且不能撤销或恢复。第一次点击 Delete account 只打开二次确认弹窗，不得删除、停用或改变任何数据。确认弹窗标题为 Permanently delete your account?，正文为 This immediately deletes your account and all of its data. This can’t be undone. Type DELETE MY ACCOUNT to confirm.，提供确认输入框、主按钮 Delete my account 和次按钮 Cancel。输入内容必须与大小写完全一致的 DELETE MY ACCOUNT 匹配后才启用主按钮；粘贴允许。确认文案只用于防误触，不能代替身份验证。每次删除账户都必须重新验证身份，不得因用户刚登录而跳过：本地密码账户再次输入当前密码；仅 Google 登录账户必须打开 Google 重新验证流程，并确认返回的 Google 唯一账户标识与当前 ImageHub 账户绑定标识完全一致，不能只按邮箱文本匹配；同时拥有两种方式的账户可使用任一已绑定方式重新验证。服务端签发的重新验证证明只能用于当前账户的一次删除请求，自签发起 5 分钟后失效，成功使用后立即失效。验证失败、取消、超时、账户不匹配或证明重复使用时不得删除任何内容。
  用户最终确认且身份验证成功后，服务端必须以不可被客户端绕过的单一账户删除流程立即取消尚未完成的任务，永久删除该账户的 Library 文件与记录、Workspace 内容、任务记录、账户设置、身份验证凭据和全部会话，并使相关素材链接、下载链接和接口访问立即失效；删除流程不得仅隐藏前端数据或只软删除账户。完成后清除本地会话，跳转到首页并显示 Account deleted.。删除请求必须幂等，重复提交不得报出其他用户数据或留下可重新登录的残余账户。任一步骤失败时不得显示删除成功，必须显示可重试错误并保持账户可访问，避免出现只删除部分数据却仍宣称成功的状态。
- 验收标准：拥有本地密码的账户可在 Account > Settings 中校验当前密码并成功修改密码，错误输入不会生效，成功后其他设备会话失效而当前设备保持登录；仅 Google 登录的账户只看到 Password is managed by Google.，没有密码表单；同时绑定 Google 和本地密码的账户仍可修改本地密码。Delete account 第一次点击只出现确认弹窗，未输入完全匹配的 DELETE MY ACCOUNT、取消、关闭、按 Escape 或身份重新验证失败时，账户及任何数据均不改变。完成确认和重新验证后，未完成任务被取消，账户、素材、Workspace、任务记录、设置、凭据和所有会话立即不可访问，原素材 URL 与接口返回未授权或不存在，原登录方式不能再登录该已删除账户；随后可按正常注册规则创建新账户，但不得恢复旧数据。1440px、1280px、1024px 和 390px 视口下，左侧 Settings、表单、危险区和确认弹窗无裁切、重叠或横向滚动；所有控件有可访问名称，错误提示与字段关联，确认弹窗具有 dialog 语义、aria-modal、焦点锁定、Escape 关闭和关闭后的焦点返回。
- 不要修改：不要为仅 Google 登录账户创建、重置或暗示存在 ImageHub 本地密码；不要将修改密码做成解除 Google 绑定；不要省略账户删除的精确输入确认和近期身份验证；不要提供回收站、宽限期、撤销、恢复、软删除或保留该账户数据的入口；不要改变登录、注册、每日免费次数、存储额度或套餐规则。

### 在用户下拉菜单新增素材库入口与容量总览

- 优先级：P1
- 页面或界面：全站登录状态下右上角用户头像下拉菜单，以及完整 Library 管理界面；覆盖桌面端与移动端
- 当前问题与线上证据：现有右上角用户菜单没有直接进入个人素材库的入口，用户也无法从全站导航快速查看全部文件、存储额度、已用空间和占用比例。
- 修改要求：在登录用户右上角头像下拉菜单中新增 Library 菜单项，使用与同级菜单一致的图标、字号、间距、悬停、键盘焦点和触摸状态。点击 Library 后关闭下拉菜单并打开完整 Library 管理界面，展示该账户全部可访问的上传素材与生成或处理结果，不得只显示当前工具、当前任务或最近文件。完整 Library 使用个人素材库任务规定的排序、缩略图、来源、时间、大小、分页或渐进加载、单张与批量永久删除、二次确认及跨账户权限校验规则。
  Library 顶部固定显示存储总览：标题 Storage、文本 {used} MB of {limit} MB · {percent}% used 和可视化进度条。used 与 limit 必须来自同一服务端额度接口的 used_bytes 和 storage_limit_bytes；MB 展示规则与现有素材库一致。percent 按 used_bytes / storage_limit_bytes × 100 计算并四舍五入为整数，不得用文件数量或客户端估算；成功上传、生成、处理、删除或执行 Free up 10 MB 后立即刷新。若成功结果使占用超过额度，文字允许如实显示超过 100% 的比例，进度条视觉填充最多为 100%，并同时显示现有 Storage limit reached 状态和管理入口。加载中使用稳定占位，接口失败时显示 Unable to load storage usage. 和 Retry，不得把失败误显示为 0 MB。
  未登录状态不显示 Library 菜单项；直接访问 Library 管理地址时应进入现有登录流程，登录成功后返回 Library。素材库空状态仍显示存储总览和 No images in your Library yet.，并提供返回可用图片工具的明确入口；有素材时允许通过键盘和触摸打开、选择、下载及进入删除流程。
- 验收标准：登录后从首页、任一功能落地页和 Workspace 的用户头像菜单都能看到并打开 Library；打开后可查看账户全部文件，文件集合、顺序、大小和删除结果与 Add an image 弹窗中的 Library 数据一致。容量区域准确显示 used、limit 和整数占用比例；测试上传、生成和删除后无需刷新整页即可更新，超过额度时文本不被错误限制为 100%，接口失败不显示伪造的零占用。未登录时菜单中没有 Library，直接访问会先登录并正确返回。1440px、1280px、1024px 和 390px 视口下，菜单、文件网格、容量文字和进度条无裁切、重叠或横向滚动，头像菜单和 Library 可通过键盘完整操作。
- 不要修改：不要公开其他用户的文件或容量；不要把容量比例按素材数量计算；不要创建第二套与素材库任务不同的存储、排序或删除规则；不要改变未登录用户可在独立功能页直接处理任务的现有规则；不要新增价格、升级按钮或具体付费套餐权益。

### 修复全站移动端首屏性能和静态资源传输

- 优先级：P1
- 页面或界面：https://imagehub.ai/ 首页、全部 32 个独立工具页、About、Privacy、Terms、Changelog 及共用 Header、Footer、Account、Sign in 和 Workspace 入口；覆盖首次访问的移动端与桌面端
- 当前问题与线上证据：2026-09-15 使用 Lighthouse 12.8.2 默认移动模拟对线上页面测试，首页 Performance 为 53、FCP 6.6 秒、LCP 10.0 秒、CLS 0.119、初始传输约 3.08 MB；AI Background Remover 页面 Performance 为 58、FCP 6.5 秒、LCP 10.2 秒、CLS 0.027、初始传输约 2.67 MB。两类模板均加载约 1.19 MB 字体，其中 Material Symbols 字体约 1.13 MB；显示为约 32px 的 Header Logo 下载约 436 KB；静态 CSS 和 JavaScript 未返回 gzip 或 Brotli 内容编码；图片缺少响应式候选，Lighthouse 估算首页可减少约 1,118 KiB、工具页可减少约 877 KiB 图片传输。该问题会拖慢首屏内容呈现，并使字体替换造成布局移动。
- 修改要求：移除全站对完整 Material Symbols 可变字体的依赖，将实际使用的界面图标全部改为现有视觉风格一致的本地 SVG；图标保持当前含义、尺寸和可访问名称，不得继续加载 Material Symbols 字体或将图标名称文本短暂显示给用户。将 Alexandria 和 Manrope 改为自托管 WOFF2，并只交付页面实际使用的字符集、字重和样式；只预加载首屏必需字体，其余字体延后加载，设置与现有视觉最接近的系统字体 fallback 和匹配的字体度量，避免字体加载改变标题、按钮和卡片尺寸。不得继续从 fonts.googleapis.com 或 fonts.gstatic.com 加载生产字体资源。
  为各页面 Header 中实际显示的 Logo 提供尺寸接近对应渲染需求的轻量资源，单次传输不超过 15 KiB；完整 Workspace 使用其已批准的桌面端不超过 28px、移动端不超过 24px 显示高度，其他页面保持各自现有显示尺寸。保留结构化数据和社交分享需要的高分辨率品牌图，不得把小尺寸 Header 文件用于需要高分辨率的场景。所有公开内容图片根据实际布局生成至少移动端与桌面端两个合理宽度候选，统一使用 picture：AVIF source 提供响应式 srcset，WebP img 作为回退，并设置正确 sizes，让浏览器不下载明显大于渲染尺寸的文件。每页最多只允许一张实际位于首屏的图片使用 loading=eager 和 fetchpriority=high；其余图片使用 loading=lazy 和 decoding=async。首页不得再同时 eager 加载 5 张工具卡图片；轮播或横向列表只先加载当前视口实际可见内容，交互前不得预取整套画廊。所有图片继续提供准确 width、height 和 alt，避免布局跳动。
  对 HTML、CSS、JavaScript、JSON、SVG 和 XML 文本响应启用 Brotli，客户端不支持 Brotli 时回退 gzip；压缩响应必须返回正确 Content-Encoding 和 Vary: Accept-Encoding。带内容哈希的静态资源继续使用长期 immutable 缓存；HTML、Sitemap、robots.txt 和接口响应不得因缓存配置返回过期用户状态或过期页面内容。减少首屏不需要的 CSS 和脚本，只把当前页面所需的样式和行为放入关键加载路径；登录、验证、Account、Library 等非首屏弹窗资源在不影响首次点击可用性的前提下延后加载。优化后不得通过隐藏服务器端正文、移除结构化数据、延迟 H1 或删除功能来换取分数。
- 验收标准：在生产环境清缓存后，以 390×844 视口、Lighthouse 12.8.2 或更高版本默认移动配置连续运行 3 次，取中位数；首页和至少 AI Background Remover、AI Edit、AI Image Upscaler 各自达到 Performance ≥ 90、LCP ≤ 2.5 秒、CLS < 0.1、TBT < 200 毫秒，且 Lighthouse SEO 不低于 100。首页首次加载总传输不超过 1.5 MB，抽测工具页不超过 1.5 MB；页面不得请求 fonts.googleapis.com、fonts.gstatic.com 或完整 Material Symbols 字体。Header Logo 单次传输不超过 15 KiB；首页不再同时 eager 请求 5 张工具卡图片。使用支持 Brotli 的请求访问 HTML、CSS、JavaScript、JSON、SVG 和 XML 时返回 br，禁用 Brotli但支持 gzip 时返回 gzip，二者均包含 Vary: Accept-Encoding。1440px、390px 及 200% 缩放下文字、图标、导航、弹窗、Before/After 和工具输入区不发生可见错位、图标闪烁、内容缺失或横向滚动；所有功能仍可使用。
- 不要修改：不要删除或减少公开页面正文、FAQ、案例图、结构化数据或功能入口来降低传输量；不要改变字体和品牌视觉风格；不要降低结果图下载质量；不要缓存带账户身份、Library、Workspace、每日额度或任务状态的私有响应；不要改变每日 3 次免费额度、登录规则、并发规则或任务处理行为。

### 统一全站数据保存与免费使用声明

- 优先级：P1
- 页面或界面：https://imagehub.ai/ai-image-upscaler/、全站 Sign in 弹窗及其营销侧栏、首页和全部独立工具页中可见或初始 HTML 内的产品事实文案，以及对应 FAQ 和 JSON-LD
- 当前问题与线上证据：AI Image Upscaler 当前公开显示 ImageHub does not retain or scrape your image data. 和 No data retained or scraped，但 Privacy 说明未登录免费任务的上传与结果会在完成后 24 小时内从活动系统删除，已批准的个人 Library 还会长期保存登录用户素材。全站 Sign in 弹窗初始 HTML 还包含 Create without limits，与全站共享每用户每日 3 次免费任务的规则冲突。这些绝对表述可能被搜索引擎或生成式引擎单独提取为错误产品事实。
- 修改要求：本任务与个人 Library 及 Privacy/Terms 更新同批上线。删除 AI Image Upscaler 中所有 ImageHub does not retain or scrape your image data.、No data retained or scraped 及意思相同的绝对声明。首屏原位置改为 ImageHub processes your image only to provide the requested task. See our Privacy Policy for retention details.，其中 Privacy Policy 链接到 https://imagehub.ai/privacy/。卖点列表将 No data retained or scraped 改为 Not used for model training or advertising。涉及上传图片保存的 FAQ 答案统一为以下英文，逐字一致：ImageHub processes your upload only to provide the upscaling task. Content from tasks run without signing in is deleted from active systems within 24 hours after completion. When you are signed in, uploads and results are saved to your Library until you delete them or delete your account. ImageHub does not use your images to train models or for advertising.
  将所有 Sign in 弹窗营销侧栏中的 Create without limits 逐字替换为 Create, edit, and keep your work in one place.，其下说明逐字改为 Use individual tools without signing in, or sign in to start tasks from the all-in-one workspace.。全站搜索初始 HTML、可见正文、折叠内容、弹窗、按钮辅助文本、FAQ、Meta、Open Graph、Twitter 和 JSON-LD，删除 unlimited、no limits、without limits、no cap、as many as you want、no data retained 及其他与每日额度或保存规则冲突的表述。免费规则统一为 3 free tasks per user per day, shared across all ImageHub tools.；独立工具页继续说明无需登录，首页 Workspace 继续说明必须登录；不得把免费改成无限，也不得把无需登录改成无需遵守每日额度。
- 验收标准：AI Image Upscaler 的首屏、卖点、FAQ、页面源码和 JSON-LD 不再出现 does not retain、no data retained 或同义绝对表述，指定替换文案逐字一致，Privacy Policy 链接返回 200。未登录任务 24 小时删除、登录素材保存到 Library、不用于模型训练或广告的表述与同批上线的 Privacy 完全一致。全站任一 Sign in 弹窗及 37 个 Sitemap 页面初始 HTML 均不再包含 Create without limits 或其他无限使用文案；每个工具页的 Tool facts 仍准确显示每日 3 次共享免费任务，首页 FAQ、可见说明和 JSON-LD 不出现相反答案。登录、上传、任务提交和下载流程保持正常。
- 不要修改：不要删除无水印、独立工具页无需登录或允许商业使用的现有真实规则；不要把 Privacy 的未登录任务 24 小时删除改成即时删除或长期保存；不要提前宣传付费套餐、价格、无限额度或扩展容量；不要把 Privacy 链接做成不可抓取按钮。

### 将首页结构化工具列表补全为全部 32 个工具

- 优先级：P2
- 页面或界面：https://imagehub.ai/ 首页 JSON-LD，以及首页导航、工具选择器和 https://imagehub.ai/sitemap.xml 中的公开工具清单
- 当前问题与线上证据：首页导航和 Sitemap 当前包含 32 个独立工具页，但首页 JSON-LD 中名为 ImageHub AI image tools 的 ItemList 只有 16 项，numberOfItems 也为 16。该列表作为首页 CollectionPage 的 mainEntity，会向搜索引擎和生成式引擎提供不完整的产品能力清单。
- 修改要求：将首页 ImageHub AI image tools ItemList 更新为 Sitemap 中全部 32 个当前公开工具。numberOfItems 必须为 32，itemListElement 必须有且只有 32 项，position 使用连续且不重复的 1–32；每项保留 ListItem，并包含指向该工具自引用 Canonical 的绝对 HTTPS URL，以及与工具页 Title、H1 和实际功能一致的 WebApplication name、description、applicationCategory、operatingSystem、isAccessibleForFree 和 publisher。首页可见导航、工具选择器、ItemList 和 Sitemap 使用同一份当前公开工具集合，新增或移除工具时必须同步更新，不得继续维护互相不一致的手工子集。
  保留现有 Organization、WebSite、CollectionPage、FAQPage 和其他有效 JSON-LD 节点及稳定 @id；首页 CollectionPage 的 mainEntity 继续指向完整 ItemList。结构化数据中的免费、登录、每日额度、输入和输出信息不得超出对应页面可见事实，也不得加入评分、评论、用户数、价格或效果数据，除非对应数据已在页面公开并有已批准依据。
- 验收标准：首页源代码只有一份有效的主 JSON-LD 图；JSON 可解析，ItemList numberOfItems 为 32，实际元素数为 32，position 完整覆盖 1–32。32 个 URL 均返回 200、位于 Sitemap、Canonical 自引用且可从首页导航或工具选择器到达；不存在重复、缺失、404、重定向 URL 或非公开 Workspace URL。Schema.org Validator 无语法错误，Google Rich Results Test 不出现由本次修改新增的严重错误；页面可见内容与 JSON-LD 名称和描述一致。
- 不要修改：不要新增不存在的工具、能力、定价、评分、评论或用户数据；不要把 Account、Library、Workspace、Privacy、Terms 或 Changelog 计入 32 个工具；不要删除现有有效的 FAQ、Breadcrumb、WebApplication、Organization 或 WebSite 数据。

### 为公开案例图片加入图片 Sitemap

- 优先级：P2
- 页面或界面：https://imagehub.ai/sitemap.xml、robots.txt，以及首页和全部 32 个工具页中的公开案例图、Before/After 图、画廊图和工作流示例图
- 当前问题与线上证据：当前 XML Sitemap 只列出 37 个页面 URL，没有使用 Google 图片 Sitemap 扩展列出站内大量公开案例图。ImageHub 的核心内容高度依赖生成示例和处理前后对比，缺少图片 Sitemap 会减少搜索引擎直接发现和关联这些视觉内容的明确信号。
- 修改要求：直接扩展现有 https://imagehub.ai/sitemap.xml，在 urlset 上加入 xmlns:image="http://www.google.com/schemas/sitemap-image/1.1"，并在每个首页或工具页 URL 下，为该页面真实展示且允许公开索引的内容图片输出 image:image 和绝对 HTTPS image:loc。只收录案例图、Before/After、公开画廊和解释工作流所需的内容图片；不收录 Logo、图标、头像占位、上传控件占位、加载图、验证码、装饰背景、重复导航图片、用户上传内容、用户生成结果、Workspace、Library、Account 或任何需要登录的私有素材。相同图片在同一页面只列一次；图片 URL 必须与页面实际 img 或 picture 使用的规范资源一致，不添加已废弃的 image:caption、image:title、image:license 或 image:geo_location。
  Sitemap 必须由当前公开页面和内容图片集合生成，页面或公开案例图新增、替换或移除时同步更新；每页 lastmod 只在该页面正文、结构化数据或公开案例图真实变化时更新。robots.txt 继续允许抓取 Sitemap 中的页面和图片，并继续指向 https://imagehub.ai/sitemap.xml。响应 Content-Type 保持 application/xml，XML 使用 UTF-8 且正确转义。
- 验收标准：Sitemap 返回 200、可通过 XML 验证，并包含正确的图片命名空间；首页与 32 个工具页的每张入选 image:loc 均返回 200 和正确 image Content-Type，使用 HTTPS，不需要 Cookie、登录或临时签名。抽查每个工具页，Sitemap 中的图片确实出现在该页公开 HTML 的 img 或 picture 中；不存在私有用户素材、空 src、data URL、Blob URL、404、重定向、重复 URL 或纯装饰资源。robots.txt 仍返回 200 并指向该 Sitemap；普通页面 URL、Canonical 和现有 lastmod 规则不受破坏。
- 不要修改：不要公开、复制或索引用户上传、用户生成、Workspace、Library 或 Account 数据；不要为了填充 Sitemap 新造案例图；不要加入 Google 已废弃的图片 Sitemap 字段；不要把图片 Sitemap 拆成需要另行决定或提交的新地址。

### 扩充 About 页的可引用产品事实

- 优先级：P2
- 页面或界面：https://imagehub.ai/about/ 的可见正文、页面目录、Meta Description、Open Graph、Twitter 和 AboutPage JSON-LD
- 当前问题与线上证据：About 当前只有一段产品概述、运营主体和联系方式。虽然 Organization 与 AboutPage 结构化数据已存在，但页面没有用自包含问答明确产品是什么、如何使用、登录边界、免费额度和上传内容保存方式，生成式引擎难以从一个稳定权威页面提取完整且互相一致的第一方事实。
- 修改要求：保留现有 H1 About ImageHub、运营主体、地址和邮箱，在现有产品介绍后依次新增以下 6 个 H2 及英文正文，标题和正文逐字一致：
  1. What is ImageHub? / ImageHub is a browser-based collection of AI image tools for generating, editing, enhancing, restoring, and transforming images. Each tool provides a focused workflow with clear inputs and a downloadable result.
  2. How does ImageHub work? / Choose the tool that matches your task, provide the requested image or text input, review the generated or processed result, and download it from the same browser page. ImageHub processes one task at a time in each tool tab, while separate tabs can run other tasks concurrently.
  3. Do I need an account? / You can run tasks from any individual tool page without creating an account or signing in. You must sign in to start tasks from the all-in-one Workspace on the ImageHub homepage and to use your personal Library.
  4. What are the free usage limits? / Every user can complete up to three free tasks per day, shared across all ImageHub tools. ImageHub does not add a watermark to completed results, and each task processes one request.
  5. Who operates ImageHub? / ImageHub is operated by QUEST LABS LIMITED at RM 1605 HO KING COMM CTR, 2-16 FA YUEN ST, MONG KOK, HONG KONG. Product and privacy questions can be sent to support@imagehub.ai.
  6. How does ImageHub handle uploaded images? / Content from tasks run without signing in is deleted from active systems within 24 hours after completion. When you are signed in, uploads and results are saved to your personal Library until you permanently delete them or delete your account. ImageHub does not use your images or prompts to train models or for advertising. Read the Privacy Policy for complete details.
  将斜杠视为标题与正文的分隔符，不得输出斜杠字符或序号。第 6 项中的 Privacy Policy 必须是可抓取链接并指向 https://imagehub.ai/privacy/。这些内容与 Library、每日 3 次免费规则和 Privacy/Terms 更新同批上线。保留 AboutPage 和 Organization JSON-LD，使 visible name、description、operator、address、email 和 dateModified 与页面可见内容一致；不得把未公开的公司信息、团队成员、成立年份、客户、合作方或技术供应商写入页面。Meta Description、og:description 和 twitter:description 统一为：Learn what ImageHub is, how its AI image tools work, when an account is required, the free usage limits, and how QUEST LABS LIMITED handles uploaded content.
- 验收标准：About 返回 200，只有一个 H1，并按指定顺序显示 6 个 H2；每段英文逐字一致，Privacy Policy 为普通可抓取链接。页面关于登录、每日 3 次、并发、无水印、Library、未登录任务 24 小时删除和模型训练的事实与首页、工具页、Privacy 和 Terms 完全一致。Meta、Open Graph 和 Twitter Description 逐字匹配指定文案；AboutPage 与 Organization JSON-LD 可解析，运营主体、地址、邮箱及真实发布日期一致；Sitemap lastmod 和 dateModified 使用本次实际上线日期。桌面端和 390px 移动端无裁切、重叠或横向滚动，标题层级可被屏幕阅读器正确识别。
- 不要修改：不要加入团队姓名、公司注册号、成立日期、客户 Logo、媒体报道、合作伙伴、外部评价、无依据指标或供应商名称；不要改变现有运营主体、地址、邮箱、每日免费次数、登录边界、并发规则、无水印、NSFW、Privacy 或 Terms 的已批准业务规则；不要增加 FAQPage 标记，除非页面明确以 FAQ 形式呈现并且结构化数据与可见内容逐字一致。

### 更新 Privacy 和 Terms 的素材保存、存储额度与账户删除说明

- 优先级：P1
- 页面或界面：https://imagehub.ai/privacy/ 和 https://imagehub.ai/terms/，以及对应的 Meta Description、Open Graph、Twitter 和页面级 JSON-LD 日期
- 当前问题与线上证据：Privacy 当前写明所有免费任务的上传内容和生成结果在任务完成后 24 小时内从活动系统删除，只笼统说明主动保存到 Workspace 的内容会被保留；Terms 没有说明自动保存的个人 Library、免费账户 100 MiB 存储额度、超限行为、素材永久删除或账户删除后的立即数据清除规则。新素材库和账户删除功能上线后，这些公开规则会与实际数据保存方式不一致。
- 修改要求：素材库功能与本任务必须同批上线。保留 Privacy 中未登录任务的 24 小时删除规则，但将 How long content is kept 部分改写为以下四段英文，逐字一致：For tasks you run without signing in, the content you upload and the result we generate are deleted from our active systems within 24 hours of the task completing. / When you are signed in, images you upload and images ImageHub generates or processes for you are automatically saved to your Library. Library items are kept until you permanently delete them or your account is deleted. / Deleting an item from your Library permanently deletes it. ImageHub does not provide a recycle bin, and deleted items cannot be restored. / Free accounts include 100 MiB of Library storage. Storage limits may differ between account plans. When your Library reaches its limit, you must permanently delete items before you can upload or generate more images. 将斜杠视为段落分隔符，不得输出斜杠字符。同步将 Security 中只适用于全部免费任务 24 小时删除的表述改为同时符合未登录临时任务和登录 Library 长期保存的事实；将 Your requests 中 Saved Workspace items 改为 Library items。
  在 Privacy 的 How long content is kept 部分继续新增以下独立英文段落，逐字一致：When you delete your account, ImageHub immediately and permanently deletes your account and all data associated with it, including your Library items, Workspace content, task history, and account settings. Deleted accounts and data cannot be restored.
  在 Terms 的 Accounts 之后新增标题为 Library and storage 的章节，正文逐字为：When you are signed in, images you upload and images ImageHub generates or processes for you are automatically saved to your personal Library. Free accounts include 100 MiB of Library storage, and storage limits may differ between account plans. ImageHub may prevent new uploads and image tasks when your Library is at or above its storage limit. / You can permanently delete individual items, multiple selected items, or the oldest items needed to free storage space. Library deletion is immediate, cannot be undone, and has no recycle bin. Keep your own copies of any images you do not want to lose. 将斜杠视为段落分隔符，不得输出斜杠字符。现有 Your content 对存储和处理的许可继续保留，但不得声称登录素材仍在 24 小时内自动删除。在 Terms 的 Accounts 章节同时新增以下独立英文段落，逐字一致：Deleting your account permanently deletes the account and all data associated with it immediately, including Library items, Workspace content, task history, and account settings. This action cannot be undone.
  Privacy 和 Terms 的可见 Effective date 均改为本批次实际公开日期，并同步更新各自的 time datetime、Sitemap lastmod 及页面级 JSON-LD dateModified；日期不得早于素材库实际上线日期。Meta Description、og:description 和 twitter:description 必须准确提及 Library 保存或存储规则，但不得宣传尚未存在的付费套餐、价格或扩展容量购买方式。
- 验收标准：素材库和账户删除功能上线时，Privacy 明确区分未登录任务 24 小时删除、登录 Library 长期保存和删除账户后全部账户数据立即永久删除；Terms 明确说明自动保存、免费账户 100 MiB、套餐可配置额度、超限限制、素材永久删除和账户删除后立即清除全部数据。指定英文段落逐字一致，没有互相矛盾的保存周期、回收站、宽限期或恢复承诺。两个页面返回 200，Effective date、datetime、Sitemap lastmod 和 JSON-LD dateModified 使用同一真实发布日期；Meta、Open Graph 和 Twitter 摘要与正文一致。
- 不要修改：不要加入备份最迟清除时间、最低使用年龄、适用法律、法院管辖、具体付费套餐、价格、购买方式或尚未提供的恢复能力；不要删除运营主体 QUEST LABS LIMITED、地址、support@imagehub.ai、NSFW 禁止条款、权利投诉方式或其他现有法律内容；不要把未登录任务改为长期保存，也不要继续声称登录用户的 Library 素材会在 24 小时内自动删除。

### 发布个人素材库、账户设置与 Workspace 移动端适配的公开 Changelog

- 优先级：P1
- 页面或界面：https://imagehub.ai/changelog/
- 当前问题与线上证据：当前 Changelog 尚未记录个人素材库、历史素材复用、免费账户存储额度、永久删除与快捷清理能力，也未记录新的密码和账户删除设置；用户同时确认 Workspace 尚未完成移动端适配。这些内容属于登录用户可明显感知的重要功能和兼容性更新，需要在实际发布后合并为一条记录。
- 修改要求：仅在素材库功能、100 MiB 免费存储额度、单张与批量永久删除、Free up 10 MB、用户菜单 Library 入口、Account Settings、密码修改、账户删除、Privacy/Terms 更新和 Workspace 移动端适配全部实际上线后，在现有 Changelog 顶部新增一条使用真实发布日期的英文记录：Added a personal Library for signed-in users, with reusable uploads and generations, 100 MB of free storage, storage management, new account settings, and a fully responsive Workspace for mobile devices. 保留全部既有记录及日期，并让新记录排在最前。
- 验收标准：https://imagehub.ai/changelog/ 返回 200；新记录日期与实际功能上线日期一致，正文逐字匹配指定英文文案，并且提及的素材库、账户设置和移动端 Workspace 均已在线可用；现有历史记录、Title、Meta Description、Canonical、H1、页脚链接、Sitemap lastmod 和 JSON-LD dateModified 保持正常。
- 不要修改：不要提前发布记录，不要描述未上线的付费套餐、价格或未来容量；不要写入代码文件、组件、数据库、对象存储、架构、仓库、分支、提交、基础设施、服务商配置、成本、密钥、安全敏感实现、客户数据、内部指标、AI 提示词或内部工作流；不要记录与本批次无关的普通文案、轻微视觉或内部维护调整。
