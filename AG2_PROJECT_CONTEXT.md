# AG2_PROJECT_CONTEXT.md

# AG2 多数字员工自主协作系统 — 项目长期上下文

> 本文件是本项目的长期上下文基准。记录已确认的技术选型、已验证进度、开发约束和后续路线。更新时必须区分事实、待验证事项与计划，不得将计划描述为已实现功能。

## 1. 项目基本信息

- 项目名称：AG2 多数字员工自主协作系统
- GitHub 仓库：sidekick-boy/ag2_stu
- 默认分支：main
- 开发平台：Windows 11
- IDE：PyCharm
- 编程语言：Python
- 依赖管理：pip，使用 requirements.txt 管理项目依赖
- 多智能体框架：项目依赖已固定为 AG2 1.3.4；本地虚拟环境升级及版本验证待完成（此前已验证 1.3.2）
- 模型服务：DeepSeek
- 前端交互方向：AG-UI

## 2. 项目最终目标

构建一个基于 AG2 多智能体协作框架的自主数字员工团队。

目标能力包括：

1. 接收用户提出的业务任务。
2. 理解任务并自主规划、拆解子任务。
3. 根据岗位职责分配任务。
4. 由多个数字员工通过消息传递和协作完成任务。
5. 根据需要调用工具和外部服务。
6. 对执行结果进行检查、反馈和必要的修正。
7. 汇总并交付最终结果。

项目目标不只是创建多个 Agent，而是逐步建立可验证、可扩展的自主协作流程。上述能力是最终建设目标，不代表目前均已实现。

## 3. 已确认的技术选型

| 技术领域 | 已确认选型 |
|---|---|
| 操作系统 | Windows 11 |
| 开发工具 | PyCharm |
| 编程语言 | Python |
| 多智能体框架 | AG2 1.3.4（requirements.txt 目标版本；本地安装待验证） |
| 模型服务 | DeepSeek |
| 前端交互方向 | AG-UI |
| 依赖管理 | pip / requirements.txt |
| 代码托管 | GitHub |

未经用户同意，不得擅自更换上述技术路线。涉及版本升级或架构调整时，应先说明原因、影响和替代方案，再由用户决定。

## 4. 当前数字员工团队

目前初步建立的团队由以下角色组成：

### Coordinator（协调员）

- 接收和理解用户任务。
- 协调数字员工团队。
- 组织任务执行流程。

### Planner（规划员）

- 分析任务需求。
- 拆解任务并制定执行计划。
- 为团队执行提供规划依据。

### Writer（执行员）

- 根据任务计划执行内容生产工作。
- 输出执行结果，供协调流程使用。

以上是当前初始角色定位。具体职责、提示词、消息流转和控制逻辑，以仓库实际代码及运行验证为准。后续可根据业务需求增加其他岗位。

## 5. 开发环境与项目位置

- 本地项目目录：`D:\\ag2\\code\\code1`
- Python 虚拟环境目录：项目根目录下的 `.venv`
- 环境变量文件：项目根目录下的 `.env`
- 已通过 PyCharm 使用虚拟环境运行项目。

注意：本节记录的是此前对话中确认的本地环境信息。若目录或配置发生变化，应由用户反馈后更新；不要猜测本地文件内容或密钥配置。

## 6. 已完成进度

根据项目教学对话及用户提供的运行结果，已确认：

- [x] Windows 11、Python、pip 和 PyCharm 开发环境已准备。
- [x] AG2 1.3.0 已安装并完成基础验证。
- [x] 已确定使用 DeepSeek 作为模型服务。
- [x] 已将 AG-UI 纳入项目技术规划。
- [x] 已创建本地项目目录及基础文件。
- [x] 已编写并运行初始 Agent / 协调流程。
- [x] 已初步建立 Coordinator、Planner、Writer 团队。
- [x] 用户提供过程序启动及协调流程运行日志。
- [x] GitHub 仓库已连接，且用户确认曾成功提交项目内容。

运行成功的日志至少显示程序能够启动并进入 Coordinator 协调流程；这不等于完整的多 Agent 自主协作闭环已经验证。

## 7. 尚待验证或完善

以下事项不能视为已完成，需在后续教学中逐项验证：

