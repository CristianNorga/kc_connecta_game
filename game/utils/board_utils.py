# funciones de validación de índice de columna

from game.models.square_board import SquareBoard
from data.settings import BOARD_LENGTH


def _is_non_full_column(board: SquareBoard, num: int) -> bool:
    return not board._columns[num].is_full()

def _is_within_column_range(board: SquareBoard, num: int) -> bool:
    return num >= 0 and num < BOARD_LENGTH

def _is_int(aString: str) -> bool:
    try:
        num = int(aString)
        return True
    except:
        return False