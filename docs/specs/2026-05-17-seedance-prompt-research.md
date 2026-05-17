---
description: Seedance 2.0 提示词调研快照（2026-05-17）。6 步公式、8 种官方运镜、Timeline Prompting [0s][3s][6s] 格式、@image / @video / @audio 引用语法、避坑清单、与 Veo / Sora / Runway 对比。Seedance 专属 prompt 写法、多模态引用时参考。
---

# Seedance 2.0 提示词攻略调研

> 调研日期：2026-05-17
> 调研基础：6 个权威来源（字节官方 blog、Apiyi 官方手册解读、MindStudio Timeline 专文、fal.ai 集成方指南、ChatCut 5 公式、TheSeanClaude Substack 完整指南）+ 多个英中文搜索摘要
> 用途：与本地通用知识库（运镜 / 景别角度 / 光线 / 构图景深 / 节奏时长）对照，补充实战经验
> 状态：v0.1 调研快照（Seedance 持续更新，建议每季度复查）

---

## TL;DR — 7 条跨源核心共识

1. **6 步公式是主流**，但顺序有分歧（详见第二章）。**共同要素**：主体 / 动作 / 环境 / 运镜 / 光线 / 风格
2. **官方运镜只有 8 种术语**：push/pull/pan/track/orbit/aerial/handheld/fixed —— 比我们 25 条少很多，但每条都"AI 听得懂"
3. **prompt 长度 60-100 词最佳**，超 150 词 AI "回归平均"（说人话：胡乱出片）
4. **光线是杠杆最高的元素**——官方手册原话：单行光线描述 > 十个形容词
5. **只用一个主运镜**：堆叠两个运镜是抖动乱帧的头号原因
6. **多模态参考用 @ 语法**：`@image1`、`@video1`、`@audio1` 在 prompt 里精确指代
7. **音视频一体化是 2.0 核心新功能**：声音和画面在同一次生成里时序锁定，不用后期同步

---

## 一、Seedance 2.0 是什么

- **发布时间**：2026 年 2 月（字节即梦平台上线）
- **核心定位**：字节豆包大模型团队的多模态视频生成模型
- **关键升级 vs 1.5**：
  - 统一多模态架构（文 / 图 / 视频 / 音频任意组合）
  - 双声道立体声（一次生成自带音轨）
  - 多镜头序列一次生成（4-15s）
  - 视频编辑 + 视频延续（不用重新生成）
  - 复杂运动稳定性提升、指令跟随能力升级
- **输入能力**：最多 9 张图 + 3 段视频 + 3 段音频 + 自然语言
- **官方推荐场景**：商业广告、解说视频、多人互动竞技、专业音视频内容

---

## 二、官方 prompt 结构公式（4 个版本对比）

各家攻略的公式略有不同，但**6 个要素是共识**：

| 来源 | 顺序 | 字数建议 |
|---|---|---|
| **Apiyi（官方手册解读）** | 主体 → 动作 → 环境 → 运镜 → 风格 → 约束 | 60-100 词 |
| **TheSeanClaude** | 运镜 → 主体 → 动作 → 环境 → 光线 → 风格 | 50-70 词 |
| **fal.ai** | 主体 + 动作 → 运镜 → 音效 → 镜头切换 | 35-80 词 |
| **中文社区（即梦）** | 主体 + 动作 + 场景 + 光影 + 镜头 + 风格 + 画质 + 约束 | 灵活 |

### 我的判断

- **顺序差异不致命**——只要 6 个要素都在
- **关键是分明扣**：每个要素一句话，别混在一起。比如不要写"a beautiful slow dolly in toward woman in romantic golden light forest"，要写：
  > **主体**: woman, **动作**: gently turns head, **环境**: forest at golden hour, **运镜**: slow dolly in, **光线**: warm sidelight, **风格**: cinematic
- **字数甜区：60-80 词**——保守取 Apiyi 和 TheSeanClaude 的交集

