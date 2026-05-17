# Agent Skill 规范、构建与设计模式

> 作者：阿里淘天集团-淘宝平台事业部-客户运营部
> 来源：阿里妹 / 微信公众号
> WeChat: `mp.weixin.qq.com/s?__biz=MzIzOTU0NTQ0MA==&mid=2247559942&idx=1`
> 阅读日期：2026-05-16

---

## 一、文章结构

把 Agent Skill 拆成三层方法论：

| 层 | 来源 | 解决什么 |
|---|---|---|
| 规范 | Anthropic（2025-12 发布，33+ Agent 产品采纳） | Skill 长什么样 |
| 构建 | Anthropic Skill-Creator + Obra Superpowers writing-skills | 怎么造一个好 Skill |
| 设计 | Google ADK 团队 | 不同任务用哪种 Skill 结构 |

---

## 二、规范层（最基础但最重要）⭐⭐⭐

### 文件结构
```
skill-name/
├── SKILL.md          # 必需：YAML frontmatter + Markdown body
├── scripts/          # 可选：可执行脚本
├── references/       # 可选：按需加载的参考文档
└── assets/           # 可选：模板、资源文件
```

### YAML frontmatter 字段

| 字段 | 必填 | 约束 |
|---|---|---|
| `name` | ✅ | 1-64 字符，小写字母数字+连字符；不头尾不连续；**必须与文件夹名一致** |
| `description` | ✅ | 1-1024 字符，包含触发关键词 |
| `license` | ❌ | 许可证名或引用 |
| `compatibility` | ❌ | 最多 500 字符 |
| `metadata` | ❌ | 自定义键值对（author/version 等） |
| `allowed-tools` | ❌ | 实验性，空格分隔 |

### 三层渐进式加载（核心机制）

| 层 | 加载内容 | 时机 | Token 成本 |
|---|---|---|---|
| **L1 目录层** | name + description | 会话启动 | ~50-100 / skill |
| **L2 指令层** | 完整 SKILL.md body | Skill 被激活 | 建议 <5000 |
| **L3 资源层** | scripts/references/assets 内文件 | 指令引用时按需 | 视文件 |

> 装 20 个 Skill 启动只多花 1000-2000 tokens，对比单体 prompt 节省约 90%。

### description 写法

**好示例**：
```
Analyze CSV and tabular data files — compute summary statistics,
add derived columns, generate charts, and clean messy data. Use this
skill when the user has a CSV, TSV, or Excel file and wants to
explore, transform, or visualize the data, even if they don't
explicitly mention "CSV" or "analysis."
```

**关键要点**（来自 Superpowers writing-skills 的发现）：

> description **只描述触发条件**，绝不要总结 Skill 的工作流程。

```yaml
# ❌ 总结工作流 → Agent 可能直接按 description 执行，跳过正文
description: Use when executing plans - dispatches subagent per task with code review

# ✅ 只有触发条件 → Agent 会完整阅读 Skill
description: Use when executing implementation plans with independent tasks in the current session
```

---

## 三、构建层

### Skill-Creator（Anthropic 官方）

**设计哲学**：像做机器学习一样做 Prompt Engineering——训练集、测试集、评估指标、迭代优化、防过拟合。

**6 阶段闭环**：
```
需求捕获 → 编写 Skill → A/B 测试（with vs without skill）→
评估 / 评审 → 迭代改进 → 优化与发布（含 description 优化循环）
```

**3 个子 Agent**：

| Agent | 职责 | 关键设计 |
|---|---|---|
| **Grader** | 评估断言通过 + 评价评估本身 | 自我批评："弱断言通过比无用更糟，制造虚假信心" |
| **Comparator** | 双盲对比 A/B 输出 | 不知道哪个来自 with_skill，去偏见 |
| **Analyzer** | 揭盲分析 + 基准统计 | 找出"为什么赢家赢了"+ 隐藏模式 |

**7 种 JSON Schema 形成数据管道**：
```
evals → timing → metrics → grading → benchmark → comparison → analysis → history
```

### Writing-Skills（Superpowers 框架）

**RED-GREEN-REFACTOR**：
- **RED**：不带 Skill 跑压力场景，记录 Agent 的合理化借口
- **GREEN**：针对发现的具体失败编写最小 Skill
- **REFACTOR**：堵住 Agent 找的新借口

**4 种 Skill 类型 + 对应测试策略**：

| 类型 | 例子 | 测试方法 |
|---|---|---|
| **纪律执行型** | TDD 强制 | 压力场景：时间+沉没成本+疲劳组合施压 |
| **技术指导型** | 条件等待、根因追踪 | 应用场景：能否正确应用？边界情况？ |
| **思维模式型** | 降低复杂度、信息隐藏 | 识别场景：能否判断何时适用 |
| **参考资料型** | API 文档 | 检索场景：信息可发现性 |

---

