from gamewinner.strategies.istrategy import IStrategy
from gamewinner.team import Team


class HighestWins(IStrategy):
    def pick(self, team1: Team, team2: Team) -> Team:
        assert team1.rank_nat != team2.rank_nat
        diff = team1.rank_reg - team2.rank_reg
        if diff > 0:
            return team1
        if diff < 0:
            return team2
        if diff == 0:
            if team1.rank_nat > team2.rank_nat:
                return team2
            return team1
        raise ValueError(f"impossible outcome: {team1=}, {team2=}")

    def predict_score(self, winner: Team, loser: Team) -> tuple[int, int]:
        return 81, 67
