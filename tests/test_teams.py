from football.leagues import League
from football.teams import Team
from football.seasons import Season
from football.players import Player, Goalkeeper, Defender, Midfielder, Attacker
from football.match import Match

import pytest

def test_team_creation():

	team = Team(League('Joes League'))

	assert isinstance(team.name, str)
	assert isinstance(team.rating, float)
	assert isinstance(list(team.getteam.values())[0], Player)

	first11 = team.pick_team()
	assert len(first11) == 11
	
	formation = team.style
	assert len([i for i in first11 if isinstance(i, Defender)]) == int(formation[0])
	assert len([i for i in first11 if isinstance(i, Midfielder)]) == int(formation[1])
	assert len([i for i in first11 if isinstance(i, Attacker)]) == int(formation[2])

	rating = team.rating
	team.upgrade(0) #equivalent to finishing first
	assert team.rating == rating + (0.07*rating)

def test_team_matches():

	team1 = Team(League('Joes League'))
	team2 = Team(League('Joes League'))

	match = Match(team1, team2, roundd=1, seasonind=1)

	# test add win

	team1.win(csi='1', goals_for=2, goals_against=1)
	assert team1.goals_for('1') == 2
	assert team1.goals_against('1') == 1
	assert team1.wins('1') == 1
	assert team1.played('1') == 1

	# test add loss

	team1.lose(csi='1', goals_for=2, goals_against=3)
	assert team1.goals_for('1') == 4
	assert team1.goals_against('1') == 4
	assert team1.loses('1') == 1
	assert team1.played('1') == 2

	# test add draw

	team1.draw(csi='1', goals_for=2, goals_against=2)
	assert team1.goals_for('1') == 6
	assert team1.goals_against('1') == 6
	assert team1.draws('1') == 1
	assert team1.played('1') == 3

	#totals
	assert team1.wins() == 1
	assert team1.loses() == 1
	assert team1.goals_for() == 6
	assert team1.goals_against() == 6
	assert team1.draws() == 1
	assert team1.played() == 3

	# test add match 
	match.play()

	assert isinstance(team1.get_match(season='1', roundd='1'), Match)

	assert team1.played('1') == 4

	match2 = Match(team1, team2, roundd=2, seasonind=2)
	match2.play()
	assert team1.played('2') == 1
	assert team1.played() == 5

def test_team_player():

	team = Team(League('Joes League'))

	assert isinstance(team.get_player(list(team._Team__whole_team.keys())[0]), Player)

