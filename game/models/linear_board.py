from data.settings import BOARD_LENGTH, VICTORY_STRIKE
from game.utils.list_utils import find_streak

class LinearBoard():
  @classmethod
  def fromList(cls, list):
      board = cls()
      board._column = list
      return board

  def __init__(self) -> None:
    self._column = [None for i in range(BOARD_LENGTH)]

  def as_list(self) -> list:
    return self._column

  def is_full(self) -> bool:
    return all(map(lambda x: x != None, self._column))

  def is_victory(self, user_notation) -> bool:
    return find_streak(self._column, user_notation, VICTORY_STRIKE)
  
  def add(self, user_notation) -> None:
    if not self.is_full():
      i = self._column.index(None)
      self._column[i] = user_notation

  def is_tie(self, user1_notation, user2_notation) -> bool:
    return self.is_victory(user1_notation) == False and self.is_victory(user2_notation) == False
  
  # Dunders
  def __len__(self) -> int:
    return len(self._column)