---
description: 涉及具体镜头运动指令、运镜术语翻译、运镜组合搭配、AI 模型对运镜的友好度判断时加载。
---

# AI 视频运镜提示词库

> 用途：可粘贴到 Seedance / 可灵 / Veo3 / Sora2 / Runway 等 AI 视频模型的运镜参考库
> 状态：v0.2（25 条运镜 + 运镜组合习惯章节；视频参考方案待定）
> 数据：基于公开影视摄影经验整理，难度评级为经验估计（非实测）
> 最后更新：2026-05-17

## 怎么用

1. **按需查找**：用下方索引按"机械动作"或"叙事用途"定位
2. **复制英文模板**：英文 prompt 在主流 AI 视频模型上精度更高
3. **看难度评级**：决定要不要多抽几次、是不是该简化 prompt
4. **读"易混淆"**：AI 经常误解某些术语，那一栏告诉你怎么避坑

**难度图例**（⭐~⭐⭐⭐⭐）：

- ⭐ **简单**：物理直观 + 训练数据丰富，AI 通常一次出活
- ⭐⭐ **中等**：常见但需精度控制，偶尔抽卡
- ⭐⭐⭐ **较难**：术语相对小众或语义复合，建议多抽几次
- ⭐⭐⭐⭐ **困难**：高约束 / 物理矛盾 / 小众术语，需要精细 prompt + 反复抽卡

**难度怎么估**：综合两个维度——① 运镜本身的物理/语义复杂度（约束越多越难复现）② 该术语在影视/视频训练数据中的常见度（小众即训练样本少 → AI 难学）。**不是实测值**，仅为先验估计，你实测后可以直接改这个评级。

---

## 索引

### 按机械动作

| 类别 | # | 运镜 | 难度 |
|---|---|---|---|
| 平移 | 1 | 推镜头 Dolly In | ⭐ |
| 平移 | 6 | 拉镜头 Dolly Out | ⭐ |
| 平移 | 7 | 横移 Truck / Crab | ⭐⭐ |
| 平移 | 8 | 跟随 Tracking Shot | ⭐⭐ |
| 平移 | 9 | 稳定器跟随 Steadicam | ⭐⭐ |
| 旋转 | 2 | 摇镜头 Pan | ⭐ |
| 旋转 | 10 | 俯仰 Tilt Up / Down | ⭐ |
| 旋转 | 11 | 荷兰角 Dutch Tilt | ⭐⭐ |
| 旋转 | 12 | 转场摇 Whip Pan | ⭐⭐⭐ |
| 升降 | 3 | 升镜头 Crane Up | ⭐⭐ |
| 升降 | 13 | 降镜头 Crane Down | ⭐⭐ |
| 升降 | 14 | 无人机航拍 Drone Shot | ⭐ |
| 焦距 | 15 | 变焦推进 Zoom In | ⭐ |
| 焦距 | 16 | 变焦拉远 Zoom Out | ⭐ |
| 焦距 | 17 | 拉焦 Rack Focus | ⭐⭐⭐ |
| 复合 | 4 | 希区柯克变焦 Dolly Zoom | ⭐⭐⭐⭐ |
| 复合 | 18 | 环绕 Orbit / Arc | ⭐⭐ |
| 复合 | 19 | 螺旋 Spiral | ⭐⭐⭐ |
| 复合 | 20 | 子弹时间 Bullet Time | ⭐⭐⭐⭐ |
| 复合 | 21 | 长镜头 Long Take | ⭐⭐⭐⭐ |
| 持机 | 5 | 手持跟随 Handheld Follow | ⭐⭐ |
| 视点 | 22 | 第一人称 POV | ⭐⭐ |
| 视点 | 23 | 越肩镜头 OTS | ⭐⭐ |
| 视点 | 24 | 上帝视角 Top-Down | ⭐ |
| 静止 | 25 | 固定镜头 Static | ⭐ |

### 按叙事用途

- **揭示宏大 / 全貌**：Crane Up、Dolly Out、Drone Shot、Top-Down、Zoom Out
- **强调情绪 / 细节**：Dolly In、Zoom In、Rack Focus
- **不安 / 眩晕 / 紧张**：Dolly Zoom、Dutch Tilt、Handheld Follow、Whip Pan
- **跟随主体**：Tracking、Steadicam、Handheld Follow、POV
- **空间巡视 / 探索**：Pan、Tilt、Orbit、Arc、Truck
- **焦点转移 / 注意力引导**：Rack Focus、Pan + Tilt
- **时间感塑造**：Long Take（沉浸延续）、Bullet Time（凝固）、Static（凝视）
- **对话 / 双人构图**：OTS、Truck（横向对话跟拍）
- **戏剧化亮相**：Orbit、Spiral、Crane Down 配 Tilt Up
- **结尾抽离**：Dolly Out、Crane Up、Drone Pull-back

---

## 1. 推镜头 / Dolly In

**别名**：Push In / Track In / 推进
**机械动作**：摄影机沿轨道向主体匀速逼近（焦距不变，与变焦本质不同）
**难度**：⭐ 简单（物理直观、术语高频、训练数据丰富）

**画面**：
- 主体在画面中越来越大，但**视觉透视不被压缩**——这是和变焦的本质差异
- 前景物体随机位前移而快速从画面边缘"飞过"，背景平缓变大，产生明显的空间纵深感
- 主体周围环境随距离缩短被"挤出"画面边缘，造成"被吸入"的视觉

**叙事用途**：
- **情绪积累**：随主体放大，观众注意力被强制聚焦到角色情绪上，适合关键决定/顿悟瞬间
- **强调反应**：当角色得知重要消息或目击关键事件时，推近至面部特写"拉入"其内心
- **沉浸感建立**：开场推进进入某空间（房间/走廊/角色背影），建立观看视角
- **悬疑铺垫**：缓慢推近一个看似平常的物件，暗示"它很重要"
- **经典参考**：《教父》开场对柯里昂的缓慢推进；《盗梦空间》推近梦境层级；《社交网络》对扎克伯格的多次心理推进

**英文模板**：
```
slow dolly in toward [subject], camera physically moves forward, shallow depth of field, [N] seconds, cinematic
```

**中文模板**：
```
镜头缓慢推进靠近[主体]，相机平稳向前移动，浅景深，[N]秒
```

**完整示例**：
> A young woman sits alone at a rainy café window, hands wrapped around a cup. Slow dolly in over 4 seconds, from medium shot to close-up on her eyes, shallow depth of field, soft window light, cinematic mood.

**参数维度**：
- 速度：`slow` / `medium` / `fast push in`
- 起止：`from wide to medium` / `from medium to close-up`
- 节奏：`smooth` / `accelerating`

**易混淆**：AI 模型常把 `dolly in` 误解为 `zoom in`（变焦）。**强调** `camera physically moves forward` 或 `tracking forward` 可以避免。Zoom in 画面会压缩、缺乏空间感；Dolly in 才是真"走过去"。

---

## 2. 摇镜头 / Pan

**别名**：Panning / 横摇
**机械动作**：摄影机位置不动，绕垂直轴水平旋转（左右摇）
**难度**：⭐ 简单（基本运镜、术语极高频）；whip pan（快摇）独立评 ⭐⭐⭐

**画面**：
- 机位钉死，画面像绕一根垂直轴扫视，背景从一侧持续推到另一侧
- 慢摇时观众有"导览"感，能看清新出现的元素；快摇（whip pan）时画面接近运动模糊"瞬移"
- 与 tracking 的视觉差异：pan 的前后景**同步移动无视差**；tracking 有近大远小的视差
- 视野中心始终是焦点，画面边缘元素"划过"

**叙事用途**：
- **建立空间**：开场摇过一片场景告诉观众"这是哪里、有什么"，常见纪录片/史诗片开场
- **揭示画外信息**：从主体摇向某物，暗示因果关联或对比（如：摇过血迹找到凶器）
- **跟随移动主体**：行人/车辆/动物在画面中横向移动时，机位转身跟随
- **转场（whip pan）**：极快摇制造模糊运动，常作两个场景的"运动剪辑"衔接
- **逐一介绍多个对象**：在一群人/一排物件间扫过，依次让观众认知
- **经典参考**：《荒野大镖客》开场对小镇的慢摇；《老无所依》大量慢摇建立空间紧张感；昆汀作品大量使用 whip pan 做风格化转场

