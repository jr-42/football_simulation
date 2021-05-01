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
        self.__goals_scored: dict = {}
        self.__appearances: dict = {}
        if team_rating:
            self.__ca = random.randint(20+((5-team_rating*100)*10), 95)/100.0
        else:
            self.__ca = random.randint(20, 95)/100.0
        self.__fa = min(self.__ca + random.randint(-10, 100)/100.0, 0.95)
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

    
    def appearances(self, season: str, roundd: str=None):
        
        if season:
            if not roundd:
                return self.__appearances[season]
            else:
                return self.__appearances[season][roundd]

        else:
            return sum([sum(i) for i in list(self.__appearances.values())])

    def add_appearance(self, season: str, roundd: str, appearance: int=1):
        
        if season in self.__appearances.keys():
            if str(round) in self.__appearances[season]:
                self.__appearances[season][roundd].append(appearance)
            else:
                self.__appearances[season][roundd] = appearance
        else:
            self.__appearances[season] = {roundd:appearance}

    def goals_scored(self, season: str, roundd: str=None):
        
        if season:
            if not roundd:
                return self.__goals_scored[season]
            else:
                return self.__goals_scored[season][roundd]
        else:
            return sum([sum(i) for i in list(self.__goals_scored.values())])

    def add_goal(self, season: str, roundd: str, goals_scored: int):
        
        if season in self.__goals_scored.keys():
            if str(round) in self.__goals_scored[season]:
                self.__goals_scored[season][roundd].append(goals_scored)
            else:
                self.__goals_scored[season][roundd] = goals_scored
        else:
            self.__goals_scored[season] = {roundd:goals_scored}


class Goalkeeper(Player):

    def __init__(self, team=None, team_rating=None):
        Player.__init__(self, team, team_rating)
        self.__position = 'gk'
        self.__value = self.value + 1000000
        self.__goal_scoring = self.rating/5.0

    @property
    def position(self):
        return self.__position


class Defender(Player):

    def __init__(self, team=None, team_rating=None):
        Player.__init__(self, team, team_rating)
        self.__position = 'def'
        self.__value = self.value + 3000000
        self.__goal_scoring = 0.1 + self.rating/5.0

    @property
    def position(self):
        return self.__position


class Midfielder(Player):

    def __init__(self, team=None, team_rating=None):
        Player.__init__(self, team, team_rating)
        self.__position = 'mid'
        self.__value = self.value + 7000000
        self.__goal_scoring = 0.3 + self.rating/5.0

    @property
    def position(self):
        return self.__position


class Attacker(Player):

    def __init__(self, team=None, team_rating=None):
        Player.__init__(self, team, team_rating)
        self.__position = 'att'
        self.__value = self.value + 11000000
        self.__goal_scoring = 0.5 + self.rating/5.0

    @property
    def position(self):
        return self.__position
