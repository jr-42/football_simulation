from football.teams import Team
from football.seasons import Season

class League:

    def __init__(self, name='Reed League'):
        self.__name = name
        self.__teams = [Team(league=self.__name) for i in range(20)]
        self.__teams_dict = {i.name: i for i in self.__teams}
        self.__seasons = []
        self.__current_season = None
        self.__current_season_index = None

    def __repr__(self):
        return self.name

    def __str__(self):
        return self.name

    @property
    def name(self):
        return self.__name

    @property
    def current_season(self):
        return self.__current_season

    @property
    def current_season_index(self):
        return self.__current_season_index

    @property
    def teams(self):
        return self.__teams

    def get_team(self, team):
        return self.__teams_dict[team]

    def relegation(self):
        keep_teams = self.__teams[:-3]
        new_teams= [Team(league=self.__name) for i in range(3)]
        self.__teams = keep_teams + new_teams
        self.__teams_dict = {i.name: i for i in self.__teams}


    def new_season(self):
        if len(self.__seasons) > 0:
            self.relegation()
        season_ = Season(league=self, number=len(self.__seasons))
        self.__seasons.append(season_)
        self.__current_season = self.__seasons[-1]
        self.__curent_season_index = len(self.__seasons) + 1
        return season_


    def get_season(self, index):
        return self.__seasons[index-1]