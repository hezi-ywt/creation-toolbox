---
description: 涉及单镜头时间感（慢动作 / 升降格变速 / 延时 / 凝固 / 反向）、镜头内节奏控制时加载。注意这是单镜头层面，整片节奏拆解看 narrative-economy.md。
---

# 节奏与时长

> 用途：可粘贴到 Seedance / 可灵 / Veo3 / Sora2 / Runway 等 AI 视频模型的节奏与时间控制参考库
> 状态：v0.3（8 条 + 节奏组合习惯）
> 数据：基于公开影视摄影/剪辑经验整理，难度评级为经验估计（非实测）
> 最后更新：2026-05-17

## 怎么用

1. **节奏 ≠ 剪辑**：这一份主要讲**单镜头内可控的时间感**（慢动作、变速、延时、凝固等），AI prompt 能直接传达
2. **单镜头时长**和**镜头内运动节奏**是 AI 视频 prompt 的核心可控变量
3. **剪辑节奏**（多镜头组合）发生在生成之后，但 prompt 仍能通过"暗示风格"影响——末尾会讲
4. 不同 AI 模型对时间操控支持差别大：**Sora 和 Veo 慢动作做得很好，Seedance 一般，Runway 中等**

**难度图例**（同前）：⭐ 简单 / ⭐⭐ 中等 / ⭐⭐⭐ 较难 / ⭐⭐⭐⭐ 困难

---

## 单镜头时长选择（写在条目前的总论）

AI 视频模型的输出时长各不相同：

| 模型 | 单次输出时长 | 适合 |
|---|---|---|
| Seedance | 5-10 秒 | 单一动作、短暂氛围 |
| 可灵 | 5-10 秒 | 单一动作、短氛围 |
| Veo3 | 8 秒 | 多一点动作但仍受限 |
| Sora2 | 5-60 秒 | 长镜头、复杂动作 |
| Runway Gen-4 | 5-10 秒 | 单一动作 |

**时长选择的经验法则**：
- **3-4 秒**：单一情绪（凝视、反应、特写定格）—— 节奏快剪用
- **5-6 秒**：单一动作（推近、走过、拿起）—— 默认主力
- **7-10 秒**：复合动作（多步骤）—— 给观众"看清"的时间
- **超 10 秒**：仅 Sora 等长输出模型支持，做小型 long take

**别迷信"越长越好"**：超过单一动作覆盖时长，AI 容易出"卡帧、姿态突变、物理崩坏"。复杂场景拆段生成 + 剪辑拼接质量更高。

---

## 索引

| # | 中文 | English | 核心特征 | 难度 |
|---|---|---|---|---|
| 1 | 慢动作 | Slow Motion | 主体动作慢于正常 | ⭐ |
| 2 | 快动作 / 加速 | Fast Motion / Speed Up | 主体动作快于正常 | ⭐⭐ |
| 3 | 升降格变速 | Speed Ramp | 镜头内速度变化 | ⭐⭐⭐ |
| 4 | 延时摄影 | Time-Lapse | 极快速展示长时间过程 | ⭐⭐ |
| 5 | 超延时 | Hyperlapse | 延时 + 机位移动 | ⭐⭐⭐ |
| 6 | 凝固 | Freeze Frame | 画面瞬间静止 | ⭐⭐⭐ |
| 7 | 反向 / 倒放 | Reverse / Backwards | 时间反向播放 | ⭐⭐ |
| 8 | 镜头内节奏 | Pacing within Shot | 加速 / 减速 / 匀速 | ⭐⭐ |

---

## 1. 慢动作 / Slow Motion

**别名**：Slo-Mo、High-Speed Footage、慢镜头、升格
**机制**：实拍用高帧率（60/120/240fps）拍摄，按 24fps 播放时变慢；AI 视频里直接 prompt 指定
**难度**：⭐ 简单（AI 极擅长慢动作，是出"高级感"的杀手锏之一）

**画面**：
- 主体动作明显慢于现实（1/2 速度到 1/10 速度）
- 物理细节被放大：水珠飞溅、衣物飘动、烟雾扩散、爆炸碎屑
- 表情瞬间被拉长，情绪被"凝视"
- 通常配合柔光、cinematic 调性

**叙事用途**：
- **戏剧化高潮**：动作戏、暴力、爆炸、运动巅峰
- **情绪强化**：眼泪滴落、第一次见面的"那一刻"
- **诗意美感**：水滴、烟雾、毛发、织物的运动
- **风格化签名**：Zack Snyder 大量；运动品牌广告必用
- **经典参考**：《300 勇士》大量慢动作；《黑客帝国》子弹慢动作；耐克广告标配

