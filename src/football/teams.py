import random
import pandas as pd
from football.players import Goalkeeper, Defender, Midfielder, Attacker
from football.names_lists import town_names

team_suffix = ['Town', 'Rovers', 'United', 'City', '', 'Wanderers',
               'F.C.']


def team_dataframe(gks, defs, mids, atts):

    players = gks + defs + mids + atts
    cols = ['Name', 'DOB', 'Age', 'Nationality', 'Position',
            'Foot', 'Rating', 'Value']
    df = pd.DataFrame(columns=cols)

    for i, player in enumerate(players):
        df.loc[i, 'Name'] = player.name
        df.loc[i, 'DOB'] = player.dob
        df.loc[i, 'Age'] = player.age
        df.loc[i, 'Nationality'] = player.nationality
        df.loc[i, 'Position'] = player.position
        df.loc[i, 'Foot'] = player.foot
        df.loc[i, 'Rating'] = player.rating
        df.loc[i, 'Value'] = player.value

    return df


class Team(object):

    def __init__(self,
                 league=None):
        self.__name = random.choice(town_names) + ' ' + random.choice(team_suffix)
        self.__rating = random.randint(1, 5)
        self.__gks = [Goalkeeper(team=self.__name, team_rating=self.__rating)
                      for i in range(3)]
        self.__defs = [Defender(team=self.__name, team_rating=self.__rating)
                       for i in range(8)]
        self.__mids = [Midfielder(team=self.__name, team_rating=self.__rating)
                       for i in range(7)]
        self.__atts = [Attacker(team=self.__name, team_rating=self.__rating)
                       for i in range(5)]

        self.__whole_team = self.__gks + self.__defs + self.__mids + self.__atts
        self.__whole_team = {i.name:i for i in self.__whole_team}

        self.__equip = team_dataframe(self.__gks, self.__defs,
                                      self.__mids, self.__atts)

        self.__style = random.choice(['442', '343', '532', '433'])

        self.__league = league

        self.__wins = {}
        self.__loses = {}
        self.__draws = {}
        self.__gf = {}
        self.__ga = {}
        self.__matches = {}

    def __repr__(self):
        return self.name

    def __str__(self):
        return self.name

    @property
    def name(self):
        return self.__name

    @property
    def rating(self):
        return self.__rating

    @property
    def gks(self):
        return self.__gks

    @property
    def defs(self):
        return self.__defs

    @property
    def mids(self):
        return self.__mids

    @property
    def atts(self):
        return self.__atts

    @property
    def theteam(self):
        return self.__equip

    @property
    def style(self):
        return self.__style

    @property
    def league(self):
        return self.__league

    @league.setter
    def league(self, name):
        self.__league = name

    def wins(self, season=None):
        if season:
            return self.__wins.get(season, 0)
        else:
            return sum(list(self.__wins.values()))

    def loses(self, season=None):
        if season:
            return self.__loses.get(season, 0)
        else:
            return sum(list(self.__loses.values()))

    def draws(self, season=None):
        if season:
            return self.__draws.get(season, 0)
        else:
            return sum(list(self.__draws.values()))

    def goals_for(self, season=None):
        if season:
            return self.__gf.get(season, 0)
        else:
            return sum(list(self.__gf.values()))
    
    def goals_against(self, season=None):
        if season:
            return self.__ga.get(season, 0)
        else:
            return sum(list(self.__ga.values()))

    def matches(self, season, round=None):
        if not round:
            return self.__matches[season]
        else:
            return self.__matches[season][str(round)]

    def add_match(self, season, round, match):
        if season in self.__matches.keys():
            if str(round) in self.__matches[season]:
                self.__matches[season][str(round)].append(match)
            else:
                self.__matches[season][str(round)] = match
        else:
            self.__matches[season] = {str(round):match}

    def win(self, csi: int, goals_for: int, goals_against: int):

        if csi == 0:
            raise Exception

        if str(csi) in self.__wins.keys():
            self.__wins[str(csi)]  = self.__wins[str(csi)]  + 1
        else:
            self.__wins[str(csi)] = 1

        if str(csi) in self.__gf.keys():
            self.__gf[str(csi)]  = self.__gf[str(csi)]  + goals_for
        else:
            self.__gf[str(csi)] = goals_for

        if str(csi) in self.__ga.keys():
            self.__ga[str(csi)]  = self.__ga[str(csi)]  + goals_against
        else:
            self.__ga[str(csi)] = goals_against

    def lose(self, csi: int, goals_for: int, goals_against: int):

        if str(csi) in self.__loses.keys():
            self.__loses[str(csi)] = self.__loses[str(csi)] + 1
        else:
            self.__loses[str(csi)] = 1

        if str(csi) in self.__gf.keys():
            self.__gf[str(csi)]  = self.__gf[str(csi)]  + goals_for
        else:
            self.__gf[str(csi)] = goals_for

        if str(csi) in self.__ga.keys():
            self.__ga[str(csi)] = self.__ga[str(csi)]  + goals_against
        else:
            self.__ga[str(csi)] = goals_against

    def draw(self, csi: int, goals_for: int, goals_against: int):

        if str(csi) in self.__draws.keys():
            self.__draws[str(csi)]  = self.__draws[str(csi)]  + 1
        else:
            self.__draws[str(csi)] = 1

        if str(csi) in self.__gf.keys():
            self.__gf[str(csi)] = self.__gf[str(csi)]  + goals_for
        else:
            self.__gf[str(csi)] = goals_for

        if str(csi) in self.__ga.keys():
            self.__ga [str(csi)] = self.__ga[str(csi)]  + goals_against
        else:
            self.__ga[str(csi)] = goals_against


    def get_player(self, player):
        return self.__whole_team[player]

    def pick_team(self):

        team = self.theteam
        formation = self.style

        gk = team.loc[team.loc[:, 'Position'] == 'gk', :].sort_values(
            ['Rating', 'Value'], ascending=[False, False]
            ).loc[:, 'Name'].values[0]
        gk = [i for i in self.__gks if i.name == gk]

        deff = team.loc[team.loc[:, 'Position'] == 'def', :].sort_values(
            ['Rating', 'Value'], ascending=[False, False]
            ).loc[:, 'Name'].values[:int(formation[0])]
        deff = [i for i in self.__defs if i.name in deff]

        midd = team.loc[team.loc[:, 'Position'] == 'mid', :].sort_values(
            ['Rating', 'Value'], ascending=[False, False]
            ).loc[:, 'Name'].values[:int(formation[1])]
        midd = [i for i in self.__mids if i.name in midd]

        att = team.loc[team.loc[:, 'Position'] == 'att', :].sort_values(
            ['Rating', 'Value'], ascending=[False, False]
            ).loc[:, 'Name'].values[:int(formation[2])]
        att = [i for i in self.__atts if i.name in att]

        team = gk + deff + midd + att

        return team
