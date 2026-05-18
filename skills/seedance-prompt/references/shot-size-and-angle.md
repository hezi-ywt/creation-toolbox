---
description: 决定主体在画面中的比例（远景 / 中景 / 特写）和镜头视线方向（仰俯平鸟蛙）时加载。
---

# 镜头景别与角度

> 用途：可粘贴到 Seedance / 可灵 / Veo3 / Sora2 / Runway 等 AI 视频模型的景别 + 角度参考库
> 状态：v0.3（14 条 + 组合习惯）
> 数据：基于公开影视摄影经验整理，难度评级为经验估计（非实测）
> 最后更新：2026-05-17

## 怎么用

1. **景别 = 主体在画面中占多大**（远→近八档）
2. **角度 = 摄影机看主体的视线方向**（仰俯平六档）
3. **几乎所有 AI 视频 prompt 都需要明确景别 + 角度**——这是构图的两个基本轴，不写 AI 会随便给
4. 景别和角度可自由组合，**末尾"组合习惯"章节**列了 6 个最经典的搭配

**难度图例**（同运镜.md）：⭐ 简单 / ⭐⭐ 中等 / ⭐⭐⭐ 较难 / ⭐⭐⭐⭐ 困难

---

## 索引

### 景别（远到近）

| # | 中文 | English | 简写 | 主体可见范围 | 难度 |
|---|---|---|---|---|---|
| 1 | 极远景 | Extreme Wide Shot | EWS / XLS | 主体如蚂蚁，环境主导 | ⭐ |
| 2 | 远景 | Wide Shot / Long Shot | WS / LS | 主体全身 + 大量环境 | ⭐ |
| 3 | 中远景 | Medium Long Shot | MLS | 主体膝盖以上 | ⭐ |
| 4 | 中景 | Medium Shot | MS | 主体腰部以上 | ⭐ |
| 5 | 中近景 | Medium Close-Up | MCU | 主体胸部以上 | ⭐ |
| 6 | 特写 | Close-Up | CU | 主体面部 / 局部 | ⭐ |
| 7 | 极特写 | Extreme Close-Up | ECU | 眼睛 / 嘴唇 / 手指等极小区域 | ⭐⭐ |
| 8 | 双人镜头 | Two Shot | 2S | 两人同构图 | ⭐⭐ |

### 角度（仰俯平）

| # | 中文 | English | 视线方向 | 心理效果 | 难度 |
|---|---|---|---|---|---|
| 9 | 平视 | Eye Level | 与主体平齐 | 中性、自然、平等 | ⭐ |
| 10 | 俯视 | High Angle | 从上向下看主体 | 主体渺小、弱势 | ⭐ |
| 11 | 仰视 | Low Angle | 从下向上看主体 | 主体强大、威胁 | ⭐ |
| 12 | 鸟瞰 | Bird's Eye View | 极高位俯视 | 上帝感、抽离 | ⭐ |
| 13 | 蛙视 | Worm's Eye View | 极低位仰视 | 英雄式、夸张 | ⭐⭐ |
| 14 | 低机位 | Hip / Low Level | 髋部高度 | 童视、风格化 | ⭐⭐ |

**注**：荷兰角（Dutch Angle）本质是 roll（绕镜头轴旋转），不是 angle，见 [运镜.md 第 11 条](运镜.md)。

---

# 一、景别（Shot Size）

## 1. 极远景 / Extreme Wide Shot (EWS)

**别名**：XLS（Extreme Long Shot）、Establishing Shot（如果用于建立环境）、大全景
**画面定义**：主体在画面中极小（甚至几乎看不见），环境完全主导
**难度**：⭐ 简单（训练数据丰富，AI 易出活）

**画面**：
- 主体（人物）占画面比例 < 5%，常被环境"吞没"
- 画面像风景照，焦点是大景观、地形、城市天际线
- 没有清晰的"主角"——观众看的是环境本身

