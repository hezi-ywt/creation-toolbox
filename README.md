# 创作工具箱

两个 Claude Code skill，组成完整的"从故事到 AI 视频"创作流水线。

## 包含的 skill

### [story-creator](./skills/story-creator/)

从一个种子（一句话 / 一个画面 / 一首歌）跟 AI 协作出故事。**三角色软切换**（挖矿工 / 分岔者 / 挑刺者），**两态状态机**（草稿 / 已定），让 AI 当问问题的合伙人而不是替你写故事。

### [ai-video-prompt](./skills/ai-video-prompt/)

接收 story-creator 输出的故事，**三阶段**拆解为 AI 视频提示词：

```
故事 → 剧本分镜（视频语言脚本，让人审核） → Seedance Timeline 提示词
```

核心是**叙事经济学**：拒绝机械均分时长，按戏剧重要性主次分明。配套维度知识库（运镜 / 景别角度 / 光线 / 构图景深 / 节奏时长）按需加载。

## 安装到自己的 Claude Code

```bash
# 1. clone
git clone https://github.com/<你的用户名>/创作工具箱.git
cd 创作工具箱

# 2. 让 Claude Code 识别 skills

# Windows（PowerShell，需要开发者模式或管理员）
New-Item -ItemType Junction -Path .claude\skills -Target skills

# Windows（cmd，普通用户即可，推荐）
mklink /J .claude\skills skills

# Mac / Linux
mkdir -p .claude && ln -s ../skills .claude/skills
```

或者直接把 `skills/` 下的两个文件夹复制到 `~/.claude/skills/`（全局可用）。

## 工作流示意

```
[你] "我想写个故事"
   ↓ 触发 story-creator skill
[AI] 挖矿 + 分岔 + 挑刺 → 故事 .md

[你] "把这个故事做成 1 分钟视频"
   ↓ 触发 ai-video-prompt skill
[AI] 读故事 → 拆剧本分镜（草稿）→ 等你审核
[你] "通过" / "第二场太慢"
[AI] 调整 / 转 Seedance Timeline prompt
   ↓
[你] 拿到的 prompt 喂 Seedance / 可灵 / Veo / Sora
```

## 文件结构

```
创作工具箱/
├── README.md
├── skills/                              # 标准 skill 分享目录
│   ├── story-creator/
│   │   ├── SKILL.md
│   │   ├── references/                  # 按需加载
│   │   └── tests/
│   └── ai-video-prompt/
│       ├── SKILL.md
│       ├── references/                  # 按需加载
│       │   ├── narrative-economy.md     # 叙事经济学（主次取舍 / 省略 / 侧面）
│       │   ├── script-to-storyboard.md  # 剧本分镜骨架
│       │   ├── shot-prompt-templates.md # 单场次 prompt 模板
│       │   ├── camera-movements.md      # 运镜参考
│       │   ├── lighting.md              # 光线参考
│       │   ├── shot-size-and-angle.md   # 景别角度参考
│       │   ├── composition-and-depth.md # 构图景深参考
│       │   └── pacing-and-duration.md   # 节奏时长参考
│       └── tests/
├── docs/
│   ├── 交付物格式规范.md                # 项目规范
│   ├── specs/                          # 设计文档
│   └── deliveries/                     # 交付报告
└── 阅读笔记/                            # 设计灵感来源（Harness 知识沉淀 / Agent Skill 规范）
```

## 设计原则

- **创作者主权**：AI 当问问题的合伙人，不抢笔
- **AI 无记忆约束**：Seedance 每次生成独立，prompt 设计要重述人物 / 资产
- **不机械均分**：剧本分镜按戏剧节奏分配时长（关键场 30-60s，过场 3-10s）
- **草稿可改**：场次用标题不用序号，散文为主，待商榷挂出

## License

MIT
