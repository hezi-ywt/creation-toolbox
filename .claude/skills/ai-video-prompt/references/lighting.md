---
description: 决定画面光影氛围、时段（黄金 / 蓝色 / 夜）、风格化照明（noir / cyberpunk / 高低调）时加载。光线是 AI 视频出片质感的最高杠杆。
---

# 光线

> 用途：可粘贴到 Seedance / 可灵 / Veo3 / Sora2 / Runway 等 AI 视频模型的光线参考库
> 状态：v0.3（18 条 + 光线组合习惯）
> 数据：基于公开影视摄影经验整理，难度评级为经验估计（非实测）
> 最后更新：2026-05-17

## 怎么用

1. **光线是 AI 视频里最影响"出片感"的维度**——同一构图换个光线，气质完全不同
2. 光线分四个维度：**方向**（光从哪里来）/ **质感**（硬还是软）/ **时段**（自然光的时间）/ **风格**（电影流派的打光习惯）
3. 一个 prompt 通常需要**明确写出 1-2 个维度**，例如 `golden hour sidelight, soft warm`
4. 末尾"组合习惯"章节列了 6 个经典光线 + 构图组合，可直接套用

**难度图例**（同前）：⭐ 简单 / ⭐⭐ 中等 / ⭐⭐⭐ 较难 / ⭐⭐⭐⭐ 困难

---

## 索引

### 一、光的方向

| # | 中文 | English | 核心特征 | 难度 |
|---|---|---|---|---|
| 1 | 顺光 | Front Light | 光源在镜头方向，主体平面化 | ⭐ |
| 2 | 侧光 | Side Light | 光源在主体侧面，立体感强 | ⭐ |
| 3 | 逆光 / 剪影 | Back Light / Silhouette | 光源在主体后方，主体变暗或剪影 | ⭐ |
| 4 | 顶光 / 底光 | Top / Bottom Light | 光源从上方或下方，戏剧 / 恐怖感 | ⭐⭐ |

### 二、光的质感

| # | 中文 | English | 核心特征 | 难度 |
|---|---|---|---|---|
| 5 | 硬光 | Hard Light | 明确边缘的阴影、对比强烈 | ⭐ |
| 6 | 软光 | Soft Light | 柔和过渡的阴影、温和均匀 | ⭐ |

### 三、时段光（自然光）

| # | 中文 | English | 色温 | 难度 |
|---|---|---|---|---|
| 7 | 黄金时刻 | Golden Hour | 温暖橙金 | ⭐ |
| 8 | 蓝色时刻 | Blue Hour | 冷蓝紫 | ⭐⭐ |
| 9 | 正午 | Harsh Daylight | 中性高对比 | ⭐ |
| 10 | 阴天 | Overcast | 中性灰、漫射 | ⭐ |
| 11 | 夜晚 | Night | 极低光 + 人工补光 | ⭐⭐ |
| 12 | 黎明 | Dawn | 冷调过渡到暖 | ⭐⭐ |

### 四、风格化光线

| # | 中文 | English | 流派 | 难度 |
|---|---|---|---|---|
| 13 | 高调 | High-Key Lighting | 喜剧 / 广告 / 清新 | ⭐ |
| 14 | 低调 | Low-Key Lighting | 戏剧 / 惊悚 / 黑色 | ⭐⭐ |
| 15 | 明暗对比 | Chiaroscuro | 巴洛克画 / 经典戏剧 | ⭐⭐⭐ |
| 16 | 黑色电影 | Film Noir Lighting | 1940s 黑色电影 | ⭐⭐⭐ |
| 17 | 霓虹 / 赛博 | Neon / Cyberpunk | 现代都市 / 科幻 | ⭐⭐ |
| 18 | 三点布光 | Three-Point Lighting | 电影标准布光 | ⭐⭐ |

---

# 一、光的方向

## 1. 顺光 / Front Light

**别名**：Frontal Lighting、Flat Light、Beauty Light（柔和顺光时）
**光源位置**：与摄影机同方向（在镜头附近或正对主体）
**难度**：⭐ 简单

**画面**：
- 主体面部均匀照亮，几乎没有阴影
- 立体感弱，主体看起来"扁平"
- 肤色还原好，瑕疵被光均匀照亮（也"无遮无掩"）
- 背景与主体亮度接近

**叙事用途**：
- **广告 / 美妆**：让主体看起来完美无瑕、清新明亮
- **新闻 / 纪实**：信息清晰、无戏剧感
- **儿童 / 喜剧**：明亮欢快
- **怀旧家庭录像**：80-90 年代闪光灯感
- **经典参考**：广告大片、电视新闻、家庭聚会快照

**英文模板**：
```
front lighting, even illumination on subject's face, soft warm tones, [N] seconds
```

**中文模板**：
```
顺光，主体面部均匀照亮，柔和暖调，[N]秒
```

