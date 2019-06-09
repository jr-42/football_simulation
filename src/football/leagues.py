import pandas as pd
from football.teams import Team


def league_table(teams, results=None):

    cols = ['Name', 'Team_Rating', 'Squad_Value',
            'P', 'W', 'D', 'L', 'GF', 'GA', 'GD', 'Points']
    df = pd.DataFrame(columns=cols)

    for i, team in enumerate(teams):
        df.loc[i, 'Name'] = team.name
        df.loc[i, 'Team_Rating'] = team.rating
        df.loc[i, 'Squad_Value'] = team.theteam.loc[:, 'Value'].sum()

    df.fillna(0, inplace=True)

    return df


class League:

    i = 1

    def __init__(self):
        self.i += 1
        self.__name = 'League {}'.format(self.i)
        self.__teams = [Team(league=self.__name) for i in range(20)]
        self.__results = None

    @property
    def name(self):
        return self.__name

    @property
    def teams(self):
        return self.__teams

    @property
    def leaguetable(self):
        return league_table(self.__teams)
