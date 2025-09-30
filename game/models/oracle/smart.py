from copy import deepcopy

from data.settings import BOARD_LENGTH
from game.models.oracle.base import BaseOracle, ColumnClassification, ColumnRecommendation
from game.models.square_board import SquareBoard


class SmartOracle(BaseOracle):
    def _get_column_recommendation(self, board: SquareBoard, index: int, player) -> ColumnRecommendation:
        recommendation = super()._get_column_recommendation(board, index, player)
        if recommendation.classification == ColumnClassification.MAYBE:
            if self._is_winning_move(board, index, player):
                recommendation.classification = ColumnClassification.WIN
            elif self._is_losing_move(board, index, player):
                recommendation.classification = ColumnClassification.LOSE

        return recommendation

    def _is_losing_move(self, board, index, player) -> bool:
        will_lose = False
        for i in range(0, BOARD_LENGTH):
            if self._is_winning_move(board, i, player.opponent) and i != index:
                will_lose = True
                break
        return will_lose

    def _is_winning_move(self, board, index, player) -> bool:
        tmp = self._play_on_tmp_board(board, index, player)

        return tmp.is_victory(player.char)

    def _play_on_tmp_board(self, board: SquareBoard, index: int, player) -> SquareBoard:
        tmp = deepcopy(board)

        tmp.add(index, player.char)

        return tmp