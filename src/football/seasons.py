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

    def fixture_list(self):
        """ Create a schedule for the teams in the list and return it"""
        teams = self.__league.teams
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

        self.__fixture_list = fixture_list

    @property
    def fixtures(self, round):
        ind = round - 1
        fixs = self.__fixture_list[ind]
        for i in fixs:
            print(i[0] + ' ' + i[1])

    def play_round(self):
        results = [Match(i[0], i[1]).play() for i in self.__fixture_list[0]]
        self.__results = results
    
    @property
    def results(self):
        return self.__results

    def play_season(self):
        pass

    def update_league(self):
        pass
