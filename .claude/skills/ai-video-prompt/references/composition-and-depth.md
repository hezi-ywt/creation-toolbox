---
description: 决定画面元素布局（三分 / 对称 / 引导线 / 框架 / 负空间）和虚实关系（浅深景深 / 散景）时加载。
---

# 构图与景深

> 用途：可粘贴到 Seedance / 可灵 / Veo3 / Sora2 / Runway 等 AI 视频模型的构图 + 景深参考库
> 状态：v0.3（12 条 + 组合习惯）
> 数据：基于公开影视摄影/绘画构图经验整理，难度评级为经验估计（非实测）
> 最后更新：2026-05-17

## 怎么用

1. **构图 = 画面元素如何布局**（主体在哪、其他元素怎么衬托）；**景深 = 前后景的虚实关系**
2. 构图是 AI 视频里**最容易出"AI 味"的地方**——多数模型默认中心构图，不写就会千篇一律
3. 景深是控制"画面注意力"的核心工具，**浅景深是 AI 视频的最佳出片杀手锏之一**
4. 这一份里很多构图原则在 AI 视频里**难以完全精确执行**（比如严格三分法），把它们当"风格倾向"而不是"几何约束"

**难度图例**（同前）：⭐ 简单 / ⭐⭐ 中等 / ⭐⭐⭐ 较难 / ⭐⭐⭐⭐ 困难

---

## 索引

### 一、构图原则

| # | 中文 | English | 核心特征 | 难度 |
|---|---|---|---|---|
| 1 | 三分法 | Rule of Thirds | 主体在 1/3 交点 | ⭐⭐ |
| 2 | 中心构图 | Central Composition | 主体在正中 | ⭐ |
| 3 | 对称构图 | Symmetrical | 左右镜像或上下镜像 | ⭐⭐⭐ |
| 4 | 引导线 | Leading Lines | 线条引导视线到主体 | ⭐⭐⭐ |
| 5 | 框架构图 | Frame within Frame | 前景框包围主体 | ⭐⭐⭐ |
| 6 | 负空间 | Negative Space | 大量留白突出主体 | ⭐⭐ |
| 7 | 三角构图 | Triangular | 三个元素形成三角 | ⭐⭐ |
| 8 | 层次构图 | Foreground / Midground / Background | 三层空间纵深 | ⭐⭐ |

### 二、景深与焦点

| # | 中文 | English | 核心特征 | 难度 |
|---|---|---|---|---|
| 9 | 浅景深 | Shallow Depth of Field | 主体清晰，背景模糊 | ⭐ |
| 10 | 深景深 | Deep Depth of Field | 前后全清晰 | ⭐⭐ |
| 11 | 选择性对焦 | Selective Focus | 只对焦在特定位置 | ⭐⭐ |
| 12 | 散景 | Bokeh | 背景光斑虚化美 | ⭐ |

**注**：拉焦（Rack Focus，焦点切换）已在 [运镜.md 第 17 条](运镜.md) 详述。

---

# 一、构图原则

## 1. 三分法 / Rule of Thirds

**别名**：三分构图、九宫格、Phi Grid（黄金分割的近似）
**画面定义**：将画面纵横各分为三等份，主体放在 4 个交点或沿着线条
**难度**：⭐⭐ 中等（AI 难精确放在交点，但可以"偏置"主体）

**画面**：
- 画面被分为 9 个等分（3×3 网格）
- 主体不在正中，而在 4 个"力点"（黄金交点）之一
- 地平线放在上 1/3 或下 1/3 线上（不要正中）
- 整体感觉自然、有"动感"

**叙事用途**：
- **专业感**：摄影/电影的"默认正确构图"
- **视线引导**：观众视线自然落在力点
- **避免呆板**：相比中心构图更有活力
- **留白意义**：偏置主体后另一侧的空间承载意义
- **经典参考**：摄影教科书第一课；几乎所有专业风景摄影；纪录片/新闻摄影