**英文模板**：
```
camera pans [left/right] slowly, revealing [scene/subject], [N] seconds, steady tripod
```

**中文模板**：
```
镜头缓慢向[左/右]摇移，展示[场景/主体]，[N]秒，三脚架稳定
```

**完整示例**：
> Wide shot of a misty mountain valley at dawn. Camera pans slowly from left to right over 6 seconds, revealing a distant temple emerging from the fog. Steady tripod, soft golden hour light.

**参数维度**：
- 方向：`pan left` / `pan right`
- 速度：`slow pan` / `whip pan`（极快，常用于转场）
- 起止：明确"from X to Y"比单说"pan"效果更可控

**易混淆**：
- vs **Tracking Shot**：Pan 是机位不动转身；Tracking 是机位在动
- vs **Tilt**：Pan 是水平摇；Tilt 是垂直摇（俯仰）
- `whip pan` 在 AI 模型上抽卡率明显更高，容易出模糊乱帧——建议慢镜头开始，需要快摇时多次重试

---

## 3. 升镜头 / Crane Up

**别名**：Crane Shot / Jib Up / 升降镜头
**机械动作**：摄影机由低向高垂直上升（常配合俯仰角度变化）
**难度**：⭐⭐ 中等（垂直运动精度要求高，且 AI 容易跟 drone shot 混淆）

**画面**：
- 起始机位通常贴近主体（人物身边、地面附近），运动结束时机位在高处俯视
- 升起过程中前景元素**下沉出画**，远处的环境/风景持续显现，形成"打开世界"感
- 常配合 tilt down（俯角变化）让主体保持在画面下半部分
- 与 drone shot 的关键区别：crane 通常短距离（几米到十几米），运动连贯但保守

**叙事用途**：
- **结尾抽离**：剧情终结时机位渐升，让角色变小，造"故事告一段落"的距离感
- **表现渺小**：角色在巨大环境中（沙漠、雪地、废墟、城市）的孤独与无力
- **史诗感开场**：从角色或物件开始升起揭示宏大世界观，常见奇幻/科幻片开场
- **战场/事件全景**：从地面战士升起到俯瞰整个战场，告诉观众规模和位置关系
- **从私密到公共**：从角色独处的房间升起到俯瞰整个建筑/街区，表现个体与社会
- **经典参考**：《卡萨布兰卡》结尾的升镜头；《光荣战役》战场升起揭示伤亡；《辛德勒的名单》集中营场景多次使用

**英文模板**：
```
camera cranes up from [low position] to [high position], revealing [wider scene], [N] seconds, smooth motion
```

**中文模板**：
```
镜头从[低位]缓慢升起至[高位]，展现[更广的场景]，[N]秒，平稳运动
```

**完整示例**：
> A lone figure walks across an empty parking lot at dusk. Camera starts at ground level behind them, then cranes up smoothly over 5 seconds, ending in a high wide shot revealing the vast empty city beyond. Cinematic, melancholic mood.

**参数维度**：
- 起点：`from ground level` / `from eye level`
- 终点：`to bird's eye view` / `to high angle`
- 配合：常配 `+ tilt down`（升起同时俯视）
- 速度：`slow` 出史诗感，`rapid` 出戏剧感

**易混淆**：
- vs **Tilt Up**：Tilt up 是机位不动只抬头；Crane up 是机位整体上升
- vs **Drone Shot**：Crane up 通常短距离（几米内）+ 保守轨迹；Drone 是远距离飞行，画面运动幅度大
- AI 模型偶尔会把 crane up 渲染成 drone fly-over，prompt 加 `short vertical movement, not aerial` 可缓解

---

## 4. 希区柯克变焦 / Dolly Zoom

**别名**：Vertigo Effect / Trombone Shot / 滑动变焦
**机械动作**：摄影机推进的同时反向变焦（dolly in + zoom out），或反之——保持主体大小不变，但背景透视急剧扭曲
**难度**：⭐⭐⭐⭐ 困难（物理矛盾约束 + 术语小众 + AI 训练样本稀少）

**画面**：
- 主体大小**完全不变**，但背景透视急剧扭曲——像"现实在弯曲"
- `dolly in + zoom out` 版：背景元素从角色身边**远离**，世界"撤退"
- `dolly out + zoom in` 版：背景元素向角色**逼近**，世界"压迫"
- 必然伴随景深变化（焦距改变），主体周围会出现微妙模糊/锐化
- 整体画面有强烈的"非现实感"——这是它最大的视觉标识

**叙事用途**：
- **心理震惊瞬间**：角色得知颠覆性真相、看到不该看的东西、意识到自己处境的瞬间
- **现实扭曲**：从清醒过渡到梦境/幻觉/恐惧/药物影响的转折瞬间
- **恐惧具象化**：恐怖片中常用，让观众"感受到"角色看到威胁时的眩晕
- **关键悟出/失忆瞬间**：智识层面的颠覆（不只情绪），如"原来一直被骗"
- **使用频率忠告**：通常一部片只用 1-2 次，多用即廉价、即套路
- **经典参考**：希区柯克《迷魂记》楼梯戏（命名来源）；斯皮尔伯格《大白鲨》海滩戏（Roy Scheider 看到鲨鱼）；《好家伙》餐馆戏；《指环王》弗罗多多次的小山丘戏

**英文模板**：
```
dolly zoom on [subject], vertigo effect, subject stays same size while background warps, [N] seconds, dramatic
```

**中文模板**：
```
对[主体]使用希区柯克变焦，眩晕效果，主体大小不变背景透视扭曲，[N]秒，戏剧性
```

**完整示例**：
> Close-up on a man's face as he realizes a terrible truth. Dolly zoom over 3 seconds, his face remains the same size in frame while the hallway behind him stretches and warps, creating vertigo effect. Cinematic, tense, slight handheld feel.

**参数维度**：
- 方向：`dolly in + zoom out`（背景拉远，更常见的"vertigo"感）/ `dolly out + zoom in`（背景压近，更压迫）
- 速度：通常 2-4 秒最佳，太长会破效果
- 强度：明确 `subtle` 或 `extreme` 影响透视扭曲幅度

**易混淆**：
- 这是 AI 视频模型**最难稳定复现**的运镜之一。原因：模型对"主体不变 + 背景变形"这个矛盾约束理解不稳定
- **抽卡建议**：用 `vertigo effect` 这个广为人知的术语比 `dolly zoom` 命中率高
- 失败模式 1：变成普通推镜头（无背景扭曲）
- 失败模式 2：变成普通变焦（主体也跟着变大）
- 加入参考 `like in Vertigo (Hitchcock)` 或 `like in Jaws beach scene` 可能提升识别率

---

## 5. 手持跟随 / Handheld Follow

**别名**：Handheld Tracking / Run-and-Gun / 手持跟拍
**机械动作**：摄影师手持摄影机跟随主体移动，画面带自然抖动
**难度**：⭐⭐ 中等（运动本身常见，但"自然抖动而非乱抖"需要 prompt 精度）

**画面**：
- 画面整体小幅持续抖动，**模拟人类步行/跑动时的自然摇晃**——不是机械振动，是有呼吸的
- 主体在画框内位置略有漂移（不像稳定器那样钉死），更具"被人拍下"的真实感
- 跟拍距离通常较近（人物胸部以上构图为主），强化"贴身"观感
- 转身、加速、停顿都会带画面的对应反应（不像稳定器那样平滑过渡）