- [ ] Coordinator、Planner、Writer 之间的完整消息传递。
- [ ] 任务拆解、分配、执行和结果汇总的闭环。
- [ ] Agent 自主协作及终止条件。
- [ ] 执行结果审核、反馈和修正机制。
- [ ] 工具调用及外部 API 集成。
- [ ] 异常处理、失败恢复和超时控制。
- [ ] requirements.txt 与实际项目依赖的一致性。
- [ ] AG-UI 的实际集成和交互验证。
- [ ] 日志、监控、配置和安全管理。

## 8. 教学与开发约束

本项目采用“用户亲自操作、助手分阶段指导”的教学方式。以下规则必须持续遵守：

1. 按阶段、按步骤教学，不跳过关键学习环节。
2. 助手负责解释原理、提供操作步骤、示例和验证方法。
3. 用户亲自使用 PyCharm 编写、修改和运行项目代码。
4. 未经用户明确授权，助手不得直接编写、修改或提交项目业务代码。
5. 每个阶段应说明学习目标、操作步骤、预期结果和验证方式。
6. 用户反馈实际运行结果后，再进入下一阶段。
7. 对已经确认的环境、版本、模型和技术决策，不重复询问。
8. 优先讲清 AG2 的工作机制，不只提供可复制的代码。
9. 以实际仓库代码和运行结果判断项目状态，不凭空推断。
10. 对不确定的信息明确标记“待确认”或“待验证”，不得编造。

## 9. 上下文文件维护规则

- 本文件由助手负责创建和维护，保存在 GitHub 仓库根目录。
- 每完成重要开发阶段，助手应整理并提出本文件的更新内容。
- 涉及重大技术路线、架构或项目目标变更时，先向用户说明并取得确认。
- 更新进度时，只将有代码或运行结果支持的事项标记为已完成。
- 保留未完成事项和下一步任务，避免新会话重复盘问已知背景。
- 每次更新应使用清晰的 Git 提交说明。
- 若文档与仓库实际代码不一致，以实际代码和可复现的运行验证为准，并修正文档。
- 本文件用于保存项目事实与进度，不替代代码、README、设计文档或测试记录。

## 10. 建议实施路线与课程总规划

本项目采用由基础机制到业务实战、再到数字员工标准化和平台化的渐进路线。课程内容是后续教学计划，不代表相关能力已经实现。

### 阶段一：AG2 基础与初始团队

- AG2 环境安装与版本验证。
- DeepSeek 模型接入。
- Agent 创建、配置与运行。
- Coordinator、Planner、Writer 初始团队。
- Agent 消息传递、对话控制和终止条件。
- Agent-as-Tool 与基础任务委派。

### 阶段二：Tool 机制与 Python 工具开发

- Python Function Tool 注册与调用。
- 单参数、多参数工具及参数 Schema。
- 参数类型、可选参数、默认值和约束。
- 参数校验与业务异常处理。
- 结构化返回值（字典、JSON、状态与错误信息）。
- 多 Tool 注册、选择与组合调用。
- 工具调用控制、结果可信度和提示词约束。
- 面向中国象棋业务设计查询、规则校验和棋步执行工具。

### 阶段三：中国象棋业务实战

- 棋盘与棋子状态建模。
- 棋子信息和局面查询。
- 合法走棋规则校验。
- 棋步执行、吃子与状态更新。
- 将军、将死、困毙和胜负判断。
- 规则引擎、Pygame 图形界面与 Agent 协作层分离。
- 通过测试验证规则正确性。

### 阶段四：AG2 多 Agent 自主协作

- Agent 消息机制与 GroupChat。
- Speaker Selection 与团队控制策略。
- Task Delegation 和动态任务分配。
- 自主任务规划与多轮协作。
- 执行结果审核、反馈和修正。
- 失败重试、异常恢复和终止条件。
- 建立可验证的自主协作闭环。

### 阶段五：数字员工标准化建设

本阶段把单个 Agent 从“能运行的角色”提升为“可定义、可复用、可治理的标准化数字员工”。MCP、Skills、知识库/RAG 和 Memory 在此阶段系统学习，不作为当前 AG2 Tool 入门阶段的前置条件。