**英文模板**：
```
slow motion shot of [subject and action], [N]x speed, high-speed footage aesthetic, [duration] seconds
```

**中文模板**：
```
[主体和动作]的慢动作镜头，[N]倍慢速，升格质感，[时长]秒
```

**完整示例**：
> Slow motion shot of a martial artist mid-spin kick, his hair and clothing flowing dramatically. 4x slow motion, water droplets suspended in air around him, sharp focus on his face, 5 seconds, cinematic, high-speed footage aesthetic.

**参数维度**：
- 速度：`2x slow` / `4x slow` / `8x slow` / `extreme slow motion`
- 风格：`cinematic slow mo` / `sports slow mo` / `dreamy slow mo`
- 配合：常配 `dramatic lighting` / `water droplets` / `flowing fabric` 强化质感

**易混淆**：
- AI 用 `slow motion` 命中率极高
- 强度过高会"假"：`extreme slow motion` 偶尔变成卡顿——`smooth slow motion` 更稳
- vs **Freeze Frame**：slow mo 仍在运动只是慢；freeze 是完全静止

---

## 2. 快动作 / Fast Motion

**别名**：Sped Up、Time-Lapse（窄义，专指自然过程）、Undercranking、降格
**机制**：低帧率拍摄按 24fps 播放变快；AI 视频里 prompt 指定加速
**难度**：⭐⭐ 中等（不如慢动作受欢迎，AI 偶尔渲染成"机械感动作"）

**画面**：
- 主体动作明显快于现实（2-10 倍速度）
- 步行变小跑、人群在画面里"快速流动"
- 云、汽车、人流的快速流动美感
- 喜剧或紧迫感

**叙事用途**：
- **喜剧 / 滑稽**：让普通动作变滑稽（早期默片质感）
- **紧迫感**：交叉剪辑里突出"时间紧"
- **效率展示**：烹饪、装修、化妆教程的过程加速
- **流动美感**：街道人流、云、车流的快速涌动
- **经典参考**：早期默片大量；《本杰明巴顿奇事》多次加速；纪录片自然类（云）

**英文模板**：
```
fast motion shot of [subject and action], sped up [N]x, [duration] seconds
```

**中文模板**：
```
[主体和动作]的快动作镜头，[N]倍加速，[时长]秒
```

**完整示例**：
> Fast motion shot of a busy intersection at dusk, people and cars sped up 8x. Pedestrians flowing like streams, cars leaving light trails, sky transitioning from day to night. 6 seconds, urban time-lapse aesthetic.

**参数维度**：
- 速度：`2x faster` / `4x faster` / `8x faster` / `time-lapse speed`
- 用法：`comedic fast motion`（喜剧风）/ `urgent sped up`（紧迫感）

**易混淆**：
- vs **Time-Lapse**：fast motion 通常用于普通动作的加速；time-lapse 专指"长时间自然过程压缩"（云、植物、星空）
- AI 偶尔渲染成"机械感卡顿动作"——加 `smooth fast motion` 缓解

---

## 3. 升降格变速 / Speed Ramp

**别名**：Speed Ramp、Variable Speed、Slo-Mo to Real-time、变速
**机制**：镜头内速度变化（如先正常 → 突然慢 → 突然快）
**难度**：⭐⭐⭐ 较难（AI 视频对镜头内速度变化的精控目前较弱）

**画面**：
- 镜头内速度发生变化
- 经典模式：正常 → 关键瞬间慢 → 恢复正常
- 或：正常 → 加速冲过 → 突然慢下凝固
- 强烈的节奏感、戏剧张力

**叙事用途**：
- **强调关键瞬间**：正常速度跑过来 → 关键时刻慢动作 → 击中目标
- **戏剧节奏**：在快慢之间制造"心跳"
- **风格化签名**：Zack Snyder、《疯狂的麦克斯》标志运动
- **运动 MV / 体育片**：扣篮的腾空慢 + 落地正常
- **经典参考**：《300 勇士》大量 speed ramp；《疯狂的麦克斯》追逐戏；现代运动广告

**英文模板**：
```
speed ramp shot of [subject], real-time to slow motion on [key moment] back to real-time, [duration] seconds
```

**中文模板**：
```
[主体]的变速镜头，正常速度到[关键瞬间]慢动作再回正常，[时长]秒
```

**完整示例**：
> Speed ramp shot of a basketball player taking a shot. Real-time as he jumps, dramatic slow motion at the peak of his arc as the ball leaves his hand (water droplets in air), back to real-time as the ball swooshes through the net. 6 seconds, cinematic, sports aesthetic.

