import asyncio

from ag2 import Agent

from config.llm_config import get_llm_config
from tools.chess_tools import get_board_info
from tools.chess_tools import get_piece_count


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

不得凭空编造工具返回的数据。
""",
        config=llm_config,
        tools=[get_board_info, get_piece_count],
    )

    # 3. 向 Agent 提出问题
    reply = await chess_agent.ask(
        "请查询黑方的初始棋子数量。"
    )

    # 4. 输出 Agent 最终回答
    print("\n[Agent最终回答]")
    print(reply.body)


if __name__ == "__main__":
    asyncio.run(main())