**完整示例**：
> Front lighting on a young woman smiling at the camera, even illumination on her face, no harsh shadows, soft warm tones, blurred bright background, beauty advertisement style, 5 seconds, cinematic.

**易混淆**：
- vs **Soft Light**：顺光是**方向**；软光是**质感**——可以叠加（"soft front light"）
- 大多数 AI 视频默认就是顺光，**写 prompt 时如果想要其他方向必须明确**

---

## 2. 侧光 / Side Light

**别名**：Sidelight、3/4 Lighting（侧前光）、Rembrandt Lighting（伦勃朗光，特定侧光位置）
**光源位置**：主体侧面（90 度）或侧前 45 度
**难度**：⭐ 简单（电影摄影最常用之一）

**画面**：
- 主体一半亮、一半暗，立体感强
- 鼻子、颧骨、下颌的阴影清晰
- 伦勃朗光：暗面的眼睛下方有一个倒三角形亮斑
- 强化纹理、轮廓、戏剧感

**叙事用途**：
- **戏剧感**：剧情片标准打光，强化主体立体感
- **角色塑造**：让面部有"故事感"、不平庸
- **古典质感**：模仿油画（伦勃朗、卡拉瓦乔）的光感
- **暗示二元性**：明暗对应内心矛盾
- **经典参考**：《教父》大量侧光阴影；伦勃朗肖像画；几乎所有奥斯卡剧情片

**英文模板**：
```
side lighting from [left/right], strong contrast between light and shadow on subject, [N] seconds, cinematic
```

**中文模板**：
```
来自[左/右]侧的侧光，主体明暗对比强烈，[N]秒，电影感
```

**完整示例**：
> Side lighting from the left, illuminating only half of an elderly man's face. Strong contrast between bright side and shadow side, Rembrandt-style triangle of light under the right eye. Warm tungsten tones, 5 seconds, cinematic portrait.

**易混淆**：
- vs **Rembrandt Lighting**：Rembrandt 是特定位置的侧光（约 45 度），不是所有 side light
- AI 用 `Rembrandt lighting` 高级感很强，但出活率不如简单的 `side light + strong contrast`

---

## 3. 逆光 / Back Light / Silhouette

**别名**：Backlight、Rim Light（轮廓光，逆光的弱版）、Silhouette（极端逆光出剪影）
**光源位置**：主体正后方或侧后方
**难度**：⭐ 简单（视觉冲击力强、AI 出活率高）

**画面**：
- 强逆光：主体变暗甚至剪影，背景明亮
- 中等逆光：主体边缘有亮光勾边（rim light），中间偏暗
- 头发、肩膀的轮廓被勾出来
- 透明物体（玻璃、雾、烟、毛发）发光

**叙事用途**：
- **戏剧化氛围**：神秘、英雄、宗教感
- **剪影构图**：黑色主体 + 明亮背景，纯轮廓表达
- **浪漫黄金时刻**：日落逆光下的恋人
- **悬疑 / 反派**：暗示"看不清真相"
- **经典参考**：《荒野猎人》多次逆光剪影；《教父 II》Michael 多场剪影；几乎所有日落浪漫戏

**英文模板**：
```
backlit shot of [subject], silhouette / rim light, bright [light source] behind subject, [N] seconds, cinematic
```

**中文模板**：
```
[主体]的逆光镜头，剪影/轮廓光，明亮的[光源]在主体后方，[N]秒，电影感
```

**完整示例**：
> Backlit shot of a lone figure walking across a misty meadow at sunset. Strong rim light outlining their silhouette, golden hour sun directly behind them, glowing mist around their feet, 7 seconds, cinematic, ethereal mood.

**易混淆**：
- vs **Rim Light**：rim light 是逆光的轻量版（只在边缘）；full backlight 整个主体变暗
- AI 用 `silhouette` 极易出活；用 `backlit, rim light` 出"轮廓发光"感
- 失败模式：AI 偶尔会"补光"让主体变亮——加 `subject in shadow, only edges lit`

---

## 4. 顶光 / 底光 / Top & Bottom Light

**别名**：Overhead Light（顶光）、Underlight（底光）、Horror Light（底光的戏剧叫法）
**光源位置**：主体上方（顶光）或下方（底光）
**难度**：⭐⭐ 中等（视觉特征明确但 AI 偶尔渲染不到位）

**画面（顶光）**：
- 额头、肩膀亮，眼窝、鼻下、下巴暗
- 接近正午太阳的角度
- 头发顶部高光
- 心理：戏剧化、压抑、宗教感

**画面（底光）**：
- 下巴、鼻下、眼下亮，额头暗
- 反自然（地球上几乎没有从下打光的自然光源）
- 心理：诡异、恐怖、超自然
- 经典恐怖片打光（拿手电筒从下往上照脸）