**英文模板**：
```
rule of thirds composition, [subject] positioned at upper-left / upper-right / lower-left / lower-right intersection, [N] seconds
```

**中文模板**：
```
三分法构图，[主体]放在[左上/右上/左下/右下]力点，[N]秒
```

**完整示例**：
> Rule of thirds composition: a fisherman silhouette positioned at the lower-right intersection, vast sea horizon along the lower third line, big sky filling upper two-thirds with golden sunrise clouds. 6 seconds, cinematic.

**易混淆**：
- AI 模型对三分法理解参差——更稳的写法是描述具体位置（"subject in lower-right area"）而非抽象的 "rule of thirds"
- vs **黄金分割**（Golden Ratio）：黄金分割位置比三分法略偏中心；视觉上区别小，AI 都搞不清楚——直接写 `rule of thirds` 简单实用
- 失败模式：AI 仍把主体放正中——加强表述 `subject off-center, NOT in middle`

---

## 2. 中心构图 / Central Composition

**别名**：Centered Composition、Symmetrical Center、对称中心
**画面定义**：主体在画面正中央，周围对称或均匀
**难度**：⭐ 简单（AI 默认就是中心构图）

**画面**：
- 主体严格居中
- 通常配合对称背景（道路、走廊、对称建筑）
- 给人庄严、稳定、仪式感
- 可能显得"呆"，但用得对很强力

**叙事用途**：
- **庄严仪式**：婚礼、宗教、葬礼
- **戏剧凝视**：角色直视镜头的关键时刻
- **风格化签名**：Wes Anderson 大量使用、Stanley Kubrick 经典中心构图
- **悬疑威胁**：单一角色在画面正中带来"被监视"感
- **经典参考**：Wes Anderson 每部都有；《2001 太空漫游》多次中心；《闪灵》Danny 骑车走廊镜头

**英文模板**：
```
centered composition, [subject] in exact middle of frame, symmetrical surroundings, [N] seconds, cinematic
```

**中文模板**：
```
中心构图，[主体]在画面正中，对称背景，[N]秒，电影感
```

**完整示例**：
> Centered composition: a young monk standing in exact middle of frame, long temple corridor stretching symmetrically behind him on both sides, ornate red doors at the end. 6 seconds, cinematic, ceremonial mood.

**易混淆**：
- AI **默认就是中心构图**——所以反而要写"非中心"才能改变
- 想要 Wes Anderson 风：明确 `symmetrical centered composition, Wes Anderson style`
- 想要库布里克风：`Kubrick one-point perspective, centered composition`（注意 one-point perspective 是配套的"单点透视"，对称走廊感）

---

## 3. 对称构图 / Symmetrical

**别名**：Mirror Composition、Bilateral Symmetry、镜像构图
**画面定义**：画面以中轴线（垂直/水平）镜像对称
**难度**：⭐⭐⭐ 较难（AI 难精确执行严格对称，常出"近似对称"）

**画面**：
- 左右镜像（最常见）或上下镜像（水中倒影）
- 强烈的几何美感
- 强调秩序、平衡、完美
- 偶尔配合主体打破对称（戏剧张力）

**叙事用途**：
- **完美 / 秩序**：建筑摄影、礼仪、设计感
- **风格化签名**：Wes Anderson 招牌；库布里克
- **倒影场景**：湖面、雨后路面、玻璃
- **戏剧反讽**：完美对称中的不完美个体（孤独感）
- **经典参考**：Wes Anderson 几乎所有镜头；库布里克 one-point perspective 大量；《卧虎藏龙》竹林戏

**英文模板**：
```
symmetrical composition, mirror image left-to-right, [subject] at center, Wes Anderson style, [N] seconds
```

**中文模板**：
```
对称构图，左右镜像，[主体]居中，韦斯安德森风格，[N]秒
```

