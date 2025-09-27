from game.utils.board_utils import _is_within_column_range, _is_non_full_column, _is_int
from game.models.oracle import BaseOracle, ColumnClassification, ColumnRecommendation
from game.models.square_board import SquareBoard

class Player:
    def __init__(self, name, char = None, opponent = None, oracle: BaseOracle=BaseOracle()) -> None:
        self.name = name
        self.char = char
        self._oracle = oracle
        self.opponent = opponent
        self.last_move = None

    @property
    def opponent(self):
        return self._opponent

    @opponent.setter
    def opponent(self, other):
        self._opponent = other
        if other != None:
            assert other.char != self.char
            other._opponent = self

    def play(self, board: SquareBoard) -> None:
        (best, recommendations) = self._ask_oracle(board)
        self._play_on(board, best.index)

    def _play_on(self, board, position) -> None:
        board.add(position, self.char)
        self.last_move = position

    def _ask_oracle(self, board) -> tuple[ColumnRecommendation, list[ColumnRecommendation]]:
        recommendations = self._oracle.get_recommendation(board, self)
        best = self._choose(recommendations)

        return (best, recommendations)

    def _choose(self, recommendations: list[ColumnRecommendation]) -> ColumnRecommendation:
        recommendation = next(filter(lambda r: r.classification != ColumnClassification.FULL, recommendations), None)

        if recommendation is None:
            raise Exception("No hay columnas disponibles")
        return recommendation
    
class HumanPlayer(Player):
    def __init__(self, name, char = None, view=None) -> None:
        super().__init__(name, char)
        self.view = view

    def _ask_oracle(self, board) -> tuple[ColumnRecommendation, None]:
        while True:
            raw = self.view.ask_column() if self.view else input('Selecciona una columna: ')
            if _is_int(raw) and _is_within_column_range(board, int(raw)) and _is_non_full_column(board, int(raw)):
                position = int(raw)
                return (ColumnRecommendation(position, None), None)