**叙事用途**：
- **顶光**：审讯戏、宗教/仪式戏、监狱、戏剧化压抑
- **底光**：恐怖片、超自然、反派变形、营火故事
- **经典参考**：
  - 顶光：《教父》Vito 病床、《沉默的羔羊》多场审讯
  - 底光：经典恐怖片、《指环王》咕噜、动画《柯瑞琳》

**英文模板（顶光）**：
```
top lighting, harsh overhead light, deep shadows under eyes and chin, [N] seconds, dramatic
```

**英文模板（底光）**：
```
underlight, light coming from below subject's face, eerie shadows on forehead, [N] seconds, horror style
```

**中文模板**：
```
顶光，强烈头顶光源，眼下和下巴深阴影，[N]秒，戏剧化
底光，光源从主体面部下方，额头诡异阴影，[N]秒，恐怖风格
```

**完整示例（顶光）**：
> Top lighting on a prisoner being interrogated. Harsh overhead bulb directly above, deep shadows pooling in eye sockets and under his chin, illuminating only his forehead and shoulders. 5 seconds, cinematic, oppressive mood.

**完整示例（底光）**：
> Underlight on a child telling a ghost story by campfire. Light from the fire below illuminates her face from below, eerie shadows on her forehead and around her eyes, dark forest behind. 4 seconds, horror style, unsettling.

**易混淆**：
- 顶光 vs 正午阳光：正午是自然顶光，但更宽广；prompt 里"top lighting"暗示人工/戏剧性
- 底光对 AI 来说是相对小众的术语，加具体来源（"flashlight from below", "fire light from below"）更稳

---

# 二、光的质感

## 5. 硬光 / Hard Light

**别名**：Direct Light、Specular Light
**光源特性**：未经扩散的直接光源（点光源、远距离强光）
**难度**：⭐ 简单（强烈对比，AI 易理解）

**画面**：
- 阴影边缘**清晰锐利**
- 高光和阴影对比强烈
- 纹理被强化（皱纹、纹理、汗珠）
- 主体看起来"硬朗"

**叙事用途**：
- **戏剧张力**：冲突、对峙、英雄式
- **西部片 / 阳光下场景**：正午太阳的硬光
- **强化质感**：让粗糙表面（石头、铁、皮肤纹理）更突出
- **冷峻角色塑造**：硬汉、反派
- **经典参考**：西部片大量硬光；《疯狂的麦克斯》沙漠戏；经典动作片

**英文模板**：
```
hard lighting, harsh direct light source, sharp-edged shadows, strong contrast, [N] seconds, cinematic
```

**中文模板**：
```
硬光，强烈直射光源，阴影边缘锐利，对比强，[N]秒，电影感
```

**完整示例**：
> Hard lighting on a cowboy standing in a sun-baked desert at noon. Harsh direct sunlight from above, razor-sharp shadow under his hat brim, strong contrast between bright sand and deep shadow. 6 seconds, cinematic Western.

**易混淆**：
- vs **Soft Light**：硬光阴影锐利；软光阴影柔和
- AI 默认渲染稍偏软光（更"好看"），所以想要硬光要明确写

---

## 6. 软光 / Soft Light

**别名**：Diffused Light、Wrap-around Light
**光源特性**：经过扩散的光源（大面积光源、阴天、柔光罩）
**难度**：⭐ 简单（最常用，AI 默认偏向软光）

**画面**：
- 阴影边缘**柔和、模糊**
- 高光和阴影过渡平滑
- 皮肤光滑、瑕疵不明显
- 整体氛围温和

**叙事用途**：
- **美妆 / 广告**：让人/产品看起来精致
- **浪漫戏**：恋人对视、温馨家庭
- **童话感**：奇幻、温暖故事
- **室内戏**：现代家居、咖啡馆、办公室
- **经典参考**：浪漫喜剧大量软光；婚纱摄影；现代广告

**英文模板**：
```
soft lighting, diffused light source, gentle shadows, smooth gradient between light and shadow, [N] seconds, cinematic
```

**中文模板**：
```
软光，漫射光源，柔和阴影，明暗过渡平滑，[N]秒，电影感
```

**完整示例**：
> Soft lighting on a young couple sitting together by a large window at dusk. Diffused window light wrapping gently around their faces, smooth shadow gradients, no harsh edges anywhere. 6 seconds, cinematic, romantic mood.

**易混淆**：
- vs **Hard Light**：软光是默认风格——大多数现代商业片都是软光
- 想要"美颜感"，加 `beauty soft light` 或 `wrap-around lighting`

---

# 三、时段光（自然光）

## 7. 黄金时刻 / Golden Hour

**别名**：Magic Hour（广义）、Sunset / Sunrise Light、日落时分
**时段**：日出后第一小时 / 日落前第一小时
**难度**：⭐ 简单（AI 视频最受欢迎的光线之一，训练数据极多）

**画面**：
- 色温暖：橙金、玫瑰金、淡红
- 光线角度低，长投影、长光斑
- 大气散射强，画面有"金色雾"
- 主体被温暖光"镀金"，背景有 lens flare

