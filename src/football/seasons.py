import pandas as pd
from football.match import Match
from football.leagues import League


class Season:

    def __init__(self,
                 league=None):
        if not league:
            self.__league = League()
        else:
            self.__league = league

        self.__results = []

    @property
    def league(self):
        return self.__league

    @staticmethod
    def make_fixture_list(teamlist):
        """ Create a schedule for the teams in the list and return it"""
        teams = teamlist
        fixture_list = []
        if len(teams) % 2 == 1:
            teams = teams + [None]
        # manipulate map_ (array of indexes for list) instead of list itself
        # this takes advantage of even/odd indexes to determine home vs. away
        n = len(teams)
        map_ = list(range(n))
        mid = n // 2
        for i in range(n-1):
            l1 = map_[:mid]
            l2 = map_[mid:]
            l2.reverse()
            round = []
            for j in range(mid):
                t1 = teams[l1[j]]
                t2 = teams[l2[j]]
                if j == 0 and i % 2 == 1:
                    # flip the first match only, every other round
                    # (this is because the first match always involves
                    # the last player in the list)
                    round.append((t2, t1))
                else:
                    round.append((t1, t2))
            fixture_list.append(round)
            # rotate list by n/2, leaving last element at the end
            map_ = map_[mid:-1] + map_[:mid] + map_[-1:]

        return fixture_list

    def fixtures(self, round):
        ind = round - 1
        fixs = self.__fixture_list[ind]
        for i in fixs:
            print(i[0].name + ' VS ' + i[1].name)

    @staticmethod
    def play_round(day):
        results = [Match(i[0], i[1]).play() for i in day]
        return results

    def results(self, round):
        round_results = self.__results[round-1]
        round_fixtures = self.__fixture_list[round-1]
        print('Results for match day: {}'.format(round))
        for r, f in zip(round_results, round_fixtures):
            print(f[0].name + ' ', r[2][0], '-', r[2][1], ' ' + f[1].name)

    @staticmethod
    def make_league_table(teams):

        cols = ['Name', 'P', 'W', 'D', 'L', 'GF', 'GA', 'GD', 'Points']
        df = pd.DataFrame(columns=cols)

        for i, team in enumerate(teams):
            df.loc[i, 'Name'] = team.name
            # df.loc[i, 'Team_Rating'] = team.rating
            # df.loc[i, 'Squad_Value'] = team.theteam.loc[:, 'Value'].sum()
            df.loc[i, 'P'] = team.wins + team.loses + team.draws
            df.loc[i, 'W'] = team.wins
            df.loc[i, 'D'] = team.draws
            df.loc[i, 'L'] = team.loses
            df.loc[i, 'GF'] = team.goals_for
            df.loc[i, 'GA'] = team.goals_against
            df.loc[i, 'GD'] = team.goals_for - team.goals_against
            df.loc[i, 'Points'] = (3*team.wins) + team.draws

        # df.fillna(0, inplace=True)

        df = df.sort_values(
            ['Points', 'GD', 'GF'],
            ascending=[False, False, False]).reset_index(drop=True)

        df.index = range(1, len(df)+1)

        return df

    @property
    def league_table(self):
        return self.make_league_table(self.league.teams)

    def play_season(self):

        part1 = self.make_fixture_list(self.__league.teams)
        part2 = self.make_fixture_list(self.__league.teams[::-1])
        self.__fixture_list = part1 + part2

        for day in self.__fixture_list:
            self.__results.append(self.play_round(day))

    def new_season(self):
        pass