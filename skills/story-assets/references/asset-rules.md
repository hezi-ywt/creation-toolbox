---
description: 故事项目化后的资产 frontmatter 规范。每次创建 / 修改 角色 / 世界观 / 场景 等资产 .md 文件时加载。跟 asset-index CLI 核心字段一致。
---

# 资产规范（frontmatter / 类型 / 状态）

故事**升级为项目化**（多文件目录）后，每个角色、世界观、场景文件都是一个**资产**，需要标准 frontmatter。

跟 `asset-index` CLI（[npmjs.com/package/asset-index-cli](https://www.npmjs.com/package/asset-index-cli)）核心字段一致——装了 CLI 后可 `asset-index check` 自动校验。**不装 CLI 也 OK**，story-creator 自己读 frontmatter 做基本验证。

## 标准 frontmatter

```yaml
---
title: 男主              # 必填 · 资产显示名
type: 角色               # 必填 · 资产类型（见下方清单）
status: 草稿             # 必填 · 草稿 / 已定 / 待审
name: 林默               # 角色 / 场景 / 道具 类型必填
tags: [主角, 男, 中年]    # 可选 · 数组或逗号分隔字符串
created: 2026-05-17      # 必填 · YYYY-MM-DD
modified: 2026-05-17     # 必填 · YYYY-MM-DD
---
```

## 类型清单

| type | 用途 | 额外必填 |
|---|---|---|
| `角色` | 人物 / 主角 / 配角 / 反派 | `name` |
| `世界观` | 设定（规则 / 社会 / 历史 / 地理）| - |
| `场景` | 物理场景 / 地点 | `name` |
| `道具` | 关键物件 | `name` |
| `剧本` | 单集 / 单片剧本 | `episode` |
| `原始故事` | 章节制（小说 / 漫画原作）| `chapter` |
| `故事小说` | 故事整体 | - |

## 状态枚举

| status | 含义 | 何时用 |
|---|---|---|
| `草稿` | 正在迭代，随时改 | 默认 |
| `已定` | 锁定，改它要走 SKILL.md 行为 ③ 流程 | 用户明示「定了」|
| `待审` | 创作者后审 | AI 不确定是否定，挂出来 |
| `已整理` | 内容稳定但还能调（非锁定）| 中期 |
| `已迁移` | 资产已被合并 / 拆分到别处 | 重构后 |

## 命名约定

### 文件名
- **资产名 + .md**（如 `男主.md` / `女主.md` / `停车场.md`）
- 中文 OK（跟 asset-index 默认一致）
- **同类型唯一**——同一目录里不能两个角色都叫 `老王.md`
- 重名加 disambiguation：`老王-警察.md` / `老王-车夫.md`

### 目录名
- 中文（`角色/` `世界观/` `场景大纲/`）
- 不嵌套太深（一般 2 层够）

## 项目结构（推荐）

```
故事/<故事名>/
├── index.md                # 故事核心（type: 故事小说）
├── .asset-index/rules.yaml # 可选 · asset-index 装了才有用
├── 角色/
│   ├── 男主.md             # type: 角色
│   └── 女主.md
├── 世界观/
│   └── 时代背景.md         # type: 世界观
├── 场景大纲/
│   └── 主线.md             # type: 剧本 或 原始故事
├── 场景/                   # 可选 · 当场景多到要独立管理
│   └── 停车场.md           # type: 场景
└── 草稿/
    └── 讨论-2026-05-17.md  # 不算资产，纯讨论历史
```

## 跟 asset-index CLI 联动（可选）

如果创作者装了 `asset-index-cli`，可以做"创建 → 检查闭环"：

```bash
# 创作者第一次启用项目化时，初始化规则
cd 故事/<故事名>/
asset-index init       # 生成 .asset-index/rules.yaml

# AI 每次创建 / 修改资产后立即检查
asset-index check --file 角色/男主.md

# 项目健康度检查
asset-index scan .
asset-index stats
asset-index list --type 角色 --status 草稿
```

**没装 CLI 时**：story-creator 不强制 frontmatter（按需），但**建议**关键字段（title / type / status）始终在。

## 不要做

- ❌ 把 frontmatter 字段塞太多业务属性（如 `age: 45` 放 frontmatter）—— 那些属于正文「## 基础」段，frontmatter 只放索引性的
- ❌ status 自创枚举值（如 "进行中"、"半成品"）—— 用上面 5 个标准值
- ❌ 跨故事共用资产（同一个"老王"在两个故事里）—— 一故事一目录，重名也独立

## 跟 SKILL.md 其他行为的关系

- **行为 ④ 升级项目化**：触发"创建初始资产目录结构"——按本文件规范建
- **行为 ⑤ 管理资产**：创建 / 修改资产时，frontmatter 必须合规
- **行为 ③ 改已定**：改 `status: 已定` 的资产要走 grep + 用户确认流程

更深的"防污染"设计见 [asset-hygiene.md](./asset-hygiene.md)。
