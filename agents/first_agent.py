
import asyncio
import os

from dotenv import load_dotenv
from ag2 import Agent
from ag2.config import OpenAICompletionsConfig


# 1. 加载项目根目录中的环境变量
load_dotenv()

api_key = os.getenv("DEEPSEEK_API_KEY")

if not api_key:
    raise RuntimeError(
        "未找到 DEEPSEEK_API_KEY，请检查项目根目录下的 .env 文件"
    )


# 2. 配置 DeepSeek 大模型
llm_config = OpenAICompletionsConfig(
    model="deepseek-flash",
    api_key=api_key,
    base_url="https://api.deepseek.com",
)


# 3. 创建第一个数字员工
assistant = Agent(
    name="dugu",
    prompt="""
你是一个专业的 AI 数字员工，名字叫独孤。

你的职责：
1. 理解用户提出的任务和需求。
2. 分析问题并给出合理的解决方案。
3. 提供准确、清晰、专业的回答。
4. 使用中文与用户交流。
5. 不确定的信息必须明确说明，不得编造。

你的工作原则：
- 认真负责
- 逻辑清晰
- 注重执行结果
- 以解决问题为导向
""",
    config=llm_config,
)


# 4. 启动数字员工
async def main():
    print("=" * 50)
    print("AG2 数字员工系统启动")
    print("员工名称：独孤")
    print("模型：DeepSeek")
    print("=" * 50)

    reply = await assistant.ask(
        "你好，我正在组建一支 AI 数字员工团队。"
        "请介绍你自己，以及你能够承担的工作。"
    )

    print("\n独孤的回复：")
    print("-" * 50)
    print(reply.body)
    print("-" * 50)


if __name__ == "__main__":
    asyncio.run(main())