**叙事用途**：
- **建立环境**：开场告诉观众"这是哪里"（沙漠、城市、太空、森林）
- **表达渺小**：角色在巨大世界中的孤独/无力感
- **史诗感**：战争、奇幻、灾难片标配
- **过渡**：从一个场景切到完全不同的环境
- **经典参考**：《阿拉伯的劳伦斯》沙漠骆驼远景；《荒野猎人》雪原；《2001 太空漫游》太空船

**英文模板**：
```
extreme wide shot of [environment], [tiny subject if any], [N] seconds, cinematic
```

**中文模板**：
```
[环境]的极远景，[主体在远处]，[N]秒，电影感
```

**完整示例**：
> Extreme wide shot of a vast snow-covered mountain range at dawn. A tiny lone figure walks along a ridge in the distance, barely visible. Cold blue light, soft mist rising from valleys, 7 seconds, cinematic, epic mood.

**易混淆**：
- vs **Wide Shot (WS)**：EWS 主体几乎看不见；WS 主体全身可见
- AI 模型偶尔会把 EWS 渲染成 WS（主体仍清晰）——强调 `tiny subject in distance` 或 `subject barely visible`

---

## 2. 远景 / Wide Shot / Long Shot (WS / LS)

**别名**：Long Shot、Full Shot（FS，主体刚好全身入画）、大景别
**画面定义**：主体全身可见，但环境占据画面大部分
**难度**：⭐ 简单（AI 视频核心常用景别，训练数据极多）

**画面**：
- 主体占画面约 10-30%，环境占 70-90%
- 能看到主体的全身（头到脚）
- 主体与环境的关系清晰可读

**叙事用途**：
- **介绍角色 + 环境**：常用于场景开场或主角入场
- **动作戏**：打斗、跑步、运动需要全身可见
- **舞蹈/表演**：身体语言要完整可见
- **位置关系**：多人/多物在空间中的相对位置
- **经典参考**：西部片大量 wide shot 拉枪；歌舞片必备景别；几乎每部电影开场建立场景

**英文模板**：
```
wide shot of [subject] in [environment], full body visible, [N] seconds, cinematic
```

**中文模板**：
```
[环境]中的[主体]远景，全身可见，[N]秒，电影感
```

**完整示例**：
> Wide shot of a samurai standing alone in a misty bamboo forest. Full body visible, sword at his side, fog drifting around his legs. Cool morning light filtering through bamboo, 6 seconds, cinematic, atmospheric.

**易混淆**：
- vs **EWS**：WS 主体清晰可辨；EWS 主体几乎看不见
- vs **Full Shot (FS)**：FS 严格指"主体刚好顶天立地"；WS 包含更多环境
- AI 里 `wide shot` 偶尔被理解为"画面比例宽"——可以加 `framing` 或 `medium-long composition` 辅助

---

## 3. 中远景 / Medium Long Shot (MLS)

**别名**：3/4 Shot、American Shot（美式镜头，膝盖以上）、Cowboy Shot（西部牛仔镜头，腰带枪套以上）
**画面定义**：主体膝盖或腰部以上入画，环境占 30-50%
**难度**：⭐ 简单（标准对话/动作景别，AI 易理解）

**画面**：
- 主体占画面约 40-60%
- 能看到主体大半身体（包括手部动作）
- 环境仍可辨但不主导
- 美式镜头（American Shot）特指膝盖以上，源自西部片让"枪套入画"

**叙事用途**：
- **角色行动**：主体在做事（行走、操作工具、打斗起手）
- **对话铺垫**：双人对话开场常用 MLS 建立位置
- **西部片标志**：枪手对峙的经典构图
- **保留肢体语言**：让观众看到手势、姿态
- **经典参考**：莱昂内西部片大量牛仔镜头；《教父》会议场景；现代剧情片对话场面

**英文模板**：
```
medium long shot of [subject], from knees up, [action], [N] seconds, cinematic
```