**叙事用途**：
- **紧迫感**：追逐戏、危机时刻，画面动荡放大观众心跳
- **纪实风格**：模仿新闻/纪录片质感，告诉观众"真实事件正在发生"
- **主观体验**：观众像"跟着角色一起呼吸"，强代入感
- **恐怖追逐**：与角色一同奔跑/被追，让观众分担紧张
- **伪纪录片**：故意暴露"摄影机存在"，营造"有人在拍"的元叙事观感
- **战争/动作戏**：使观众和角色同处战场，区别于稳定的英雄视角
- **经典参考**：《拯救大兵瑞恩》诺曼底登陆；《女巫布莱尔》全片伪纪录片用法；《谍影重重》系列动作戏；《罗马》（虽用稳定器，但风格相似的贴身跟随）

**英文模板**：
```
handheld camera follows [subject] from behind, natural shake, documentary style, [N] seconds
```

**中文模板**：
```
手持相机从背后跟随[主体]，自然抖动，纪实风格，[N]秒
```

**完整示例**：
> A young man runs through a crowded night market, weaving between vendors and customers. Handheld camera follows him from behind at shoulder height, natural shake, neon lights blurring past. Documentary style, urgent feel, 6 seconds.

**参数维度**：
- 跟随位置：`from behind` / `beside subject` / `in front, walking backward`
- 抖动强度：`subtle handheld` / `aggressive shake` / `natural breathing motion`
- 风格：`documentary` / `found footage` / `cinematic verite`

**易混淆**：
- vs **Steadicam Follow**：Steadicam 是丝滑跟随、无抖动；Handheld 是有自然抖动
- vs **Tracking Shot**：Tracking 通常用轨道/稳定器，机械感强；Handheld 强调人为质感
- 加 `slight handheld motion` 比 `shaky cam` 效果更克制——后者 AI 模型容易抖到过度乱帧
- 反例：想做温馨家庭片但用了 handheld，会出意外的纪录片观感

---

## 6. 拉镜头 / Dolly Out

**别名**：Pull Out / Track Out / 拉远
**机械动作**：摄影机沿轨道远离主体，与推镜头反向；焦距不变（区别于 zoom out）
**难度**：⭐ 简单（与推镜头镜像，物理直观、术语高频）

**画面**：
- 主体在画面中越来越小，前景空间持续扩展
- 背景元素新出现在画面边缘，揭示环境
- 与 zoom out 区别：dolly out 有视差（前后景以不同速度变化），zoom out 是纯压缩

**叙事用途**：
- **情绪抽离**：从角色面部退到全景，表达"距离感"或"剧情告一段落"
- **揭示真相**：主体周边突然出现意想不到的元素（close-up 上一个人 → dolly out 显示他在医院/监狱/坟前）
- **从私密到公共**：从角色独处的房间退到周围的世界
- **戏剧反转**：揭示"看似温馨" 实则有威胁元素（恐怖片常用）
- **经典参考**：《肖申克的救赎》结尾海滩拉远；《辛德勒的名单》多次从特写拉到广角；《闪灵》对称式拉远

**英文模板**：
```
slow dolly out from [subject], camera moves backward, revealing [wider scene], [N] seconds
```

**中文模板**：
```
镜头从[主体]缓慢拉远，相机向后移动，揭示[更广场景]，[N]秒
```

**完整示例**：
> Close-up of a child's hand holding a teddy bear in dim light. Slow dolly out over 5 seconds, revealing the child sitting alone in an empty hospital corridor. Cold institutional lighting, melancholic mood, cinematic.

**参数维度**：
- 速度：`slow` / `medium pull out` / `rapid pullback`
- 起止：`from close-up to wide` / `from medium to extreme wide`
- 节奏：`smooth` / `accelerating reveal`

**易混淆**：
- vs **Zoom Out**：dolly out 有视差（前后景速度不同）；zoom out 是变焦无空间纵深变化
- AI 模型偶尔会把 dolly out 渲染成静止背景下主体缩小——强调 `camera physically pulls back` 可缓解

---

## 7. 横移 / Truck / Crab

**别名**：Trucking / Crabbing / Side Tracking / 横移
**机械动作**：摄影机平行于主体或场景做水平移动（与 pan 的根本区别：机位整体移动，不是旋转）
**难度**：⭐⭐ 中等（术语稍混乱：truck 指水平整体移动，crab 指短距离横移；AI 易跟 pan 混）

**画面**：
- 机位水平移动，画面构图基本保持，但背景横向滑动
- 前景物体掠过画面、背景缓慢移动，强烈视差效果（这是和 pan 的核心视觉差异）
- 主体可保持画面中心（横向跟拍）或主体不动（横向巡视）

**叙事用途**：
- **横向跟拍人物**：行人、车辆、动物侧向移动时
- **空间巡视**：横扫一排物件、一群人、一面墙
- **对话场面**：演员侧身走动谈话时
- **平行剪辑提示**：两条并行叙事的"视觉提示"
- **经典参考**：《天才雷普利》街边咖啡馆横移；《布达佩斯大饭店》大量对称横移；《1917》多次横向跟拍

**英文模板**：
```
camera trucks [left/right] alongside [subject], parallel motion, [N] seconds
```

**中文模板**：
```
镜头与[主体]平行向[左/右]横移，[N]秒
```

**完整示例**：
> Two friends walking and talking along a beach at sunset. Camera trucks right alongside them at waist level, keeping them centered in frame, ocean visible behind. Smooth tracking, warm golden hour light, 8 seconds.

**参数维度**：
- 方向：`truck left` / `truck right`
- 跟主体关系：`parallel to subject`（横向跟拍）/ `independent of subject`（巡视）
- 速度：匹配主体速度才显自然

**易混淆**：
- vs **Pan**：truck 是机位移动（有视差）；pan 是机位旋转（无视差）
- vs **Tracking Shot**：tracking 是大类（含 truck、follow），truck 特指水平横移
- AI 模型可能把 truck 输出成 pan 或弧形运动——明确 `parallel sideways motion, not rotation`

---

## 8. 跟随镜头 / Tracking Shot

**别名**：Following Shot / Track / 跟拍
**机械动作**：摄影机随主体一同移动，保持相对位置；机位移动是大类，含轨道、推车、稳定器、手持等
**难度**：⭐⭐ 中等（语义宽泛 + AI 易跟 dolly 混；明确跟随方位是关键）

**画面**：
- 主体在画面中位置/构图相对稳定，背景持续滚动
- 主体周围空间感强烈，观众"跟着主体走"
- 与 dolly in 的区别：tracking 是跟随主体的运动；dolly in 是相对主体推近

**叙事用途**：
- **沉浸跟随**：长时间跟随角色穿行场景，建立"陪伴感"
- **动作戏**：跟拍运动主体（奔跑、骑车、开车）
- **空间探索**：跟随角色进入新场景，让观众"和角色一起发现"
- **长镜头基础**：长镜头里大部分内容是 tracking shot 的衔接
- **经典参考**：《好家伙》餐馆长镜头；《鸟人》全片伪一镜到底；《1917》连续跟随

**英文模板**：
```
tracking shot following [subject] from [angle], camera maintains [distance], [N] seconds
```

**中文模板**：
```
跟拍镜头，从[角度]跟随[主体]，相机保持[距离]，[N]秒
```

**完整示例**：
> A chef walks rapidly through a busy restaurant kitchen, checking each station. Tracking shot following from behind at shoulder height, maintaining 2 meters distance, smooth motion, warm kitchen lighting, 7 seconds.

**参数维度**：
- 跟随位置：`from behind` / `from in front` / `beside` / `from above`
- 距离：`close tracking` / `medium distance` / `wide tracking`
- 设备暗示：`smooth tracking`（稳定器感）/ `handheld tracking`（手持感）

**易混淆**：
- vs **Dolly In**：tracking 是跟主体一起动；dolly 是机位独立推近主体
- vs **Pan**：tracking 机位移动；pan 机位旋转
- 明确"跟随谁、从哪个方位、什么距离"是 AI 出活的关键

---

## 9. 稳定器跟随 / Steadicam Follow

**别名**：Steadicam Shot / Gimbal Follow / 稳像跟随
**机械动作**：摄影机用稳定器（Steadicam、Gimbal）跟拍，画面丝滑无抖动
**难度**：⭐⭐ 中等（与 handheld 区分需要 prompt 精度）

