import football.teams as ft
import football.match as fm
import football.seasons as fs


def test_match():
    m = fm.Match(ft.Team(), ft.Team())
    return m


def test_season():

    s = fs.Season()
    s.play_season()

    return s
