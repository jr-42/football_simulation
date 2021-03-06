import random
from typing import Dict, List
import pandas as pd

from football.players import Player, Goalkeeper, Defender, Midfielder, Attacker
from football.names_lists import town_names

team_suffix = ['Town', 'Rovers', 'United', 'City', '', 'Wanderers',
               'F.C.']


def team_dataframe(gks: List[Player], defs: List[Player], mids: List[Player], atts: List[Player]) -> pd.DataFrame:

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


class Team:

    def __init__(self,
                 league=None):

        self.__name = random.choice(town_names) + ' ' + random.choice(team_suffix)
        self.__rating = random.randint(1, 10)/10.0
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

        self.__wins: Dict = {}
        self.__loses: Dict = {}
        self.__draws: Dict = {}
        self.__gf: Dict = {}
        self.__ga: Dict = {}
        self.__matches: Dict = {}

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
    def squadlist(self):
        return self.__equip

    @property
    def getteam(self):
        return self.__whole_team

    @property
    def style(self):
        return self.__style

    @property
    def league(self):
        return self.__league

    # @league.setter
    # def league(self, name: str):
    #     self.__league = name

    def played(self, season: str=None):
        if season:
            return self.__wins.get(season, 0) + self.__draws.get(season, 0) + self.__loses.get(season, 0)
        else:
            return sum(list(self.__wins.values())) + sum(list(self.__loses.values())) + sum(list(self.__draws.values()))

    def wins(self, season: str=None):
        if season:
            return self.__wins.get(season, 0)
        else:
            return sum(list(self.__wins.values()))

    def loses(self, season: str=None):
        if season:
            return self.__loses.get(season, 0)
        else:
            return sum(list(self.__loses.values()))

    def draws(self, season: str=None):
        if season:
            return self.__draws.get(season, 0)
        else:
            return sum(list(self.__draws.values()))

    def goals_for(self, season: str=None):
        if season:
            return self.__gf.get(season, 0)
        else:
            return sum(list(self.__gf.values()))
    
    def goals_against(self, season: str=None):
        if season:
            return self.__ga.get(season, 0)
        else:
            return sum(list(self.__ga.values()))

    def get_match(self, season: str, roundd: str):
        
        if not season or not roundd:
            raise Exception('Need season and roundd identifier')
        else:
            return self.__matches[season][roundd]

    def add_match(self, season: str, roundd: str, match):
        
        if season in self.__matches.keys():
            if str(round) in self.__matches[season]:
                self.__matches[season][roundd].append(match)
            else:
                self.__matches[season][roundd] = match
        else:
            self.__matches[season] = {roundd:match}

    def win(self, csi: str, goals_for: int, goals_against: int):

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

    def lose(self, csi: str, goals_for: int, goals_against: int):

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

    def draw(self, csi: str, goals_for: int, goals_against: int):

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


    def get_player(self, player: str) -> Player:
        return self.__whole_team[player]

    
    def pick_team(self) -> List[Player]:

        team = self.squadlist
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
