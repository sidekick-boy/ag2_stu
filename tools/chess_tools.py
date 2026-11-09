from ag2 import tool

@tool
def get_board_info() -> str:
    """
    获取中国象棋棋盘的基本信息。
    """
    print("[Tool执行] 正在查询中国象棋棋盘信息")
    return (
        "中国象棋棋盘：9列10行。"
        "红黑双方各有16枚棋子，合计32枚。"
    )


@tool
def get_piece_count(side: str) -> str:
    """
    查询中国象棋指定一方的初始棋子数量。

    Args:
        side: 棋子所属方，只能是红方或黑方。

    Returns:
        指定一方的棋子数量。
    """
    print(f"[Tool执行] 正在查询{side}棋子数量")

    if side == "红方":
        return "红方初始棋子数量：16枚"

    elif side == "黑方":
        return "黑方初始棋子数量：16枚"

    else:
        return "参数错误：side 只能是红方或黑方"


@tool
def validate_move(
    piece: str,
    from_position: str,
    to_position: str
) -> str:
    """
    接收中国象棋的一次走棋请求。

    Args:
        piece: 棋子名称，例如马、车、炮。
        from_position: 棋子的起始位置。
        to_position: 棋子的目标位置。

    Returns:
        返回接收到的走棋请求信息。
    """

    print(
        f"[Tool执行] 收到走棋请求："
        f"棋子={piece}，"
        f"起点={from_position}，"
        f"终点={to_position}"
    )

    return (
        f"已收到走棋请求："
        f"{piece} 从 {from_position} 移动到 {to_position}。"
        f"本次仅验证参数传递，不判断走棋是否合法。"
    )

@tool
def get_piece_count_by_side(
        side: str,
        count: int,
        include_general: bool
) -> str:

    print(f"[Tool执行] 棋方={side}，数量={count}，是否包含将帅={include_general}")
    return f"返回结果：{side}，数量{count}，包含将帅={include_general}"