**画面**：
- 主体在画面中稳定如钉，背景平滑流动
- 转向、上下楼梯、绕过障碍都不抖
- 区别于 handheld：稳定器是"飘浮"感，handheld 是"呼吸"感

**叙事用途**：
- **丝滑沉浸**：让观众感觉"被无形地推着跟随"
- **复杂空间穿行**：跟主体上下楼梯、穿过门廊、绕过障碍
- **优雅长镜头**：影片标志性长镜头几乎都用稳定器
- **现代商业大片感**：区别于 handheld 的"粗粝"，更"商业大片"质感
- **经典参考**：《闪灵》Danny 骑三轮车穿酒店走廊；《罗马》全片稳定器长镜头

**英文模板**：
```
steadicam follows [subject] smoothly through [environment], no shake, fluid motion, [N] seconds
```

**中文模板**：
```
稳定器丝滑跟随[主体]穿过[环境]，无抖动，流畅运动，[N]秒
```

**完整示例**：
> A young woman in a flowing dress walks confidently through a bustling hotel lobby. Steadicam follows her from behind at hip height, gliding smoothly past other guests and decorative columns. No shake, fluid motion, soft warm lighting, 8 seconds.

**参数维度**：
- 跟随位置：同 tracking
- 高度变化：`maintaining hip height` / `gliding through space`
- 风格：`elegant Steadicam` / `dynamic gimbal`

**易混淆**：
- vs **Handheld**：steadicam 强调 `smooth, no shake`；handheld 强调 `natural shake`
- vs **Drone**：steadicam 通常贴近主体（地面到肩高）；drone 在更高远位置
- 强调 `gliding` 或 `floating motion` 帮助 AI 区分

---

## 10. 俯仰 / Tilt Up / Tilt Down

**别名**：Tilting / 抬升摇 / 俯摇
**机械动作**：摄影机位置不动，绕水平轴垂直旋转（上抬 = tilt up，下俯 = tilt down）
**难度**：⭐ 简单（基本运镜、训练数据极多）

**画面**：
- 机位钉死，视野像"抬头/低头"一样上下扫视
- 前景元素从画面顶部/底部滑出，新空间在另一边出现
- 与 crane up/down 的区别：tilt 机位不动，只转视角；crane 整体上下移动

**叙事用途**：
- **介绍规模感**（tilt up）：从角色脚到头介绍人物，强调身材；从地面 tilt up 到天空表达宏大
- **揭示关键信息**（tilt down）：从面部到桌上的物件（信、武器、戒指）
- **建立威严**（tilt up）：从下而上仰拍角色出场，给力量感
- **悲剧揭示**（tilt down）：从生还的角色 tilt down 到地上的尸体
- **经典参考**：《2001 太空漫游》开场猿人投骨头 → tilt up 接太空船；西部片大量用 tilt up 介绍反派

**英文模板**：
```
camera tilts [up/down] from [start] to [end], steady tripod, [N] seconds
```

**中文模板**：
```
镜头从[起点]向[上/下]俯仰至[终点]，三脚架稳定，[N]秒
```

**完整示例**：
> Close-up of an ornate ceremonial knife on a wooden table. Camera tilts up slowly over 4 seconds, revealing the hands and then the face of a stern old monk holding it. Steady tripod, candlelight ambiance, cinematic mood.

**参数维度**：
- 方向：`tilt up` / `tilt down`
- 起止：明确"from [low element] to [high element]"
- 速度：`slow tilt`（揭示感）/ `quick tilt`（节奏感）

**易混淆**：
- vs **Crane Up/Down**：tilt 机位不动；crane 整体上下
- vs **Pan**：tilt 是垂直；pan 是水平
- 想要"边升边俯"，明确说 `camera cranes up while tilting down`（见组合章节）

---

## 11. 荷兰角 / Dutch Tilt

**别名**：Dutch Angle / Canted Angle / 倾斜镜头 / 蜘蛛人镜头
**机械动作**：摄影机绕镜头中轴旋转，使画面水平线倾斜（不是 tilt 的俯仰，而是 roll 的滚转）
**难度**：⭐⭐ 中等（视觉特征极鲜明，但术语对 AI 不算高频）

**画面**：
- 画面水平线倾斜（通常 10°-30°），所有垂直线都歪
- 与正常镜头并置时，造成强烈"不对劲"感
- 通常是静止状态，偶尔有动态（从正画面 roll 到倾斜）

**叙事用途**：
- **不安、混乱**：角色心理失衡、迷茫、失控
- **戏剧化反派**：暗示角色危险、不可信
- **超现实/科幻**：异常空间、外星感
- **风格化暴力**：动作戏中夸张张力
- **经典参考**：《第三个人》大量倾斜镜头建立战后维也纳压抑；《蝙蝠侠：黑暗骑士》小丑系列；《蜘蛛人 2002》多次倾斜镜头

**英文模板**：
```
dutch angle, camera tilted [N] degrees, off-balance composition, [scene description], [N] seconds
```

**中文模板**：
```
荷兰角，镜头倾斜[N]度，失衡构图，[场景描述]，[N]秒
```

**完整示例**：
> A man stands at the end of an empty subway platform, looking down the tunnel. Dutch angle, camera tilted 20 degrees, fluorescent lights flickering, off-balance composition emphasizing his unease. 6 seconds, cinematic, slight handheld motion.

**参数维度**：
- 倾斜角度：`15 degrees` / `30 degrees`（越大越不安，超 45° 接近抽象）
- 方向：`tilted left` / `tilted right`
- 状态：`static dutch angle` / `rolling into dutch`（动态进入）

**易混淆**：
- vs **Tilt Up/Down**：tilt 是俯仰（pitch）；dutch tilt 是滚转（roll），别被名字骗了
- AI 模型用 `dutch angle` 比 `dutch tilt` 命中率高（前者更高频）
- 加 `off-balance composition` 提示 AI 渲染"歪斜"特征

---

## 12. 转场摇 / Whip Pan

**别名**：Swish Pan / Snap Pan / 急摇 / 快摇
**机械动作**：极快速度的 pan 摇镜头，画面运动模糊到接近"瞬移"
**难度**：⭐⭐⭐ 较难（运动模糊难精控，常导致乱帧）

**画面**：
- 起止画面清晰，中间是高速运动模糊
- 持续时间短（通常 < 1 秒）
- 常与剪辑配合：whip pan 进 + 切到另一场景的 whip pan 出，等于"运动剪辑"

**叙事用途**：
- **场景转换**：A 场景 whip pan 出 + B 场景 whip pan 入 = 流畅剪辑
- **快节奏强调**：动作戏、喜剧节奏点
- **主观惊吓**：角色突然转头看到威胁，第一人称对应的画面
- **风格化签名**：昆汀、Edgar Wright、Sam Raimi 标志运镜
- **经典参考**：《疯狂的麦克斯：狂暴之路》大量 whip pan；昆汀《杀死比尔》打斗段落

**英文模板**：
```
whip pan from [scene A] to [scene B], rapid motion blur, [N] seconds total
```

**中文模板**：
```
急摇从[场景A]到[场景B]，急速运动模糊，[N]秒
```

**完整示例**：
> A detective stares intently at evidence on a desk. Suddenly, whip pan to the right, motion blur, revealing a colleague rushing into the office with urgent news. 2 seconds total, sharp focus at both start and end, cinematic.

**参数维度**：
- 速度：`whip pan`（最快）/ `snap pan`（稍慢，画面仍可辨）
- 方向：`whip pan right` / `whip pan left`
- 起止清晰度：`sharp start and end, blur in middle`

**易混淆**：
- AI 常把 whip pan 渲染成完全模糊或乱帧——试 `quick pan with motion blur, sharp at start and end`
- 失败模式：画面变成动态噪声、主体消失
- 抽卡建议：缩短时长（"over 1 second"），强调起止清晰

---

## 13. 降镜头 / Crane Down

**别名**：Crane Shot Down / Jib Down / 下降镜头
**机械动作**：摄影机由高向低垂直下降（与 crane up 互补）
**难度**：⭐⭐ 中等（同 crane up，但更少使用，训练样本相对少）