**叙事用途**：
- **浪漫 / 温暖**：恋人、家庭、童年回忆
- **史诗感**：英雄站在金色光中
- **怀旧 / 治愈**：感伤但美好的氛围
- **广告标配**：旅游、汽车、奢侈品
- **经典参考**：《麦田守望者》（Days of Heaven，被誉为黄金时刻摄影巅峰）；几乎所有浪漫片日落戏；旅游广告

**英文模板**：
```
golden hour lighting, warm orange-gold tones, long shadows, soft lens flare, [N] seconds, cinematic
```

**中文模板**：
```
黄金时刻光，温暖橙金色调，长投影，柔和镜头光晕，[N]秒，电影感
```

**完整示例**：
> Golden hour lighting on a young woman standing in a wheat field. Warm orange-gold sun low on the horizon behind her, long shadows stretching toward camera, soft lens flare, hair catching the light, 7 seconds, cinematic, dreamy.

**易混淆**：
- vs **Magic Hour**：Magic Hour 是宽义（含 golden + blue hour）；Golden Hour 特指日落金色
- AI 极易出"过于浓烈"的金色——加 `subtle golden hour` 或 `early golden hour` 缓解
- 想要更日出感：`dawn golden hour`，想要日落：`sunset golden hour`

---

## 8. 蓝色时刻 / Blue Hour

**别名**：Twilight、Civil Twilight、薄暮时分
**时段**：日出前 30 分钟 / 日落后 30 分钟（太阳在地平线下）
**难度**：⭐⭐ 中等（术语稍小众，AI 偶尔渲染成单纯的夜景）

**画面**：
- 天空深蓝、靛蓝、紫色
- 地面有少量残光（西边略亮）
- 路灯、窗灯开始亮起，与冷天空对比
- 大气清晰、色彩冷静

**叙事用途**：
- **诗意 / 忧郁**：都市孤独、深思、告别
- **科幻 / 赛博**：冷色基调与霓虹对比
- **侦探 / 悬疑**：城市夜景的开场
- **过渡时刻**：从白天到黑夜的暧昧时段
- **经典参考**：《银翼杀手》多次 blue hour；《赛博朋克 2077》风格；现代都市片

**英文模板**：
```
blue hour lighting, deep blue sky after sunset, warm window lights against cool tones, [N] seconds, cinematic
```

**中文模板**：
```
蓝色时刻，日落后深蓝天空，温暖窗光与冷调对比，[N]秒，电影感
```

**完整示例**：
> Blue hour shot of a quiet city street after sunset. Deep blue sky, glowing warm yellow window lights, cool wet pavement reflecting neon signs, a lone figure walking with an umbrella. 8 seconds, cinematic, melancholic urban mood.

**易混淆**：
- vs **Night**：blue hour 有微弱日光余晖；night 完全是人工光主导
- vs **Golden Hour**：blue hour 是日落"后"30 分；golden hour 是日落"前"
- 加 `deep blue twilight sky` 帮 AI 锁定时段

---

## 9. 正午 / Harsh Daylight

**别名**：Midday Sun、Overhead Sun、Noon Light、High Noon
**时段**：太阳接近顶空（约上午 11 点-下午 2 点）
**难度**：⭐ 简单

**画面**：
- 顶光角度，阴影直接落在主体下方
- 眼窝、鼻下、下巴有深阴影
- 高光强烈，整体高对比
- 颜色饱和但偏冷（蓝白色调）

**叙事用途**：
- **西部片**：High Noon 决斗场面
- **沙漠 / 海滩**：日晒感、热感
- **运动 / 户外**：力量、活力
- **戏剧化压迫**：暗示酷热、暴露、无处躲藏
- **经典参考**：《正午》（High Noon）经典片名；西部片大量正午戏；运动广告

**英文模板**：
```
harsh midday sunlight, overhead sun, deep shadows under eyes and chin, high contrast, [N] seconds, cinematic
```

**中文模板**：
```
正午烈日，头顶太阳，眼下下巴深阴影，高对比，[N]秒，电影感
```

**完整示例**：
> Harsh midday sunlight on a lone gunslinger standing on a dusty Western street. Overhead sun creating deep shadow under his hat brim, sharp shadow at his feet, bright sandy ground, distant heat shimmer. 5 seconds, cinematic Western.

**易混淆**：
- AI 默认"daylight"通常给软一点的光——明确 `harsh midday` 或 `noon sun` 才出强烈感
- 与 `top light` 重叠：正午是自然顶光，但更宽广、更明亮

---

## 10. 阴天 / Overcast

**别名**：Cloudy Daylight、Diffused Daylight、Soft Sky
**时段**：阴天或多云的白天
**难度**：⭐ 简单

**画面**：
- 整个天空是巨大的柔光罩
- 阴影柔和模糊，几乎没有明确光源方向
- 色调中性偏冷（蓝灰）
- 高动态范围低，画面整体温和