**完整示例**：
> Symmetrical composition of a hotel lobby: ornate doors centered, identical chandeliers on left and right, perfectly mirrored chairs and decorations, a bellboy standing in the exact middle wearing a red uniform. 6 seconds, Wes Anderson aesthetic.

**易混淆**：
- AI 难做"严格对称"，多数是"近似对称"——加 `perfectly symmetrical, mirror image` 强化
- vs **Central**：中心构图只要求主体居中；对称要求整个画面镜像
- 倒影对称（水面/玻璃）效果好：`subject and its reflection, perfect water reflection`

---

## 4. 引导线 / Leading Lines

**别名**：Leading Lines、Compositional Lines、视线引导线
**画面定义**：画面中的线条（道路、铁轨、河流、栏杆、视线）引导观众视线到主体
**难度**：⭐⭐⭐ 较难（需要场景配合，AI 不一定能精确执行"线条指向主体"）

**画面**：
- 明显的线条元素：道路、河流、铁轨、栏杆、桥、走廊
- 线条从画面前景延伸到主体或远景焦点
- 透视感强（线条远端汇聚）
- 主体在线条终点或交汇处

**叙事用途**：
- **强化纵深**：道路、河流通向远方主体
- **聚焦主体**：观众视线自然被线条带到目标
- **路途感**：旅程、追寻、归途
- **建筑/几何美**：现代建筑大量使用
- **经典参考**：《这个杀手不太冷》街景引导；《阿拉伯的劳伦斯》沙漠中的脚印；公路片大量

**英文模板**：
```
leading lines composition, [line element] guiding eye toward [subject], strong perspective, [N] seconds, cinematic
```

**中文模板**：
```
引导线构图，[线条元素]将视线引向[主体]，强透视感，[N]秒，电影感
```

**完整示例**：
> Leading lines composition: a long empty country road stretching from foreground to distant horizon, vanishing point at the silhouette of a lone traveler walking away. Strong perspective, golden hour light, 7 seconds, cinematic, journey mood.

**易混淆**：
- AI 抽象的 "leading lines" 命中率不高——具体描述线条元素更稳，如 `long road from foreground to distant subject`
- 强化透视感：`vanishing point at [subject]` 帮 AI 理解线条汇聚
- 失败模式：AI 渲染了线条但与主体位置不一致——多次抽卡或调整 prompt

---

## 5. 框架构图 / Frame within Frame

**别名**：Frame within Frame、Natural Frame、嵌套框
**画面定义**：用前景元素（门、窗、洞、树枝）"框住"主体
**难度**：⭐⭐⭐ 较难（需要前景元素配合，AI 偶尔会忽略框架）

**画面**：
- 前景有明显的"框"：门、窗、拱门、树枝拱形、洞、镜子边
- 主体在框内（远处或中景）
- 框通常较暗（暗框 + 亮主体的对比）
- 给人"窥探"、"被引导观看"感

**叙事用途**：
- **窥视感**：暗示偷窥、监视、私密
- **意义层次**：框暗示"另一个世界"或"边界"
- **强化主体**：框把视线锁定在中心
- **风格化美感**：建筑摄影、东方山水画感
- **经典参考**：《教父》多次门框；《色,戒》窗框；中国山水画大量用框窗

**英文模板**：
```
frame within frame composition, [subject] framed by [foreground frame element], [N] seconds, cinematic
```

**中文模板**：
```
框架构图，[主体]被[前景框架]框住，[N]秒，电影感
```

**完整示例**：
> Frame within frame composition: a young woman seen through a doorway from inside a dark room, her figure framed by the door's silhouette. Bright sunlight outside, dim foreground, soft shadows. 6 seconds, cinematic, voyeuristic mood.

**易混淆**：
- AI 用具体框架词更稳：`framed by doorway` / `seen through window` / `archway frames the subject`
- 失败模式：AI 给了框但主体不在框内中心——明确 `subject centered within the frame`
- vs **OTS**（越肩）：OTS 用肩膀做"半框"；frame within frame 用全围合的物理框架

---

