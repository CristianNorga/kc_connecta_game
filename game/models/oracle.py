from game.models.square_board import SquareBoard
from enum import Enum, auto

class ColumnClassification(Enum):
  FULL = auto()
  MAYBE = auto()

class ColumnRecommendation():
  # dunders
  def __init__(self, index, classification) -> None:
    self.index = index
    self.classification = classification

  def __eq__(self, other) -> bool:
    if not isinstance(other, self.__class__):
      return False
      
    return self.index == other.index and self.classification == other.classification
  
  def __hash__(self) -> int:
    return hash((self.index, self.classification))

class BaseOracle:
  def __init__(self) -> None:
    pass

  def get_recommendation(self, board: SquareBoard, player) -> list[ColumnRecommendation]:
    recommendations = []
    for i, linear_board in enumerate(board.columns_as_linear_board()):
      recommendations.append(self._get_column_recommendation(linear_board, i, player))
    return recommendations

  def _get_column_recommendation(self, col, index: int, player) -> ColumnRecommendation:
    if col.is_full():
      return ColumnRecommendation(index, ColumnClassification.FULL)
    else:
      return ColumnRecommendation(index, ColumnClassification.MAYBE)