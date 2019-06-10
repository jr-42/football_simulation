from football.teams import Team


class League:

    i = 1

    def __init__(self):
        self.i += 1
        self.__name = 'League {}'.format(self.i)
        self.__teams = [Team(league=self.__name) for i in range(20)]

    @property
    def name(self):
        return self.__name

    @property
    def teams(self):
        return self.__teams
