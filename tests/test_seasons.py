from football.leagues import League
from football.teams import Team
from football.seasons import Season

import pytest

def test_season_creation():

	league = League('Joe')

	season = Season(league=league, index=1)

	assert season.league == league
	assert season.current_season_index == '1'

	assert season.league_table['P'].sum() == 0

def test_fixture_maker():

	league = League('Joe')

	season = Season(league=league, index=1)

	fixture_list = season.make_fixture_list(league.teams) + season.make_fixture_list(league.teams[::-1])

	# 38 rounds
	assert len(fixture_list) == 38
	# 380 matches
	assert sum([len(i) for i in fixture_list]) == 380
	# fixture is made of teams
	assert isinstance(fixture_list[0][0][0], Team)
	# no team plays itseld
	for day in fixture_list:
		for matchup in day:
			assert matchup[0] != matchup[1]

	# team A plays all other teams
	teamA = fixture_list[0][0][0].name
	opposition = []
	for day in fixture_list:
		for matchup in day:
			if teamA == matchup[0].name:
				opposition.append(matchup[1].name)
			elif teamA == matchup[1].name:
				opposition.append(matchup[0].name)


	unique_opposition = list(set(opposition))
	unique_opposition + [teamA] == [team.name for team in league.teams]

def test_season_play_season():

	league = League('Joe')

	season = Season(league=league, index=1)

	season.play_season()

	assert season.league_table['P'].sum() == 760
	assert season.league_table['W'].sum() == season.league_table['L'].sum()
	assert season.league_table['GF'].sum() == season.league_table['GA'].sum()
	assert season.league_table['GD'].sum() == 0

	assert len(season._Season__get_results_by_round(1)) == 10