**叙事用途**：
- **纪实 / 自然**：纪录片标配
- **忧郁 / 平静**：北欧片、文艺片
- **现代时尚**：高级感冷淡风
- **公平光**：任何角度看主体都一致，适合多镜头戏
- **经典参考**：北欧电影大量；时尚摄影；纪录片户外场景

**英文模板**：
```
overcast lighting, soft diffused sky, even illumination, cool neutral tones, [N] seconds, cinematic
```

**中文模板**：
```
阴天光，柔和漫射天空，均匀照明，中性冷调，[N]秒，电影感
```

**完整示例**：
> Overcast lighting in a coastal village. Soft diffused gray sky, no harsh shadows, cool neutral tones across stone houses and weathered fishing boats, light mist over the harbor. 7 seconds, cinematic, contemplative mood.

**易混淆**：
- vs **Soft Light**：阴天是自然产生的软光，宽广均匀；soft light 可以是人工的局部柔光
- AI 用 `overcast` 命中率高，出"灰调氛围"

---

## 11. 夜晚 / Night

**别名**：Night Scene、Low Light、Moonlight（月光）
**时段**：完全黑夜
**难度**：⭐⭐ 中等（AI 容易过度补光或过度黑暗，需要精控）

**画面**：
- 几乎无自然光，全靠月光、星光、人工光
- 高对比：黑暗背景 + 亮点光源（窗、灯、火）
- 月光为主时偏冷蓝；人工光（钨丝灯）偏暖橙
- 色彩饱和度低，氛围浓

**叙事用途**：
- **悬疑 / 惊悚 / 恐怖**：未知威胁的氛围
- **都市夜景**：现代故事的浪漫/孤独
- **罪案 / 侦探**：黑色电影标配
- **梦境 / 超现实**：朦胧夜色配合幻想
- **经典参考**：黑色电影（Film Noir）几乎全片夜戏；《银翼杀手》；《七宗罪》大量夜雨戏

**英文模板**：
```
night scene, low light, [moonlight / window glow / streetlight] as main source, deep shadows, [N] seconds, cinematic
```

**中文模板**：
```
夜景，低光，[月光/窗光/街灯]为主光源，深阴影，[N]秒，电影感
```

**完整示例**：
> Night scene of a detective standing in an empty alleyway. Single streetlight casting a cone of warm yellow light from above, deep shadows in corners, slight mist visible in the light beam, cool blue tones in surrounding shadows. 7 seconds, cinematic, noir mood.

**易混淆**：
- AI 写 `night` 不写其他东西可能出"几乎全黑"的画面——必须**指定主光源**（月光、街灯、窗光、火光）
- 不要写 `dark night`，更稳的是 `night scene with [light source]`
- 想要日式动漫的明亮夜景：`anime style night with neon streetlights`

---

## 12. 黎明 / Dawn

**别名**：Pre-Dawn、Early Morning Light、破晓
**时段**：日出前 30 分钟到日出后 30 分钟
**难度**：⭐⭐ 中等（与 golden hour 和 blue hour 有重叠，但有独特色温过渡）

**画面**：
- 东方天空从蓝到粉到橙的渐变
- 西方仍是深蓝/紫
- 地面冷色，光线方向自东而来
- 雾气、露水常见

**叙事用途**：
- **新的开始**：希望、重生、英雄出发
- **疲惫归来**：通宵之后的回家
- **战争前夕**：战场上的紧张静默
- **诗意时刻**：哲思、独白
- **经典参考**：《拯救大兵瑞恩》多场黎明；《指环王》多次破晓；战争片黎明出发场面

**英文模板**：
```
dawn lighting, pre-sunrise sky, cool blue transitioning to warm orange on horizon, [N] seconds, cinematic
```

**中文模板**：
```
黎明光，日出前天空，地平线从冷蓝过渡到暖橙，[N]秒，电影感
```

**完整示例**：
> Dawn lighting over a quiet mountain lake. Pre-sunrise sky transitioning from deep blue overhead to soft pink and orange on the eastern horizon, mist rising from the still water, single bird flying across the gradient. 8 seconds, cinematic, contemplative mood.

**易混淆**：
- vs **Golden Hour Sunrise**：dawn 包含日出前的冷调时段；golden hour 主要是太阳出来后的暖调
- vs **Blue Hour**：dawn 是从蓝→暖的过渡；blue hour 是固定深蓝
- 想要更明确的"破晓瞬间"：`moment of sunrise, first light on horizon`

---

# 四、风格化光线

## 13. 高调 / High-Key Lighting

**别名**：High-Key、Bright Lighting、明亮风格
**特征**：整体明亮、阴影极少、对比低
**难度**：⭐ 简单

**画面**：
- 主体和环境都被明亮光均匀照亮
- 阴影几乎消失，少量浅灰过渡
- 背景常是白色或高亮中性色
- 整体氛围明快、清新、欢乐