**画面**：
- 起始机位在高处（空中、楼上、屋顶），运动结束时贴近主体或地面
- 下降过程中远处环境/全景**消失**在画面上方，近处主体/细节进入画面
- 常配合 tilt up（下降同时仰视主体）

**叙事用途**：
- **开场建立**：从天空/全景慢慢下降到地面角色，"切入故事"
- **凝聚焦点**：从宏大降到微小，强调个体在宏大事件中的位置
- **戏剧降临**：高位俯视后下降到主体，暗示"目光锁定"
- **梦境/超现实**：从天空慢慢降落进入梦境/异世界
- **经典参考**：《海上钢琴师》码头下降镜头；动画片大量使用从云端下降到人物

**英文模板**：
```
camera cranes down from [high position] to [low position], focusing on [subject], [N] seconds
```

**中文模板**：
```
镜头从[高位]缓慢下降至[低位]，聚焦[主体]，[N]秒
```

**完整示例**：
> Aerial view of a wedding ceremony in a sunlit garden. Camera cranes down slowly over 6 seconds, descending from above the crowd to a close shot of the bride's face as she says vows. Smooth motion, golden hour light, romantic cinematic.

**参数维度**：
- 起点：`from high angle` / `from bird's eye view`
- 终点：`to medium shot` / `to ground level`
- 配合：常配 `+ tilt up`（下降同时仰视）

**易混淆**：
- vs **Tilt Down**：tilt down 是机位不动只低头；crane down 是机位整体下降
- vs **Drone descent**：crane 通常短距离；drone 是远距离飞行下降
- AI 对 crane down 偶尔渲染成 drone descent

---

## 14. 无人机航拍 / Drone Shot

**别名**：Aerial Shot / Drone Flythrough / 航拍
**机械动作**：摄影机由无人机搭载，空中自由飞行（水平、垂直、环绕、推进等组合）
**难度**：⭐ 简单（训练数据极丰富，是 AI 视频时代最受欢迎的镜头类型之一）

**画面**：
- 视角通常较高，俯瞰场景
- 运动幅度大，覆盖距离远（几十米到数百米）
- 常见类型：fly-over（掠过）、fly-through（穿过）、orbit（环绕）、reveal（揭示）

**叙事用途**：
- **建立环境**：开场航拍展示城市/自然/建筑
- **史诗感**：宏大场景、风景片、旅游宣传
- **追逐戏**：高速跟拍车辆/动物
- **过渡镜头**：从一个场景"飞到"下一个
- **现代感签名**：商业广告、短视频高频使用
- **经典参考**：《荒野猎人》航拍雪山；《权力的游戏》各城市航拍片头；几乎所有现代旅游/汽车广告

**英文模板**：
```
drone shot, aerial view, [movement type] over [scene], [N] seconds, cinematic
```

**中文模板**：
```
无人机航拍，[运动类型]，越过[场景]，[N]秒，电影感
```

**完整示例**：
> Drone shot soaring over a misty pine forest at dawn. Camera flies forward at 30 meters altitude, slowly tilting down to reveal a winding river below. Cinematic aerial view, golden morning light, 8 seconds.

**参数维度**：
- 运动类型：`fly forward` / `fly over` / `aerial orbit` / `descending drone`
- 高度：`low aerial` / `medium altitude` / `high aerial`
- 速度：`slow drone` / `fast flythrough`

**易混淆**：
- 与 crane shot 区别：drone 离地远（几十米起步）、飞行距离长
- AI 默认渲染 drone 时画面会偏"高级感"——这也是它易出活的原因
- 不要写 "helicopter shot"（可能真出现直升机），用 "drone shot" 或 "aerial view"

---

## 15. 变焦推进 / Zoom In

**别名**：Zoom / Push Zoom（注意：中文里"拉镜头"有时指 zoom，容易混）
**机械动作**：摄影机位置不动，改变焦距让主体在画面中放大
**难度**：⭐ 简单（极基本，AI 极易出活）

**画面**：
- 主体放大，但**空间没有真正变化**（前后景以相同速度放大，无视差）
- 透视被压缩——远处物体被"拉近"而非"走近"
- 与 dolly in 对比：zoom in 画面"扁"，dolly in 画面有"穿过空间感"

**叙事用途**：
- **快速强调**：突然 zoom in 到某个细节，戏剧性强调
- **怀旧/家庭录像风格**：模仿 80-90 年代 DV 摄像质感
- **新闻/纪录片**：远距离拍摄时不得不用变焦
- **风格化签名**：昆汀、PTA、Edgar Wright 偶尔用 zoom in 制造"戏剧反应"
- **经典参考**：《杀死比尔》多次 snap zoom；《热血警探》喜剧式 zoom；纪录片中常见

**英文模板**：
```
zoom in on [subject], no camera movement, focal length changes, [N] seconds
```

**中文模板**：
```
对[主体]变焦推进，相机位置不动，焦距变化，[N]秒
```

**完整示例**：
> Wide shot of a chess board with two players. Slow zoom in over 4 seconds on the king piece, focal length changes, no camera movement, shallow depth of field at the end. Cinematic, tense atmosphere.

**参数维度**：
- 速度：`slow zoom` / `snap zoom`（突然变焦）
- 起止：`from wide to close-up via zoom`
- 风格：`cinematic zoom` / `documentary zoom`

**易混淆**：
- vs **Dolly In**：zoom 机位不动；dolly 机位移动
- AI 有时附加机位移动（变成 zoom + dolly），强调 `static camera, only focal length changes`
- 影视圈里"zoom in"被认为是相对廉价/电视风格的运镜，专业作品多用 dolly in

---

## 16. 变焦拉远 / Zoom Out

**别名**：Pull Zoom / 拉镜头
**机械动作**：摄影机位置不动，焦距缩短让主体在画面中变小
**难度**：⭐ 简单（同 zoom in，AI 易出活）

**画面**：
- 主体变小，画面边缘新元素出现
- 仍是焦距变化，无视差
- 与 dolly out 对比：zoom out 无"后退"的物理感

**叙事用途**：
- **揭示规模**：从一个细节 zoom out 到整体环境
- **滑稽抽离**：戏剧性"原来如此"——dolly out 是郑重抽离，zoom out 是轻松抽离
- **纪录片揭示**：从动物特写 zoom out 到栖息地
- **梗式使用**：网络视频常用 zoom out 制造"突然发现什么"的笑点
- **经典参考**：《饥饿游戏》游戏区域 zoom out；纪录片自然类经典手法；YouTube 短视频中"原来是 XX"的爆梗运用

**英文模板**：
```
zoom out from [subject], revealing [wider context], static camera, [N] seconds
```

**中文模板**：
```
从[主体]变焦拉远，揭示[更广背景]，相机不动，[N]秒
```

**完整示例**：
> Close-up of a single sunflower in a field. Slow zoom out over 5 seconds, revealing rows of sunflowers stretching to the horizon under a vast blue sky. Static camera, summer afternoon light, peaceful cinematic.

**参数维度**：
- 速度：`slow zoom out` / `rapid pullback`
- 起止：`from close-up to wide`
- 配合：常配 `+ tilt up`（拉远同时抬头展示天空）

**易混淆**：
- vs **Dolly Out**：zoom out 静止机位；dolly out 实际后退
- AI 偶尔会渲染成"主体缩小但环境不变"——强调 `revealing wider context`

---

## 17. 拉焦 / Rack Focus

**别名**：Focus Pull / Focus Shift / 焦点切换
**机械动作**：摄影机不动，景深变化让画面焦点从前景转到背景（或反之）
**难度**：⭐⭐⭐ 较难（AI 难精确控制景深变化、焦点切换的时间点）

**画面**：
- 画面构图不变，但**注意力强制转移**：原焦点变虚、新焦点变清晰
- 前后景必须有明显距离差，才能产生戏剧性
- 常在浅景深下使用（大光圈，景深极薄）

