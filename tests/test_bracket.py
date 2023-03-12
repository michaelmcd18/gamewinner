import pytest

from gamewinner.games.bracket import Bracket
from gamewinner.team import Team

first_four = (
    ("Notre Dame", "Rutgers"),
    ("Texas A&M-Corpus Christi", "Texas Southern"),
    ("Bryant", "Wright State"),
    ("Wyoming", "Indiana"),
)


class TestBracketBestWins:
    @pytest.mark.parametrize("winner,loser", first_four)
    def test_playoffs(
        self, best_wins_bracket: Bracket, winner: Team, loser: Team
    ) -> None:
        bracket = best_wins_bracket
        bracket.play()

        teams = {
            team.name
            for team in bracket.west.teams
            + bracket.east.teams
            + bracket.south.teams
            + bracket.midwest.teams
        }
        assert winner in teams
        assert loser not in teams

    def test_bracket_with_best_wins(self, best_wins_bracket: Bracket) -> None:
        bracket = best_wins_bracket
        bracket.play()

        # should be all #1s
        assert bracket.west.winner.name == "Gonzaga"
        assert bracket.east.winner.name == "Baylor"
        assert bracket.south.winner.name == "Arizona"
        assert bracket.midwest.winner.name == "Kansas"

        assert bracket.winner.name == "Arizona"
        assert bracket.runner_up.name == "Gonzaga"

    def test_all_first_round_matchups(self, best_wins_bracket: Bracket) -> None:
        """Make sure we set out the games in right order"""
        bracket = best_wins_bracket
        bracket.play()

        region = bracket.west.name.value.lower()
        gameorder = (
            ("Gonzaga", "Georgia State"),
            ("Boise State", "Memphis"),
            ("Connecticut", "New Mexico State"),
            ("Arkansas", "Vermont"),
            ("Alabama", "Notre Dame"),
            ("Texas Tech", "Montana State"),
            ("Michigan State", "Davidson"),
            ("Duke", "Cal State Fullerton"),
        )
        for idx, teams in enumerate(gameorder):
            gamenum = idx + 1
            winner = eval(f"bracket.{region}.w{gamenum}.name")
            loser = eval(f"bracket.{region}.l{gamenum}.name")
            assert winner == teams[0]
            assert loser == teams[1]


class TestBracketWorstWins:
    @pytest.mark.parametrize("best,worst", first_four)
    def test_playoffs(
        self, worst_wins_bracket: Bracket, best: Team, worst: Team
    ) -> None:
        bracket = worst_wins_bracket
        bracket.play()

        teams = {
            team.name
            for team in bracket.west.teams
            + bracket.east.teams
            + bracket.south.teams
            + bracket.midwest.teams
        }
        assert worst in teams
        assert best not in teams

    def test_bracket_with_best_wins(self, worst_wins_bracket: Bracket) -> None:
        bracket = worst_wins_bracket
        bracket.play()

        # should be all #1s
        assert bracket.west.winner.name == "Georgia State"
        assert bracket.east.winner.name == "Norfolk State"
        assert bracket.south.winner.name == "Wright State"
        assert bracket.midwest.winner.name == "Texas Southern"

        assert bracket.winner.name == "Texas Southern"
        assert bracket.runner_up.name == "Georgia State"
