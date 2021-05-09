import random
from typing import Tuple
from football.teams import Team
from numpy import cumsum


class Match:

    def __init__(self,
                 team1: Team,
                 team2: Team,
                 roundd: int,
                 seasonind: int):

        self.__home: Team = team1
        self.__away: Team = team2
        self.__round: int = roundd
        self.__seasonind: int = seasonind
        self.__homegoals: int = None
        self.__awaygoals: int = None
        self.__result: Tuple = None
        self.__lineups = None
        self.__scorers: dict = {}

    def __str__(self):
        return f"{self.home_team}  {self.home_goals} - {self.away_goals}  {self.away_team}"

    def __repr__(self):
        return f"{self.home_team}  {self.home_goals} - {self.away_goals}  {self.away_team}"

    @property
    def season_index(self):
        return self.__seasonind

    @property
    def round(self):
        return self.__round

    @property
    def home(self):
        return self.__home

    @property
    def away(self):
        return self.__away

    @property
    def home_team(self):
        return self.__home.name

    @property
    def away_team(self):
        return self.__away.name

    @property
    def result(self):
        return self.__result

    @property
    def home_goals(self):
        return self.__homegoals

    @property
    def away_goals(self):
        return self.__awaygoals

    @property
    def lineups(self):
        return self.__lineups

    def scorers(self, side: str=None):
        if side:
            return self.__scorers[side]
        else:
            return self.__scorers

    def result_probability(self, team1: Team, team2: Team) -> Tuple[float, float, float]:
        # relative player rating
        team1_r = sum([i.rating for i in team1])/len(team1)/100.0
        team2_r = sum([i.rating for i in team2])/len(team2)/100.0

        team1_rn = random.uniform(0.4, 0.6)*team1_r/(team1_r+team2_r)
        team2_rn = random.uniform(0.4, 0.6)*team2_r/(team1_r+team2_r)

        # home advantage
        team1_r = team1_rn + random.uniform(0.15, 0.2)
        team2_r = team2_rn + random.uniform(0.05, 0.2)

        # relative team rating
        team1_r = team1_r + random.uniform(0.1, 0.2)*self.home.rating / \
            (self.home.rating+self.away.rating)
        team2_r = team2_r + random.uniform(0.1, 0.2)*self.away.rating / \
            (self.home.rating+self.away.rating)

        # Final
        p1 = team1_r
        p2 = team2_r
        pdr = 1 - p1 - p2

        return (p1, p2, pdr)

    def who_scored(self, home11: list, away11: list, score: tuple) -> list:

        scorers = []
        for team, score in zip([home11, away11], list(score)):
            scorers.append([])
            for goal in range(score):
                val = random.uniform(0, 1.0)
                cumsu = cumsum([i.goalscoring for i in team])
                cumsu_norm = [abs((i/sum(cumsu))-val) for i in cumsu]
                index = cumsu_norm.index(min(cumsu_norm))
                scorers[-1].append(team[index])

        return scorers
            

    def play(self) -> Tuple[Team, Team, int, int, Tuple[int, int]]:

        home11 = self.home.pick_team()
        away11 = self.away.pick_team()

        self.__lineups = {self.home.name:home11, self.away.name:away11}

        h, a, d = self.result_probability(home11, away11)

        v = random.random()

        if v <= h:
            hp = 3
            ap = 0
            score = random.choice([(2, 1), (3, 1), (1, 0), (2, 0)])
            self.__result = score

            self.home.win(self.season_index, score[0], score[1])
            self.away.lose(self.season_index, score[1], score[0])

        elif h < v <= (h+a):
            hp = 0
            ap = 3
            score = random.choice([(0, 1), (1, 3), (1, 2), (0, 2)])
            self.__result = score

            self.away.win(self.season_index, score[1], score[0])
            self.home.lose(self.season_index, score[0], score[1])

        else:
            hp = 1
            ap = 1
            score = random.choice([(1, 1), (3, 3), (2, 2), (0, 0)])
            self.__result = score

            self.away.draw(self.season_index, score[1], score[0])
            self.home.draw(self.season_index, score[0], score[1])

        self.__homegoals = score[0]
        self.__awaygoals = score[1]

        self.home.add_match(str(self.season_index), str(self.round), self)
        self.away.add_match(str(self.season_index), str(self.round), self)

        for player in home11 + away11:
            player.add_appearance(str(self.season_index), str(self.round))

        scorers = self.who_scored(home11, away11, score)

        for player in scorers[0] + scorers[1]:
            player.add_goal(str(self.season_index), str(self.round), 1)

        self.__scorers['home'] = scorers[0]
        self.__scorers['away'] = scorers[1]

        
        return self.home, self.away, hp, ap, score
