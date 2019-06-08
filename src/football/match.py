import pandas as pd
import random


class Match:

    def __init__(self,
                 team1,
                 team2):

        self.__home = team1
        self.__away = team2

        @property
        def home(self):
            return self.__home

        @property
        def away(self):
            return self.__away

        @staticmethod
        def result_probability(team1, team2):
            pass
            # return (p1, p2, pd)

        def play(self):

            home11 = self.home.pick_team()
            away11 = self.away.pick_team()

            h, a, d = self.result_probability(home11, away11)

            v = random.random()

            if v <= h:
                hp = 3
                ap = 0
                score = random.choice([(2, 1), (3, 1), (1, 0), (2, 0)])
            elif h < v <= (h+a):
                hp = 0
                ap = 3
                score = random.choice([(0, 1), (1, 3), (1, 2), (0, 2)])
            else:
                hp = 1
                ap = 1
                score = random.choice([(1, 1), (3, 3), (2, 2), (0, 0)])

            return hp, ap, score