**叙事用途**：
- **喜剧**：轻松、幽默场面
- **广告 / 美妆**：清新、健康、积极
- **儿童内容**：温暖、安全
- **时尚高调**：现代极简风
- **歌舞片**：欢乐场面
- **经典参考**：经典好莱坞歌舞片；现代喜剧《老友记》风格；广告大片

**英文模板**：
```
high-key lighting, bright even illumination, minimal shadows, low contrast, white / pastel background, [N] seconds, cinematic
```

**中文模板**：
```
高调光，明亮均匀照明，几乎无阴影，低对比，白色/淡色背景，[N]秒，电影感
```

**完整示例**：
> High-key lighting on a young woman holding a cup of coffee in a sunlit kitchen. Bright even illumination, minimal shadows, white walls, pastel colors, cheerful expression, 5 seconds, cinematic, commercial style.

**易混淆**：
- vs **Soft Light**：high-key 是整体明亮 + 低对比的**风格**；soft light 是光的**质感**——可叠加
- AI 用 `high-key` 出"广告感";想要更艺术风可叠加 `minimalist high-key`

---

## 14. 低调 / Low-Key Lighting

**别名**：Low-Key、Dramatic Lighting、暗调
**特征**：整体暗，强光源点亮主体局部，大量阴影
**难度**：⭐⭐ 中等（AI 易出"全暗看不清"，需要精控光源位置）

**画面**：
- 大部分画面是黑或深阴影
- 单一或少量强光照亮主体的一部分（通常面部）
- 高对比，强烈明暗反差
- 神秘、戏剧、压迫氛围

**叙事用途**：
- **惊悚 / 悬疑 / 恐怖**：未知威胁、隐藏真相
- **戏剧片**：内心冲突、道德困境
- **黑色电影**：经典 Film Noir 风格
- **角色塑造**：复杂、有秘密、危险的角色
- **经典参考**：《教父》大量低调；《公民凯恩》经典低调；几乎所有黑色电影

**英文模板**：
```
low-key lighting, dark scene with single light source illuminating subject's face, deep shadows everywhere else, high contrast, [N] seconds, cinematic
```

**中文模板**：
```
低调光，暗调场景，单一光源照亮主体面部，其余深阴影，高对比，[N]秒，电影感
```

**完整示例**：
> Low-key lighting on a middle-aged man sitting alone at a desk in a dark office. Single desk lamp illuminating only his face and hands, deep shadows engulfing the rest of the room, smoke from a cigarette curling through the light beam. 6 seconds, cinematic, noir mood.

**易混淆**：
- vs **Night Scene**：low-key 是一种**风格选择**，不一定是夜；night 是时段
- 失败模式：AI 渲染成"全画面黑掉"——必须明确"主体面部被光照亮"
- 加 `single light source` 或 `Rembrandt lighting` 帮 AI 锁定经典低调感

---

## 15. 明暗对比 / Chiaroscuro

**别名**：Chiaroscuro、Caravaggio Lighting（卡拉瓦乔光）
**特征**：极致明暗对比，仿照巴洛克绘画的戏剧性
**难度**：⭐⭐⭐ 较难（术语小众，AI 训练样本主要在艺术领域）

**画面**：
- 与 low-key 类似但更极端
- 单一强光来自侧上方
- 暗部几乎完全黑，亮部极亮
- 主体仿佛"从黑暗中浮现"
- 油画质感

**叙事用途**：
- **古典戏剧 / 历史片**：仿照油画质感
- **宗教 / 神秘**：神圣或仪式感
- **艺术片**：强调风格化、绘画感
- **极致戏剧化时刻**：揭示、顿悟、死亡
- **经典参考**：卡拉瓦乔、伦勃朗、维米尔的画；《拨弦师》（The Lighthouse）；《年轻与美丽》（Mr. Turner）

**英文模板**：
```
chiaroscuro lighting, Caravaggio-style dramatic contrast, single strong light from upper side, deep velvet shadows, [N] seconds, cinematic, painterly
```

**中文模板**：
```
明暗对比光，卡拉瓦乔式戏剧对比，侧上方单一强光，深邃阴影，[N]秒，电影感，绘画质感
```

**完整示例**：
> Chiaroscuro lighting on a scholar reading by candlelight. Caravaggio-style dramatic contrast, single candle on a wooden table illuminating his face and the open book, deep velvet shadows engulfing the rest of the room, painterly quality. 6 seconds, cinematic, classical painting aesthetic.

**易混淆**：
- vs **Low-Key**：chiaroscuro 更极致，光源方向明确（侧上方），亮部更亮
- AI 用 `Caravaggio style` 或 `Rembrandt style` 比 `chiaroscuro` 命中率更高（具体引用）
- 失败模式：AI 渲染成普通的低调而非"绘画感"——加 `painterly quality, oil painting aesthetic`

---