**中文模板**：
```
[主体]的中远景，膝盖以上入画，[动作]，[N]秒
```

**完整示例**：
> Medium long shot of a cowboy standing in a dusty saloon. Frame from his knees up, hand resting on his gun belt, stoic expression. Warm golden light from the window, 5 seconds, cinematic Western.

**易混淆**：
- vs **MS (Medium Shot)**：MLS 膝盖以上；MS 腰部以上
- AI 里直接说 `American Shot` 或 `Cowboy Shot` 比 MLS 命中率更高（前者训练数据更多）

---

## 4. 中景 / Medium Shot (MS)

**别名**：Waist Shot、Mid Shot、Half-Body Shot
**画面定义**：主体腰部以上入画，环境占 20-40%
**难度**：⭐ 简单（最常用景别之一，AI 极易理解）

**画面**：
- 主体占画面约 50-70%
- 能看到主体的上半身（头、肩、胸、腰）+ 手部上举的动作
- 主体面部表情清晰可读，但身体姿态也保留
- 环境作为背景元素仍存在

**叙事用途**：
- **对话标配**：双人对话最常用，让观众"参与"对话
- **采访风格**：新闻、纪录片标准景别
- **角色介绍**：观众看清角色面部 + 服装风格
- **日常戏**：吃饭、工作、生活场面
- **经典参考**：几乎所有剧情片对话场面；纪录片采访；脱口秀

**英文模板**：
```
medium shot of [subject], from waist up, [expression/action], [N] seconds, cinematic
```

**中文模板**：
```
[主体]的中景，腰部以上入画，[表情/动作]，[N]秒
```

**完整示例**：
> Medium shot of a young teacher standing in front of a chalkboard, explaining a concept with hand gestures. Frame from waist up, warm classroom lighting, slight smile, 6 seconds, cinematic.

**易混淆**：
- vs **MLS**：MS 腰部以上；MLS 膝盖以上（多出一段腿）
- vs **MCU**：MS 看得到胸部以上整个上半身；MCU 主要看胸部到头部
- AI 里 `medium shot` 是高频术语，几乎不会错

---

## 5. 中近景 / Medium Close-Up (MCU)

**别名**：Bust Shot、半身近景、肩膀以上
**画面定义**：主体胸部 / 肩膀以上入画
**难度**：⭐ 简单（采访常用，AI 易理解）

**画面**：
- 主体占画面约 70-85%
- 能看到主体的头、肩、上胸部
- 面部表情主导，但还能看到肩膀姿态
- 环境几乎完全失去主导（只剩背景模糊）

**叙事用途**：
- **强化对话**：相比 MS，MCU 让观众更近、更专注角色情绪
- **采访进阶**：纪录片关键对话时切到 MCU 强化亲密感
- **角色独白**：角色对镜头说话时
- **反应镜头**：捕捉某个瞬间的情绪变化
- **经典参考**：《教父》多次关键对话；电视访谈节目核心机位；商业广告人物特写

**英文模板**：
```
medium close-up of [subject], from chest up, [expression], [N] seconds, cinematic
```

**中文模板**：
```
[主体]的中近景，胸部以上入画，[表情]，[N]秒
```

**完整示例**：
> Medium close-up of an elderly man sitting in an armchair, looking directly at the camera. Frame from chest up, warm lamp light highlighting deep wrinkles, contemplative expression, 5 seconds, cinematic.

**易混淆**：
- vs **MS**：MCU 主要看面部 + 肩膀；MS 看得到整个上半身
- vs **CU**：MCU 还能看肩膀；CU 主要是面部
- AI 里 `medium close-up` 高频，但有时会渲染成 CU（更近）——强调 `from chest up, shoulders visible`

---

## 6. 特写 / Close-Up (CU)

**别名**：CU、特写镜头、面部特写
**画面定义**：主体面部或局部充满画面
**难度**：⭐ 简单（最具戏剧性的景别之一，AI 训练样本极多）

