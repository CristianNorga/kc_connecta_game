from enum import Enum
from copy import deepcopy

from game.models.square_board import SquareBoard

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