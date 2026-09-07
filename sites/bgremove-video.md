---
site_id: "bgremove-video"
name: "BGRemove"
production_url: "https://bgremove.video/"
changelog_url: "https://bgremove.video/changelog/"
delivery_method: "direct_publish"
target_repository: "not_applicable"
default_branch: "not_applicable"
updated_at: "2026-09-08"
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

### 重新生成 Agencies 卡片中人物变形的案例图

- 优先级：`P2`
- 页面或界面：`https://bgremove.video/change-background/` 的 `Make More Versions From One Cutout` 模块、`Agencies` 卡片配图
- 当前问题与线上证据：用户于 2026-09-08 提供的线上截图显示，笔记本屏幕中的人物肩颈和身体比例明显变形，而且笔记本里是背对镜头的人物，手机里却是正面人物，无法表达文案所说的“同一段素材生成多个交付版本”。异常人物会降低页面的真实感和可信度。截图中的红色箭头是用户标注，不是页面内容。
- 修改要求：用图片生成 AI 重新生成一张真实摄影风格的 `16:9` 案例图，不得使用简图、插画或抽象占位图。使用以下英文提示词：`Photorealistic commercial lifestyle photograph, 16:9. A clean modern creative-agency desk in soft daylight. An open laptop on the left and an upright smartphone on the right. Both screens display the exact same waist-up female presenter from the exact same source frame: front-facing, natural proportions, symmetrical shoulders, dark emerald blouse, blonde hair tied in a low ponytail, calm neutral expression. The laptop version has a warm mustard studio background; the phone version has a cool light-grey studio background, demonstrating one cutout used for two deliverables. The presenter’s identity, face, pose, clothing, body shape, scale and orientation must be identical on both screens. Realistic screen perspective and reflections, anatomically correct human, crisp screen content, no distortion, no duplicated body parts, no reversed head, no warped shoulders or torso, no text, no logos, no watermark, no arrows, no UI overlays. Leave comfortable margins around both devices; premium SaaS landing-page photography.` 生成后人工检查并选择无畸形版本，替换当前图片，同时把图片 alt 设置为 `The same presenter shown on a laptop and phone against two different backgrounds`。响应式显示必须保持图片原始比例，不能通过拉伸填满容器。
- 验收标准：笔记本和手机中是同一个可辨认的人物、同一正面姿势、同一服装和同一源画面，只改变背景；人物面部、肩颈、躯干和身体比例自然，没有扭曲、断裂、重复肢体或错误朝向；设备透视合理，图片中没有文字、品牌、水印、箭头或界面叠层；桌面端和 `390px`、`768px` 宽度下图片不被拉伸，人物与两台设备的关键信息没有被裁掉；alt 与实际画面一致。
- 不要修改：`Agencies` 标题、正文、链接、卡片顺序、模块布局，以及同模块的 `Ecommerce`、`Creators` 配图和文案。不得把示例描述成真实客户、客户案例或已取得的业务成果。

### 纠正 Sep 6 的错误竖屏声明并记录实际修复

- 优先级：`P1`
- 页面或界面：`https://bgremove.video/changelog/`
- 当前问题与线上证据：线上 `Sep 6, 2026 · Fix · 2.0` 条目当前声称竖屏视频会在预览、所有背景和导出文件中保持正确方向，但用户于 2026-09-08 的生产复测确认竖屏预览仍会横向播放。该条目同时包含方向元数据、高帧率和“其他副作用”等实现诊断，既不真实也不符合简洁、脱敏的用户向更新日志要求；其中 `Colour`、`Blur` 选择流程和更清晰的处理反馈已由用户确认上线。
- 修改要求：立即把 `Sep 6, 2026` 条目的标题改为 `Background controls now wait for your choice`，正文完整替换为：`Colour and Blur controls now wait for your choice before updating, with clearer progress and retry feedback while the preview is being prepared.` 保留该条目的日期、版本和类型。本批次竖屏方向修复和 Agencies 案例图实际发布并经过生产验证后，再新增恰好一条带真实发布日期的记录，只概括实际上线的用户可见变化。竖屏方向可使用：`Vertical videos now keep the correct orientation in previews and exported MP4 files.`；案例图可概括为：`The agency example now shows one consistent presenter across both finished versions.` 未上线或未验证的内容必须省略；如果两项都没有成功上线，则不要新增记录。
- 验收标准：`Sep 6, 2026` 条目不再声称竖屏方向已经修复，不再出现方向元数据、高帧率、副作用或其他实现诊断，只描述已经确认上线的控件和处理反馈。本批次恰好新增一条真实日期的简洁记录，且只包含生产环境已经验证的竖屏修复和/或案例图改进。
- 不要修改：`Sep 6, 2026` 条目的原日期、版本和类型，以及其他历史记录及其日期。不得提及文件名、组件名、代码架构、仓库、分支、提交、基础设施或服务商配置、成本、密钥、安全敏感实现、客户数据、内部指标、AI 提示词或内部工作流程。