**参数维度**：
- 模式：`real-time → slow → real-time`（最经典）/ `slow → real-time → slow`（反向，少见）
- 关键瞬间描述：`slowing down at [key moment description]`

**易混淆**：
- AI 视频里 speed ramp 精控难度高——多数模型只支持"全片同速"
- 实践上：分段生成（正常段 + 慢动作段），后期剪辑拼接更稳
- 失败模式：AI 渲染成全片慢动作 or 全片正常速度

---

## 4. 延时摄影 / Time-Lapse

**别名**：Timelapse、加速摄影、缩时
**机制**：以极低帧率拍摄（每秒拍 1 帧或更少），按 24/30fps 播放
**难度**：⭐⭐ 中等（AI 视频对长时间过程压缩有支持，但效果不一）

**画面**：
- 长时间过程被压缩到短短几秒
- 经典对象：云、星空、日出日落、植物生长、人流车流、施工
- 时间感被极端压缩，平静的事物变流动
- 通常配合广角 / 静态机位

**叙事用途**：
- **过程压缩**：建造、烹饪、化妆、艺术创作的全过程
- **自然壮丽**：云的流动、星空的旋转、四季的更替
- **都市感**：车流的光带、人潮的流动
- **过渡 / 蒙太奇**：在两个场景间表达"时间过去了"
- **经典参考**：《Koyaanisqatsi》全片延时；纪录片自然/城市类大量；纪录片《地球脉动》

**英文模板**：
```
time-lapse of [scene/process], [duration of real time] compressed into [N] seconds, static camera
```

**中文模板**：
```
[场景/过程]的延时摄影，[实际时间]压缩到[N]秒，固定机位
```

**完整示例**：
> Time-lapse of clouds moving across a mountain valley from dawn to noon. Static camera, soft sunlight progressing through the scene, shadows shifting across the slopes, fog rising and dissipating. 8 seconds time-lapse, cinematic nature documentary aesthetic.

**参数维度**：
- 对象：`clouds` / `stars` / `traffic` / `growing plant` / `sunset to night`
- 机位：通常 `static camera`（机位移动版本是 Hyperlapse）
- 时长：`several hours compressed into 8 seconds` 等具体描述

**易混淆**：
- vs **Hyperlapse**：time-lapse 机位静止；hyperlapse 机位移动
- AI 对 time-lapse 处理参差——具体的对象描述（"clouds moving fast"）比抽象的 "time-lapse" 更稳
- 失败模式：AI 仅给"快速版本"而非"长时间压缩感"

---

## 5. 超延时 / Hyperlapse

**别名**：Hyperlapse、Motion Time-Lapse、行走延时
**机制**：延时摄影 + 机位有规律移动（推、拉、横移）
**难度**：⭐⭐⭐ 较难（机位移动 + 时间压缩的双重控制）

**画面**：
- 时间被压缩（同 time-lapse）
- 机位有持续运动（前进、绕物体一圈、上升等）
- 环境飞速变化（云在跑、太阳在动）同时机位也在移动
- 强烈的"穿越时空"感

**叙事用途**：
- **穿越展示**：城市探索、自然徒步
- **建筑环绕**：在建筑周围转一圈展示
- **诗意旅行**：旅行片头
- **音乐 MV**：现代流行风
- **经典参考**：网络旅游短片大量；现代音乐 MV；汽车广告

**英文模板**：
```
hyperlapse, time-lapse with moving camera, [camera motion] around [scene], [N] seconds
```

**中文模板**：
```
超延时，延时摄影 + [机位运动]，绕[场景]运动，[N]秒
```

**完整示例**：
> Hyperlapse around a futuristic skyscraper at sunset. Camera orbits the building over what represents several hours, sun setting and city lights turning on during the orbit, cars below leaving streaks. 8 seconds, cinematic, urban time-lapse aesthetic.

**参数维度**：
- 机位运动：`walking hyperlapse` / `orbiting hyperlapse` / `forward hyperlapse`
- 时间跨度：明确"什么变化"如 sunset to night

**易混淆**：
- AI 难精控 hyperlapse——`walking time-lapse with sky changing` 比抽象的 `hyperlapse` 更稳
- vs **Drone Time-Lapse**：drone time-lapse 是航拍版的 hyperlapse

---

## 6. 凝固 / Freeze Frame

**别名**：Freeze Frame、Still Frame、Frozen Moment、定格
**机制**：画面在某瞬间完全静止（运动停止），其他元素可能仍在动或全停
**难度**：⭐⭐⭐ 较难（与 bullet time 相关，AI 难做"主体凝固而镜头/环境继续动"）