- 数字员工岗位、职责、输入输出和边界标准化。
- Agent 配置模板、System Prompt 与版本管理。
- Tool 接口规范、注册管理、描述和权限边界。
- MCP 基础概念、协议角色及 Client / Server 架构。
- MCP Server 开发或接入、工具与资源发现、调用和授权。
- Skills 的定义、目录组织、加载、复用与版本管理。
- Skills 与 MCP 的职责边界及协同方式。
- 领域知识库建设、文档处理与知识更新。
- Embedding、向量检索、RAG 流程及检索质量评估。
- Agent Memory：会话记忆、持久化记忆及其与知识库的区别。
- 多数字员工共享知识、数据隔离和访问控制。
- 数字员工能力测试、效果评估与回归验证。

### 阶段六：数字员工平台化与 AG-UI

- 数字员工注册、配置、启停和生命周期管理。
- 员工岗位、Skills、MCP 服务、工具和知识库的关联配置。
- 多员工团队编排、任务分发和运行状态管理。
- AG-UI 前后端通信与 Agent 状态展示。
- 任务过程、工具调用和协作过程可视化。
- 用户交互、人工审批与人工接管。
- 统一日志、监控、权限、成本和运行质量管理。

### 阶段七：产品化、部署与持续运维

- 配置与密钥管理。
- 安全策略、最小权限和审计。
- 服务部署、运行环境与依赖管理。
- 自动化测试、故障处理和性能优化。
- 版本发布、升级、备份和持续维护。

### 阶段推进原则

- 按“原理讲解—用户亲自编写—运行验证—复盘总结”推进。
- 前一阶段的关键机制经过实际验证后，再进入依赖它的后续阶段。
- 可根据中国象棋实战需求穿插练习，但不混淆课程目标和已实现功能。
- MCP、Skills、知识库/RAG、Memory 属于数字员工能力标准化建设的重要内容；当前优先完成 AG2 Tool 基础和多 Agent 协作基础。
- 涉及技术路线、关键依赖或架构顺序的重大调整，先向用户说明并取得确认。

## 11. 中国象棋软件实战项目（已确认目标）

本项目的 AG2 多数字员工团队将以“自主协作开发一款可运行的中国象棋软件”作为核心实战案例。这里的“自主”首先指数字员工团队协作完成软件开发任务，不代表第一版就必须由两个 Agent 直接进行棋盘对弈。

### 11.1 第一版技术选型

| 技术领域 | 选型 | 用途 |
|---|---|---|
| 核心开发语言 | Python | 游戏逻辑与应用开发 |
| 图形界面 | Pygame | 棋盘绘制、鼠标交互和游戏显示 |
| 多智能体框架 | AG2 1.3.0 | 数字员工分工协作 |
| Agent 大语言模型 | DeepSeek | Agent 需求分析、规划、执行和协作 |

以上选型已由用户确认，不得擅自替换。

### 11.2 第一版功能范围

| 功能模块 | 第一版具体要求 |
|---|---|
| 棋盘 | 标准 9×10 中国象棋棋盘 |
| 棋子 | 红黑双方共 32 枚棋子 |
| 棋子类型 | 将/帅、士、象、马、车、炮、兵/卒 |
| 走棋交互 | 鼠标选择棋子并移动棋子 |
| 规则判断 | 合法走棋、吃子、将军、将死 |
| 胜负判断 | 将死、困毙 |
| 游戏控制 | 重新开始、悔棋 |
| AI 对弈 | 后续扩展，不列为第一版必需功能 |

### 11.3 需求边界与实施原则

- 第一版先实现可运行的本地双人中国象棋游戏，重点保证棋盘显示、交互、规则判断和游戏控制正确。
- AI 对弈属于后续阶段；不得将其描述为第一版已实现或当前必须完成。
- AG2 数字员工团队负责协作分析需求、规划任务、调用工具、检查结果并推进软件开发；Pygame 应用本身负责棋盘和玩家交互。
- 后续学习 AG2 Tool 时，以中国象棋项目中的真实开发任务为案例，例如棋盘状态查询、走棋规则校验、棋步执行和局面分析等。具体工具边界须先讲解设计，再由用户亲自编写和验证。
- 应逐步拆分游戏规则引擎、棋盘状态、图形界面和 Agent 协作层，避免把全部逻辑堆进单一模块。
- 任何功能只有在用户完成编码并提供运行或测试结果后，才能标记为已完成。


## 12. AG2 Tool 学习进度（已完成基础验证）

本节记录用户在 AG2 1.3.0 中通过中国象棋示例掌握并实际验证的 Tool 基础机制。相关代码已提交至仓库，运行结果由用户在教学过程中反馈。