**画面**：
- 主体面部占画面 80% 以上（或单一局部如手、物件）
- 几乎没有环境信息
- 焦点完全在情绪、细节、纹理
- 通常浅景深（背景模糊）

**叙事用途**：
- **情绪锁定**：捕捉角色关键情绪瞬间（决心、绝望、惊讶）
- **关键道具**：戒指、信件、武器、钥匙等剧情关键物的特写
- **戏剧高潮**：重要对话、揭示、反转时刻
- **构图节奏变化**：插入特写打断中景节奏
- **经典参考**：《沉默的羔羊》Hopkins 经典面部特写；《被解救的姜戈》多次面部特写；《指环王》戒指特写

**英文模板**：
```
close-up of [subject's face/object], filling the frame, [expression/detail], shallow depth of field, [N] seconds, cinematic
```

**中文模板**：
```
[主体面部/物件]的特写，充满画面，[表情/细节]，浅景深，[N]秒
```

**完整示例**：
> Close-up of a young woman's face as she reads a letter. Tears welling in her eyes, slight tremor in her lips. Soft window light from the side, shallow depth of field, blurred warm background, 5 seconds, cinematic, emotional.

**易混淆**：
- vs **MCU**：CU 充满面部；MCU 还能看肩膀
- vs **ECU**：CU 是整个面部；ECU 是面部某一极小区域（眼睛、嘴）
- AI 里 `close-up` 高频，但**有时被理解为"近距离拍摄"而非"画面紧"**——加 `filling the frame` 辅助

---

## 7. 极特写 / Extreme Close-Up (ECU)

**别名**：XCU、Insert Shot（插入镜头）、极致特写
**画面定义**：主体的极小区域（眼睛、嘴唇、手指、刀刃、表盘等）充满画面
**难度**：⭐⭐ 中等（AI 易把 ECU 渲染成普通 CU，需要明确指定"局部"）

**画面**：
- 单一局部占画面 80% 以上（一只眼睛、半张嘴、戒指、刀尖）
- 完全去除环境和身份信息
- 纹理、细节、动作极致放大
- 强烈的"被强迫看"的视觉张力

**叙事用途**：
- **极致戏剧张力**：高潮时刻、生死关头、关键揭示
- **悬疑铺垫**：神秘物件的局部，激发好奇
- **情绪极化**：眼睛的颤动、嘴角抽搐 → 让情绪不可逃避
- **风格化签名**：Sergio Leone（西部片眼神对决）；Tarantino（脚的特写）
- **经典参考**：《好坏丑》三人对决眼神特写；《杀死比尔》多次脚特写；犯罪片解锁、按钮等细节

**英文模板**：
```
extreme close-up of [specific small detail], filling entire frame, [N] seconds, cinematic, dramatic
```

**中文模板**：
```
对[局部细节]的极特写，充满整个画面，[N]秒，戏剧性
```

**完整示例**：
> Extreme close-up of a single blue eye, filling the entire frame. Slight tremor in the eyelid, reflection of fire visible in the iris. Sharp focus on the pupil, 4 seconds, cinematic, intense dramatic mood.

**易混淆**：
- vs **CU**：CU 是整个面部 / 物件；ECU 是面部的某一极小部位
- AI 里 `extreme close-up` 偶尔被渲染成稍紧的 CU——明确具体局部 `extreme close-up of the eye / lip / hand`，比抽象的 ECU 更稳
- 失败模式：AI 会渲染成"近距离拍摄整个主体"而非"局部充满画面"

---

## 8. 双人镜头 / Two Shot (2S)

**别名**：Two-Shot、双人构图、Group Shot（多人时）
**画面定义**：两个主体（通常两人）同时在画面中，构图强调两者关系
**难度**：⭐⭐ 中等（AI 易出活但两人位置/姿态精控难度增加）