## 6. 负空间 / Negative Space

**别名**：Negative Space、Empty Space、留白
**画面定义**：画面大部分是空白/单调区域，主体只占很小比例，"空"主导
**难度**：⭐⭐ 中等

**画面**：
- 主体占画面 10-30%（甚至更小）
- 其余 70-90% 是"空"：天空、海面、墙、雾、雪、纯色背景
- 极简美学
- 给人孤独、空灵、深思感

**叙事用途**:
- **孤独 / 渺小**：人物在巨大空白中
- **极简美学**：现代设计感、东方水墨意境
- **冥想 / 哲思**：让观众"凝视空白"
- **强化主体**：大量空让小主体更突出
- **经典参考**：中国水墨画"留白"传统；《荒野猎人》大量雪景留白；《2046》空间留白

**英文模板**：
```
negative space composition, [subject] small in vast emptiness, minimalist, [N] seconds, cinematic
```

**中文模板**：
```
负空间构图，[主体]在大量留白中很小，极简风，[N]秒，电影感
```

**完整示例**：
> Negative space composition: a single small figure walking across a vast snow field, occupying only the lower-left tenth of the frame. The rest is white emptiness fading into pale gray sky. 7 seconds, cinematic, minimalist, lonely mood.

**易混淆**：
- vs **EWS**（极远景）：EWS 是"景别"概念（主体小）；negative space 是"构图"概念（空主导意义）——常一起用
- 强化"空"的元素：`vast empty [sky/sea/wall/snow]`，AI 才知道留白是什么

---

## 7. 三角构图 / Triangular Composition

**别名**：Triangle Composition、Pyramid Composition、三角形构图
**画面定义**：画面主要元素形成三角形（三人、三个元素、底宽顶尖的金字塔形）
**难度**：⭐⭐ 中等（多人场面常用，AI 可控但易出"三人随机散乱"）

**画面**：
- 三个主要元素的位置组成三角形
- 经典：底宽顶尖（稳定感）/ 倒三角（紧张感）
- 古典油画大量使用（圣母与圣婴的三角群像）
- 给人稳定、平衡、戏剧化群像感

**叙事用途**：
- **群像戏**：三人对话、家庭照、团队组合
- **稳定感**：底宽顶尖的金字塔感强化主体威严
- **戏剧张力**：三角关系（爱情三角、对峙三角）
- **古典美**：致敬文艺复兴绘画
- **经典参考**：达芬奇《最后的晚餐》（中心三角）；古典油画大量；《教父》家庭照三角群像

**英文模板**：
```
triangular composition, three main elements forming a triangle, [subjects] arranged in triangle, [N] seconds, cinematic
```

**中文模板**：
```
三角构图，三个主要元素形成三角，[主体们]按三角排布，[N]秒，电影感
```

**完整示例**：
> Triangular composition: three people sitting around a campfire at night. The tallest figure at the back center forming the apex, two seated figures at front-left and front-right forming the base. Warm firelight illuminating their faces. 6 seconds, cinematic, intimate mood.

**易混淆**：
- AI 抽象的 "triangular composition" 命中率一般——描述具体位置更稳：`one person standing behind, two seated in front, forming triangle`
- 倒三角（顶宽底尖）效果："inverted triangular composition, unstable feeling"

---

## 8. 层次构图 / Foreground / Midground / Background

**别名**：Three-Layer Composition、Depth Layers、纵深层次
**画面定义**：画面有清晰的前景 / 中景 / 远景三层，形成纵深感
**难度**：⭐⭐ 中等（AI 视频极有效的"出片质感"杀手锏）

**画面**：
- **前景**：靠近镜头的物件（草、树枝、栏杆、虚化的窗框）
- **中景**：主体所在的距离
- **远景**：远处的环境（山、海、城市）
- 三层有明确空间分离

