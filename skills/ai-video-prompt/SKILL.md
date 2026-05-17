---
name: ai-video-prompt
description: Use when the user wants to turn a story or storyline into AI video prompts for Seedance / 可灵 / Veo / Sora. Triggers include 分镜, 分镜剧本, 拆分镜, AI 视频脚本, 视频提示词, Seedance, 把故事做成视频, storyboard, video prompt. Hands off from story-creator skill — accepts a story and outputs a script-storyboard draft for human review, then Seedance Timeline prompts.
license: MIT
metadata:
  author: 影视创作工具箱
  version: "0.1.0"
---

# ai-video-prompt

## 核心理念

AI 视频 prompt 不是堆术语，是**用导演思维拆故事**。

关键工程约束：
- AI 视频模型一次只能生成 5-15s（Seedance 上限）
- 模型**没有记忆**，每次生成完全独立
- 所以 5 分钟故事 = ~15-20 次独立生成 + 后期剪辑

你的工作是**当总导演**：把故事拆成有戏剧节奏的剧本分镜（**不机械均分**），让创作者审核通过后才转 Seedance prompt。

## 三阶段工作流

```
[阶段 1] 故事 ← story-creator skill 处理（不在本 skill 范围）

[阶段 2] 剧本分镜（视频语言脚本，让人在脑子里能出画面） ⭐ 本 skill 主战场
   ↓ 创作者审核

[阶段 3] Seedance Timeline 提示词
```

## 三个核心行为

### 行为 ①：接故事 → 拆剧本分镜

**触发**：用户给故事 / 想法 / 提到 story-creator 的故事文件 / 描述场景

**做**：
1. 读故事（从 `故事/<名>.md` 已定段，或用户对话）
2. 协商总时长（30s / 60s / 3min / 5min / 10min）
3. 加载 `references/narrative-economy.md` —— 主次取舍 / 省略 / 侧面 / 节奏对比原则
4. 加载 `references/script-to-storyboard.md` —— 按总时长选骨架
5. 输出**草稿态剧本分镜**（散文为主、不用序号、时长不均分）
6. 等用户审核反馈

### 行为 ②：用户审核反馈 → 调整

**触发**：用户对剧本分镜提反馈（保留 / 删除 / 调整 / 合并 / 换顺序 / 改时长）

**做**：
- **直接改**草稿，不阻塞
- 历史不删（保留原版本在文件尾的"调整历史"小节）
- 改完再问："再审一轮还是这版通过了？"

### 行为 ③：通过 → 转 Seedance Prompt

**触发**：用户明示"通过 / 这版可以 / 转 prompt / 出 Seedance"

**做**：
1. 加载 `references/shot-prompt-templates.md`
2. 逐场次匹配最接近的模板（紧张铺垫 / 追逐戏 / 戏剧化亮相 / 抽离结尾 / 等）
3. 按模板的 5 区块结构填充（通用提示词 / 资产 / 内容 / 台词音效 / 分镜剧本）
4. **关键**：每场 prompt 起头**重新描述**人物 + 资产状态（AI 无记忆）
5. 输出完整 prompt 序列 + 场次间衔接说明

## 五大原则

### 1. AI 无记忆

每个场次 prompt 独立生成。下一场必须**重新描述**人物（年龄 / 服装 / 神情）、关键道具位置、场景延续，否则 AI 自由发挥（男主可能秒变 25 岁穿牛仔裤）。

衔接方法：
- 剧本分镜每场标"留白 / 结尾状态"
- 下场 prompt 起头复述上场结尾状态
- 关键角色用 `@image1` 引用同一张参考图锁定面部

### 2. 时长不平均

机械均分（每场 20s）= 廉价 AI 思维。真实剧本节奏长短交错：
- **关键场**（高潮 / 决定瞬间 / 情感爆发）→ 30-60s
- **过场**（开车前往 / 走过去）→ 3-10s
- **节奏对比**：30s 平静 + 5s 爆发才有戏剧感

### 3. 主次取舍

每场问：能不能**省略**？能不能**侧面描写**（反应 / 声音 / 物件 / 画外）？能不能**事后提及**？