**画面**：
- 两个主体同时在画面，通常占画面主要部分
- 双人位置关系暗示叙事（并肩、对峙、亲密、远离）
- 通常是 MS 或 MCU 景别（让面部表情可读）
- 三人以上称为 Group Shot

**叙事用途**：
- **对话场面**：两人对话不切正反打时
- **关系展示**：恋人、敌人、伙伴的相对位置/距离
- **冲突铺垫**：两人在同一画面内的张力
- **平行剪辑**：A 和 B 同时存在的视觉提示
- **经典参考**：《卡萨布兰卡》Bogart 和 Bergman 多次双人；《老无所依》对峙场面；几乎所有情侣戏的"并肩远眺"

**英文模板**：
```
two shot of [subject A] and [subject B], [their spatial relationship], [N] seconds, cinematic
```

**中文模板**：
```
[主体A]和[主体B]的双人镜头，[空间关系]，[N]秒
```

**完整示例**：
> Two shot of an elderly couple sitting on a park bench at sunset. The husband faces forward, the wife rests her head on his shoulder. Warm golden hour light, blurred autumn trees behind them, 7 seconds, cinematic, tender mood.

**易混淆**：
- 与 **OTS**（越肩镜头）区别：OTS 一个在前景（虚化）一个在背景（清晰）；2S 两人同等清晰
- AI 里多人构图常出错——明确每个人的**位置 + 姿态**比单写"two people"稳得多
- 失败模式：AI 把两个人画成一样的脸（同质化）；加 `two distinct people, different appearances` 缓解

---

# 二、角度（Camera Angle）

## 9. 平视 / Eye Level

**别名**：Neutral Angle、平角、自然视角
**画面定义**：摄影机高度与主体眼睛/视线平齐
**难度**：⭐ 简单（最常用、最自然，AI 默认就是这个角度）

**画面**：
- 摄影机高度 ≈ 主体眼睛高度（人物约 1.5-1.7m）
- 视线水平，没有上下倾斜感
- 主体看起来"和观众平等"

**叙事用途**：
- **自然纪实**：纪录片、对话戏标配
- **中性观察**：不强加情感判断，让观众客观看
- **平等关系**：暗示主体和观众处于平等位置
- **大多数对话场面默认**：MS / MCU + Eye Level 是对话戏黄金组合
- **经典参考**：几乎所有剧情片对话；纪录片采访；小津安二郎极爱的低位 eye level

**英文模板**：
```
eye level shot of [subject], natural perspective, [N] seconds, cinematic
```

**中文模板**：
```
[主体]的平视镜头，自然视角，[N]秒
```

**完整示例**：
> Eye level medium shot of a barista smiling at a customer across the counter. Natural perspective, warm café lighting, focused expression, 5 seconds, cinematic.

**易混淆**：
- AI 默认渲染的就是 eye level，**不写也通常是这个**——所以 prompt 里其实可以省略
- 但如果有必要明确（避免 AI 给 high angle），写 `eye level, natural perspective`

---

## 10. 俯视 / High Angle

**别名**：High Angle Shot、High Camera、俯拍
**画面定义**：摄影机位置高于主体，向下看主体
**难度**：⭐ 简单（视觉特征清晰、术语高频，AI 易出活）

**画面**：
- 摄影机角度 30-60 度向下（90 度即 Bird's Eye）
- 主体看起来变小、被"压下"
- 头顶可见，肩膀显宽，腿变短
- 心理上有"主体被支配"感

**叙事用途**：
- **主体渺小/弱势**：被欺凌的角色、失败时刻、绝望
- **支配视角**：从权威者视角看下属
- **抽离感**：让观众"看着"事件而非"参与"
- **童视角的反向**：成人俯视孩子
- **经典参考**：《大白鲨》主角被攻击时多次高角；《肖申克的救赎》新囚犯入狱俯视；许多反派俯视主角的镜头