## 16. 黑色电影 / Film Noir Lighting

**别名**：Film Noir、Hardboiled Lighting、1940s Crime Lighting
**特征**：综合风格——低调 + 硬光 + 百叶窗阴影 + 黑白思维
**难度**：⭐⭐⭐ 较难（需要多元素组合，AI 偶尔只给一两个特征）

**画面**：
- 低调光 + 硬光的组合
- **标志性元素**：百叶窗的条纹阴影投在墙上/脸上
- 烟雾在光束中飘
- 高对比、深阴影
- 通常雨夜、办公室、酒吧

**叙事用途**：
- **侦探 / 犯罪**：硬汉侦探、致命女人
- **黑色幽默**：暗调讽刺
- **怀旧致敬**：现代片回归 1940s 风格
- **道德灰色地带**：复杂角色、模糊正义
- **经典参考**：《双重赔偿》、《唐人街》、《银翼杀手 2049》（现代 noir）；《罪恶之城》（极致 noir）

**英文模板**：
```
film noir lighting, low-key with venetian blind shadows on wall and face, cigarette smoke in light beam, harsh shadows, [N] seconds, cinematic, 1940s style
```

**中文模板**：
```
黑色电影光，低调 + 百叶窗条纹阴影投在墙上和脸上，烟雾在光束中，硬阴影，[N]秒，电影感，1940年代风格
```

**完整示例**：
> Film noir lighting on a hardboiled detective sitting at his office desk at night. Strong slanting light through venetian blinds casting striped shadows across his face and the wall behind him, cigarette smoke curling through the light beam, rain visible through the window. 7 seconds, cinematic, 1940s style.

**易混淆**：
- 这是组合风格，要"全套元素"：低调 + 百叶窗阴影 + 烟雾 + 高对比
- AI 用 `film noir style` 出活率高（训练数据多），但偶尔只给低调光忘了百叶窗——明确 `venetian blind shadows`
- 想要现代 noir：`modern neo-noir style`，会偏《银翼杀手》风

---

## 17. 霓虹 / Cyberpunk / Neon

**别名**：Neon Lighting、Cyberpunk、Synthwave、Vaporwave
**特征**：饱和的紫、粉、青、蓝霓虹色彩主导
**难度**：⭐⭐ 中等（AI 视频圈极爱、训练数据丰富，但容易俗套）

**画面**：
- 主光来自霓虹标志、LED 屏、灯条
- 紫色、品红、青色、蓝色饱和度极高
- 反射在湿润的街道、玻璃、皮肤上
- 烟雾、雨、雾气增强光晕感

**叙事用途**：
- **赛博朋克 / 科幻**：未来都市、反乌托邦
- **现代都市夜景**：东京、香港、上海风
- **音乐 MV / 时尚**：合成器风、80 年代回归
- **酷感商业广告**：年轻、科技、潮流
- **经典参考**：《银翼杀手》原版 + 2049；《攻壳机动队》；《赛博朋克 2077》；80s 风音乐 MV

**英文模板**：
```
neon lighting, saturated pink and cyan and purple, wet reflective streets, cyberpunk aesthetic, [N] seconds, cinematic
```

**中文模板**：
```
霓虹光，饱和的粉/青/紫色，湿润反光街道，赛博朋克美学，[N]秒，电影感
```

**完整示例**：
> Neon lighting in a rainy Tokyo back alley at night. Saturated pink and cyan neon signs reflecting on wet pavement, a lone figure in a trench coat walking past, purple haze in the air, holographic advertisements glowing in the distance. 7 seconds, cinematic, cyberpunk aesthetic.

**易混淆**：
- AI 极擅长 cyberpunk neon——风险是"出活太套路"
- 想区分风格：`Blade Runner cyberpunk` / `Akira cyberpunk` / `Hong Kong neon` / `Vegas neon`
- 失败模式：颜色饱和到失控；加 `restrained cyberpunk, subtle neon` 节制

---

## 18. 三点布光 / Three-Point Lighting

**别名**：Classic Three-Point、Hollywood Lighting、电影标准布光
**特征**：Key Light（主光）+ Fill Light（补光）+ Back Light（背光）的经典组合
**难度**：⭐⭐ 中等（AI 偶尔渲染但难精确控制三个光源）

**画面**：
- **Key Light**：主光，照亮主体一侧（通常 45 度前侧）
- **Fill Light**：补光，柔化主光产生的阴影（强度通常是主光的 50%）
- **Back Light**：背光/轮廓光，从主体后方勾边
- 主体在画面中**立体感强**、与背景**有空间分离**
- 这是好莱坞、电视剧、人像摄影的"标准答案"

**叙事用途**：
- **专业感**：广告、企业宣传、电视访谈、电影剧情
- **人像清晰**：让主体被"塑造"得最好看
- **稳定打光**：多镜头剧不需要重新打光
- **经典参考**：好莱坞经典电影；电视访谈节目；高端商业广告

