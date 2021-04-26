import random
import pandas as pd
from football.players import Goalkeeper, Defender, Midfielder, Attacker
from football.names_lists import town_names

random.seed(1) # seed whist in dev so names stay the same during testing

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

        self.__wins = 0
        self.__loses = 0
        self.__draws = 0
        self.__gf = 0
        self.__ga = 0
        self.__matchs = []

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

    @property
    def wins(self):
        return self.__wins

    @wins.setter
    def wins(self, value):
        self.__wins = value

    @property
    def loses(self):
        return self.__loses

    @loses.setter
    def loses(self, value):
        self.__loses = value

    @property
    def draws(self):
        return self.__draws

    @draws.setter
    def draws(self, value):
        self.__draws = value

    @property
    def goals_for(self):
        return self.__gf

    @property
    def goals_against(self):
        return self.__ga

    @goals_for.setter
    def goals_for(self, value):
        self.__gf = value

    @goals_against.setter
    def goals_against(self, value):
        self.__ga = value

    @property
    def matchs(self):
        return self.__matchs

    @matchs.setter
    def matchs(self, value):
        self.__matchs = self.matchs + [value]

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