### 标准模板

```
[主体描述], [动作描述], in [环境 + 光线], camera [运镜], [风格修饰], [N] seconds, avoid [负面].
```

---

## 三、官方支持的 8 种运镜清单

**这是关键发现**——官方手册明确列出的"AI 听得懂"的运镜术语只有 8 个：

| 中文 | 英文 | 与本地知识库对应 |
|---|---|---|
| 推镜 | push-in / dolly in | [运镜.md 第 1 条](运镜.md) |
| 拉镜 | pull-out / dolly out | [运镜.md 第 6 条](运镜.md) |
| 摇镜 | pan / lateral motion | [运镜.md 第 2 条](运镜.md) |
| 跟镜 | tracking shot / follow | [运镜.md 第 8 条](运镜.md) |
| 环绕 | orbit / arc | [运镜.md 第 18 条](运镜.md) |
| 航拍 | aerial / drone shot | [运镜.md 第 14 条](运镜.md) |
| 手持 | handheld | [运镜.md 第 5 条](运镜.md) |
| 固定 | fixed / locked-off | [运镜.md 第 25 条](运镜.md) |

### 我的判断

- **我们 25 条覆盖了官方 8 条 + 17 条扩展**（含希区柯克变焦、荷兰角、拉焦、子弹时间、长镜头等）
- **官方 8 条在 Seedance 上稳定出活**；扩展的 17 条**理论上能用但要多抽卡**——这跟我们标的"难度评级"方向一致
- **可灵 / Veo / Sora 也认识扩展的 17 条**（基于训练数据相似性），所以保留全集合理

### 给本地知识库的修订建议

在运镜.md 每条加一行 **"Seedance 友好度"**：
- ✅ 官方 8 条
- ⚠️ 扩展条目（手抽多次）
- ❓ 高难（dolly zoom / bullet time 等）

---

## 四、长度与节奏的硬规则

来自 5 个来源的共识：

| 规则 | 来源 |
|---|---|
| 单镜头 prompt 60-100 词 | Apiyi、TheSeanClaude、ChatCut |
| 超 150 词 AI"回归平均" | TheSeanClaude |
| 单镜头最多 1 个主运镜 + 1 个主动作 | Apiyi、fal.ai、官方 |
| 10-15 秒视频不超过 4 个镜头 | fal.ai |
| 5 秒视频 2-3 个 beat / 10 秒 3-4 个 | MindStudio |

### 危险词（六源共同警告）

| 词 | 为什么危险 | 替代写法 |
|---|---|---|
| `fast` | 不限定主体的快会导致全画面乱抖 | 只让**一个元素**fast（e.g. "fast moving water"）|
| `cinematic`（单独使用）| 太模糊，AI 出 generic | 加具体描述："cinematic 35mm film tone, warm" |
| `epic` | 模型不理解此抽象词 | 描述具体视觉（"vast mountain backdrop"）|
| `amazing` / `beautiful` | 无实际指令价值 | 用具体光线 + 构图替代 |
| `lots of movement` | 引发画面崩坏 | 描述**单一**具体运动 |

---

## 五、Timeline Prompting（Seedance 独门高级技巧）

来自 MindStudio 专文。这是 Seedance 2.0 区别于其他模型的**结构化进阶写法**。

### 格式

用方括号时间戳分段：

```
[0s] 建立场景描述
[3s] 第一个动作 / 运镜
[6s] 第二个 beat
[8s] 收尾 / hold
```

**5 秒视频**：用 `[0s]` `[2s]` `[4s]`
**10 秒视频**：用 `[0s]` `[3s]` `[6s]` `[8s]`

### 完整示例