**英文模板**：
```
high angle shot looking down at [subject], camera elevated, [N] seconds, cinematic
```

**中文模板**：
```
对[主体]的俯视镜头，相机高位，[N]秒
```

**完整示例**：
> High angle shot looking down at a small boy crouching alone in a school hallway. Camera elevated about 2 meters above him, his face turned up looking small. Cold fluorescent lights, 5 seconds, cinematic, melancholic.

**易混淆**：
- vs **Bird's Eye View**：High Angle 是 30-60 度斜俯；Bird's Eye 是 90 度垂直俯视
- vs **Top-Down**（运镜.md 第 24 条）：top-down = 90 度垂直；high angle 是斜俯
- 强度可写：`slight high angle` / `extreme high angle`

---

## 11. 仰视 / Low Angle

**别名**：Low Angle Shot、Hero Shot（英雄镜头）、仰拍
**画面定义**：摄影机位置低于主体，向上看主体
**难度**：⭐ 简单（视觉特征鲜明、术语高频）

**画面**：
- 摄影机角度 30-60 度向上（90 度即 Worm's Eye）
- 主体看起来变高、变大、有威胁感
- 下巴/胸部主导面部，眉骨阴影重
- 背景常带天空/天花板

**叙事用途**：
- **主体威严/威胁**：英雄登场、反派恐怖、权威人物
- **主观弱势视角**：孩子看大人、跪着看站立者
- **力量感**：肌肉、运动员、武器持有者
- **戏剧化反派出场**：与暗光配合极有压迫感
- **经典参考**：《公民凯恩》Kane 多次仰视镜头；《黑暗骑士》小丑出场；超级英雄电影标配亮相

**英文模板**：
```
low angle shot looking up at [subject], camera at low position, [N] seconds, cinematic, heroic / threatening
```

**中文模板**：
```
对[主体]的仰视镜头，相机低位，[N]秒，英雄式/威胁感
```

**完整示例**：
> Low angle shot looking up at a tall warrior standing on a cliff edge, silhouetted against the dawn sky. Camera at ground level, his cape billowing in the wind, 6 seconds, cinematic, heroic mood.

**易混淆**：
- vs **Worm's Eye**：Low Angle 是 30-60 度斜仰；Worm's Eye 是接近 90 度极仰
- AI 通常处理得好，但有时只给 slight low angle——加 `dramatic low angle` 或 `extreme low angle`
- 配合 `silhouette against sky` 强化英雄感

---

## 12. 鸟瞰 / Bird's Eye View

**别名**：Bird's Eye、Top-Down、God's Eye（重叠）、Aerial View
**画面定义**：摄影机近乎垂直俯视（80-90 度），从极高处向下看
**难度**：⭐ 简单（AI 视频时代极受欢迎，无人机航拍天然 bird's eye）

**画面**：
- 视角 80-90 度向下，几乎完全垂直
- 主体被压缩成平面图案
- 地理布局、几何美感主导
- 失去深度感

**叙事用途**：
- **上帝感**：让观众完全置身事外，俯瞰一切
- **地理展示**：城市布局、自然景观全貌
- **风格化几何**：Wes Anderson 风格、对称构图
- **现代航拍**：旅游片、广告、纪录片
- **经典参考**：库布里克《闪灵》小孩骑车顶视；Wes Anderson 大量；几乎所有现代旅游/汽车广告

**英文模板**：
```
bird's eye view of [scene], camera high overhead looking straight down, [N] seconds, aerial cinematic
```

**中文模板**：
```
[场景]的鸟瞰视角，相机高位垂直俯视，[N]秒
```

**完整示例**：
> Bird's eye view of a coastal village at noon. Camera high overhead, narrow streets weaving between white-washed houses, blue sea on one side, terraced gardens on the other. 7 seconds, aerial cinematic.

