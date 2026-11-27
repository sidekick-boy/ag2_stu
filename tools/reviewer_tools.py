from typing import Literal

from ag2 import tool
from ag2.network import ChannelInject
from ag2.network.workflow_helpers import set_context


@tool
async def submit_review(
    review_status: Literal["APPROVED", "REJECTED"],
    review_feedback: str,
    channel: ChannelInject
) -> str:
    """
    提交审核结果，并更新 Workflow 共享上下文。

    Args:
        review_status: 审核状态，APPROVED 或 REJECTED。
        review_feedback: 审核意见及需要修改的内容。

    Returns:
        审核结果提交信息。
    """

    if channel is None:
        return "审核失败：当前没有可用的 Workflow Channel"

    await set_context(
        channel,
        "review_status",
        review_status
    )

    await set_context(
        channel,
        "review_feedback",
        review_feedback
    )

    print(
        f"[Reviewer] 审核状态={review_status}，"
        f"审核意见={review_feedback}"
    )

    return f"审核结果已提交：{review_status}"