```
[0s] Wide shot: A figure in a long coat stands at an empty rain-slicked city street at night.
     Camera static, framed from behind. Neon signs reflect in puddles.
[3s] Slow dolly forward begins, closing in from behind. Rain falls in foreground,
     shallow depth of field with bokeh streetlights.
[6s] Camera continues push in, now medium shot. Figure turns head slightly—
     profile barely visible. Tension holds.
[8s] Rack focus: background city blur sharpens briefly, then returns to subject.
     Cinematic, 35mm film grain, desaturated with cold blue tones, anamorphic lens flare.
```

### 适合 / 不适合

| 适合 ✅ | 不适合 ❌ |
|---|---|
| 角色渐次揭示 | 快剪蒙太奇（分镜独立生成更好）|
| 自然渐进式揭示 | 复杂多角色互动 |
| 商业产品旋转展示 | 跨地点硬切（用 cut 切，不要 timeline）|
| 戏剧张力构建 | |
| 5-10 秒内的叙事推进 | |

### 给本地知识库的修订建议

在 [节奏与时长.md](节奏与时长.md) 添加"Timeline Prompting"专章——这是单镜头内"自带分镜"的官方推荐写法，比单 prompt 出片质感强很多。

---

## 六、多模态参考语法（@ 引用）

来自 ChatCut + 字节官方 blog。**这是 Seedance 2.0 最强的"控制权"工具**——上传参考资料后，必须在 prompt 里明示每个参考的用途。

### 基本语法

```
@image1 作为产品设计参考
@image2 作为主体角色参考
@video1 作为运镜方式参考
@audio1 作为音乐氛围参考
```

### 关键原则

> "Seedance 不能可靠推断每个文件的用途，除非你明确说明。" —— ChatCut

参考资源优先级（按 Seedance 训练倾向）：
1. **摄影 / 运动参考**（最强影响）
2. **主体一致性参考**
3. **氛围 / 音乐参考**

### 5 套场景化公式（基于多模态参考）

| 公式 | 用途 | 示例 |
|---|---|---|
| **A. 基础多模态** | 综合使用图 + 视频 + 音频 | `@image1 作为产品 @video1 作为运镜 @audio1 作为音乐... [时间轴]` |
| **B. 镜头参考复用** | 把已有视频的运镜"借"给新主体 | `参考 @video1 的镜头工作，生成紧张走廊场景，希区柯克变焦` |
| **C. 视频延续** | 在已有视频基础上延长 | `延续 @video1 6秒。0-2s：镜头上倾。2-4s：蒸汽升起` |
| **D. 目标编辑** | 改原视频里某个元素 | `保留 @video1 的运动和镜头路径。将角色头发改为长红发` |
| **E. 效果借用** | 借用转场或视觉效果 | `参考 @video1 的拼图碎裂转场。使用 @image1 作为主体` |

### 中文 prompt 写法

中文社区实例（搜索摘要）：

```
@图片1的女星作为主体，参考@视频1的运镜方式进行有节奏的推拉摇移
```

中英文都支持，但**英文精度更高**（训练数据偏英文）。中文 prompt 适合：
- 中文场景描述（古装、仙侠、汉字招牌）
- 中文社区参考
- 中文人物姓名 / 文化符号

---

## 七、综合避坑清单（六源共识）

### 必带的负面 prompt（避免常见失败模式）

```
avoid: jitter, bent limbs, temporal flicker, identity drift, chaotic composition,
       distorted hands, extra fingers, blurred subject
```

中文版：

```
避免：抖动、扭曲四肢、时间闪烁、身份漂移、混乱构图、手部畸形、多手指、主体模糊
```

### Top 10 常见错误