**画面**：
- 主体的动作在某一帧定格
- 可能整个画面都凝固（最简单），或只有主体凝固而镜头/环境继续动（bullet time 风）
- 强烈的"时间停止"感

**叙事用途**：
- **戏剧化标点**：关键瞬间凝固让观众"凝视"
- **章节结束 / 命运点**：常用作场景结尾
- **回忆 / 倒叙**：从凝固画面开始倒叙
- **戏仿 / 风格**：早期电视剧标志（每集结尾凝固）
- **经典参考**：《四百击》经典结尾凝固镜头；80 年代电视剧片头标配；《角斗士》多场凝固

**英文模板**：
```
freeze frame at [moment description], action stops mid-motion, [N] seconds
```

**中文模板**：
```
在[瞬间描述]时凝固，动作中途停止，[N]秒
```

**完整示例**：
> A boy running on a beach in slow motion, then freeze frame at the exact moment his foot touches the wet sand mid-stride. He remains perfectly still while gulls continue to fly through the frame and waves wash behind him. 5 seconds total, cinematic.

**参数维度**：
- 凝固范围：`everything freezes` / `only [subject] freezes while environment moves`
- 时机：明确凝固的具体瞬间

**易混淆**：
- AI 视频里"凝固"难精确实现——简化做法是用慢动作模拟（`extreme slow motion approaching freeze`）
- vs **Bullet Time**（见 [运镜.md 第 20 条](运镜.md)）：bullet time 是"凝固 + 镜头环绕"的合成；freeze frame 是单纯静止
- 失败模式：AI 渲染成普通定格画面（无运动元素）—— 加 `subject frozen while environment continues to move`

---

## 7. 反向 / Reverse / Backwards

**别名**：Reverse Motion、Backwards Playback、倒放
**机制**：画面时间反向播放
**难度**：⭐⭐ 中等

**画面**：
- 所有动作反向：水从地上回到杯里、人物倒退着走、烟雾收回
- 物理反常感强烈
- 极易识别（任何观众都能看出来）

**叙事用途**：
- **超现实**：梦境、回忆、魔法
- **创意广告**：吸引眼球的反常感
- **意味深长**：暗示"时间倒流"的隐喻
- **音乐 MV**：风格化创意
- **经典参考**：《盗梦空间》梦境段落；《本杰明巴顿奇事》倒着活；OK Go 多个反向 MV

**英文模板**：
```
reverse motion shot of [subject and action played backwards], [duration] seconds
```

**中文模板**：
```
[主体动作]的反向镜头，反向播放，[时长]秒
```

**完整示例**：
> Reverse motion shot of broken glass reassembling itself. Pieces of a shattered wine glass on the floor leap upward and reconstruct into a whole glass on the table, red wine flowing back into it. 4 seconds, surreal, cinematic.

**参数维度**：
- 描述：`played in reverse` / `time flowing backwards` / `rewind effect`
- 配合：常配 `surreal` / `dreamlike` 等氛围词

**易混淆**：
- AI 用 `reverse motion` 或 `backwards playback` 命中率不错
- 失败模式：AI 渲染了正向动作 + 文字标"reverse"——明确 `physical objects moving backwards in time`

---

## 8. 镜头内节奏 / Pacing within Shot

**别名**：Internal Pacing、Beat within Shot、镜头内速度变化
**机制**：单镜头内的运动节奏控制——加速、减速、匀速、停顿
**难度**：⭐⭐ 中等（不是单独的效果而是"运镜节奏的描述"）

**画面**：
- **匀速**：稳定、可预测，平静感（默认）
- **加速 (accelerating)**：从慢到快，紧迫感、戏剧感
- **减速 (decelerating / ease out)**：从快到慢，沉思、定格前奏
- **停顿 (pause / hold)**：到某点突然停止再继续

**叙事用途**：
- **加速**：揭示瞬间的接近、追逐戏的"扑面而来"
- **减速**：到达某点的"凝重"、戏剧化定格前的预备
- **匀速**：观察、纪实、客观
- **停顿**：呼吸节奏、悬念
- **经典参考**：希区柯克电影大量"减速到凝重"；《教父》多次推近"渐慢到 close-up 凝重"

**英文模板**：
```
[运镜], pacing: [accelerating / decelerating / smooth constant / with hold], [N] seconds
```

**中文模板**：
```
[运镜]，节奏：[加速/减速/匀速/带停顿]，[N]秒
```

**完整示例**：
> Slow dolly in toward an elderly man's face. Pacing: decelerating—starts at medium speed, gradually slows down until almost still at the final close-up, holds for the last second on his solemn expression. 6 seconds, cinematic, contemplative.

