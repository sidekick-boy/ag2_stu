
import asyncio

from config.llm_config import get_llm_config
from agents.planner_agent import create_planner_agent
from agents.writer_agent import create_writer_agent
from agents.coordinator_agent import create_coordinator_agent


async def main():

    # 1. 初始化模型配置
    llm_config = get_llm_config()

    # 2. 创建两个专业员工
    planner = create_planner_agent(llm_config)
    writer = create_writer_agent(llm_config)

    # 3. 创建团队主管
    coordinator = create_coordinator_agent(
        config=llm_config,
        planner=planner,
        writer=writer,
    )

    print("=" * 60)
    print("AG2 多数字员工自主协作系统启动")
    print("模型：DeepSeek")
    print("团队：Coordinator + Planner + Writer")
    print("=" * 60)

    # 4. 用户只需要向团队主管下达任务
    user_task = """
请为一家企业制定 AI 数字员工团队建设方案。

要求：
1. 分阶段实施。
2. 明确每个阶段的建设目标。
3. 明确主要工作内容。
4. 明确阶段交付成果。
5. 方案具有实际落地价值。
"""

    print("\n[Coordinator] 正在协调数字员工团队...")
    print("-" * 60)

    # 5. Coordinator 自主调用 Planner 和 Writer
    # reply = await coordinator.ask(user_task)
    try:
        reply = await coordinator.ask(user_task)

    except Exception as exc:
        print("\n[错误诊断]")
        print("异常类型：", type(exc).__name__)
        print("异常信息：", str(exc))

        response = getattr(exc, "response", None)

        if response is not None:
            print("HTTP 状态码：", response.status_code)
            print("服务端错误详情：", response.text)

        raise
    # 6. 输出最终结果
    print("\n[团队最终交付成果]")
    print("-" * 60)
    print(reply.body)

    print("\n" + "=" * 60)
    print("数字员工团队协作任务结束")
    print("=" * 60)


if __name__ == "__main__":
    asyncio.run(main())
