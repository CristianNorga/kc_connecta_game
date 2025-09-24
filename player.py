from oracle import BaseOracle, ColumnClassification, ColumnRecommendation
from square_board import SquareBoard

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