### 12.1 已掌握的核心概念

- **Agent-as-Tool**：将一个 Agent 封装为另一个 Agent 可调用的工具，例如当前 Coordinator 使用 `planner.as_tool(...)`、`writer.as_tool(...)` 委派任务。这是 Agent 之间的能力委派机制。
- **Python Function Tool**：将普通 Python 函数注册为 Agent 可调用的工具。函数负责执行确定性逻辑，LLM 负责根据用户意图选择是否调用以及传递参数。
- Tool 函数不需要自行调用 LLM；其输入、执行过程和返回值由 Python 函数定义。
- `@tool` 装饰器用于将 Python 函数注册为 AG2 Tool；通过 Agent 的 `tools=[...]` 参数将工具提供给 Agent。
- 函数文档字符串（docstring）用于向模型说明工具用途、参数含义和返回值；参数名称、类型和说明应清晰一致。
- 工具调用链路：用户提出问题 → Agent 判断并选择工具 → AG2 根据参数定义调用 Python 函数 → 函数执行并返回结果 → Agent 根据工具结果组织最终答复。

### 12.2 已提交并检查的示例文件

- `tools/chess_tools.py`：定义 `get_board_info()`、`get_piece_count(side)`、`validate_move(piece, from_position, to_position)` 和 `get_piece_count_by_side(side, count, include_general=True)` 四个工具；并定义 `ChessSide(str, Enum)` 枚举。
- `run_chess_tool_agent.py`：创建 `ChessAssistant`，加载 DeepSeek 配置，并注册上述四个工具。

仓库实际代码已检查：
- `get_board_info() -> str`：返回中国象棋棋盘为 9 列 10 行、红黑双方各 16 枚棋子、共 32 枚的信息。
- `get_piece_count(side: str) -> str`：根据 `side` 为“红方”或“黑方”返回对应初始棋子数量；其他值返回参数错误信息。
- 两个函数均有执行日志输出，可用于验证 Python 函数是否真正执行。
- Agent 的提示词要求在相应问题下调用指定工具，并正确传递 `side` 参数。

### 12.3 已验证结果

- [x] 普通 Python 环境下直接调用工具函数，成功返回棋盘信息。
- [x] 通过 Agent 提问触发 `get_board_info`，控制台出现 `[Tool执行]` 日志，确认工具由 AG2 实际调用，而非仅由模型凭知识回答。
- [x] Agent 根据“查询黑方初始棋子数量”的请求选择 `get_piece_count`，成功传递 `side="黑方"`。
- [x] Python 函数执行日志显示正在查询黑方棋子数量，并返回 16 枚；Agent 最终答复与工具返回数量一致。
- [x] 用户已将上述示例文件提交到 GitHub，且助手已读取仓库文件确认其存在。
- [x] 多参数工具 `validate_move(piece, from_position, to_position)` 已由 Agent 实际调用。
- [x] 用户反馈控制台日志确认三个业务参数均正确到达 Python 函数：棋子=马、起点=b1、终点=c3。
- [x] Agent 最终答复正确引用工具返回，并明确说明本次仅验证参数传递、不判断走棋是否合法。
- [x] 使用 `enum.Enum` 定义 `ChessSide(str, Enum)`，枚举成员为 `RED="红方"`、`BLACK="黑方"`。
- [x] 用户通过 AG2 Agent 实际调用枚举参数工具，正常传入红方时，Python 函数成功执行并通过 `side.value` 读取枚举值；验证了当前 AG2 1.3.0 调用链下的正常枚举参数兼容性。
- [x] 多参数工具 `get_piece_count_by_side(side, count, include_general=True)` 已注册到 Agent，包含棋方枚举、整数数量和带默认值的布尔参数。
- [x] 用户已在函数体内实现四项业务校验：棋方必须是 `ChessSide` 成员；`count` 必须满足 `type(count) is int`（排除 Python 中 `bool` 是 `int` 子类的情况）；`count` 范围为 1～16；`include_general` 必须满足 `type(include_general) is bool`。
- [x] 用户反馈 `count=17` 的 Agent 调用被工具拒绝，返回“参数错误：count 必须在 1 到 16 之间”，确认数量上限校验生效。
- [x] 用户确认本轮参数校验测试已完成。

