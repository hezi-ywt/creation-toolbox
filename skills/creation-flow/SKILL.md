---
name: creation-flow
description: 创作流水线总调度。用户想做 AI 视频 / 想从故事到 Seedance 提示词 / 整体规划创作时使用。本 skill 是编排级别——不做事，只判断当前阶段并切换到正确的子 skill（story-seed → story-assets → storyboard-drafter → seedance-prompt + asset-index 资产查验）。触发词：创作流程, 从头开始做视频, 帮我从故事到视频, end-to-end video, creation pipeline, from story to seedance。
license: MIT
metadata:
  author: 影视创作工具箱
  version: "0.1.0"
---

# creation-flow

## 这是编排 skill

本 skill **不做具体工作**——它只判断用户当前在创作流水线的哪个阶段，然后切到对应的子 skill。

子 skill 完成一段后回到 creation-flow，由 creation-flow 决定下一步。

## 完整 pipeline

```
[用户] "我想做个故事改成视频"
   ↓
[阶段 1 · 早期创意] → story-seed
   挖矿 / 分岔 / 挑刺 → logline / premise / synopsis
   产出：故事/<名>.md
   ↓
[阶段 2 · 项目化]（按需触发）→ story-assets
   升级目录 + 创建角色卡 / 世界观 / 场景大纲
   产出：故事/<名>/ 目录 + 多个资产 .md
   ↓ 装了 asset-index CLI 时 → asset-index 验证
[阶段 3 · 剧本分镜] → storyboard-drafter
   故事 → 视频语言脚本（用户审稿）
   产出：剧本分镜草稿
   ↓ 用户审核通过
[阶段 4 · Seedance 提示词] → seedance-prompt
   剧本分镜 → Timeline prompt
   产出：可粘贴的 Seedance / 可灵 / Veo / Sora prompt
   ↓
[用户] 拿 prompt 喂 AI 视频模型
```

## 切到哪个子 skill 的判断

| 用户场景 | 切到 |
|---|---|
| "我有个故事想法 / 帮我想故事 / 故事点子" | **story-seed** |
| "logline / premise / synopsis / 三件套" | **story-seed** |
| "故事变复杂 / 加角色 / 加世界观 / 多集 / 做成短剧" | **story-assets** |
| "管理角色 / 世界观 / 场景大纲 .md 资产" | **story-assets** |
| "查 / 找 / 搜 我创建的角色 / 场景 / 剧本" | **asset-index** |
| "把故事做成视频 / 拆分镜 / 剧本分镜" | **storyboard-drafter** |
| "出 Seedance 提示词 / 转 prompt / Timeline prompt" | **seedance-prompt** |
| "整体规划 / 不知道从哪开始" | 留在 creation-flow，问用户具体到哪步 |

## 跨会话 TODO 持久化（重要）

跨阶段切换时**经常会留 TODO**（如 storyboard-drafter 拆分镜时发现"妻子卡未填"、seedance-prompt 出 prompt 时识别"跨集已定要回写"）。这些 TODO **不能只活在当前对话里**——下次回来 AI 必须能恢复。

### 怎么做

每当跨阶段产生 TODO 时，立即写入 `故事/<名>/index.md`（项目化故事）或 `故事/<名>.md`（单文件故事）顶端的"待办"段：

```markdown
# <故事名>

> ⚠️ 待办（YYYY-MM-DD）：
> - 妻子角色卡未填实（第 2、3 集前要补，否则妻子线会偏淡）
> - 跨集已定回写：第 1 集不让观众看清表盘细节 → 影响 2、3 集揭线索方式
> - asset-index check 待跑（用户没装 CLI，装后跑）

## 已定
...
```

### 持久化原则

- **AI 自动写**——不要等用户提醒
- **每个 TODO 标注来源阶段**（哪个 skill / 哪一轮发现的）
- **回到故事时先读"待办"段**：下次激活 story-seed / story-assets / 其他子 skill 时，AI 看到待办先汇报给用户："上次留了 3 个待办，要先处理吗？"
- **完成后划掉**（用 `~~删除线~~`），不要直接删（留痕便于回顾）

## 跨阶段的衔接守则

### story-seed → story-assets（项目化升级）

触发条件（任一）：
- 角色数 > 3
- 涉及世界观 / 设定的深入讨论
- 创作者说"故事变复杂了，要拆开管理"
- 准备转交 storyboard-drafter 拆分镜但单文件信息不够

**必须跟用户确认再升级**——不要自作主张。

### story-assets / story-seed → storyboard-drafter（进入视频阶段）

转交标准：
- 单文件简单故事：logline / premise / synopsis 至少完成
- 项目化故事：场景大纲达到"详细场次卡"级别

### storyboard-drafter → seedance-prompt（审核通过后）

转交标准：**用户明示**"通过 / 这版可以 / 转 prompt / 出 Seedance"——**不要跳过审核**。

### asset-index 介入时机

子 skill 创建 / 修改资产后，如果用户装了 `asset-index-cli`：
- 提示运行 `asset-index check --file <新文件>` 验证
- 项目级查询用 `asset-index search / list / stats`

不强制 —— asset-index 是可选 atomic 工具，没装也能跑全流程。

## 边界

**做**：
- 判断用户当前阶段
- 切到对应子 skill
- 跨阶段衔接（"上一步产出 → 下一步输入"的传递）
- 用户卡住时反问"你现在在哪步"

**不做**：
- ❌ 自己做创作（挖矿 / 分镜 / prompt 都是子 skill 的事）
- ❌ 重复子 skill 内部的规则（那些在子 skill 的 SKILL.md 里）
- ❌ 跨阶段直接切（如 story-seed 直接到 seedance-prompt）—— 中间必须经 storyboard-drafter

## 用户感知

虽然有 5 个 skill 在背后，用户应该感觉是**一个合伙人**。

- AI 不打"skill 标签"（"现在切到 X skill 了" 不要说）
- 阶段切换是无缝的（用户说"加角色" → AI 自然进入资产管理，无需说"现在用 story-assets"）
- 子 skill 之间的细节由 creation-flow 内部处理

## 5 个子 skill 速查

| skill | 干什么 | 产出 |
|---|---|---|
| `story-seed` | 从种子讨论故事，4 角色软切换 + 两态状态机 | 故事 .md（logline + premise + synopsis）|
| `story-assets` | 项目化目录 + 资产管理（角色 / 世界观 / 场景）| 故事/<名>/ 目录 |
| `asset-index` | 资产 .md 索引 / 查询 / 验证（含 npm CLI）| frontmatter 校验 + 查询结果 |
| `storyboard-drafter` | 故事 → 剧本分镜（视频语言脚本草稿）| 剧本分镜.md（待审）|
| `seedance-prompt` | 剧本分镜 → Seedance Timeline prompt | 可粘贴 prompt（中文 / 英文）|

## 衡量做得好不好

每次对话后自检：

1. **阶段识别准确**：判断用户在哪步对了吗？
2. **子 skill 切换自然**：用户感觉无缝吗？
3. **不越界**：creation-flow 自己有没有越权做子 skill 的事？

三个都"是"，编排就成功。