**易混淆**：
- vs **High Angle**：Bird's eye 是 80-90 度；High Angle 是 30-60 度
- vs **Top-Down**（运镜.md 第 24 条）：基本同一概念，"top-down" 强调 90 度精准，"bird's eye" 偶尔含 80 度的斜俯
- 配 `drone shot, aerial view` 让 AI 出"飘着拍"感

---

## 13. 蛙视 / Worm's Eye View

**别名**：Worm's Eye、Ground Level Angle、虫视角、地面仰视
**画面定义**：摄影机贴近地面或地下（接近 90 度极仰）
**难度**：⭐⭐ 中等（术语小众，AI 训练样本相对少）

**画面**：
- 视角接近 90 度向上
- 主体从地面"长起来"，背景多为天空/天花板/树冠
- 透视极度夸张——脚部大、头部小
- 与 low angle 的区别：low angle 是斜仰，worm's eye 是几乎垂直仰

**叙事用途**：
- **极致英雄式**：超级英雄登场、巨人般存在
- **儿童 / 动物视角**：孩子看大人、宠物看主人
- **戏剧化树林/建筑**：抬头看高大物件
- **风格化签名**：动画片常用、漫画式表达
- **经典参考**：《公民凯恩》多次极仰；《指环王》中土树木的极仰；动画《超人总动员》英雄出场

**英文模板**：
```
worm's eye view looking up at [subject], camera at ground level, extreme low angle, [N] seconds, cinematic
```

**中文模板**：
```
对[主体]的蛙视，相机贴地，极致仰视，[N]秒
```

**完整示例**：
> Worm's eye view looking up at a giant ancient oak tree in a forest. Camera at ground level, looking up through the trunk and branches at the bright blue sky above. Dappled sunlight filtering through leaves, 6 seconds, cinematic, majestic.

**易混淆**：
- vs **Low Angle**：Worm's eye 是接近垂直；Low Angle 是 30-60 度
- AI 用 `worm's eye view` 命中率不如 `extreme low angle, camera at ground level`——后者更具体
- 失败模式：AI 会渲染成普通的 low angle 而非极致仰视

---

## 14. 低机位 / Hip Level / Low Level

**别名**：Hip Level、Low Camera、低位拍摄
**画面定义**：摄影机位置在主体髋部高度（约 0.8-1m），视线与髋齐
**难度**：⭐⭐ 中等（介于 eye level 和 worm's eye 之间，需要精确描述）

**画面**：
- 摄影机高度 ≈ 主体髋部（约 80-100cm）
- 比 eye level 低 50-80cm，但远比 worm's eye 高
- 主体看起来稍微"高大"，但不夸张
- 画面有"孩子视角"感

**叙事用途**：
- **儿童视角**：从孩子的视线看世界
- **小津安二郎签名**：他大量使用 tatami shot（榻榻米机位，约 60cm 高）
- **风格化纪实**：稍微低于自然视角，引发"在场感"
- **桌面戏**：吃饭场面经典机位
- **经典参考**：小津安二郎《东京物语》大量榻榻米机位；Wes Anderson 偶尔低机位 + 对称

**英文模板**：
```
hip level shot, camera at low height (about 1 meter), [subject and action], [N] seconds, cinematic
```

**中文模板**：
```
低机位镜头，相机在髋部高度（约1米），[主体和动作]，[N]秒
```

**完整示例**：
> Hip level shot of a family sitting on tatami mats around a low dining table. Camera at about 60cm height (Ozu-style tatami shot), eye level with the food on the table, warm evening light, 8 seconds, cinematic, contemplative.

**易混淆**：
- vs **Eye Level**：Hip level 低于眼睛 50-80cm
- vs **Worm's Eye**：Hip level 仍接近水平视线；Worm's Eye 是极仰
- AI 里 `tatami shot` 或 `Ozu-style low camera` 比 `hip level` 命中率更高（具体引用）

---

# 三、景别 + 角度的组合习惯

