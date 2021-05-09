from football.players import Player, Goalkeeper, Defender, Midfielder, Attacker
from football.teams import Team
from football.match import Match

import pytest

def test_player():

	player = Player('team joe', 0.5)

	assert isinstance(player.name, str)
	assert isinstance(player.nationality, str)
	assert player.foot in ['left', 'right']

	assert isinstance(player.age, int)


def test_spec_player():

	players = [Goalkeeper(), Defender(), Midfielder(), Attacker()]
	assert all([i.position for i in players])
	assert all([i.goalscoring for i in players])



def test_player_stats():

	team1 = Team()
	team2 = Team()

	match = Match(team1, team2, 1, 1)
	match.play()
	match = Match(team1, team2, 2, 1)
	match.play()
	match = Match(team1, team2, 3, 1)
	match.play()
	match = Match(team1, team2, 4, 1)
	match.play()
	match = Match(team1, team2, 5, 1)
	match.play()

	players = list(team1.getteam.values())
	player = max(players, key=lambda x: x.rating)

	assert player.appearances('1') == 5
	assert player.appearances() == 5
	assert player.appearances('1', '1') == 1