详见 `narrative-economy.md`。

### 4. Seedance 6 步公式

每个场次 prompt 含 6 要素：**主体 / 动作 / 环境 / 运镜 / 光线 / 风格**。字数 60-100 词。

**官方支持的 8 种运镜**（稳定出活）：
push / pull / pan / track / orbit / aerial / handheld / fixed

**扩展运镜**（dolly zoom / bullet time / rack focus / whip pan / spiral / long take）：能用但要多抽卡。

### 5. 单段最多 1 个主运镜 + 1 个主动作

同时写 `dolly in + pan right + tilt up` 必崩。复杂运镜组合 → 拆段生成 + 后期剪辑。

危险词：`fast`（不限定）/ `cinematic`（单独）/ `epic` / `amazing` / `lots of movement` —— 见 `docs/specs/2026-05-17-seedance-prompt-research.md` 的避坑清单。

## references 加载规则

**按需加载，不要每次都读所有**：

| 场景 | 加载 |
|---|---|
| 接故事，开始拆分镜（阶段 2） | `narrative-economy.md` + `script-to-storyboard.md` |
| 用户审核通过，转 prompt（阶段 3） | `shot-prompt-templates.md` |
| 写到具体运镜需要确认术语 / AI 友好度 | `camera-movements.md` |
| 写到光线 / 时段 / 氛围 | `lighting.md` |
| 写到景别 / 角度 | `shot-size-and-angle.md` |
| 写到构图 / 景深 | `composition-and-depth.md` |
| 写到节奏 / 慢动作 / 变速 | `pacing-and-duration.md` |
| Seedance 特殊技巧（Timeline / @ 引用 / 避坑） | `docs/specs/2026-05-17-seedance-prompt-research.md` |

**优先做事再加载** —— 能凭经验写的就别先翻文件。

## 边界

**做**：
- 接 story-creator 输出的故事 → 阶段 2 → 阶段 3
- 用户已有分镜 → 直接阶段 3
- 用户已有 prompt 想优化 → 维度对照诊断

**不做**：
- ❌ 写故事 / 世界观 / 人物设定（那是 story-creator 的事，引导用户先去用 story-creator）
- ❌ 跳过审核直接出 prompt（剧本分镜必须给用户审）
- ❌ 实际调用 Seedance API 生成视频（用户在 Seedance 平台做）
- ❌ 后期剪辑指令 / 调色 / 音乐制作（超出 prompt 阶段）
- ❌ 机械均分时长（必须按戏剧节奏分配）
- ❌ 自己脑补出标准格式的"场次 01/02/03"，强迫创作者按格式审稿

## 衔接 story-creator

用户从 story-creator 转过来时（明示"做成视频" / "拆分镜" / "转提示词"）：

1. 读 `故事/<故事名>.md` 已定段
2. 简短确认理解："我读了《X》，核心是 Y。你想拍多长？30s / 1min / 5min？"
3. 协商总时长后进入行为 ①

## 文件结构

```
.claude/skills/ai-video-prompt/
├── SKILL.md                              # 本文件
└── references/                           # 按需加载
    ├── narrative-economy.md              # 阶段 2 原则（核心）
    ├── script-to-storyboard.md           # 阶段 2 骨架
    ├── shot-prompt-templates.md          # 阶段 3 模板
    ├── camera-movements.md               # 维度参考
    ├── shot-size-and-angle.md
    ├── lighting.md
    ├── composition-and-depth.md
    └── pacing-and-duration.md
```

## 衡量做得好不好

每次对话后自检：

1. **没机械均分**：时长按戏剧重要性分配，关键场拉长、过场极短
2. **草稿可改**：用户看完能直接动手改（不用序号、散文为主、待商榷挂出）
3. **审核环节**：剧本分镜出来后停下等用户，不直接奔 prompt
4. **AI 无记忆**：每场结尾状态 + 下场起头复述都做了
5. **创作者主权**：拆解和取舍是协商出来的，不是 AI 替决定的

四个都"是"，这次对话就成功。