**测试记录边界：** 当前对话中明确留存的具体测试输出是 `count=17` 被拒绝；其余边界值和类型测试虽由用户确认已完成，但各项输入、控制台日志和返回结果未逐项留存在当前上下文，因此不将它们单独标记为已通过。`count=17` 的错误返回说明函数走到了数量范围拒绝分支；仍应结合 `[Tool执行]` 日志判断是否进入正常业务执行分支。

**当前掌握程度边界：** 已验证单工具调用、工具选择、单参数和三参数传递、可选参数默认值的代码定义、正常枚举参数调用，以及至少一个明确的业务范围拒绝场景。尚未验证结构化返回值、统一业务错误码、异常处理策略、工具组合或真实象棋规则引擎。模型曾补充工具未返回的棋子构成信息，因此后续需学习如何约束回答依据，并设计结构化、完整的数据返回方式。

### 12.5 TypedDict 结构化返回值（已完成用户测试并提交）

用户已在 `tools/chess_tools.py` 中完成 TypedDict 类型定义和结构化返回值改造，并反馈代码已测试、提交 GitHub。助手已检查当前仓库文件，确认实现包含以下内容：

- 从 `typing` 导入 `TypedDict` 和 `Optional`。
- 定义 `PieceCountData(TypedDict)`，字段为 `side: str`、`count: int`、`include_general: bool`。
- 定义 `ChessToolResult(TypedDict)`，字段为 `success: bool`、`code: str`、`message: str`、`data: Optional[PieceCountData]`。
- `get_piece_count_by_side(...) -> DataInput` 保留 AG2 的 `DataInput` 返回注解；函数内部先构造符合 `ChessToolResult` 的字典，再通过 `DataInput(result)` 返回。
- 四个失败分支均返回统一结构：`INVALID_SIDE`、`INVALID_COUNT_TYPE`、`INVALID_COUNT`、`INVALID_BOOLEAN`；失败时 `success=False`、`data=None`。
- 成功分支返回 `success=True`、`code="OK"`、`message="查询成功"`，并在 `data` 中提供棋方、数量和是否包含将帅。

**已反馈的运行验证：**
- [x] 成功场景：红方、数量 16、`include_general=True`，工具执行日志确认参数正确，Agent 最终答复为查询成功，进程退出代码为 0。
- [x] 数量范围失败场景：红方、数量 0，返回 `success=False`、`code=INVALID_COUNT`、范围错误信息和 `data=None`，进程退出代码为 0。
- [x] 用户反馈其余失败分支已完成测试，并已将代码提交 GitHub；各分支的具体输入与逐项控制台输出未在当前对话中逐条提供，因此不记录未经展示的具体测试值。

**概念边界：**
- `TypedDict` 为字典提供静态类型结构和 IDE/类型检查支持，本身不会在运行时自动执行字段校验。
- `Optional[PieceCountData]` 表示 `data` 这个键仍然是必填键，但它的值可以是 `PieceCountData` 或 `None`；这与“键可以缺省”不同。
- `DataInput` 仍承担 AG2 结构化返回包装的职责，不能因为定义了 `ChessToolResult` 就将函数返回注解随意替换为该 TypedDict。

### 12.4 AG2 Tool 与中国象棋业务的边界

- Agent/LLM 负责理解自然语言需求、判断何时调用工具、选择工具并提供参数。
- Python 工具和后续规则引擎负责可确定性验证的业务逻辑，例如棋盘状态查询、走棋合法性校验和棋步执行。
- 不得让 LLM 凭自然语言知识替代象棋规则引擎；工具返回应成为业务事实的依据。
- 当前示例工具只是教学用信息查询工具，不是完整象棋规则实现。

### 12.6 TypedDict 进阶：total、Required、NotRequired 与 Optional（概念学习已完成，进阶代码验证待完成）

用户已完成本轮 TypedDict 进阶概念学习与问答练习，掌握范围如下：

- `total=True`：当前 TypedDict 类体中未单独标注的字段默认必填。
- `total=False`：当前 TypedDict 类体中未单独标注的字段默认可缺省；该设置只作用于当前 TypedDict，不会传递到嵌套 TypedDict。
- `Required[T]`：将当前字段明确设为必填，即使外层使用 `total=False`。
- `NotRequired[T]`：将当前字段明确设为可缺省，即使外层使用 `total=True`。
- `Optional[T]`：表示字段值允许为 `None`，不负责决定键是否必须存在。
- 嵌套 TypedDict 各自执行自身的字段必填规则；外层的 `total` 不会改变内层字段规则。

