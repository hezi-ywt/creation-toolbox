---
name: seedance-prompt
description: 剧本分镜 → Seedance Timeline 提示词。当用户说"出 Seedance 提示词 / 转 prompt / Timeline prompt / 出可粘贴的 AI 视频 prompt"时使用。前置：剧本分镜已经过用户审核（由 storyboard-drafter 产出）。本 skill 把每个场次按模板转成 Seedance / 可灵 / Veo / Sora 可粘贴的 Timeline 格式 prompt，含 6 步公式、8 官方运镜、5 大维度参考。
license: MIT
metadata:
  author: 影视创作工具箱
  version: "0.1.0"
---

# seedance-prompt

## 核心理念

AI 视频 prompt 是**工程**——不是文学。

关键工程约束：
- AI 视频模型一次只能生成 5-15s（Seedance 上限）
- 模型**没有记忆**，每次生成完全独立
- 所以剧本分镜的每个场次 → 一次独立 prompt（含完整人物 / 场景描述）

本 skill 负责把审核过的剧本分镜场次**逐场转成 Timeline prompt**，AI 抽卡命中率最高。

## 工作流

```
[输入] 审核过的剧本分镜（来自 storyboard-drafter）
   ↓
[本 skill] 逐场次匹配模板 + 填充 5 维度参考
   ↓
[输出] Timeline 格式 prompt（中文 / 英文 / 中英双版）
   ↓
[用户] 复制粘贴到 Seedance / 可灵 / Veo / Sora
```

## 核心行为

### 行为 ①：剧本分镜 → Timeline prompt

**触发**：用户明示"出 Seedance / 转 prompt / Timeline prompt" + 剧本分镜已审过

**做**：

1. 加载 `references/shot-prompt-templates.md` —— 10 个 15s 单场次模板
2. 逐场次匹配最接近的模板（紧张铺垫 / 追逐戏 / 戏剧化亮相 / 抽离结尾 / 关键道具引入 / 等）
3. 按模板的 5 区块结构填充：
   - 通用提示词（这个模板的全局风格基线）
   - 资产（角色 + 场景）
   - 内容（剧情 + 画面感）
   - 台词 / 音效
   - **分镜剧本**（Timeline 格式 prompt · 中文 + 英文）
4. **关键**：每场 prompt 起头**重新描述**人物 + 资产状态（AI 无记忆）
5. 输出完整 prompt 序列 + 场次间衔接说明

### 行为 ②：用户反馈 → 调 prompt

**触发**：用户说"第 X 场的 prompt 出来效果不对 / 这个运镜不对 / 加个细节"

**做**：
- 不重做整个 prompt，只改对应字段
- 加载对应维度 references（运镜 → camera-movements.md / 光线 → lighting.md / 等）
- 改完给出新版 + 说明改了哪 1-2 处

## 五大原则

### 1. AI 无记忆（再次强调）

**每场 prompt 起头必须重新描述**：
- 人物（年龄 / 服装 / 神情 / 标志特征）
- 关键道具的位置 / 状态
- 场景延续标注

否则 AI 自由发挥——男主可能秒变 25 岁穿牛仔裤。

衔接方法：
- 上场剧本分镜末尾标的"留白 / 结尾状态" → 本场 prompt 起头复述
- 关键角色用 `@image1` 引用同一张参考图锁定面部（Seedance 多模态特性）

### 2. Seedance 6 步公式

每个场次 prompt 含 6 要素：**主体 / 动作 / 环境 / 运镜 / 光线 / 风格**。字数 60-100 词。

### 3. 官方支持的 8 种运镜

稳定出活的：
`push (推) / pull (拉) / pan (摇) / track (跟) / orbit (环绕) / aerial (航拍) / handheld (手持) / fixed (静止)`

**扩展运镜**（`dolly zoom / bullet time / rack focus / whip pan / spiral / long take`）：能用但要多抽卡。

