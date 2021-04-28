import pandas as pd
from typing import List, Tuple
from football.match import Match

class Season:

    def __init__(self,
                 league=None,
                 index: int=None):
        
        if not league:
            self.__league = League()
        else:
            self.__league = league

        self.__results: List = None
        self.__index: str = str(index)

        part1 = self.make_fixture_list(league.teams)
        part2 = self.make_fixture_list(league.teams[::-1])
        self.__fixture_list = part1 + part2

    def __repr__(self):
        return f'Season {self.__index} of {self.league}'

    def __str__(self):
        return f'Season {self.__index} of {self.league}'

    @property
    def league(self):
        return self.__league

    @property
    def current_season_index(self):
        return self.__index

    @staticmethod
    def make_fixture_list(teamlist: List) -> List:
        """ Create a schedule for the teams in the list and return it"""
        fixture_list = []
        if len(teamlist) % 2 != 0:
            raise Exception('Uneven number of teams')
        # manipulate map_ (array of indexes for list) instead of list itself
        # this takes advantage of even/odd indexes to determine home vs. away
        n = len(teamlist)
        map_ = list(range(n))
        mid = n // 2
        for i in range(n-1):
            l1 = map_[:mid]
            l2 = map_[mid:]
            l2.reverse()
            roundd = []
            for j in range(mid):
                t1 = teamlist[l1[j]]
                t2 = teamlist[l2[j]]
                if j == 0 and i % 2 == 1:
                    # flip the first match only, every other round
                    # (this is because the first match always involves
                    # the last player in the list)
                    roundd.append((t2, t1))
                else:
                    roundd.append((t1, t2))
            fixture_list.append(roundd)
            # rotate list by n/2, leaving last element at the end
            map_ = map_[mid:-1] + map_[:mid] + map_[-1:]

        return fixture_list

    def __get_fixtures_by_round(self, roundd: str):
        ind = int(roundd) - 1
        fixs = self.__fixture_list[ind]
        return fixs


    def fixtures_by_round(self, roundd: str):
        fixs = self.__get_fixtures_by_round(roundd)
        for i in fixs:
            print(i[0].name + ' VS ' + i[1].name)

    def play_round(self, fix_of_round: List[Tuple], roundd=int) -> List:
        results = [Match(matchup[0], matchup[1], roundd=roundd, seasonind=self.current_season_index).play() for matchup in fix_of_round]
        return results

    def __get_results_by_round(self, roundd: str):
        round_results = self.__results[int(roundd)-1]
        return round_results

    def results_by_round(self, roundd: str):
        round_results = self.__get_results_by_round(roundd)
        print('Results for match day: {}'.format(roundd))
        for match in round_results:
            print(match[0].name + ' ', match[-1][0], '-', match[-1][1], ' ' + match[1].name)

    def __get_results_by_team(self, team: str):
        team_results = [[i for i in j if (team in (i[0].name, i[1].name))] for j in self.__results]
        team_results = [i[0] for i in team_results]
        return team_results

    def results_by_team(self, team: str):
        team_results = self.__get_results_by_team(team)
        print('Results for team: {}'.format(team))
        for match in team_results:
            print(match[0].name + ' ', match[-1][0], '-', match[-1][1], ' ' + match[1].name)

    def make_league_table(self, teams: List):

        cols = ['Name', 'P', 'W', 'D', 'L', 'GF', 'GA', 'GD', 'Points']
        df = pd.DataFrame(columns=cols)

        for i, team in enumerate(teams):
            df.loc[i, 'Name'] = team.name
            # df.loc[i, 'Team_Rating'] = team.rating
            # df.loc[i, 'Squad_Value'] = team.theteam.loc[:, 'Value'].sum()
            df.loc[i, 'P'] = team.wins(season=str(self.current_season_index)) + team.loses(season=str(self.current_season_index))  + team.draws(season=str(self.current_season_index))
            df.loc[i, 'W'] = team.wins(season=str(self.current_season_index))
            df.loc[i, 'D'] = team.draws(season=str(self.current_season_index))
            df.loc[i, 'L'] = team.loses(season=str(self.current_season_index))
            df.loc[i, 'GF'] = team.goals_for(season=str(self.current_season_index))
            df.loc[i, 'GA'] = team.goals_against(season=str(self.current_season_index)) 
            df.loc[i, 'GD'] = team.goals_for(season=str(self.current_season_index)) - team.goals_against(season=str(self.current_season_index))
            df.loc[i, 'Points'] = (3*team.wins(season=str(self.current_season_index))) + team.draws(season=str(self.current_season_index)) 

        # df.fillna(0, inplace=True)

        df = df.sort_values(
            ['Points', 'GD', 'GF'],
            ascending=[False, False, False]).reset_index(drop=True)

        df.index = list(range(1, len(df)+1))

        return df

    @property
    def league_table(self) -> pd.DataFrame:
        return self.make_league_table(self.league.teams)

    def play_season(self):

        for i, fix_of_round in enumerate(self.__fixture_list):
            if not self.__results:
                self.__results = []
            self.__results.append(self.play_round(fix_of_round, roundd=i+1))
