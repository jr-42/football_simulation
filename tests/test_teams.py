from football.leagues import League
from football.teams import Team
from football.seasons import Season
from football.players import Player, Goalkeeper, Defender, Midfielder, Attacker

import pytest

def test_team_creation():

	team = Team(League('Joes League'))

	assert isinstance(team.name, str)
	assert isinstance(team.rating, int)
	assert isinstance(list(team.getteam.values())[0], Player)

	first11 = team.pick_team()
	assert len(first11) == 11
	
	formation = team.style
	assert len([i for i in first11 if isinstance(i, Defender)]) == int(formation[0])
	assert len([i for i in first11 if isinstance(i, Midfielder)]) == int(formation[1])
	assert len([i for i in first11 if isinstance(i, Attacker)]) == int(formation[2])