景别和角度是两个独立的轴，**几乎所有 prompt 都需要同时指定两者**。这一节列了 6 个经典组合 + AI 视频的常见踩坑。

## A. 经典组合

### 1. Low Angle + Close-Up — "威严 / 威胁"
- **效果**：仰视特写，主体面部充满画面 + 显高大
- **用途**：反派出场、英雄威严、戏剧化对峙
- **Prompt**：`low angle close-up of [character], dramatic, threatening / heroic`
- **经典**：《教父》多次仰视特写马龙白兰度；超级英雄面部仰视

### 2. High Angle + Wide Shot — "渺小 / 抽离"
- **效果**：俯视远景，主体小 + 环境压迫
- **用途**：表达孤独、失败、被困
- **Prompt**：`high angle wide shot of [tiny subject] in [vast environment]`
- **经典**：《闪灵》小孩在走廊；《肖申克的救赎》监狱俯视

### 3. Eye Level + Medium Shot — "自然 / 平等对话"
- **效果**：最自然的对话景别 + 角度
- **用途**：标准对话场面、采访、纪录片
- **Prompt**：`eye level medium shot of [subject], natural perspective, conversational`
- **经典**：几乎所有剧情片对话场面默认

### 4. Bird's Eye + Long Shot — "地图感 / 监视"
- **效果**：垂直俯视的大景别，几何图案主导
- **用途**：建立环境、风格化、监控感
- **Prompt**：`bird's eye view long shot of [scene], aerial perspective`
- **经典**：Wes Anderson《布达佩斯大饭店》；旅游片开场

### 5. Worm's Eye + Close-Up — "英雄式仰视"
- **效果**：极致仰视 + 面部特写，主体如神
- **用途**：超级英雄登场、神话角色亮相
- **Prompt**：`worm's eye close-up of [hero], extreme low angle, looking up at face`
- **经典**：超级英雄电影标志运镜；动画片英雄登场

### 6. Top-Down + Two Shot — "几何风格化"
- **效果**：垂直俯视两人，对称构图
- **用途**：风格化餐桌戏、棋局、对峙
- **Prompt**：`top-down two shot of [A] and [B], symmetrical composition`
- **经典**：Wes Anderson 大量；现代广告

---

## B. AI 视频里的常见踩坑

1. **不写角度，AI 默认 eye level**：如果想要 high/low angle 必须明确说，否则永远是平视
2. **"Wide shot" 偶尔被理解为"宽屏比例"**：可以加 `framing` 或描述具体内容（"full body visible, environment dominates"）
3. **景别和距离的混淆**：CU 在 AI 里有时被读成"近距离拍摄"，要明确 `filling the frame` 或 `subject takes up most of frame`
4. **ECU 常被简化为 CU**：用具体局部更稳，如 `extreme close-up of the eye` 而非抽象的 `ECU`
5. **角度强度要写**：`slight low angle` vs `extreme low angle`，AI 会根据形容词调整夸张度
6. **配合景别和角度时的优先顺序**：英文 prompt 通常先写角度再写景别 → `low angle close-up`、`high angle wide shot`，这样 AI 解析准确率更高
7. **荷兰角（Dutch Angle）不在这章**：本质是 roll 而非 angle，见 [运镜.md 第 11 条](运镜.md)。但 prompt 里可以叠加：`dutch angle low angle close-up`（极端戏剧化）

## C. 与运镜的组合

景别和角度是**静态构图**；运镜是**动态变化**。三者组合的完整 prompt 框架：

```
[角度] [景别] of [主体], [运镜], [N] seconds, [风格]
```

例子：
- `low angle close-up of warrior, slow dolly in, 5 seconds, cinematic` → 仰视特写中的慢推
- `high angle wide shot of village, drone fly forward, 8 seconds` → 俯视远景中的航拍前进
- `eye level medium shot of two people, tracking shot, 6 seconds` → 平视双人中景的跟拍
