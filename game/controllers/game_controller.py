
from enum import Enum, auto

from game.models.square_board import SquareBoard
from game.controllers.match_controller import Match
from game.models.player import Player, HumanPlayer
from game.views.terminal_view import TerminalView

class RoundType(Enum):
    COMPUTER_VS_COMPUTER = auto()
    COMPUTER_VS_HUMAN = auto()


class DifficultyLevel(Enum):
    LOW = auto()
    MEDIUM = auto()
    HIGH = auto()


class Game():

    def __init__(
        self,
        round_type=RoundType.COMPUTER_VS_COMPUTER,
        match=Match(Player('Chip'), Player('Chop'))
    ) -> None:
        self.board = SquareBoard()
        self.round_type = round_type
        self.match = match
        self.view = TerminalView()

    def start(self) -> None:
        self.view.print_logo()
        self._configure_by_user()
        self._start_game_loop()

    def _start_game_loop(self) -> None:
        while True:
            current_player = self.match.next_player
            current_player.play(self.board)
            self.view.display_move(current_player)
            self.view.display_board(self.board)
            if self._is_game_over():
                self.view.display_result(self.match.get_winner(self.board), self.match)
                break


    def _is_game_over(self) -> bool:
        winner = self.match.get_winner(self.board)
        if winner is not None or self.board.is_full():
            return True
        else:
            return False


    def _configure_by_user(self) -> None:
        self.round_type = self._get_round_type()
        self.match = self._make_match()


    def _make_match(self) -> Match:
        if self.round_type == RoundType.COMPUTER_VS_COMPUTER:
            player1 = Player('T-X')
            player2 = Player('T-1000')
        else:
            player1 = Player('T-800')
            player2 = HumanPlayer(name=self.view.ask_human_name(), view=self.view)
        return Match(player1, player2)


    def _get_round_type(self) -> RoundType:
        response = self.view.select_round_type()
        if response == '1':
            return RoundType.COMPUTER_VS_COMPUTER
        else:
            return RoundType.COMPUTER_VS_HUMAN
