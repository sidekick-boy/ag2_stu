import asyncio

from ag2 import Agent

from config.llm_config import get_llm_config
from tools.chess_tools import get_board_info
from tools.chess_tools import get_piece_count
from tools.chess_tools import validate_move
from tools.chess_tools import get_piece_count_by_side
async def main():

    # 1. 获取 DeepSeek 模型配置
    llm_config = get_llm_config()

    # 2. 创建 Agent，并注册象棋工具
    chess_agent = Agent(
        name="ChessAssistant",
        prompt="""
你是一名中国象棋软件开发助手。

当用户询问中国象棋棋盘的基本信息时，
必须调用 get_board_info 工具获取信息。

当用户询问红方或黑方的棋子数量时，
必须调用 get_piece_count 工具。
调用时必须正确传递 side 参数。

当用户提出走棋请求时，必须调用 validate_move 工具。
必须提供三个参数：
piece：棋子名称
from_position：起始位置
to_position：目标位置

当用户要求查询某一方的棋子数量，并指定数量及是否包含将帅时，
必须调用 get_piece_count_by_side 工具。

必须正确传递三个参数：
side：棋方，字符串类型
count：棋子数量，整数类型
include_general：是否包含将帅，布尔类型

不得自行判断工具没有验证的走棋规则。

不得凭空编造工具返回的数据。
""",
        config=llm_config,
        tools=[get_board_info, get_piece_count, validate_move, get_piece_count_by_side],
    )

    # 3. 向 Agent 提出问题
    reply = await chess_agent.ask(
        "请调用工具，查询蓝方棋子数量5个，包含将帅。"
    )

    # 4. 输出 Agent 最终回答
    print("\n[Agent最终回答]")
    print(reply.body)


if __name__ == "__main__":
    asyncio.run(main())