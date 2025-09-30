from game.models.square_board import SquareBoard
from game.models.oracle import BaseOracle
from game.models.player import Player

def test_play():
    board = SquareBoard.fromList(
        [
            [None, None, None, None],
            ['x', 'o', 'x', 'o'],
            ['x', 'o', 'x', 'o'],
            ['x', None, None, None]
        ]
    )

    number_of_empty = sum(1 for row in board.columns_as_lists() for cell in row if cell is None)

    player = Player('Chip', 'x', oracle = BaseOracle())

    player.play(board)
    assert number_of_empty - 1 == sum(1 for row in board.columns_as_lists() for cell in row if cell is None)