**叙事用途**：
- **注意力引导**：让观众的视线从一个元素切换到另一个，无需剪辑
- **暗示发现/反应**：角色（前景）反应 → 焦点切到他注意的对象（背景）
- **空间关系揭示**：两个角色一前一后，焦点切换暗示对话/对峙
- **悬念铺垫**：背景出现意外元素，焦点切换让观众发现
- **经典参考**：《公民凯恩》大量深焦摄影 + 焦点切换；阿尔特曼作品深景表演中的拉焦；现代电影对话戏

**英文模板**：
```
rack focus from [foreground subject] to [background subject], shallow depth of field, static camera, [N] seconds
```

**中文模板**：
```
拉焦从[前景主体]切到[背景主体]，浅景深，相机不动，[N]秒
```

**完整示例**：
> Foreground: a wine glass on a restaurant table, sharp focus. Background: a couple sitting together, blurred. Rack focus over 2 seconds: glass becomes blurred, couple becomes sharp, revealing their tense expressions. Static camera, warm restaurant lighting, shallow depth of field.

**参数维度**：
- 方向：`rack focus from foreground to background` / 反之
- 速度：`slow focus pull`（戏剧感）/ `quick rack focus`（节奏感）
- 强度：浅景深（`shallow DoF`）才能突出焦点变化

**易混淆**：
- AI 常把 rack focus 渲染成"全画面对焦变化"而非"前后景独立焦点"——明确 `foreground sharp first, then background sharp`
- 失败模式：画面整体糊一下又清晰，没有真正的景深切换
- 抽卡建议：prompt 里画面构图明确指出"前景 X、背景 Y"

---

## 18. 环绕 / Orbit / Arc

**别名**：Orbital Shot / Circle Shot / 圆周环绕
**机械动作**：摄影机围绕主体做圆周或弧形运动，主体在画面中相对稳定
**难度**：⭐⭐ 中等（AI 视频圈高频使用、术语较好辨认，但精度有时不稳）

**画面**：
- 主体在画面中心相对不动（位置和大小），但**背景持续旋转**
- 360 度环绕：完整一圈；arc：半圆或更短
- 视觉张力极强——主体"被聚焦"，世界"绕着他转"

**叙事用途**：
- **戏剧化亮相**：英雄/反派出场，环绕一圈强调存在感
- **关键时刻凝固感**：主体处于决定性瞬间（求婚、宣誓、决斗）
- **关系揭示**：环绕两个角色，强调他们之间的关系/张力
- **风格化签名**：商业广告标志运镜；动作片"装逼时刻"
- **经典参考**：《黑客帝国》子弹时间环绕；《加勒比海盗》多场角色亮相环绕；现代商业广告几乎必用

**英文模板**：
```
orbit shot around [subject], 360 degree circle, subject centered, [N] seconds
```

**中文模板**：
```
环绕镜头围绕[主体]，360度旋转，主体居中，[N]秒
```

**完整示例**：
> A samurai stands alone in a misty bamboo forest, holding his katana. Orbit shot circles him over 6 seconds, going from front to side to back to front, subject stays centered while bamboo and mist rotate around him. Cinematic, dramatic.

**参数维度**：
- 弧度：`full 360 orbit` / `half circle arc` / `quarter arc`
- 方向：`orbit clockwise` / `counter-clockwise`
- 高度变化：`orbit at eye level` / `orbit while rising`（见组合章节）
- 速度：`slow orbit`（庄重）/ `fast circle`（炫技）

**易混淆**：
- vs **Pan**：orbit 是机位绕主体；pan 是机位转身
- AI 对 orbit 通常处理得不错，但 360 度有时只完成 180——明确 `complete 360 degree orbit`
- "Arc" 在不同语境含义不同：摄影术语指弧形运动；动画/3D 指轨道运动

---

## 19. 螺旋 / Spiral

**别名**：Helical Shot / Corkscrew Shot / 螺旋上升/下降
**机械动作**：摄影机一边环绕主体一边升起或下降，形成螺旋轨迹
**难度**：⭐⭐⭐ 较难（复合运动 + 术语不算高频，AI 出活可能简化成 orbit）

**画面**：
- 螺旋上升：环绕的同时机位升高，最终在主体上方俯视
- 螺旋下降：反之，从上方螺旋至主体身边
- 主体仍是焦点，但景别/角度持续变化（不像纯环绕那样保持构图）

**叙事用途**：
- **升华瞬间**：主体取得胜利/达成觉悟，机位螺旋上升表达"超越"
- **意识坠落**：心理崩塌、噩梦开始，螺旋下降表达"陷入"
- **戏剧化展示**：从角色到环境的渐进揭示，比纯 crane 更动感
- **超现实/奇幻**：暗示能量/魔法/精神力量
- **经典参考**：《盗梦空间》多个梦境过渡；《阿凡达》潘多拉森林展示；动画片如《幽灵公主》多次使用

**英文模板**：
```
spiral shot around [subject], camera circles while rising/descending, [N] seconds
```

**中文模板**：
```
对[主体]螺旋拍摄，镜头环绕同时升起/下降，[N]秒
```

**完整示例**：
> A girl raises her arms in joy at the center of a flower field. Spiral shot circles her clockwise while rising over 6 seconds, starting at her eye level and ending in a high overhead view of her surrounded by blooming flowers. Smooth motion, sunlight, magical mood.

**参数维度**：
- 方向：`spiral up` / `spiral down`
- 旋转方向：`clockwise` / `counter-clockwise`
- 起止：从近到远（螺旋拉远）或反之

**易混淆**：
- AI 可能把 spiral 简化成 orbit（无升降）—— 强调 `while rising` 或 `corkscrew motion`
- vs **Bullet Time**：bullet time 包含时间停止 + 多机位；spiral 只是连续运动
- 词选用：`helical` 太学术；`spiral` 最常用；`corkscrew` 形象但少见

---

## 20. 子弹时间 / Bullet Time

**别名**：Time Slice / Frozen Moment / 凝固时间
**机械动作**：主体动作高速凝固或慢速，摄影机围绕其做正常或加速运动（实际拍摄用多机位阵列合成）
**难度**：⭐⭐⭐⭐ 困难（时间+空间双重特殊处理；AI 视频里很多模型尚不能完全复现"凝固"）

**画面**：
- 主体动作明显慢于正常速度（甚至凝固），但**镜头运动正常或加速**
- 空间中"被冻结"的微粒、雨滴、爆炸碎片等元素显著
- 强烈的"时间断层"感

**叙事用途**：
- **戏剧化高潮**：动作戏的"巅峰时刻"，子弹擦过、回头一击
- **超现实/科幻**：暗示角色拥有控制时间能力
- **戏仿/风格化**：电视广告、综艺、网络视频"假高科技感"
- **使用频率忠告**：极易过度使用变廉价，一部片用 1-2 次为上
- **经典参考**：《黑客帝国》原版命名场景；《300 勇士》大量使用；动画片如《超人总动员》

**英文模板**：
```
bullet time effect, frozen action, camera orbits around [subject] at normal speed while subject is in slow motion, [N] seconds
```

**中文模板**：
```
子弹时间效果，主体动作凝固，镜头以正常速度环绕[主体]，[N]秒
```

**完整示例**：
> A martial artist mid-air, kicking out his leg in slow motion. Bullet time effect, camera orbits around him at normal speed while his motion is frozen-slow, water droplets suspended in air around him. 4 seconds, cinematic, dramatic backlighting.

**参数维度**：
- 时间错位强度：`frozen action`（完全停止）/ `extreme slow motion`（极慢）
- 环绕弧度：`180 degree bullet time` / `360 degree`
- 元素：明确"凝固"的物件（雨、碎屑、灰尘等）增强效果

**易混淆**：
- AI 视频模型最难精确再现的运镜之一——主体真正凝固很罕见，常退化成"慢动作 + 环绕"
- 失败模式 1：环绕了但主体仍正常动作
- 失败模式 2：慢动作了但镜头也慢
- 抽卡建议：用 `Matrix-style bullet time` 这个具体引用增加命中率

---

## 21. 长镜头 / Long Take

