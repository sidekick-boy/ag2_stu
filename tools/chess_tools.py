from ag2 import tool,DataInput
# from typing import Literal
from enum import Enum
from typing import TypedDict, Optional
from typing_extensions import Required, NotRequired


class ChessSide(str, Enum):
    RED = "红方"
    BLACK = "黑方"

class ErrorCode(Enum):
    INVALID_SIDE = "棋方无效"
    INVALID_COUNT_TYPE = "数量类型错误"
    INVALID_COUNT = "数量超出范围"
    INVALID_BOOLEAN = "布尔参数错误"

class PieceCountData(TypedDict):
    side: str
    count: int
    include_general: bool

class ChessToolResult(TypedDict):
    success: bool
    code: str
    message: str
    data: Optional[PieceCountData]

class ChessPlayerData(TypedDict):
    name: str
    score: int


class ChessBoardData(TypedDict, total=True):
    red_count: int
    black_count: int
    current_player: ChessPlayerData




class ChessQueryResult(TypedDict, total=True):
    success: bool
    message: str
    board: NotRequired[Optional[ChessBoardData]]
    request_id: NotRequired[str]




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
        side: ChessSide,
        count: int,
        include_general: bool = True
) -> DataInput:

    # 1. 检查棋方
    if not isinstance(side, ChessSide):
        result = {
            "success": False,
            "code": ErrorCode.INVALID_SIDE.value,
            "message": "参数错误：side 必须是有效的棋方枚举",
            "data": None
        }
        return DataInput(result)

    # 2. 检查数量类型
    if type(count) is not int:
        result = {
            "success": False,
            "code": ErrorCode.INVALID_COUNT_TYPE.name,
            "message": "参数错误：count 必须是整数",
            "data": None
        }
        return DataInput(result)

    # 3. 检查数量范围
    if not 1 <= count <= 16:
        result = {
            "success": False,
            "code": ErrorCode.INVALID_COUNT.name,
            "message": "参数错误：count 必须在 1 到 16 之间",
            "data": None
        }
        return DataInput(result)

    # 4. 检查布尔参数
    if type(include_general) is not bool:
        result = {
            "success": False,
            "code": ErrorCode.INVALID_BOOLEAN.name,
            "message": "参数错误：include_general 必须是布尔值",
            "data": None
        }

        return DataInput(result)

    print(f"[Tool执行] 棋方={side.value}，数量={count}，是否包含将帅={include_general}")

    result = {
            "success": True,
            "code": "OK",
            "message": "查询成功",
            "data": {
        "side": side.value,
        "count": count,
        "include_general": include_general
    }
        }

    return DataInput(result)

#
# if __name__ == "__main__":
#     result1: ChessQueryResult = {
#         "success": True,
#         "message": "查询成功"
#     }
#
#     result2: ChessQueryResult = {
#         "success": True,
#         "message": "查询成功",
#         "board": None
#     }
#
#     print(result1)
#     print(result2)