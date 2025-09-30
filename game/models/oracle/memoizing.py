from game.models.oracle.base import ColumnRecommendation
from game.models.oracle.smart import SmartOracle


class MemoizingOracle(SmartOracle):
    def __init__(self) -> None:
        super().__init__()
        self._past_recommendations = {}

    def _make_key(board, player) -> str:
        return f'{board.as_code().raw_code}@{player.char}'

    def get_recommendation(self, board, player) -> list[ColumnRecommendation]:
        key = self._make_key(board, player)

        if key not in self._past_recommendations:
            self._past_recommendations[key] = super().get_recommendation(board, player)

        return self._past_recommendations[key]

