import pytest
from game.models.square_board import SquareBoard
from game.models.oracle import BaseOracle
from game.models.player import Player

def test_play():
    before = SquareBoard.fromList(
        [
            [None, None, None, None],
            ['x', 'o', 'x', 'o'],
            ['x', 'o', 'x', 'o'],
            ['x', None, None, None]
        ]
    )

    after = SquareBoard.fromList(
        [
            ['x', None, None, None],
            ['x', 'o', 'x', 'o'],
            ['x', 'o', 'x', 'o'],
            ['x', None, None, None]
        ]
    )

    player = Player('Chip', 'x', oracle = BaseOracle())

    player.play(before)
    assert before == after