1. **冲突运镜**：同时写 `dolly in` + `pan right` + `tilt up` → 必崩
2. **抽象词堆叠**：`epic, amazing, cinematic, beautiful` → AI 蒙圈
3. **camera 和 subject 动作混淆**：`spinning camera around dancing person` 不如 `the dancer spins slowly. Camera holds fixed framing.`
4. **过长 prompt**：超 150 词后冲突指令暴增
5. **技术参数**：`f/2.8, ISO 800, 24fps` AI 听不懂（fal.ai 明确警告）
6. **没有光线描述**：默认 generic 光，丢掉"出片感"杠杆
7. **不分离对话和动作**：`she says "I love you" while walking` → 试 `she walks. She softly says "I love you."`
8. **品牌 / 后期术语**：rotoscope、composite、ARRI Alexa 等 AI 不认识
9. **10-15 秒塞 4+ 镜头**：建议分段生成后剪辑
10. **不写多模态参考用途**：上传了图但没说"@image1 用作 X"，AI 自己猜

### 对话场面专门技巧（来自总览）

不要写：`she says "Just looking at you."`

要写：`she softly whispers "Just looking at you."` —— **先标情绪 + 语气**，再上对白。

---

## 八、音视频一体化（Seedance 2.0 杀手锏）

**核心机制**：声音和画面在**同一次推理**里生成 → 时序天然锁定（无需后期对齐）

### 写法

在 prompt 里直接描述音频：

```
sound: ice clinking, distant traffic, soft jazz playing low
ambient: rain on windows, distant thunder
dialogue: she whispers "stay"
music: minimal piano, ambient pad
```

或用 @audio 参考：

```
@audio1 作为环境基调
```

### 已知限制（fal.ai 报告）

- **环境音 / 音效**：质量最强
- **音乐**：质量很好
- **对话唇音同步**：参差，对话密集场景建议先小范围测试
- **复杂多人对话**：偶有错位

### 与本地知识库的关系

我们的 [节奏与时长.md](节奏与时长.md) 没覆盖音频——是不是要补一份？我倾向**等做题材手册后再决定**，因为音频用法跟题材高度绑定（动作片 / 文艺片 / 广告音乐风完全不同）。

---

## 九、与其他视频模型的对比（fal.ai 视角）

| 维度 | Seedance 2.0 | Veo 3 | Sora 2 | Runway Gen-4 |
|---|---|---|---|---|
| 单次时长 | 5-10s（多镜可达 15s） | 8s | 5-60s | 5-10s |
| 多模态输入 | **极强**（9 图 + 3 视频 + 3 音频）| 中 | 中 | 中 |
| 音视频一体 | **原生**（一次生成）| 后期同步 | 部分 | 后期同步 |
| 多镜头一次生成 | **支持** | 不支持 | 部分 | 不支持 |
| 运镜精控 | 中（8 个官方稳定）| 强 | 极强 | 中 |
| 物理真实 | 强（2.0 升级）| 强 | 极强 | 中 |
| 中文友好 | **最强**（字节出品）| 弱 | 中 | 弱 |
| 价格（720p）| $0.30/s 标准, $0.24/s 快速 | 较高 | 极高 | 中 |

### 选模型的判断

- **中文题材 + 多模态资源在手** → Seedance（首选）
- **极致物理真实 + 长镜头** → Sora 2
- **单镜头精控 + 多模型对照** → Veo 3
- **预算敏感 + 快速迭代** → Runway

---

## 十、对本地知识库的 4 大启示

### 启示 1：运镜.md 加 "Seedance 友好度" 标签

**做法**：每条运镜加一行：

```
**Seedance 友好度**：✅ 官方支持 / ⚠️ 扩展 / ❓ 高难需多抽
```

**8 条 ✅**：dolly in / dolly out / pan / tracking / orbit / drone / handheld / static
**约 12 条 ⚠️**：tilt / dutch tilt / crane up/down / steadicam / truck / zoom / OTS / POV / top-down 等
**约 5 条 ❓**：dolly zoom / bullet time / rack focus / whip pan / spiral / long take

### 启示 2：节奏与时长.md 加 Timeline Prompting 专章

这是 Seedance 独家的"单 prompt 自带分镜"技巧，价值极高。建议加在末尾 **"六、Timeline Prompting（Seedance 2.0 专属）"** 章节，包含格式、示例、适用 / 不适合场景。

