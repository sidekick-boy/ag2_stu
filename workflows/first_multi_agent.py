
from ag2.network import (
    TransitionGraph,
    Transition,
    FromSpeaker,
    ContextEquals,
    AgentTarget,
    TerminateTarget,
)


def create_review_graph(writer, reviewer):

    graph = TransitionGraph(
        initial_speaker=writer.agent_id,

        transitions=[
            # 规则1：Writer 完成工作后，交给 Reviewer
            Transition(
                when=FromSpeaker(writer.agent_id),
                then=AgentTarget(reviewer.agent_id),
            ),

            # 规则2：审核通过，结束工作流
            Transition(
                when=ContextEquals(
                    "review_status",
                    "APPROVED"
                ),
                then=TerminateTarget(
                    reason="review_approved"
                ),
            ),

            # 规则3：审核拒绝，交回 Writer 返工
            Transition(
                when=ContextEquals(
                    "review_status",
                    "REJECTED"
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
