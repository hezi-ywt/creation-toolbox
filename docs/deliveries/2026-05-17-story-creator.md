# 交付报告：story-creator skill

> 日期：2026-05-17
> 状态：v0.1.0，已测试

## TL;DR

按 MVP 设计建好 `story-creator` skill：一个文件 = 一个故事，两态（草稿/已定），AI 三角色软切换，零词典。测试 **7/7 + 触发 20/20** 通过。

## 怎么用

新会话里说：

> 读 `.claude/skills/story-creator/SKILL.md` 跟我讨论一个故事。我有个想法：[你的种子]

三个核心动作：

1. **正常讨论** — AI 切换"问 / 分岔 / 挑刺"
2. **说"定了"** — AI 复述 + 问范围（世界/故事/场景）
3. **改已定** — AI grep 影响列出，不阻塞

## 文件清单

```
docs/specs/2026-05-17-story-creator-design.md     # 设计文档
.claude/skills/story-creator/
├── SKILL.md                                       # 233 行，主指令
├── references/
│   ├── excavation-questions.md                    # 269 行
│   ├── beat-structures.md                         # 195 行
│   ├── genre-conventions.md                       # 504 行
│   └── anti-cliches.md                            # 330 行
└── tests/
    ├── test-scenarios.md
    └── test-run-001.md                            # 子 agent 测试报告
```

合计 2187 行交付物。

## 我做的判断

未问就自己决的事，留给你 review：

1. **skill 装在 `.claude/skills/`**（Claude Code 项目级标准路径，不全局）—— 跟 web-access 不同结构（那个在 `.agents/skills/`），但 `.claude/` 是 Claude Code 真正能自动识别的。
2. **Claude Code 应该会自动加载** —— 下次会话开始时它会自动扫描 `.claude/skills/`，识别 story-creator。你不用主动引用就能触发（理论上）。
3. **description 中英双语关键词** —— 覆盖你的两种说话方式。
4. **没改 description 边界 #20**（"我的剧本第二幕拖"）—— 子 agent 判得对（不触发），未多加限定。

## 已知不支持

- ❌ 不支持平行分支（A/B 测试两个结局走向，需手动 cp 文件）
- ❌ 不维护多故事索引（看 `故事/` 文件夹列表）
- ❌ 不能从已存在剧本逆向拆 logline（只服务"从种子起"方向）
- ❌ 不生成工业标准剧本格式（场号、严格 sluglines、镜号）——但**散文式场景/对白/独白试写可以写**，记在草稿段

## 链接

- **为什么这么设计** → [`../specs/2026-05-17-story-creator-design.md`](../specs/2026-05-17-story-creator-design.md)
- **测试细节** → [`../../.claude/skills/story-creator/tests/test-run-001.md`](../../.claude/skills/story-creator/tests/test-run-001.md)
- **格式规范** → [`../交付物格式规范.md`](../交付物格式规范.md)
