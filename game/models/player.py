from game.utils.board_utils import _is_within_column_range, _is_non_full_column, _is_int
from game.models.oracle import BaseOracle, ColumnClassification, ColumnRecommendation
from game.models.square_board import SquareBoard

class Player:
    def __init__(self, name, char, oracle: BaseOracle) -> None:
        self.name = name
        self.char = char
        self._oracle = oracle

    def play(self, board: SquareBoard) -> None:
        recommendetions = self._oracle.get_recommendation(board, self)

        choice = self._choose(recommendetions)

        board.add(choice.index, self.char)


    def _choose(self, recommendations: list[ColumnRecommendation]) -> ColumnRecommendation:
        recommendation = next(filter(lambda r: r.classification != ColumnClassification.FULL, recommendations), None)

        if recommendation is None:
            raise Exception("No hay columnas disponibles")
        return recommendation
    
class HumanPlayer(Player):

    def __init__(self, name, char) -> None:
        super().__init__(name, char)

    def _ask_oracle(self, board) -> tuple[ColumnRecommendation, None]:
        while True:

            raw = input('Select a column: ')

            if _is_int(raw) and _is_within_column_range(board, int(raw)) and _is_non_full_column(board, int(raw)):

                position = int(raw)
                return (ColumnRecommendation(position, None), None)