**叙事用途**：
- **强化纵深**：让画面有"立体"感而非"扁平"
- **隐藏 / 暗示**：前景虚化让观众"凝视"主体
- **史诗感**：前中后景一应俱全的电影质感
- **国画意境**：传统中国山水画"三远"法（高远、深远、平远）
- **经典参考**：《2046》大量三层构图；《卧虎藏龙》竹林戏；几乎所有顶级电影摄影

**英文模板**：
```
three-layer composition: [foreground element] in foreground, [subject] in midground, [background scene] in background, depth layers, [N] seconds, cinematic
```

**中文模板**：
```
层次构图：前景[元素]，中景[主体]，远景[场景]，纵深感，[N]秒，电影感
```

**完整示例**：
> Three-layer composition: blurred wildflowers in foreground, a young woman standing in midground at clear focus, distant mountains and golden sunset sky in background. Strong depth layers, shallow depth of field, 7 seconds, cinematic, epic.

**易混淆**：
- 这是 AI 视频"出片质感"的最佳武器之一——比单纯描述场景效果好得多
- 配合 **浅景深** 极强：前景虚化 + 主体清晰 + 远景虚化
- 失败模式：AI 只给两层（主体+背景）——明确写"three layers"

---

# 二、景深与焦点

## 9. 浅景深 / Shallow Depth of Field

**别名**：Shallow DoF、Bokeh Background、大光圈虚化、奶油虚化
**画面定义**：只有焦点位置清晰，前景和/或背景明显模糊
**难度**：⭐ 简单（AI 视频里最实用的出片杀手锏之一）

**画面**：
- 主体（在焦点处）清晰锐利
- 背景明显模糊（高斯模糊感）
- 通常配合大光圈（f/1.4-f/2.8 感觉）
- 给人"电影感"、"专业感"

**叙事用途**：
- **聚焦主体**：背景虚化让观众视线锁死主体
- **情绪强化**：模糊背景烘托主体情绪
- **电影质感**：现代电影常态
- **去除杂乱**：让乱背景看起来"好看"
- **经典参考**：现代剧情片几乎全用；商业广告人物特写；婚礼摄影

**英文模板**：
```
shallow depth of field, [subject] in sharp focus, blurred background, bokeh, [N] seconds, cinematic
```

**中文模板**：
```
浅景深，[主体]清晰对焦，背景模糊，散景虚化，[N]秒，电影感
```

**完整示例**：
> Shallow depth of field on a young woman holding a book in a busy coffee shop. Her face and the book in sharp focus, all the chaotic background of customers and lights blurred into soft creamy bokeh. 5 seconds, cinematic, intimate mood.

**易混淆**：
- AI 几乎 100% 认识 `shallow depth of field`——也可以用 `f/1.4 aperture` / `bokeh` 等具体术语
- 强度：`extreme shallow DoF`（极致虚化）/ `gentle shallow DoF`（轻柔虚化）
- 想要前景也虚化：`foreground and background both blurred, subject in mid-distance sharp focus`

---

## 10. 深景深 / Deep Depth of Field

**别名**：Deep DoF、Deep Focus、Pan Focus、全景深
**画面定义**：从前景到远景所有元素都在焦点上（清晰锐利）
**难度**：⭐⭐ 中等（AI 默认偏向浅景深；想要深景深要明确写）

**画面**：
- 从镜头前几十厘米到无限远都清晰
- 通常配合小光圈（f/8-f/16 感觉）
- 信息密度高、纪实感强
- 没有"焦点引导"——观众自己选择看哪里

**叙事用途**：
- **纪实 / 纪录片**：所有信息都清晰呈现
- **戏剧深景**：前后景的同时戏剧表演（《公民凯恩》经典手法）
- **风景 / 建筑**：所有细节同等重要
- **古典美**：让画面像"绘画"，每个角落都精致
- **经典参考**：《公民凯恩》大量深焦摄影；纪录片自然类；伊朗导演阿巴斯作品

**英文模板**：
```
deep depth of field, everything in sharp focus from foreground to background, [N] seconds, cinematic
```