**已完成的概念练习：**
- [x] 判断 `total=False` 下普通字段可以缺省。
- [x] 判断 `total=True` 下普通字段必须存在。
- [x] 判断 `Required` / `NotRequired` 对 `total` 默认行为的覆盖。
- [x] 区分 `Optional[T]` 与 `NotRequired[T]`。
- [x] 理解嵌套 TypedDict 的必填规则彼此独立。

**当前仓库代码检查结果（2026-11-13）：**

`tools/chess_tools.py` 当前定义为：

```python
class ChessQueryResult(TypedDict, total=False):
    success: Required[bool]
    message: Required[str]
    board: Optional[ChessBoardData]
    request_id: str
```

该定义的实际字段规则是：
- `success`、`message` 必须存在，因为使用了 `Required`。
- `board`、`request_id` 可以缺省，因为类使用了 `total=False`。
- `board` 若存在，值还可以是 `None`，因为其类型是 `Optional[ChessBoardData]`。
- 在这个 `total=False` 类中，给 `board` 或 `request_id` 再加 `NotRequired` 不会改变字段是否必填，属于语义冗余。

**待完成：**
- [ ] 用户亲自调整或确认 `ChessQueryResult` 的字段声明风格；可比较 `total=False + Required` 与 `total=True + NotRequired` 两种表达。
- [ ] 使用静态类型检查器验证必填键、可缺省键及嵌套字段规则。
- [ ] 运行实际测试，确认类型定义与预期数据结构一致。
- [ ] 用户完成进阶代码调整和测试后，再将进阶代码实践标记为完成。

本节目前只记录概念学习与仓库代码检查，不代表进阶类型定义已经完成运行时校验；TypedDict 本身仍不会在运行时自动校验字典结构。

### 12.7 DataInput 与 TypedDict 的职责边界（源码确认，学习收尾）

用户在项目虚拟环境中通过 `inspect.getsource(DataInput)` 查看了 AG2 1.3.0 当前安装版本的类定义，实际输出为：

```python
class DataInput(Input):
    """Data input event sent to the model."""

    data: SendableMessage = Field(kw_only=False)
```

据此确认：
- `DataInput` 继承自 AG2 的 `Input`，属于 AG2 输入事件体系。
- `data` 是其承载输入内容的字段，类型标注为 `SendableMessage`。
- `Field(kw_only=False)` 表示该字段可作为位置参数传入，例如 `DataInput(result)`。
- 在本项目工具返回场景中，`TypedDict` 描述业务结果字典的字段结构；`DataInput` 则将该数据包装为 AG2 的输入事件对象。
- 这次源码查看仅用于澄清框架对象与业务数据结构的分工，不作为继续深入 AG2 内部源码的学习主线。

**学习状态：** 已完成必要概念确认。后续仅在遇到具体 API 使用问题时再查阅源码，不继续追踪该类的内部实现。

### 12.8 TransitionGraph、条件转移与审核返工（概念学习进行中，代码待验证）

用户已开始学习 AG2 Network Workflow 中的 `TransitionGraph` 与条件转移机制，并提供过当前安装版本相关的构造定义：

```python
@dataclass(slots=True)
class TransitionGraph:
    initial_speaker: str
    transitions: list[Transition] = field(default_factory=list)
    default_target: TransitionTarget = field(default_factory=...)
    max_turns: int | None = None
```

本轮已完成的概念学习与练习：
- [x] 理解从固定顺序协作升级到条件转移与审核返工的目标：在 Writer 执行后增加 Reviewer，由审核结果决定通过或退回修改。
- [x] 理解 `FromSpeaker` 根据当前发言者身份匹配转移条件。
- [x] 理解 `ContextEquals(key, value)` 根据 Workflow 共享上下文中的键值匹配转移条件；用户正确选择了以 `ContextEquals("review_status", "REJECTED")` 将拒绝结果路由回 Writer。
- [x] 初步理解 Context Variables 的用途：保存审核状态、审核次数和审核反馈等可供转移条件读取的数据。
- [x] 理解 Agent 自然语言消息“审核通过”本身不会自动改变工作流状态；必须显式更新上下文，条件转移才能读取到新状态。
- [x] 理解 `EV_CONTEXT_SET` 是官方文档示例中更新 Workflow Context Variables 的事件机制，`ContextEquals` 则负责读取状态进行条件判断。
- [x] 理解审核状态更新应保持字段语义一致：通过时更新 `review_status` 为 `APPROVED`、递增 `review_count` 并清空旧的 `review_feedback`。用户在该练习中选择 C，回答正确。
- [x] 讨论了 `review_count`（审核总次数）与 `rework_count`（实际返工次数）的区别；如需限制返工次数，建议使用独立的 `rework_count`，避免混淆。

