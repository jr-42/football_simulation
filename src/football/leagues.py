from football.teams import Team
from football.seasons import Season

class League:

    def __init__(self, name='Reed League'):
        self.__name = name
        self.__teams = [Team(league=self.__name) for i in range(20)]
        self.__teams_dict = {i.name: i for i in self.__teams}

    def __repr__(self):
        return self.name

    def __str__(self):
        return self.name

    @property
    def name(self):
        return self.__name

    @property
    def teams(self):
        return self.__teams

    def get_team(self, team):
        return self.__teams_dict[team]

    def create_season(self):
        return Season(league=self)