**中文模板**：
```
深景深，前景到背景全部清晰对焦，[N]秒，电影感
```

**完整示例**：
> Deep depth of field landscape: a farmer plowing in foreground, traditional village in midground, distant snow mountains in background, all in razor-sharp focus. Bright daylight, 7 seconds, cinematic, documentary style.

**易混淆**：
- AI 默认偏浅景深，必须明确写 `deep depth of field` / `everything in focus`
- vs **Pan Focus**：技术上是一回事，写哪个 AI 都能理解
- 失败模式：AI 仍轻微虚化背景——强化 `every detail in sharp focus, no blur anywhere`

---

## 11. 选择性对焦 / Selective Focus

**别名**：Selective Focus、Pinpoint Focus、Spot Focus
**画面定义**：在画面中只让一个非常具体的小区域清晰，其他全部虚化
**难度**：⭐⭐ 中等（比浅景深更极端的"焦点单一"）

**画面**：
- 焦点区域比浅景深更窄（可能只是面部的眼睛、或物件的一角）
- 焦点外的虚化更剧烈
- 强烈的"指挥观众看哪里"感
- 微距摄影感

**叙事用途**：
- **极致聚焦**：让观众强制看一个细节
- **微距感**：花、虫、纹理细节
- **戏剧瞬间**：眼睛流泪的瞬间、手指颤抖的瞬间
- **梦境/朦胧感**：周围全虚的梦幻氛围
- **经典参考**：自然纪录片微距；时尚摄影；情感戏中的"眼睛特写 + 周围全虚"

**英文模板**：
```
selective focus on [specific detail], extreme shallow depth of field, everything else heavily blurred, [N] seconds, cinematic
```

**中文模板**：
```
对[特定细节]的选择性对焦，极浅景深，其他全部强烈虚化，[N]秒，电影感
```

**完整示例**：
> Selective focus on a single dewdrop on a green leaf at dawn. Razor-sharp focus on the dewdrop reflecting morning light, everything else in extreme blur. Macro lens aesthetic, 5 seconds, cinematic, contemplative.

**易混淆**：
- vs **浅景深**：浅景深焦点区还有一定范围；selective focus 是"只有一个点"
- 配合 ECU（极特写）效果最强
- AI 用 `macro selective focus` 或 `pinpoint focus on [detail]` 出活率高

---

## 12. 散景 / Bokeh

**别名**：Bokeh、Background Blur Pattern、光斑虚化
**画面定义**：背景中的点光源（路灯、阳光透过树叶、霓虹）被虚化成圆形/六边形光斑
**难度**：⭐ 简单（AI 视频里"高级感"的标志性效果之一）

**画面**：
- 主体清晰（配合浅景深）
- 背景的点光源变成大圆光斑（或六边/八边形，取决于光圈叶片）
- 圆光斑大小、密度、颜色都影响氛围
- 高级镜头会产生"奶油散景"（creamy bokeh）

**叙事用途**：
- **梦幻氛围**：夜晚街道、节日灯光、阳光树影
- **浪漫场景**：恋人对视背景的暖光斑
- **高级感**：商业广告人物拍摄
- **季节感**：圣诞灯、樱花树、秋阳
- **经典参考**：现代浪漫剧情片标配；高端商业广告；婚礼/婚纱摄影

**英文模板**：
```
bokeh background, soft circular light spots behind subject, shallow depth of field, [N] seconds, cinematic
```

**中文模板**：
```
散景背景，主体后方柔和圆形光斑，浅景深，[N]秒，电影感
```

**完整示例**：
> Bokeh background: a young couple sharing an umbrella on a rainy street at night. Their faces in sharp focus, the entire background dissolved into soft glowing circles of streetlight bokeh in warm gold and cool blue. 6 seconds, cinematic, romantic.