### 启示 3：单独建一份 `多模态与参考语法.md`

@ 引用语法是 Seedance 强项，现有 5 份维度文档都没覆盖。建议新建一份独立文档：
- @image / @video / @audio 语法
- 5 套场景化公式（基础 / 镜头复用 / 视频延续 / 目标编辑 / 效果借用）
- 参考资源优先级
- 中英文 prompt 对比

### 启示 4：完整 prompt 框架对齐 Seedance 6 步公式

我们目前的框架（在 [节奏与时长.md](节奏与时长.md) 末尾）：

```
[角度] [景别] of [主体], [构图], [光线], [景深], [运镜 + 节奏], [N] seconds, [总风格]
```

对照 Seedance 6 步（主体 / 动作 / 环境 / 运镜 / 光线 / 风格 / 约束），**少了**：
- 明确的 **动作** 字段
- **约束 / 负面 prompt** 字段

建议修订为：

```
[角度] [景别] of [主体], [动作], in [环境], [构图], [光线], [景深], [运镜 + 节奏], [N] seconds, [总风格], avoid [负面]
```

---

## 十一、下一步建议

1. **立即可做（小改）**：按"启示 1"在运镜.md 加 Seedance 友好度标签（半小时活）
2. **下一份新文档**：按"启示 3"建 `多模态与参考语法.md`（200-300 行，参考本调研第六章）
3. **题材手册做之前**：先按"启示 4"修订完整 prompt 框架，让题材手册的模板都基于新框架
4. **延后再做**：音频专题（启示 2 之外的音频深入）—— 等题材手册推进后判断是否单独成文

---

## 来源链接

### 主要 fetch 源
- [Apiyi: Seedance 2.0 Official Prompt Guide In-depth Interpretation](https://help.apiyi.com/en/seedance-2-0-prompt-guide-video-generation-camera-style-tips-en.html)
- [MindStudio: Timeline Prompting with Seedance 2.0](https://www.mindstudio.ai/blog/timeline-prompting-seedance-2-cinematic-ai-video)
- [字节官方: Official Launch of Seedance 2.0](https://seed.bytedance.com/en/blog/official-launch-of-seedance-2-0)
- [fal.ai: How to Use Seedance 2.0 Like a Pro In 2026](https://fal.ai/learn/tools/how-to-use-seedance-2-0)
- [ChatCut: Seedance 2.0 Prompt Guide - 5 Formulas](https://chatcut.io/blog/seedance-2-prompt-guide)
- [TheSeanClaude (Substack): Seedance 2.0 Full Prompting Guide](https://theseanclaude.substack.com/p/seedance-20-prompt-guide-how-to-get)

### 其他搜索覆盖（未深 fetch 但摘要已用）
- [Seedance 2.0 Prompt Guide 2026: 30+ Copy-Paste Prompts](https://www.seedance.tv/blog/seedance-2-0-prompt-guide)
- [Atlabs AI: The Ultimate Seedance 2.0 Prompting Guide](https://www.atlabs.ai/blog/the-ultimate-seedance-2.0-prompting-guide-47-prompts-2026)
- [Higgsfield: Seedance 2.0 Complete Prompting Guide](https://higgsfield.ai/blog/seedance-prompting-guide)
- [字节官方 byteplus 文档](https://docs.byteplus.com/en/docs/ModelArk/2222480)
- [知乎: 即梦 Seedance 2.0 官方手册全拆解](https://zhuanlan.zhihu.com/p/2008546867957485869)
- [知乎: Seedance 2.0 提示词攻略 - 公式](https://zhuanlan.zhihu.com/p/2005428746417640272)
- [CSDN: 80+ 提示词完全指南](https://blog.csdn.net/m0_57545130/article/details/158729752)
- [GitHub: seedance-prompts curated resources](https://github.com/seedanceprompts/seedance-prompts)
- [seedance2prompt.com 集合站](https://www.seedance2prompt.com/)
