# AG2 官方资料索引

> 本文件记录 AG2 学习过程中实际查阅的官方文档与源码。每个学习阶段持续追加，保留可追溯链接与版本说明。

## 当前学习基准

- 本地已安装版本：**AG2 1.3.2**
- 版本验证方式：`python -c "import importlib.metadata; print(importlib.metadata.version('ag2'))"`
- 用户于 2026-11-20 提供的实际输出：`1.3.2`
- 官方源码链接以下列 AG2 仓库 commit 快照固定，避免 `main` 分支后续变化导致链接内容漂移：
  - 源码快照 commit：`6d2dd8bab8af873ea29ed759cfacb572466d925e`
  - 仓库：https://github.com/ag2ai/ag2
- 注意：固定 commit 的官方源码快照不自动等同于本地安装包的发布 tag。涉及版本敏感行为时，以本地 AG2 1.3.2 环境运行验证为准。

## 阶段：Network Workflow、Context Variables 与条件转移

学习目标：在 Planner → Writer → Reviewer 的中国象棋数字员工流程中，根据 Reviewer 写入的审核状态决定通过、返工或终止。

### 官方源码

| 文件 / API | 用途 | 官方链接 |
|---|---|---|
| `workflow_helpers.py`：`set_context()`、`delete_context()` | 用公开辅助函数更新或删除 Workflow 共享上下文；封装底层事件格式 | https://github.com/ag2ai/ag2/blob/6d2dd8bab8af873ea29ed759cfacb572466d925e/ag2/network/workflow_helpers.py |
| `envelope.py`：`EV_CONTEXT_SET` | 定义上下文更新事件名称 | https://github.com/ag2ai/ag2/blob/6d2dd8bab8af873ea29ed759cfacb572466d925e/ag2/network/envelope.py |
| `client/inject.py`：`ChannelInject` | 定义注入当前 Channel 的类型别名 | https://github.com/ag2ai/ag2/blob/6d2dd8bab8af873ea29ed759cfacb572466d925e/ag2/network/client/inject.py |
| `adapters/workflow.py` | Workflow Adapter 对上下文事件进行 fold，并根据状态解析后续转移 | https://github.com/ag2ai/ag2/blob/6d2dd8bab8af873ea29ed759cfacb572466d925e/ag2/network/adapters/workflow.py |

### 官方使用文档

- Workflow Adapter、TransitionGraph、ContextEquals、转移优先级、状态持续性与终止机制：
  https://github.com/ag2ai/ag2/blob/6d2dd8bab8af873ea29ed759cfacb572466d925e/website/docs/user-guide/network/workflow.mdx
- Context Variables 使用指南：
  https://github.com/ag2ai/ag2/blob/6d2dd8bab8af873ea29ed759cfacb572466d925e/website/docs/user-guide/network/context_variables.mdx

### 本阶段需要掌握的 API（不要求先读透底层源码）

- `ChannelInject`：在 Tool 参数中声明，由 AG2 注入当前 Channel。
- `set_context(channel, key, value)`：更新 Workflow 共享上下文。
- `delete_context(channel, key)`：删除共享上下文中的键。
- `ContextEquals(key, value)`：条件转移读取共享上下文并匹配指定值。
- `EV_CONTEXT_SET`：认识其为底层上下文更新事件即可；入门实操优先使用 `set_context()`，不直接手工发送事件。

### 本阶段进度（截至 2026-11-20）

- [x] 本地虚拟环境版本确认：AG2 1.3.2。
- [x] 在本地 AG2 1.3.2 安装目录搜索到 `EV_CONTEXT_SET` 和 `ChannelInject` 等符号。
- [x] 查阅上述官方源码及 Workflow 文档。
- [x] 明确采用公开辅助 API 优先的教学策略：先理解用途和用法，必要时再深入实现细节。
- [ ] 用户亲自编写 Reviewer 审核状态更新 Tool。
- [ ] 验证 `set_context()` 写入的状态可被 Workflow 条件读取。
- [ ] 配置 `ContextEquals` 条件转移。
- [ ] 实现 Writer → Reviewer → 通过 / 返工 Writer 的循环。
- [ ] 验证返工计数、状态重置、转移优先级和 `max_turns` 保护。
- [ ] 在中国象棋项目场景中完成端到端运行测试。

## 维护约定

1. 每个重要学习阶段都记录官方文档、源码文件链接和适用版本信息。
2. 源码链接优先固定到具体 commit；若引用官方文档站点，也可同时记录文档 URL。
3. 明确区分“查阅过资料”“理解概念”“代码已实现”“运行已验证”，不得混写。
4. 官方主干代码与本地安装版本可能存在差异；版本敏感 API 必须在项目虚拟环境中核实。
5. 用户以逐步实践为主，助手负责检索官方资料并维护本索引；不要求用户为每个 API 自行翻找源码。
