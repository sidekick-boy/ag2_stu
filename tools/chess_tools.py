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