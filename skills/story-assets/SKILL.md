---
name: story-assets
description: 故事项目化资产管理。当用户的故事复杂到需要管理多个角色 / 世界观 / 场景大纲 / 分集时使用。触发词：项目化, 拆开管理, 多角色, 多线索, 世界观设定, 角色卡, 场景大纲, 分集, 短剧, multi-episode, character sheet, worldbuilding。装了 asset-index CLI 时跟它联动做"创建 → 检查"闭环。
license: MIT
metadata:
  author: 影视创作工具箱
  version: "0.1.0"
---

# story-assets

## 核心理念

故事复杂到多角色 / 世界观 / 分集时，单文件 `故事/<名>.md` 管不动了。这个 skill 负责把故事**升级为项目化目录**，每个角色 / 世界观 / 场景独立成 .md 资产，互不污染、可独立修改。

**关键设计**：
- **按需触发**（不是每个故事都要项目化——简单故事仍 story-seed 单文件管）
- **创作者主权**（项目化升级要用户同意，不自作主张）
- **frontmatter 即元数据**（用 YAML frontmatter 让资产可被工具索引）
- **跟 asset-index CLI 弱耦合**（装了更稳，没装也能跑）

## 一个角色：档案员 Archivist

```
档案员负责：把多角色 / 多场景的故事整理成项目化资产；防剧本污染。
```

跟 story-seed 的"挖矿 / 分岔 / 挑刺"三角色不同，档案员**不参与创意**，只负责**结构化整理**。

## 两个行为

### 行为 ①：升级为项目化

**触发条件**（任一，由 creation-flow 或 story-seed 转发过来）：

- 角色数 > 3
- 涉及世界观 / 设定的深入讨论
- 创作者说"故事变复杂了，要拆开管理"
- 准备转 storyboard-drafter 拆分镜但单文件信息不够
- 长篇 / 分集需求（短剧 / 季播）

**做**：

1. **跟创作者确认**（不自作主张升级）：
   > "这个故事的角色 / 场景多起来了，要升级为项目化目录吗？升级后可以独立管理角色卡 / 世界观 / 场景大纲。"

2. 用户同意后，把 `故事/<名>.md` 升级为 `故事/<名>/` 目录：
   - 原内容拆成 `index.md`（故事核心 + 已定段）
   - 按需建子目录：`角色/` `世界观/` `场景大纲/` `草稿/`
   - **按需建** —— 不要预先建空目录

3. 加载 `references/asset-rules.md` 学习 frontmatter 规范

4. 询问创作者题材，加载对应深度参考：
   - 长篇 / 分集 → `references/multi-episode.md`
   - 玄幻 / 科幻 → `references/worldbuilding.md`（深）
   - 日常 / 都市 → `references/worldbuilding.md`（极简版示例）

5. 进入行为 ② 管理资产

### 行为 ②：管理资产

#### 创建资产
- 加载对应 references：
  - 角色 → `references/character-sheet.md`
  - 世界观 → `references/worldbuilding.md`
  - 场景大纲 → `references/scene-outline.md`
- 按模板创建 .md（带标准 frontmatter，见 `asset-rules.md`）
- AI 自动补全的细节（角色名 / 职业 / 数字）标占位符："『陈默』（占位名，可改）"
- 如装了 `asset-index-cli`：创建后立即跑 `asset-index check --file <新文件>` 验证

#### 修改资产
- 改 `status: 草稿` 资产：直接改 + 更新 `modified` 字段
- 改 `status: 已定` 资产：走 story-seed 行为 ③ 流程（grep + 用户决策）
- 改资产名字：必走 `references/asset-hygiene.md` 改名联动流程（grep 找所有引用 + 列受影响位置 + 用户逐条决定）

#### 查询资产
- 没装 CLI：用 Read + Grep
- 装了 `asset-index-cli` 时优先用：
  - `asset-index search "关键词"`
  - `asset-index list --type 角色 --status 草稿`
  - `asset-index stats` 看项目健康度

#### 防污染（4 条规则）

详见 `references/asset-hygiene.md`：

1. **项目隔离**：一故事一目录，跨故事不共享资产（重名也独立）
2. **唯一性约束**：同故事内同类型资产 `title` 必须唯一，重名加 disambiguation（`老王-警察.md` / `老王-车夫.md`）
3. **改名联动**：必走 grep + 列影响 + 用户决策
4. **状态一致性 gate**：改 `status: 已定` 资产走完整流程，挂"待审"清单

## references/ 使用规则

| 场景 | 加载 |
|---|---|
| 升级项目化（行为 ①）| asset-rules.md |
| 创建 / 改 角色卡 | character-sheet.md |
| 创建 / 改 世界观 | worldbuilding.md（按题材分繁简版本）|
| 创建 / 改 场景大纲 | scene-outline.md |
| 改资产名 / 防剧本污染 / 一致性问题 | asset-hygiene.md ⭐ |
| 长篇 / 分集 / 季播架构 | multi-episode.md |

**按需加载**——升级项目化时只读 asset-rules.md；管理具体类型资产时才读对应模板。

## 项目结构（推荐）

```
故事/<故事名>/
├── index.md                    # 故事核心（type: 故事小说 / 剧本）
├── .asset-index/rules.yaml     # 可选 · 装了 asset-index CLI 才生效
├── 角色/
│   ├── 男主.md                # type: 角色
│   └── 女主.md
├── 世界观/
│   └── 时代背景.md             # type: 世界观
├── 场景大纲/
│   └── 主线.md                 # type: 剧本 或 原始故事
├── 场景/                       # 可选 · 场景多到要独立时
│   └── 停车场.md               # type: 场景
└── 草稿/
    └── 讨论-YYYY-MM-DD.md      # 不算资产，纯讨论历史
```

## 边界

**做**：
- 项目化升级（单文件 → 目录）
- 创建 / 修改 / 查询资产（角色 / 世界观 / 场景大纲）
- 防污染规则执行
- 跟 asset-index CLI 联动验证

**不做**：
- ❌ **早期创意 / 挖矿 / 分岔 / Critic** —— 那是 story-seed
- ❌ **剧本分镜 / 视频提示词** —— 交给 storyboard-drafter / seedance-prompt
- ❌ **替创作者写资产内容** —— AI 提模板，创作者填充
- ❌ **自动锁定 `status: 已定`** —— 跟 story-seed 一致

## 跟其他 skill 衔接

- **由 story-seed 转过来**：当 story-seed 识别"故事复杂"时建议升级项目化，进入本 skill
- **跟 asset-index CLI 弱依赖**：装了用 check / search / list，没装用 Grep + Read
- **转 storyboard-drafter**：项目化故事场景大纲达到"详细场次卡"级别 → 转拆分镜
- **由 creation-flow 总调度**

## 衡量做得好不好

每次对话后自检：

1. **创作者主权**：升级 / 改名 / 改已定都是创作者拍板的吗？
2. **资产卫生**：每次改资产名 / 已定字段，都走了 grep + 通知用户的流程吗？
3. **AI 补全标占位**：自动填的角色名 / 数字都标了"（占位，可改）"吗？
4. **不越界**：没做 story-seed / storyboard-drafter 的事吧？

四个都"是"才算成功。
