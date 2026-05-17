# 创作工具箱 / creation-toolbox

> 状态：Beta · 持续迭代中

三个 Claude Code skill，组成 **"从故事到 AI 视频提示词"** 的完整创作流水线 + 资产管理。

## Skills

| Skill | 干什么 | 来源 |
|---|---|---|
| [`story-creator`](./skills/story-creator/) | 从一个种子（一句话 / 一个画面 / 一首歌）跟 AI 协作出故事。三角色软切换（挖矿工 / 分岔者 / 挑刺者）+ 两态状态机（草稿 / 已定）。 | Official |
| [`ai-video-prompt`](./skills/ai-video-prompt/) | 接收故事 → 拆「剧本分镜」草稿等用户审核 → 转 Seedance Timeline 提示词。核心是叙事经济学：拒绝机械均分时长。 | Official |
| [`asset-index`](./skills/asset-index/) | 资产管理（角色 / 世界观 / 场景 / 剧本 / 道具）。基于 frontmatter 的 .md 文件，扫描 / 搜索 / 验证 / 统计。配套 npm 包 `asset-index-cli`，跟 AI 协作做"创建 → 检查闭环"。 | Official |

## 安装

### 方式 1：Claude Code Plugin（推荐 · 一键）

```bash
claude plugin marketplace add hezi-ywt/creation-toolbox
claude plugin install creation-toolbox
```

`asset-index` skill 还需要独立装 npm CLI：

```bash
npm install -g asset-index-cli
```

### 方式 2：手动 link 到 `~/.claude/skills/`（全局可用）

```bash
git clone https://github.com/hezi-ywt/creation-toolbox.git
cd creation-toolbox

# Windows (cmd，普通用户即可)
mklink /J "%USERPROFILE%\.claude\skills\story-creator" "%CD%\skills\story-creator"
mklink /J "%USERPROFILE%\.claude\skills\ai-video-prompt" "%CD%\skills\ai-video-prompt"
mklink /J "%USERPROFILE%\.claude\skills\asset-index" "%CD%\skills\asset-index"

# Mac / Linux
ln -s "$PWD/skills/story-creator" ~/.claude/skills/
ln -s "$PWD/skills/ai-video-prompt" ~/.claude/skills/
ln -s "$PWD/skills/asset-index" ~/.claude/skills/

# 同时装 asset-index CLI
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

# 同时装 asset-index CLI
npm install -g asset-index-cli
```

## 工作流

```
[你]  "我想写个故事"
        ↓ 触发 story-creator
[AI] 挖矿 + 分岔 + 挑刺 → 故事 .md
        ↓
[你]  故事复杂起来了（多角色 / 世界观）
        ↓ 触发 asset-index
[AI] 把角色 / 场景 / 道具拆成独立资产 .md（带 frontmatter），用 asset-index 扫描 / 检查
        ↓
[你]  "把这个故事做成 1 分钟视频"
        ↓ 触发 ai-video-prompt
[AI] 读故事 + 资产 → 拆剧本分镜（草稿）→ 等你审核
[你]  "通过" / "第二场太慢"
[AI] 调整 / 转 Seedance Timeline prompt
        ↓
[你]  prompt 喂 Seedance / 可灵 / Veo / Sora
```

## 文件结构

```
creation-toolbox/
├── .claude-plugin/
│   ├── marketplace.json     # Plugin marketplace 注册
│   └── plugin.json          # Plugin 元数据
├── skills/
│   ├── story-creator/
│   │   ├── SKILL.md
│   │   ├── references/      # 按需加载
│   │   └── tests/
│   ├── ai-video-prompt/
│   │   ├── SKILL.md
│   │   ├── references/      # 8 个维度参考
│   │   │   ├── narrative-economy.md     # 叙事经济学
│   │   │   ├── script-to-storyboard.md  # 剧本分镜骨架
│   │   │   ├── shot-prompt-templates.md # 单场次 prompt 模板
│   │   │   ├── camera-movements.md
│   │   │   ├── lighting.md
│   │   │   ├── shot-size-and-angle.md
│   │   │   ├── composition-and-depth.md
│   │   │   └── pacing-and-duration.md
│   │   └── tests/
│   └── asset-index/
│       ├── SKILL.md         # 需要配套 npm i -g asset-index-cli
│       ├── references/
│       │   ├── schema.md    # 资产 schema + rules.yaml 格式
│       │   └── user-notes.md # 用户偏好（agent 维护）
│       └── evals/
├── scripts/
│   └── validate_skills.py   # 自检工具（零依赖）
├── README.md
└── LICENSE
```

## 设计原则

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

- [asset-index](https://github.com/hezi-ywt/asset-index) — `asset-index` skill 的配套 CLI 源码 + npm 包

## License

[MIT](./LICENSE) © 2026 hezi-ywt

---

灵感来自 [MiniMax-AI/skills](https://github.com/MiniMax-AI/skills) 的 plugin marketplace 设计。
