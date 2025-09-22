from settings import BOARD_LENGTH

class LinearBoard():
  @classmethod
  def fromList(cls, list):
      board = cls()
      board._column = list
      return board

  def __init__(self):
    self._column = []

  def as_list(self):
    return self._column

  def is_full(self):
    return len(self._column) >= BOARD_LENGTH

  def is_victory(self, user_notation):
    return self._column.count(user_notation) >= 3
  
  def add(self, user_notation):
    if not self.is_full():
      self._column.append(user_notation)

  def is_tie(self, user1_notation, user2_notation):
    return self.is_victory(user1_notation) or self.is_victory(user2_notation)