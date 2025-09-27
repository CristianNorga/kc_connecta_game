

from game.models.player import Player

class Match:
    def __init__(self, player1, player2) -> None:
        player1.char = 'x'
        player2.char = 'o'
        player1.opponent = player2
        self._players = {'x' : player1, 'o' : player2}
        self._round_robbin = [player1, player2]
        assert (player1.opponent is not None) and (player2.opponent is not None), "Players are required to have an opponent for recommendations"

    @property 
    def next_player(self) -> Player:
        next = self._round_robbin[0]
        self._round_robbin.reverse()
        return next
    
    def get_player(self, char) -> Player:
        return self._players[char]
    
    def get_winner(self, board) -> Player | None:
        if board.is_victory('x') :
            return self.get_player('x')
        elif board.is_victory('o') :
            return self.get_player('o')
        else:
            return None

    def is_match_over(self) -> bool:
        answer = input('Would you like to play another match? (Y/N) ').upper()
        return (answer != 'Y')
