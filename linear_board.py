from settings import BOARD_LENGTH

class LinearBoard():
  def __init__(self):
    self.board = []

  def is_full(self):
    return len(self.board) >= BOARD_LENGTH

  def is_victory(self, user_notation):
    return self.board.count(user_notation) >= 3
  
  def add(self, user_notation):
    if not self.is_full():
      self.board.append(user_notation)

  def is_tie(self, user1_notation, user2_notation):
    return self.is_victory(user1_notation) or self.is_victory(user2_notation)