### 4. 单段最多 1 个主运镜 + 1 个主动作

同时写 `dolly in + pan right + tilt up` 必崩。复杂运镜组合 → 拆段生成 + 后期剪辑。

### 5. 危险词清单

| 词 | 为啥危险 | 替换 |
|---|---|---|
| `fast`（不限定）| 全画面乱抖 | 只让**一个元素** fast |
| `cinematic`（单独）| 太模糊 AI 出 generic | 加具体："cinematic 35mm film tone, warm" |
| `epic` | 模型不理解此抽象词 | 描述具体视觉 |
| `amazing` / `beautiful` | 无实际指令价值 | 用具体光线 + 构图替代 |
| `lots of movement` | 画面崩坏 | 描述**单一**具体运动 |

## references/ 使用规则

**按需加载**：

| 场景 | 加载 |
|---|---|
| 转 prompt（行为 ①）| **shot-prompt-templates.md** ⭐ 必加 |
| 写到具体运镜 / 运镜组合 / AI 友好度判断 | camera-movements.md |
| 写到光线 / 时段 / 风格化照明 | lighting.md |
| 写到景别 / 角度 | shot-size-and-angle.md |
| 写到构图 / 景深 | composition-and-depth.md |
| 写到节奏 / 慢动作 / 变速 | pacing-and-duration.md |

**优先做事再加载**——能凭经验写的就别先翻文件。

## 完整 prompt 框架（供参考）

每个场次 prompt 含的字段（来自 shot-prompt-templates.md）：

```
[角度] [景别] of [主体], [动作], in [环境], [构图], [光线],
[景深], [运镜 + 节奏], [N] seconds, [总风格], avoid [负面]
```

实际示例：

```
[0s] high angle wide shot of a middle-aged man in a dark suit walking
     toward a black sedan in an empty parking lot, golden hour light,
     three-layer composition. Camera static.

[4s] Slow dolly in following the man from behind, now medium shot.
     He approaches the car, notices a folded note tucked under the
     windshield wiper. Decelerating, shallow depth of field.

[8s] Close-up on his weathered hands removing the note. Crisp paper
     sound. Dramatic golden hour rim light.

[12s] Extreme close-up on his eye, dolly zoom effect over 3 seconds.
      Pupil constricts, background warps subtly.

global: cinematic, 35mm film grain, suspense thriller mood
```

详细模板和场景对应见 `references/shot-prompt-templates.md`。

## 边界

**做**：
- 剧本分镜场次 → Seedance Timeline prompt（中 / 英 / 中英）
- 套场次模板（紧张铺垫 / 追逐戏 / 等 10 种）
- 应用 5 维度参考（运镜 / 景别角度 / 光线 / 构图景深 / 节奏时长）
- 跨场次 AI 无记忆衔接说明

**不做**：
- ❌ **拆剧本分镜** —— storyboard-drafter 的事
- ❌ **审核剧本分镜对错** —— 假设审核通过
- ❌ **改故事 / 改资产** —— story-seed / story-assets 的事
- ❌ **实际调用 Seedance API 生成视频** —— 用户在 Seedance 平台做
- ❌ **后期剪辑指令 / 调色 / 音乐制作** —— 超出 prompt 阶段

## 跟其他 skill 衔接

- **输入来自 storyboard-drafter**：已审过的剧本分镜
- **由 creation-flow 总调度**
- **不调用其他 skill**——这是流水线最后一棒

## 衡量做得好不好

1. **AI 无记忆处理**：每场 prompt 起头都重新描述人物 / 资产了？
2. **6 步公式齐**：主体 / 动作 / 环境 / 运镜 / 光线 / 风格都有？
3. **单段最多 1 个主运镜**：没堆 dolly + pan + tilt？
4. **没用危险词**：没写孤零零的 fast / cinematic / epic？
5. **官方 8 运镜优先**：扩展运镜（dolly zoom 等）只在必要时用？

五个都"是"才算成功。