**别名**：Oner / Continuous Take / 一镜到底
**机械动作**：单次曝光的连续拍摄，可包含多种运镜组合，时长显著超过常规镜头（30 秒到几分钟）
**难度**：⭐⭐⭐⭐ 困难（AI 视频模型单次输出长度有限：Seedance ~10 秒，Sora 几十秒；超出后画面失稳）

**画面**：
- 没有剪辑切换的连续画面
- 通常包含多种运镜变化（tracking、pan、tilt、push 等组合）
- 主体可能多次进出画面，事件连续发生
- 对场面调度极考究

**叙事用途**：
- **沉浸感**：让观众"和角色一起体验"事件，无剪辑切断
- **技术炫技**：电影/导演的标志性技巧
- **戏剧紧张**：复杂事件不让观众"喘气"
- **真实质感**：模仿现实"没有剪辑"的体验
- **经典参考**：《1917》全片伪一镜到底；《鸟人》全片伪连续；《俄罗斯方舟》真一镜到底 96 分钟

**英文模板**：
```
long take, continuous shot following [subject] through [multiple actions], no cuts, [N] seconds
```

**中文模板**：
```
长镜头，连续跟拍[主体]完成[多个动作]，无剪辑，[N]秒
```

**完整示例**：
> A waitress carries a tray through a crowded restaurant, weaving between tables, dropping off plates, taking new orders. Long take continuous shot following her over 12 seconds, camera tracks her smoothly while she navigates. No cuts, busy ambient sound, cinematic.

**参数维度**：
- 时长：AI 模型限制下通常 8-12 秒已是极限
- 复杂度：`single action long take`（单一行为）/ `complex long take`（多场景穿行）
- 设备暗示：通常 `steadicam` 配合最自然

**易混淆**：
- AI 视频里 "long take" 主要价值是**不要剪辑感**，而非真的拍很久
- 想模拟更长，建议 prompt 在多个相邻镜头里写 `seamless continuation of previous shot` 然后剪辑拼接

---

## 22. 第一人称 / POV

**别名**：Point of View / Subjective Camera / 主观镜头
**机械动作**：摄影机置于角色眼睛位置，画面就是角色看到的视野
**难度**：⭐⭐ 中等（语义清晰但 AI 易把 POV 误解为"角色面部特写"）

**画面**：
- 通常不见角色身体（最多见手/腿伸出画面下方）
- 画面运动模拟人类视线（转头、眨眼、聚焦切换）
- 视角高度通常 1.5-1.7 米（人眼平视高度）

**叙事用途**：
- **主观沉浸**：让观众"成为角色"，第一人称体验
- **威胁/恐怖**：从猎物视角看捕食者，或反之
- **角色限制视野**：让观众和角色一样"不知道全貌"
- **游戏感**：模仿 FPS 游戏视角
- **经典参考**：《奇爱博士》多次主观；《硬核亨利》全片 POV；恐怖片《死亡录像》系列

**英文模板**：
```
POV shot, first person perspective, [subject] sees [what they observe], camera at eye level, [N] seconds
```

**中文模板**：
```
第一人称视角，[主体]看到[内容]，相机在眼睛高度，[N]秒
```

**完整示例**：
> POV shot from a hiker's perspective. The view shows a narrow forest trail winding through tall pines. As the hiker walks forward, the trail curves to reveal a stunning waterfall. Slight natural head bobbing, eye-level perspective, 6 seconds, cinematic.

**参数维度**：
- 角色暗示：`from the perspective of [character]`
- 运动：通常配合 handheld 抖动（模拟走动）
- 视野限制：`tunnel vision` / `peripheral blur`（情绪化强调）

**易混淆**：
- AI 常把 "POV" 误解为"看着角色"而非"作为角色看"——明确 `from the perspective of` 或 `first person view`
- vs **OTS**：OTS 是越过肩膀看（第三人称），POV 是从眼睛看（第一人称）
- 别用 `selfie angle`（那是"自拍"视角，不是 POV）

---

## 23. 越肩镜头 / Over-the-Shoulder (OTS)

**别名**：OTS / Reverse Shot / 越肩
**机械动作**：摄影机置于一个角色（前景）的肩膀后方，拍摄另一个角色（背景）
**难度**：⭐⭐ 中等（构图清晰但 AI 对"肩膀框架"的呈现不一定准确）

**画面**：
- 前景：一个角色的肩膀和后脑（通常虚化或暗中）
- 背景：另一个角色面对镜头，是焦点
- 画面有明显的"对话感"——观众通过一个角色的视角看另一个

**叙事用途**：
- **对话场面标配**：双人对话的经典构图，正反打剪辑必备
- **关系揭示**：前景角色的肩膀位置/姿态暗示他们的关系
- **戏剧张力**：聚焦背景角色反应，前景角色"在场但不抢戏"
- **悬疑/威胁**：前景未知/危险角色 + 背景受害者反应
- **经典参考**：几乎所有有对话戏的电影；《辛德勒名单》多次精妙 OTS；《老无所依》对话场面

**英文模板**：
```
over-the-shoulder shot from [character A] looking at [character B], [character B's reaction/dialogue], [N] seconds
```

**中文模板**：
```
越肩镜头，从[角色A]肩膀看[角色B]，[角色B 的反应/对话]，[N]秒
```

**完整示例**：
> Over-the-shoulder shot from a man's perspective, looking across a café table at a woman who is reading a letter. His shoulder and back of head visible in foreground (out of focus), her face in focus showing surprised reaction. Warm afternoon light, 5 seconds, cinematic.

**参数维度**：
- 距离：`tight OTS`（紧贴肩膀）/ `wide OTS`（拉远）
- 焦点：`foreground out of focus, background sharp`
- 角度：`OTS from left shoulder` / `from right shoulder`

**易混淆**：
- vs **POV**：OTS 能看到前景角色的肩；POV 完全是第一人称
- AI 常把 OTS 渲染成单人镜头而忘了前景肩膀——明确 `with visible shoulder in foreground`
- 失败模式：背景角色变成普通 close-up，肩膀消失

---

## 24. 上帝视角 / Top-Down

**别名**：God's Eye / Bird's Eye / Overhead Shot / 顶视 / 垂直俯视
**机械动作**：摄影机垂直向下俯视（90 度向下），从正上方拍摄场景
**难度**：⭐ 简单（视觉特征极清晰，AI 易出活）

**画面**：
- 摄影机正对地面，主体从上往下看
- 失去深度感（无前后景，只有平面布局）
- 主体看起来"被困"或"被监视"

**叙事用途**：
- **抽离感**：将观众完全置于戏外，像看地图/棋盘
- **风格化签名**：Wes Anderson 大量使用、Stanley Kubrick 经典手法
- **特殊视角**：模仿监控/上帝视角的旁观
- **几何美学**：突出场景的对称布局、构图
- **示范类视频**：烹饪、手工、桌面演示
- **经典参考**：库布里克《闪灵》小孩骑车 + 多次顶视；Wes Anderson 几乎每部都用

**英文模板**：
```
top-down shot, camera directly overhead at 90 degrees, looking down at [subject/scene], [N] seconds
```

**中文模板**：
```
垂直俯视，相机在正上方90度向下拍摄[主体/场景]，[N]秒
```

**完整示例**：
> Top-down shot of a chef arranging ingredients on a wooden counter: chopped vegetables, herbs, raw fish. Camera directly overhead at 90 degrees, static, perfectly geometric composition, warm kitchen lighting, 6 seconds, cinematic.

**参数维度**：
- 高度：`directly overhead` / `slightly tilted from straight down`
- 状态：`static top-down` / `slowly descending top-down`（配合 crane down）
- 风格：`geometric / symmetrical composition`

**易混淆**：
- vs **High Angle**：top-down 是垂直 90 度；high angle 是 30-60 度俯视
- 想要"飘起来"感，用 `drone top-down view`；想要"监视"感，用 `surveillance top-down`
- AI 通常处理得好，但有时会渲染成 high angle 而非真正垂直

---

## 25. 固定镜头 / Static

