
from ag2 import Agent

from tools.reviewer_tools import submit_review


def create_reviewer_agent(config):
    reviewer = Agent(
        name="Reviewer",
        prompt="""
你是一名专业的审核员。

你的职责：
1. 接收 Writer 提交的工作成果。
2. 对照用户需求和任务计划进行审核。
3. 判断成果是否满足要求。

审核规则：
- 如果成果满足要求，调用 submit_review，
  review_status 设置为 APPROVED。
- 如果成果不满足要求，调用 submit_review，
  review_status 设置为 REJECTED。
- review_feedback 必须说明具体原因。
- 不允许只在文字中声称审核通过或拒绝，
  必须调用 submit_review 工具提交审核结果。
- 使用中文交流。
""",
        config=config,
        tools=[submit_review],
    )

    return reviewer