重要机制与风险：
- `ContextEquals` 读取的是 Workflow 状态，不是 Agent 消息正文。
- Context 状态可能持续保留；若 `review_status` 一直为 `REJECTED`，拒绝条件可能在后续转移评估中继续匹配。因此实际闭环需要设计状态更新/重置、规则优先级及最大轮次限制。
- 官方文档示例中的 `EV_CONTEXT_SET` / `ChannelInject` 等 API 仍需在用户的 AG2 1.3.0 虚拟环境中核实，不能仅凭最新版文档认定与安装版本完全一致。

**当前边界：** 上述内容属于概念学习和问答练习，不代表已经编写或运行 TransitionGraph、Context Variables 更新 Tool，也不代表审核返工闭环已经实现。

**下一步验证：** 用户先在项目虚拟环境运行以下命令，检查 AG2 1.3.0 是否导出相关名称，并将实际输出反馈后再继续：

```powershell
python -c "import ag2.network as n; print('EV_CONTEXT_SET:', hasattr(n, 'EV_CONTEXT_SET')); print('ChannelInject:', hasattr(n, 'ChannelInject')); print('相关名称:', [x for x in dir(n) if 'Context' in x or 'Channel' in x or 'EVENT' in x])"
```

确认 API 后，再逐步设计并由用户亲自编写 Reviewer 状态更新 Tool，最后构建最小化条件转移与审核返工示例，逐项运行验证。

## 13. 当前阶段与下一步

**当前阶段：** 初始 Coordinator、Planner、Writer 多 Agent 团队已搭建并完成基础启动验证。AG2 Tool 基础、Agent-as-Tool、Python Function Tool、工具选择与调用、单参数和多参数传递、枚举参数、默认参数及业务参数校验均已完成相应教学与实战练习。TypedDict 结构化返回值已完成用户测试并提交；TypedDict 的 total、Required、NotRequired、Optional 概念学习已完成。用户通过 AG2 1.3.0 安装环境的源码输出确认了 `DataInput` 继承自 `Input`，并以 `data: SendableMessage` 字段承载数据。用户已完成并提交 TypedDict 结构化返回值改造，且反馈成功查询和数量范围失败场景运行正常。当前教学已进入 AG2 Network Workflow 的 TransitionGraph、条件转移与审核返工机制；已完成 FromSpeaker、ContextEquals、Context Variables、EV_CONTEXT_SET 的概念讲解和审核状态更新练习，但 AG2 1.3.0 对应 API 尚未在本地核实，尚未编写或运行条件转移工作流。中国象棋软件本身尚未开始实现。

**下一步教学：** 先由用户在 AG2 1.3.0 虚拟环境检查 `EV_CONTEXT_SET`、`ChannelInject` 等实际导出，再根据实际 API 逐步编写 Reviewer 状态更新 Tool 和最小化 TransitionGraph 条件转移示例。之后再扩展为 Writer → Reviewer → 通过/返工的闭环，并验证状态重置、返工次数和 `max_turns` 等终止保护。TypedDict 进阶代码设计及静态类型检查仍保留为待完成专项练习。当前 `validate_move` 仅用于验证参数传递，不代表已经实现或验证完整象棋走棋规则。

**后续课程方向：** 完成 Tool 机制学习后，进入中国象棋业务工具实战，再系统学习 AG2 多 Agent 自主协作闭环；之后开展数字员工标准化建设（MCP、Skills、知识库/RAG、Memory、权限与评估），再推进 AG-UI、平台化和部署。

继续教学前应先检查仓库当前文件和 AG2 1.3.0 对应 API；按“原理—用户亲自编写—运行—核对实际日志和输出”的方式推进。未经用户明确授权，不直接修改项目业务代码。


## 14. 官方资料来源与版本追溯（持续维护）

