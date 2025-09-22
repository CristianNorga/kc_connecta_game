from linear_board import LinearBoard
from settings import BOARD_LENGTH
from list_utils import *

class SquareBoard():
    """
    Representa un tablero cuadrado
    """

    @classmethod
    def fromList(cls, list_of_lists):
        """
        Transforma una lista de listas en una list de LinearBoard
        """
        board = cls()
        board._columns = list(map(lambda element: LinearBoard.fromList(element), list_of_lists) )
        return board

    def __init__(self):
        self._columns = [LinearBoard() for i in range(BOARD_LENGTH)]

    def columns_as_lists(self):
        return [col.as_list() for col in self._columns]
    
    def is_full(self):
        """
        True si todos los LinearBoards están llenos
        """
        result = True
        for lb in self._columns:
            result = result and lb.is_full()
        return result

    # Detectra victorias
    def is_victory(self, char):
        return self._any_vertical_victory(char) \
            or self._any_horizontal_victory(char) \
            or self._any_sinking_victory(char) \
            or self._any_rising_victory(char)

    def _any_vertical_victory(self, char):
        result = False
        for lb in self._columns:
            result = result or lb.is_victory(char)
        return result

    def _any_horizontal_victory(self, char):
        transposed = transpose(self.columns_as_lists())

        sb_temp = SquareBoard().fromList(transposed)

        return sb_temp._any_vertical_victory(char)

    def _any_sinking_victory(self, char):
        columns_lists = self.columns_as_lists()

        d_matrix = displace_matrix(columns_lists)

        temp = SquareBoard().fromList(d_matrix)

        return temp._any_horizontal_victory(char)
    
    def _any_rising_victory(self, char):
        columns_lists = self.columns_as_lists()

        r_matrix = reverse_matrix(columns_lists)

        temp = SquareBoard().fromList(r_matrix)

        return temp._any_sinking_victory(char)


    # dunders
    def __repr__(self):
        return f'{self.__class__}:{self._columns}'