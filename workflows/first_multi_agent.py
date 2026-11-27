
from ag2.network import (
    TransitionGraph,
    Transition,
    FromSpeaker,
    ContextEquals,
    AgentTarget,
    TerminateTarget,
)

def create_review_graph(coordinator, writer, reviewer):

    graph = TransitionGraph(
        initial_speaker=coordinator.agent_id,

        transitions=[
            # 规则1：Coordinator 启动任务，交给 Writer
            Transition(
                when=FromSpeaker(coordinator.agent_id),
                then=AgentTarget(writer.agent_id),
            ),

            # 规则2：Writer 完成工作，交给 Reviewer
            Transition(
                when=FromSpeaker(writer.agent_id),
                then=AgentTarget(reviewer.agent_id),
            ),

            # 规则3：审核通过，终止
            Transition(
                when=ContextEquals(
                    key="review_status",
                    value="APPROVED",
                ),
                then=TerminateTarget(reason="review_approved"),
            ),

            # 规则4：审核拒绝，返回 Writer
            Transition(
                when=ContextEquals(
                    key="review_status",
                    value="REJECTED",
                ),
                then=AgentTarget(writer.agent_id),
            ),
        ],

        default_target=TerminateTarget(
            reason="workflow_finished"
        ),

        max_turns=10,
    )

    return graph
