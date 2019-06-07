import random
import pandas as pd
from datetime import datetime, timedelta

names = pd.read_csv('../../data/names.csv',
                    header=None, sep=',')


class Player:

    def __init__(self):
        self.__name = random.choice(names)
        self.__surname = random.choice(names)
        self.__dob = int((datetime(datetime.now().year-30, 1, 1) +
                         int(365*random.uniform(-3.0, 10.0)
                             ) * timedelta(days=1)
                          ).strftime('%Y%m%d'))
        self.__height = round(random.uniform(1.7, 1.9), 2)
        self.__weight = random.randint(65, 95)
        self.__foot = random.choice(['r', 'l'])
        self.__ca = random.randint(20, 95)
        self.__fa = self.__ca + random.randint(-10, 100-self.__ca)
        self.__value = (self.__ca/100 + self.__fa/100 + (33-self.age)/100.0
                        ) * 1000000

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
    def height(self):
        return self.__height

    @property
    def weight(self):
        return self.__weight

    @property
    def foot(self):
        return self.__foot

    @property
    def value(self):
        return self.__value

    @property
    def age(self):
        dob = datetime.strptime(str(self.__dob), '%Y%m%d')
        dtyears = datetime.now() - dob
        age = dtyears.total_seconds()/timedelta(days=365).total_seconds()
        return int(age)


class Defender(Player):

    def __init__(self):
        Player.__init__(self)
        self.__position = 'def'
        self.__value = self.value + 3000000

    @property
    def position(self):
        return self.__position


class Midfielder(Player):

    def __init__(self):
        Player.__init__(self)
        self.__position = 'mid'
        self.__value = self.value + 7000000

    @property
    def position(self):
        return self.__position


class Attacker(Player):

    def __init__(self):
        Player.__init__(self)
        self.__position = 'att'
        self.__value = self.value + 11000000

    @property
    def position(self):
        return self.__position
