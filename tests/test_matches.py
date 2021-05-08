from football.match import Match
from football.teams import Team
from football.leagues import League

import pytest

def test_match_init():

	league = League('Joe')
	team1 = Team(league)
	team2 = Team(league)

	match = Match(team1, team2, roundd=1, seasonind=1)

	assert match.season_index == 1
	assert match.round == 1
	assert match.home_team == team1.name
	assert match.home == team1
	assert match.away_team == team2.name
	assert match.away == team2


	wh, wa, draw = match.result_probability(team1.pick_team(), team2.pick_team())

	assert round(sum([wh, wa, draw]), 5) == 1


	hometeam, awayteam, hp, ap, score = match.play()

	assert match.home_goals is not None
	assert match.away_goals is not None
	assert hometeam == team1
	assert awayteam == team2

	assert team1.played('1') == 1
	assert team2.played('1') == 1
	assert team1.goals_for('1') == score[0]
	assert team2.goals_for('1') == score[1]
	assert match.result == score

	player = match.lineups[team1.name][0]
	assert player.appearances() == 1

	assert len(match.scorers('home')) == score[0]
	assert len(match.scorers('away')) == score[1]


