# 创作工具箱 / creation-toolbox

> 状态：Beta · 持续迭代中

**6 个 Claude Code skill** 组成 **"从故事到 AI 视频提示词"** 的完整创作流水线。1 个编排 skill 总调度，5 个 atomic skill 各做一件事。

## 架构（orchestrator + atomic）

```
                  [creation-flow 总调度]
                          ↓
   ┌──────────────────────────────────────────────────┐
   │  story-seed → story-assets → storyboard-drafter   │
   │              ↕ asset-index ↕                       │
   │                       → seedance-prompt            │
   └──────────────────────────────────────────────────┘
```

## Skills

| Skill | 类型 | 干什么 |
|---|---|---|
| [`creation-flow`](./skills/creation-flow/) | **编排** | 总调度——判断用户当前在创作哪一步，切到对应子 skill。不自己做事 |
| [`story-seed`](./skills/story-seed/) | atomic | 从种子讨论故事（早期）· 三角色软切换（挖矿 / 分岔 / 挑刺）+ 两态状态机（草稿 / 已定）· 输出 logline / premise / synopsis |
| [`story-assets`](./skills/story-assets/) | atomic | 项目化资产管理（中后期）· 升级 `故事/<名>/` 目录 + 创建角色卡 / 世界观 / 场景大纲 / 多集架构 + 防剧本污染 |
| [`asset-index`](./skills/asset-index/) | atomic | 资产 frontmatter 索引 / 查询 / 验证 · 配套 npm 包 [`asset-index-cli`](https://www.npmjs.com/package/asset-index-cli) |
| [`storyboard-drafter`](./skills/storyboard-drafter/) | atomic | 故事 → 剧本分镜（视频语言脚本草稿）· 审稿层 · 核心原则：不机械均分时长 |
| [`seedance-prompt`](./skills/seedance-prompt/) | atomic | 剧本分镜 → Seedance Timeline 提示词 · 6 步公式 + 8 官方运镜 + 5 维度参考 + AI 无记忆衔接 |

## 5 分钟跑通完整流程

👉 **[Quickstart 教程](./QUICKSTART.md)** —— 跟着把"便利店猫"种子做成可粘贴的 Seedance prompt，看 6 个 skill 怎么自动接力。

## 工作流

```
[你] "我想做个故事改成视频"
        ↓ creation-flow 识别阶段
[story-seed] 挖矿 + 分岔 + 挑刺 → 故事/<名>.md（logline + premise + synopsis）
        ↓ 故事复杂（多角色 / 世界观 / 分集）
[story-assets] 升级 故事/<名>/ 目录 + 创建角色卡 / 世界观 / 场景大纲
        ↓（可选）
[asset-index] 验证 frontmatter / 查询资产 / 跨集一致性
        ↓ "把故事做成视频"
[storyboard-drafter] 拆剧本分镜（草稿）→ 等你审稿
        ↓ "通过"
[seedance-prompt] 转 Seedance Timeline prompt（中 / 英 / 中英）
        ↓
[你] prompt 喂 Seedance / 可灵 / Veo / Sora
```

## 安装

### 方式 1：Claude Code Plugin（推荐 · 一键）

```bash
claude plugin marketplace add hezi-ywt/creation-toolbox
claude plugin install creation-toolbox
```

asset-index skill 配套 npm CLI 单独装：

```bash
npm install -g asset-index-cli
```

### 方式 2：手动 link 到 `~/.claude/skills/`（全局）

```bash
git clone https://github.com/hezi-ywt/creation-toolbox.git
cd creation-toolbox

# Windows
for %s in (creation-flow story-seed story-assets asset-index storyboard-drafter seedance-prompt) do mklink /J "%USERPROFILE%\.claude\skills\%s" "%CD%\skills\%s"

# Mac / Linux
for s in creation-flow story-seed story-assets asset-index storyboard-drafter seedance-prompt; do
  ln -s "$PWD/skills/$s" ~/.claude/skills/
done

npm install -g asset-index-cli
```

### 方式 3：仅当前项目用

```bash
git clone https://github.com/hezi-ywt/creation-toolbox.git
cd creation-toolbox

# Windows
mklink /J .claude\skills skills
# Mac / Linux
mkdir -p .claude && ln -s ../skills .claude/skills

npm install -g asset-index-cli
```

## 文件结构

```
creation-toolbox/
├── .claude-plugin/
│   ├── marketplace.json
│   └── plugin.json
├── skills/
│   ├── creation-flow/                  # 编排 skill
│   │   └── SKILL.md
│   ├── story-seed/                     # 早期创意
│   │   ├── SKILL.md
│   │   ├── references/                 # excavation / beat / anti-cliches / genre / finale
│   │   └── tests/
│   ├── story-assets/                   # 项目化资产
│   │   ├── SKILL.md
│   │   └── references/                 # character / world / scene / asset-rules / hygiene / multi-episode
│   ├── asset-index/                    # 资产索引（配套 npm CLI）
│   │   ├── SKILL.md
│   │   ├── references/                 # schema / user-notes
│   │   └── evals/
│   ├── storyboard-drafter/             # 剧本分镜（审稿层）
│   │   ├── SKILL.md
│   │   ├── references/                 # narrative-economy / script-to-storyboard
│   │   └── tests/                      # ABtest 历史
│   └── seedance-prompt/                # Timeline prompt
│       ├── SKILL.md
│       └── references/                 # shot-prompt-templates + 5 维度参考
├── scripts/
│   └── validate_skills.py              # 自检工具（零依赖）
├── README.md
└── LICENSE
```

## 设计原则

- **编排 + atomic**：6 个 skill 各做一件事，creation-flow 串起来
- **创作者主权**：AI 当问问题的合伙人，不抢笔
- **AI 无记忆约束**：Seedance 每次生成独立，prompt 设计要重述人物 / 资产
- **不机械均分**：剧本分镜按戏剧节奏分配时长（关键场 30-60s，过场 3-10s）
- **草稿可改**：场次用标题不用序号，散文为主，待商榷挂出
- **资产即文件**：角色 / 世界观 / 场景都是 .md + frontmatter，git 友好，无需数据库

## 开发自检

修改 / 新增 skill 时跑一下：

```bash
python scripts/validate_skills.py
```

零依赖（纯 Python 标准库）。检查：SKILL.md 存在、frontmatter 可解析、name 跟目录名一致、必填字段、无硬编码 secrets。

## 相关项目

- [asset-index](https://github.com/hezi-ywt/asset-index) — asset-index skill 的配套 CLI 源码 + npm 包（[npmjs.com/package/asset-index-cli](https://www.npmjs.com/package/asset-index-cli)）

## License

[MIT](./LICENSE) © 2026 hezi-ywt

---

灵感来自 [MiniMax-AI/skills](https://github.com/MiniMax-AI/skills) 的 plugin marketplace 设计 + orchestrator pattern。
