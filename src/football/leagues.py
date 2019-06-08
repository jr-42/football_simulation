import random
import pandas as pd

from football.teams import Team


def league_table(teams, stats=None):

    cols = ['Name', 'Team_Rating', 'Squad_Value', 'P', 'W', 'D', 'L', 'GF', 'GA', 'GD', 'Points']
    df = pd.DataFrame(columns=cols)

    for i, team in enumerate(teams):
        df.loc[i, 'Name'] = team.name
        df.loc[i, 'Team_Rating'] = team.rating
        df.loc[i, 'Squad_Value'] = team.theteam.loc[:, 'Value'].sum()

    df.fillna(0, inplace=True)

    return df


class League:

    def __init__(self):
        self.__name = 'League 1'
        self.__teams = [Team() for i in range(21)]

    @property
    def name(self):
        return self.__name

    @property
    def leaguetable(self):
        return league_table(self.__teams)
