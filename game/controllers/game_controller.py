
from enum import Enum, auto

from game.models.oracle import SmartOracle, BaseOracle
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
        if self.round_type == RoundType.COMPUTER_VS_HUMAN:
            self._difficulty_level = self._get_difficulty_level()
        self.match = self._make_match()


    def _make_match(self) -> Match:
        _levels = {
            DifficultyLevel.LOW: BaseOracle(),
            DifficultyLevel.MEDIUM: SmartOracle(),
            DifficultyLevel.HIGH: SmartOracle()
        }
        
        if self.round_type == RoundType.COMPUTER_VS_COMPUTER:
            player1 = Player('T-X', oracle=SmartOracle())
            player2 = Player('T-1000', oracle=SmartOracle())
        else:
            player1 = Player('T-800', oracle=_levels[self._difficulty_level])
            player2 = HumanPlayer(name=self.view.ask_human_name(), view=self.view)
        return Match(player1, player2)


    def _get_round_type(self) -> RoundType:
        response = self.view.select_round_type()
        if response == '1':
            return RoundType.COMPUTER_VS_COMPUTER
        else:
            return RoundType.COMPUTER_VS_HUMAN
        
    def _get_difficulty_level(self) -> DifficultyLevel:
        response = self.view.select_difficulty_level()
        if response == '1':
            level = DifficultyLevel.LOW
        elif response == '2':
            level = DifficultyLevel.MEDIUM
        else:
            level = DifficultyLevel.HIGH
        
        return level