**英文模板**：
```
three-point lighting on [subject], key light from front-left, fill light softening shadows, back light separating subject from background, [N] seconds, cinematic
```

**中文模板**：
```
对[主体]的三点布光，前左主光，补光柔化阴影，背光让主体与背景分离，[N]秒，电影感
```

**完整示例**：
> Three-point lighting on a CEO being interviewed at his desk. Key light from the front-left highlighting his face, soft fill light from the right reducing harsh shadows, back light creating a subtle glow on his hair and shoulders separating him from the dark background. 6 seconds, cinematic, professional interview style.

**易混淆**：
- AI 不一定能精确执行三个光源——把它视为"风格描述"而非"技术指令"
- 偷懒高级感：直接写 `Hollywood lighting` 或 `studio lighting`，AI 出活率高
- 想强化背景分离：明确 `strong back light creating rim glow`

---

# 五、光线组合习惯

光线极少单独使用，**通常 1-2 个维度叠加**形成完整氛围。这一节列 6 个最经典的组合 + AI 视频里的踩坑。

## A. 经典组合

### 1. Golden Hour + Side Light + Soft — "浪漫黄金时刻"
- **效果**：暖金色侧光柔和照亮主体，长投影，氛围温柔
- **用途**：恋人对视、家庭团聚、英雄归乡
- **Prompt**：`golden hour side lighting, soft warm tones, long shadows, romantic`
- **经典**：所有日落浪漫戏的"经典质感"

### 2. Night + Backlight + Neon — "赛博朋克夜街"
- **效果**：夜晚 + 主体逆光（被霓虹照亮轮廓）+ 饱和霓虹色
- **用途**：现代都市夜景、科幻、潮流广告
- **Prompt**：`night scene, backlit subject, neon lighting pink and cyan, wet streets, cyberpunk`
- **经典**：《银翼杀手》、东京夜景广告

### 3. Low-Key + Side Light + Hard — "戏剧化反派"
- **效果**：暗调中只有一侧硬光照亮主体半边脸
- **用途**：反派出场、危险瞬间、内心冲突
- **Prompt**：`low-key lighting, hard side light from left, half of face illuminated, deep shadows, dramatic`
- **经典**：《教父》、几乎所有黑色电影

### 4. Overcast + Front Light + Soft — "纪实纯净"
- **效果**：阴天均匀软光，前光让主体清晰可读
- **用途**：纪录片、采访、北欧文艺片
- **Prompt**：`overcast soft daylight, even illumination, neutral cool tones, documentary style`
- **经典**：北欧电影、自然纪录片

### 5. Blue Hour + Window Light Warm — "都市孤独"
- **效果**：冷蓝外景 + 暖黄窗光
- **用途**：城市孤独、深夜情绪、侦探片开场
- **Prompt**：`blue hour twilight, warm yellow window lights, cool blue outside, urban melancholy`
- **经典**：《银翼杀手 2049》、爱德华霍普风格

### 6. High-Key + Soft + Pastel — "广告清新"
- **效果**：明亮 + 柔和 + 淡色调
- **用途**：广告大片、美妆、生活方式
- **Prompt**：`high-key lighting, soft diffused light, pastel color palette, commercial bright`
- **经典**：现代广告、Instagram 美学

---

## B. AI 视频里的光线踩坑

1. **不写光线，AI 默认软光中性顺光**：想要其他必须明确（"side light", "backlit", "golden hour", "night"）
2. **"Night" 不写主光源就全黑**：必须配上 `moonlight` / `streetlight` / `window glow` / `firelight` 至少其一
3. **"Backlit" 偶尔被理解为"主体朝后"**：明确 `light source behind subject, subject in shadow`
4. **风格化光线（noir、cyberpunk）易出套路**：想要克制感加 `subtle`、`restrained`、`minimalist`
5. **多光源指令 AI 可能简化**：写"三点布光"的话 AI 通常只渲染 key light + back light，fill light 易丢
6. **色温和时段冲突要避免**：`golden hour with cool blue tones` 互斥，AI 会蒙圈——选一致组合

---

## C. 光线 + 景别 + 角度 + 运镜 的完整 prompt 框架

```
[角度] [景别] of [主体], [光线方向 + 质感 + 时段或风格], [运镜], [N] seconds, [总风格]
```

**例子**：
- `low angle close-up of warrior, golden hour backlit silhouette, slow dolly in, 6 seconds, epic cinematic`
- `eye level medium shot of couple, blue hour soft window light, static, 5 seconds, melancholic`
- `bird's eye view of city, neon cyberpunk night, drone fly forward, 8 seconds, blade runner aesthetic`
- `high angle wide shot of forest, overcast diffused daylight, tracking shot, 7 seconds, documentary nature`

**核心原则**：每个维度只写最必要的，**别堆砌**——5 个修饰词以内的 prompt 出活率最高，超过 8 个开始抽卡。
