from game.models.linear_board import LinearBoard
from data.settings import BOARD_LENGTH
from game.utils.list_utils import collapse_matrix, replace_all_in_matrix, transpose, displace_matrix, reverse_matrix
from game.utils.string_utils import explode_list_of_strings

class SquareBoard():
    @classmethod
    def fromList(cls, list_of_lists) -> 'SquareBoard':
        board = cls()
        board._columns = list(map(lambda element: LinearBoard.fromList(element), list_of_lists))
        return board
    
    @classmethod
    def fromBoardCode(cls, board_code) -> 'SquareBoard':
        return cls.fromBoardRawCode(board_code.raw_code)

    @classmethod
    def fromBoardRawCode(cls, board_raw_code) -> 'SquareBoard':
        list_of_strings = board_raw_code.split("|")

        matrix = explode_list_of_strings(list_of_strings)

        matrix = replace_all_in_matrix(matrix, '.', None)

        return cls.fromList(matrix)

    # dunders
    def __init__(self) -> None:
        self._columns: list[LinearBoard] = [LinearBoard() for i in range(BOARD_LENGTH)]
        
    def __repr__(self) -> str:
        return f'{self.__class__}:{self._columns}'
    
    def __eq__(self, other) -> bool:
        if not isinstance(other, self.__class__):
            return False
        
        return self.columns_as_lists() == other.columns_as_lists()
    
    def __len__(self):
        return len(self._columns)
    
    def __hash__(self):
        return hash(self._columns)

    def columns_as_lists(self) -> list[list]:
        return [col.as_list() for col in self._columns]
    
    def columns_as_linear_board(self) -> list[LinearBoard]:
        return self._columns
    
    def is_full(self) -> bool:
        result = True
        for lb in self._columns:
            result = result and lb.is_full()
        return result
    
    def as_code(self):
        return BoardCode(self)
    
    def add(self, column_index: int, user_notation) -> None:
        self._columns[column_index].add(user_notation)

    def is_victory(self, char) -> bool:
        return self._any_vertical_victory(char) \
            or self._any_horizontal_victory(char) \
            or self._any_sinking_victory(char) \
            or self._any_rising_victory(char)

    def _any_vertical_victory(self, char) -> bool:
        result = False
        for lb in self._columns:
            result = result or lb.is_victory(char)
        return result

    def _any_horizontal_victory(self, char) -> bool:
        transposed = transpose(self.columns_as_lists())

        sb_temp = SquareBoard().fromList(transposed)

        return sb_temp._any_vertical_victory(char)

    def _any_sinking_victory(self, char) -> bool:
        columns_lists = self.columns_as_lists()

        d_matrix = displace_matrix(columns_lists)

        temp = SquareBoard().fromList(d_matrix)

        return temp._any_horizontal_victory(char)
    
    def _any_rising_victory(self, char) -> bool:
        columns_lists = self.columns_as_lists()

        r_matrix = reverse_matrix(columns_lists)

        temp = SquareBoard().fromList(r_matrix)

        return temp._any_sinking_victory(char)
    
class BoardCode:

    def __init__(self, board: SquareBoard) -> None:
        self._raw_code = collapse_matrix(board.columns_as_lists())

    @property
    def raw_code(self) -> str:
        return self._raw_code

    def __eq__(self, other) -> bool:
        if not isinstance(other, self.__class__):
            return False
        else:
            return self.raw_code == other.raw_code

    def __hash__(self) -> int:
        return hash(self.raw_code)

    def __repr__(self) -> str:
        return f'{self.__class__}: {self.raw_code}'