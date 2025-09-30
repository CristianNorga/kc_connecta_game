from enum import Enum
from copy import deepcopy

from game.models.square_board import SquareBoard
from data.settings import BOARD_LENGTH

class ColumnClassification(Enum):
  FULL    = -1
  LOSE    = 1
  MAYBE   = 10
  WIN     = 100

class ColumnRecommendation():
  # dunders
  def __init__(self, index, classification) -> None:
    self.index = index
    self.classification = classification

  def __eq__(self, other) -> bool:
    if not isinstance(other, self.__class__):
      return False

    return self.classification == other.classification

  def __hash__(self) -> int:
    return hash((self.index, self.classification))

class BaseOracle:
  def __init__(self) -> None:
    pass

  def get_recommendation(self, board: SquareBoard, player) -> list[ColumnRecommendation]:
    recommendations = []
    for i in range(len(board)):
      recommendations.append(self._get_column_recommendation(board, i, player))
    return recommendations

  def _get_column_recommendation(self, board: SquareBoard, index: int, player) -> ColumnRecommendation:
    if board._columns[index].is_full():
      return ColumnRecommendation(index, ColumnClassification.FULL)
    else:
      return ColumnRecommendation(index, ColumnClassification.MAYBE)
    
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