本项目的 AG2 学习阶段必须同步记录对应的官方资料来源，避免只保存结论而无法追溯 API 定义和版本变化。详细链接清单维护在仓库文件 `docs/AG2_OFFICIAL_REFERENCES.md`。

### 14.1 当前版本基准

- 最近一次有实际输出支持的本地版本为 **AG2 1.3.2**（2026-11-20）；GitHub 的 `requirements.txt` 已于 2026-11-27 固定为 **AG2 1.3.4**，但本地虚拟环境尚待升级并重新验证。
- 本文件早期章节中出现的 AG2 1.3.0 是历史学习记录，不再代表当前安装版本。
- 查阅官方 GitHub 源码时，应记录具体 tag/commit；源码快照不自动等同于本地安装包。当前后续教学目标版本为 AG2 1.3.4，升级完成后再以本地 1.3.4 环境验证版本敏感 API。
- 当前已从本地 1.3.2 安装目录搜索到 `EV_CONTEXT_SET`、`ChannelInject`、`workflow_helpers.py`、`ContextEquals` 等相关符号；这一步只确认符号存在，不代表审核返工流程已实现或测试通过。

### 14.2 本阶段官方资料与学习边界

当前主题：AG2 Network Workflow 的 Context Variables、条件转移与审核返工。

已查阅的官方资料：
- `ag2/network/workflow_helpers.py`：`set_context()` / `delete_context()` 封装上下文事件，Tool 作者通常调用辅助函数，无需直接构造事件。
- `ag2/network/client/inject.py`：`ChannelInject` 是注入当前 Channel 的类型别名。
- `website/docs/user-guide/network/workflow.mdx`：说明 `TransitionGraph`、`ContextEquals`、条件转移顺序、状态持续性及终止机制。

本阶段采用“先掌握公开 API 的用途与调用方式，再按需深入源码”的教学策略。用户是 Python 初学者，不要求为使用高级 API 而先读懂整个事件系统或依赖注入实现。优先掌握 `ChannelInject` 用于取得当前 Channel、`set_context()` 用于更新 Workflow 共享上下文、`ContextEquals` 用于按上下文值路由；`EV_CONTEXT_SET` 作为底层事件名识别即可，暂不要求直接操作。

当前已完成 API 概念学习、官方资料查阅、本地旧版本符号搜索，并已由用户编写提交 Reviewer 状态更新 Tool。该工具尚未在真实 Workflow 中运行验证；条件转移配置、返工循环、最大返工次数及端到端运行验证仍待用户分步完成。



### 12.9 Reviewer 审核状态工具（代码已提交，运行待验证）

用户已将 Reviewer 的首个审核状态工具提交到 GitHub，提交记录：
- 提交说明：`编写第一个审核工具`
- Commit：`3aeaeb6ec91e27a62dfec67540060ac0af4e6bcc`
- 文件：`tools/reviewer_tools.py`
- 同次提交将 `requirements.txt` 中的依赖固定从 `ag2[openai,ag-ui]==1.3.2` 更新为 `ag2[openai,ag-ui]==1.3.4`。

当前工具实现内容：
- 使用 `@tool` 注册异步函数 `submit_review()`。
- `review_status` 使用 `Literal["APPROVED", "REJECTED"]` 限定审核状态。
- 使用 `ChannelInject` 接收当前 Workflow Channel。
- 使用 `set_context(channel, "review_status", ...)` 写入审核状态。
- 使用 `set_context(channel, "review_feedback", ...)` 写入审核意见。
- Channel 不存在时返回失败提示。

**状态边界：**
- [x] Reviewer 状态工具代码已由用户编写并提交。
- [x] 已从 GitHub 提交 diff 核实文件内容及依赖版本变更。
- [ ] 尚未在真实 Workflow 中验证 `ChannelInject` 是否成功注入。
- [ ] 尚未验证 `set_context()` 写入的两个字段能否被 `ContextEquals` 读取。
- [ ] 尚未注册 Reviewer Agent，也尚未验证通过/返工转移。
- [ ] 尚未完成 Writer → Reviewer → APPROVED 终止 / REJECTED 返工的端到端运行。

下一步应先完成本地 AG2 1.3.4 升级与版本确认，再按 1.3.4 的官方 API 继续 Reviewer Agent 注册和 Workflow 状态验证。不要将“代码已提交”误记为“审核返工闭环已运行通过”。
