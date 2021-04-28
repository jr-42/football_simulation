from football.leagues import League
from football.teams import Team
from football.seasons import Season

import pytest

def test_league_creation():

	league = League('Joe')

	assert league.name == 'Joe'

	assert str(league) == 'Joe'
	assert not league.current_season 

	assert not league.current_season_index
	assert isinstance(league.teams, list)
	assert isinstance(league.teams[0], Team)

	assert isinstance(league.get_team(league.teams[0].name), Team)

def test_league_and_season():

	league = League('Joe')
	season = league.new_season()
	
	assert isinstance(season, Season)
	assert isinstance(league.current_season, Season)
	assert league.current_season_index == 1
	assert isinstance(league.get_season(1), Season)

def test_league_and_new_season():

	league = League('Joe')
	season = league.new_season()
	season2 = league.new_season()

	all_teams = [t.name for t in league.teams]
	relegated = all_teams[-3:]

	season3 = league.new_season()

	assert league.current_season_index == 3
	assert not any([i in [t.name for t in league.teams] for i in relegated])


	