**参数维度**：
- 模式：`accelerating` / `decelerating / ease out` / `smooth constant` / `with mid-hold`
- 强度：`subtle acceleration` / `dramatic deceleration`

**易混淆**：
- AI 默认"匀速"——想要加速/减速必须明确
- 简单写法：`slowly` → `quickly` 等副词偶尔比 `accelerating` 更稳
- 配合 hold（停顿）效果很强：`dolly in then hold on close-up`

---

# 三、剪辑节奏（多镜头组合）的暗示

剪辑节奏发生在 AI 生成之后（用户自己剪），但 **prompt 仍能通过"风格暗示"影响单镜头特征**，使其适合慢剪或快剪。

## A. 慢节奏剪辑（Slow Pacing）

**特点**：
- 单镜头时长 6-15 秒
- 镜头内运动慢、构图静（static / slow movement）
- 镜头之间不切换太频繁

**适合**：文艺片、历史片、悬疑铺垫、纪录片

**Prompt 暗示**（生成时让镜头"适合慢剪"）：
```
slow contemplative pacing, long take feel, static or slow camera, 8 seconds
```

**经典参考**：塔可夫斯基、伯格曼、阿巴斯、是枝裕和

---

## B. 快节奏剪辑（Fast Pacing）

**特点**：
- 单镜头时长 1-3 秒
- 镜头内冲击力强（快运动、强构图）
- 镜头之间高速切换

**适合**：动作片、广告、音乐 MV、追逐戏、喜剧

**Prompt 暗示**（生成时让镜头"适合快剪"）：
```
dynamic energetic shot, strong composition for quick cut, 2 seconds
```

**经典参考**：迈克尔·贝、保罗·格林格拉斯（《谍影重重》）；MTV 风格 MV；现代广告

---

## C. Match Cut（视觉连续剪辑）

**特点**：
- 两个镜头之间通过"视觉相似性"无缝衔接
- 形状、运动方向、构图位置匹配
- 给观众"流畅过渡"的快感

**适合**：所有题材，是剪辑的"高级技巧"

**Prompt 暗示**（为 match cut 预生成镜头）：
```
shot 1: [subject A] action ending in [specific shape/motion]
shot 2: [subject B] starting in [same shape/motion at same screen position]
```

**经典 match cut**：《2001 太空漫游》猿人骨头 → 太空船（最经典）；《阿拉伯的劳伦斯》火柴 → 沙漠日出

---

# 四、AI 视频的节奏踩坑

1. **慢动作 AI 极擅长，但别过度堆叠**：8x slow 偶尔变卡顿——`smooth cinematic slow motion` 更稳
2. **快动作 AI 偶尔出"卡帧"**：加 `smooth fast motion` 或具体描述（`time-lapse style`）
3. **Speed ramp 精控难**：实践上拆段生成 + 后期变速更可控
4. **Freeze frame 真正"凝固"难**：用 `extreme slow motion almost stopping` 替代更稳
5. **Time-lapse vs Fast Motion 别混**：time-lapse 暗示"长时间过程压缩"（云、星空）；fast motion 是动作单纯加速
6. **超 10 秒慎用**：除非 Sora/Veo 长输出模型，否则物理崩坏概率高
7. **慢动作配景别**：慢动作 + close-up 最易出片；慢动作 + wide shot 易显假
8. **节奏要服务叙事**：所有动作戏都慢动作就廉价；关键时刻才用

---

# 五、完整 prompt 框架（v0.3 通用基础齐全后）

到 v0.3 通用基础 4 份齐了：**运镜 / 镜头景别与角度 / 光线 / 构图与景深 / 节奏与时长**。完整框架：

```
[角度] [景别] of [主体], [构图], [光线], [景深], [运镜 + 节奏], [N] seconds, [总风格]
```

**完整示例**：

1. **慢动作仰视近景**：
   > `low angle close-up of warrior, leading lines composition, golden hour backlit, shallow depth of field, slow dolly in with deceleration, 6 seconds, epic cinematic, slow motion fabric flowing`

2. **延时建筑全景**：
   > `eye level wide shot of city, three-layer composition, blue hour to night transition, deep focus, hyperlapse orbit, 8 seconds, cinematic urban`

3. **快剪运动单镜**：
   > `low angle medium shot of basketball player, dynamic composition, harsh midday sunlight, shallow depth, fast motion with freeze on peak, 3 seconds, sports commercial style`

4. **凝视长镜**：
   > `eye level medium close-up of elderly monk, centered composition, candlelight chiaroscuro, shallow depth of field, static camera, 8 seconds, contemplative slow pacing, painterly`

**5-8 修饰词最佳**，超过 10 个抽卡率明显升高。