**易混淆**：
- 散景需要**点光源**才能出现——AI 写 prompt 时要暗示背景有"光点"：`bokeh from streetlights / fairy lights / sun through leaves / candles`
- vs **浅景深**：浅景深是大类（背景模糊）；散景是浅景深的具体效果（点光源变光斑）
- 强度：`heavy bokeh`（夸张大光斑）/ `subtle bokeh`（克制光斑）

---

# 三、构图 + 景深的组合习惯

## A. 经典组合

### 1. 三分法 + 浅景深 — "电影感单人镜头"
- **效果**：主体偏置在 1/3 交点 + 背景虚化
- **用途**：人物镜头标配，几乎所有现代电影都用
- **Prompt**：`rule of thirds, subject at left intersection, shallow depth of field, blurred background`
- **经典**：现代剧情片人物特写

### 2. 中心构图 + 对称 + 深景深 — "Wes Anderson 标志"
- **效果**：正中 + 对称 + 全清晰
- **用途**：风格化美学
- **Prompt**：`centered symmetrical composition, deep focus, Wes Anderson aesthetic`
- **经典**：《布达佩斯大饭店》几乎全片

### 3. 引导线 + 浅景深 + 三层构图 — "纵深电影感"
- **效果**：线条引导 + 主体清晰 + 三层空间
- **用途**：公路片、旅程戏、史诗感
- **Prompt**：`leading lines from foreground to subject, three-layer composition, shallow depth on subject`
- **经典**：《阿拉伯的劳伦斯》、公路片

### 4. 框架构图 + 浅景深 — "窥视质感"
- **效果**：前景框架 + 框内主体清晰
- **用途**：暗示偷窥、私密、限制视野
- **Prompt**：`frame within frame, subject framed by [doorway/window], shallow depth of field on subject`
- **经典**：《教父》多次门框戏

### 5. 负空间 + 中心 + 深景深 — "极简意境"
- **效果**：大量空白 + 主体居中（可能很小）+ 全清晰
- **用途**：水墨意境、孤独感、哲思
- **Prompt**：`negative space composition, single small subject centered, deep focus, minimalist`
- **经典**：东方山水画、《2046》

### 6. 层次构图 + 散景 + 黄金时段 — "终极电影质感"
- **效果**：前中后三层 + 背景光斑 + 暖光
- **用途**：浪漫戏、广告大片、唯美回忆
- **Prompt**：`three-layer composition, foreground bokeh, subject in midground sharp, golden hour bokeh background`
- **经典**：现代浪漫片、高端商业广告

---

## B. AI 视频里的构图踩坑

1. **不写构图，AI 默认中心构图**：所有镜头看起来一样呆——必须明确写构图意图
2. **抽象构图术语命中率低**：`rule of thirds` 不如直接说 `subject at lower-right area`
3. **严格对称难做**：AI 大概率"近似对称"——加 `perfectly symmetrical, mirror image` 强化
4. **多元素三角构图易乱**：明确每个人/物的位置（"one standing behind center, two seated in front-left and front-right"）
5. **浅景深默认就有**：AI 大多自带浅景深；想要深景深必须明确写
6. **散景需要点光源**：要先描述背景有"光点"元素才能出散景
7. **景深不要混乱表述**：别同时写 `shallow depth of field` 和 `everything in focus`，AI 会蒙圈

## C. 与运镜 + 景别角度 + 光线的完整 prompt 框架

```
[角度] [景别] of [主体], [构图] composition, [光线], [景深], [运镜], [N] seconds, [总风格]
```

**完整示例**：
- `low angle medium shot of warrior, leading lines composition, golden hour backlit, shallow depth of field, slow dolly in, 6s, epic cinematic`
- `eye level wide shot of village, three-layer composition, overcast soft daylight, deep focus, drone fly forward, 8s, documentary nature`
- `centered close-up of monk, symmetrical composition, low-key Rembrandt lighting, extreme shallow depth, static, 5s, painterly chiaroscuro`

**保留原则**：5-8 个修饰词最甜区，超过 10 个 AI 抽卡率明显升高。
