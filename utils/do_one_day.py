from datetime import datetime

from subjects.game_day import GameDay,DayFigures
from subjects.corr_coef import CorrCoeff,TrendFunc

def do_one_day(game_day: GameDay, today:datetime,corr_coeff:CorrCoeff) ->DayFigures:
    corr_coeff.today = today
    game_day.today = today
    game_day.corr_coef = corr_coeff.coeff
    return game_day.dayfig

   