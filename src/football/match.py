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

    def result_probability(self, team1, team2):
        # relative player rating
        team1_r = sum([i.rating for i in team1])/len(team1)/100.0
        team2_r = sum([i.rating for i in team2])/len(team2)/100.0

        team1_rn = random.uniform(0.5, 0.6)*team1_r/(team1_r+team2_r)
        team2_rn = random.uniform(0.5, 0.6)*team2_r/(team1_r+team2_r)

        # home advantage
        team1_r = team1_rn + random.uniform(0.1, 0.2)
        team2_r = team2_rn

        # relative team rating
        team1_r = team1_r + random.uniform(0.15, 0.2)*self.home.rating / \
            (self.home.rating+self.away.rating)
        team2_r = team2_r + random.uniform(0.15, 0.2)*self.away.rating / \
            (self.home.rating+self.away.rating)

        # Final
        p1 = team1_r
        p2 = team2_r
        pdr = 1 - p1 - p2

        return (p1, p2, pdr)

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
