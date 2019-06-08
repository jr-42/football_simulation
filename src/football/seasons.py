import pandas as pd
from football.match import Match


class Season:

    def __init__(self,
                 league=object):
        self.__league = league