## 四、设计层 ⭐⭐⭐（Google 五种模式）

| 模式 | 一句话 | 关键设计 | 适用 |
|---|---|---|---|
| **Tool Wrapper** | SKILL.md 不含完整规范，告诉 Agent 去哪加载 | L3 资源层的典型应用 | 框架规范、风格指南 |
| **Generator** | 模板 + 风格指南填空，缺啥主动问 | 不瞎猜，缺信息直接提问 | 标准化文档、API 文档 |
| **Reviewer** | "查什么"（清单）和"怎么查"（执行）分离 | 输出 WHY not WHAT | 代码审查、合规扫描 |
| **Inversion** | Agent 先采访用户，问完才动手 | 翻转交互模式，分阶段提问 | 需求不明确的项目规划 |
| **Pipeline** | 多步严格顺序 + checkpoint | 用户不点头不能往下走 | 文档生成、多阶段内容生产 |

### 组合推荐

| 组合 | 场景 |
|---|---|
| Pipeline + Reviewer | 文档生成 + 自动质量审查 |
| Generator + Inversion | 先收集信息再填模板 |
| Pipeline + Tool Wrapper | 多步骤步骤中加载专家知识 |
| Inversion + Pipeline | 需求收集后进入执行流水线 |

---

## 五、我的判断 ⭐

### 最有价值的三个点

1. **三层渐进式加载**——这是 Skill 优于纯 Prompt 的本质。装多个技能不爆上下文，没第二条路
2. **Description 只写触发条件**（Obra 的发现）——一句话省掉以后无数次踩坑
3. **五种设计模式**——给"Skill 内部该怎么组织"提供了脚手架，不再凭感觉

### 最有争议的地方

**Skill-Creator 整套 A/B 测试体系对小 Skill 是过度工程**。文章自己诚实地引用了 GitHub Issue #514：
- 20 eval × 3 runs = 60 个 Opus 级别子会话
- 单轮优化烧掉 5 小时配额的 69%
- "operational workflow skills show 0% recall regardless of description quality"
- 修复建议（改用 haiku）至今 Open

**我的看法**：简单 Skill 直接手写，复杂 Skill 才上 Skill-Creator。

### 作者诚实程度

引用 Issue #514 + Medium 社区批评 + 列了 6 项已知局限——比同类吹捧文好得多。但仍把 Skill-Creator 作为正统范式介绍，**框架信仰** 大于 **实用主义**。

### 与第一篇（腾讯 Harness）的对比

| 维度 | 腾讯篇 | 阿里篇 |
|---|---|---|
| 视角 | 知识沉淀 | 技能封装 |
| 核心载体 | workflow + 知识仓库 | Skill 规范 + 设计模式 |
| 哲学 | 文件系统即状态机 | 渐进式加载 |
| 关键不足 | 自动提取质量没说 | Skill-Creator 太重 |

**互补关系**：腾讯篇的"工作流如何沉淀知识"，可以用阿里篇的 **Pipeline + Reviewer 模式** 来实现。

---

## 六、对画画布 / 影视创作工具箱的启发

### 立即可用

1. **写 skill 时先想"该用哪种模式"**：
   - 风格/规范注入 → Tool Wrapper
   - 模板化输出（剧本格式、分镜表）→ Generator
   - 输出审查（脚本审查、AI 生成内容质量评估）→ Reviewer
   - 用户需求模糊（"帮我做一个 X"）→ Inversion
   - 多阶段创作流水线（设定 → 大纲 → 分场 → 对白）→ Pipeline

2. **每个 skill 的 description 都按"只写触发条件"重写**：
   - 检查现有 `.agents/skills/web-access/SKILL.md` 的 description
   - 任何包含 "...does X then Y then Z" 的都重构成 "Use when [触发条件]"

3. **资源放 references/**：长规范、风格指南、术语表统统按需加载，不堆在 SKILL.md 主体里

### 不要做的事

- 不要用 Skill-Creator 跑 60 个 Opus 子会话——成本不可接受
- 不要追求 7 种 JSON schema 全套——对单人/小团队是仪式感
- 不要 description 总结工作流（这是文章里最容易踩的坑）

### 最小可行 skill 编写流程

```
1. 起 name 和 description（先写 description，确认触发清晰）
2. 直接手写 SKILL.md 正文（500 行内）
3. 长规范丢 references/
4. 试用 3-5 次真实任务，看 Agent 是否按预期触发
5. description 不够准就改 description（不要改正文堆约束）
```

---

## 七、参考资料

- 规范：https://agentskills.io/specification
- Anthropic Skills 仓库：https://github.com/anthropics/skills
- Superpowers：https://github.com/obra/superpowers
- Awesome Agent Skills（1060+）：https://github.com/VoltAgent/awesome-agent-skills
- Skill 评测：https://www.skillsbench.ai/
- 开源市场：https://skills.sh ／ https://skillsmp.com