**别名**：Static Shot / Locked Off / Fixed Camera / 定镜
**机械动作**：摄影机完全不动，画面构图不变，仅画面内主体/元素在动
**难度**：⭐ 简单（最基础的"无运镜"，但本身是重要的对照基准）

**画面**：
- 构图固定，焦距、位置、角度都不变
- 所有动态都来自画面内的主体（人物、物体、光影）
- 静与动的对比突出主体

**叙事用途**：
- **凝视/观察**：让观众安静地"看"，无任何运镜引导
- **舞台感/绘画感**：构图美学优先，每一帧像绘画
- **对照基准**：在大量运镜镜头中插入 static，形成节奏对比
- **窥视感**：监控摄像头风格，距离感
- **冥想节奏**：慢电影、艺术片常见
- **经典参考**：小津安二郎几乎全片 static + 低机位；Wes Anderson 大量 static；《波斯语课》多次静止镜头建立紧张

**英文模板**：
```
static shot, locked camera, no movement, [subject and action], [N] seconds
```

**中文模板**：
```
固定镜头，相机不动，[主体和动作]，[N]秒
```

**完整示例**：
> Static shot of an old woman sitting alone at a kitchen table, slowly stirring her tea. Camera locked, no movement at all, soft window light streaming in from the side, 8 seconds, cinematic, contemplative mood.

**参数维度**：
- 强调级别：`completely static` / `locked off camera, no shake at all`
- 配合：`+ no camera movement, only [subject] moves`

**易混淆**：
- AI 默认有时会加微小机位运动（即使写了 static），明确 `absolutely no camera movement` 或 `locked off, perfectly still`
- vs **Tripod Shot**：tripod 强调用了三脚架但**仍可能有 pan/tilt**；static 强调完全不动
- 想要"监控感"，加 `like a security camera`；想要"舞台感"，加 `theatrical, frontal composition`

---

# 运镜组合习惯

实际分镜很少是单一运镜，专业作品里常见的是**组合**（同时叠加）或**序列**（先后接续）。AI 视频里组合运镜尤其要小心——叠加越多越不稳定，超过 2 个就建议拆段落分别生成再剪辑。

## 一、常见双运镜叠加

### A. Dolly In + Tilt Down — "聚焦关键物件"

- **效果**：推近的同时低头，最终对准低位物件（桌上的信、地上的尸体、棺木内）
- **用途**：戏剧性揭示关键物件/证据/死亡
- **Prompt**：`slow dolly in while tilting down toward [object], reveal shot`
- **经典参考**：《指环王》戒指多次出现的推+俯；侦探片揭示凶器

### B. Crane Up + Tilt Down — "上帝视角揭示"

- **效果**：升起的同时俯视主体（保持主体在画面下半），最终俯瞰全景
- **用途**：结尾抽离 + 揭示场景全貌
- **Prompt**：`crane up while tilting down, ending in high angle overview of [scene]`
- **经典参考**：《卡萨布兰卡》结尾；许多战争片战场展示

### C. Tracking + Pan — "跟随的同时分散注意力"

- **效果**：跟拍主体移动，同时摇向旁边重要元素（对话对象/环境威胁）
- **用途**：在跟随中"提示注意力转移"，比单纯 tracking 信息密度高
- **Prompt**：`tracking shot following [subject] while panning right to reveal [secondary element]`
- **经典参考**：《好家伙》餐馆 long take 中多次

### D. Orbit + Rising — "螺旋戏剧化"

- **效果**：环绕主体同时机位逐渐升高，最终俯视主体
- **用途**：英雄亮相、关键时刻"升华"
- **Prompt**：`orbit shot around [subject] while slowly rising, ending in high angle`
- **经典参考**：超级英雄电影出场标配；商业广告"产品揭示"

### E. Push In + Rack Focus — "心理转折"

- **效果**：推近一个角色，同时焦点从前景元素切到他的眼睛
- **用途**：角色顿悟、内心变化的精确视觉化
- **Prompt**：`slow dolly in toward [character], rack focus from foreground object to their eyes`
- **经典参考**：心理剧、悬疑片关键瞬间

### F. Handheld + Whip Pan — "追逐转场"

- **效果**：手持跟拍中突然急摇，转到新对象/场景
- **用途**：动作戏的瞬间转移视线、风格化转场
- **Prompt**：`handheld following [subject A], sudden whip pan to [subject B]`
- **经典参考**：《疯狂的麦克斯》大量；动作片对峙戏

---

## 二、经典分镜序列（先后接续，需要剪辑拼接）

### 1. 三段式开场
1. **远景静止**（建立空间，2-3s） →
2. **缓慢推进**（聚焦主体，4-5s） →
3. **切到特写**（情绪锁定，3-4s）
- **用途**：电影/剧集开场标配；建立"哪里-谁-为什么"
- **AI 实践**：分别生成 3 段，剪辑拼接

### 2. 揭示式（Reveal）
1. **局部特写**（神秘物件、模糊轮廓，3s） →
2. **Dolly Out 或 Crane Up**（揭示更广背景，5s）
- **用途**：悬念解谜、戏剧反转
- **AI 实践**：用 dolly out 比 zoom out 出片质感更好

### 3. 紧张铺垫
1. **静止远景**（环境压抑，3s） →
2. **Push In**（缓慢推近角色，4s） →
3. **Dolly Zoom**（顿悟/恐惧瞬间，2s）
- **用途**：心理戏、惊悚片关键转折
- **AI 实践**：dolly zoom 是难点，可能要重抽多次

### 4. 追逐戏
1. **Handheld 跟拍**（角色奔跑，5-8s） →
2. **Whip Pan**（极快转场，1s） →
3. **切到追逐者视角**（OTS 或 POV，3-5s）
- **用途**：动作片、惊悚片
- **AI 实践**：whip pan 是难点，可能要 quick pan 代替

### 5. 抽离结尾
1. **角色特写**（情绪定格，4s） →
2. **Slow Crane Up**（缓慢升起，6s） →
3. **航拍远景**（最终全景，5s）
- **用途**：结尾告别、情感升华
- **AI 实践**：3 段分别生成、剪辑接续；最后航拍可独立用 drone shot

### 6. 关键道具引入
1. **Static 远景**（场景全貌，3s） →
2. **Rack Focus**（焦点切到前景道具，2s） →
3. **Push In**（推近道具特写，3s）
- **用途**：悬疑、解谜、reveal "原来这是关键"
- **AI 实践**：rack focus 是难点；可用 cut + zoom in 替代

---

## 三、AI 视频里的组合实践要点

1. **单段 AI 视频最多组合 2 个运镜**：超过就抽卡率飙升。三个以上的复杂运镜建议拆段拼接
2. **难度是叠加的**：⭐ + ⭐ 可能变 ⭐⭐；⭐⭐ + ⭐⭐⭐ 可能直接到 ⭐⭐⭐⭐
3. **prompt 写"主+次"顺序**：主要运镜先写，次要用 `while` 接续。例：`slow dolly in while tilting down`，不是 `tilt down and dolly in`
4. **运镜配景别变化要一致**：
   - 推/拉必然伴随景别变化（远→近 或 近→远）
   - 摇/横移景别基本不变
   - 升降可以两者
   - 环绕景别不变
   - **prompt 里别写矛盾**（如 "dolly in from medium to wide"—— dolly in 应该 to closer）
5. **学会拆 + 剪比硬塞 prompt 强**：复杂运镜组合，分段生成 + 剪辑拼接的成片质量远高于一次性生成。AI 视频时代的"分镜"思维 = 一段一个核心运镜
6. **组合前先单独试**：你想组合 A + B，先各自测一遍 AI 出活情况。两个都⭐再组合；一个⭐⭐⭐⭐就别想组合了
7. **常见踩坑**：
   - 同时写 dolly + zoom：AI 会蒙圈，要么变 dolly zoom（如果命中），要么乱
   - 同时写 handheld + steadicam：互斥概念，AI 不知道选哪个
   - 三个以上方向的运动：tilt up + pan right + dolly in，几乎必崩
