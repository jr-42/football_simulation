import random
from datetime import datetime, timedelta
from football.names_lists import player_names

nationality = ['English', 'French', 'German', 'Spanish', 'Italian', 'Dutch',
               'Brazilian', 'Argentinian', 'Scottish', 'Portuguese']

class Player:

    def __init__(self,
                 team: str='Free Agent',
                 team_rating: int=None,
                 ):

        self.__name = random.choice(player_names).lower().capitalize()
        self.__surname = random.choice(player_names).lower().capitalize()
        self.__dob = int((datetime(datetime.now().year-30, 1, 1) +
                         int(365*random.uniform(-3.0, 10.0)
                             ) * timedelta(days=1)
                          ).strftime('%Y%m%d'))
        self.__nationality = random.choice(nationality)
        self.__height = round(random.uniform(1.7, 1.9), 2)
        self.__weight = random.randint(65, 95)
        self.__foot = random.choice(['right', 'left'])
        self.__team = team

        if team_rating:
            self.__ca = random.randint(20+((5-team_rating)*10), 95)
        else:
            self.__ca = random.randint(20, 95)
        self.__fa = self.__ca + random.randint(-10, 100-self.__ca)
        self.__value = (self.__ca/100 + self.__fa/100 + (33-self.age)/100.0
                        ) * 1000000

    def __repr__(self):
        return self.name

    def __str__(self):
        return self.name

    @property
    def name(self):
        return self.__name

    @property
    def surname(self):
        return self.__surname

    @property
    def dob(self):
        return self.__dob

    @property
    def nationality(self):
        return self.__nationality

    @property
    def height(self):
        return self.__height

    @property
    def weight(self):
        return self.__weight

    @property
    def foot(self):
        return self.__foot

    @property
    def team(self):
        return self.__team

    @property
    def value(self):
        return self.__value

    @property
    def rating(self):
        return self.__ca

    @property
    def age(self) -> int:
        dob = datetime.strptime(str(self.__dob), '%Y%m%d')
        dtyears = datetime.now() - dob
        age = dtyears.total_seconds()/timedelta(days=365).total_seconds()
        return int(age)

    @property
    def info(self):
         
        infos = f"Name: {self.name} {self.surname}\n\
        Age: {self.age}\n\
        Nationality: {self.nationality}\n\
        Rating: {self.rating}\n\
        Value: €{self.value}"
        print(infos)


class Goalkeeper(Player):

    def __init__(self, team=None, team_rating=None):
        Player.__init__(self, team=None, team_rating=None)
        self.__position = 'gk'
        self.__value = self.value + 1000000

    @property
    def position(self):
        return self.__position


class Defender(Player):

    def __init__(self, team=None, team_rating=None):
        Player.__init__(self, team=None, team_rating=None)
        self.__position = 'def'
        self.__value = self.value + 3000000

    @property
    def position(self):
        return self.__position


class Midfielder(Player):

    def __init__(self, team=None, team_rating=None):
        Player.__init__(self, team=None, team_rating=None)
        self.__position = 'mid'
        self.__value = self.value + 7000000

    @property
    def position(self):
        return self.__position


class Attacker(Player):

    def __init__(self, team=None, team_rating=None):
        Player.__init__(self, team=None, team_rating=None)
        self.__position = 'att'
        self.__value = self.value + 11000000

    @property
    def position(self):
        return self.__position
