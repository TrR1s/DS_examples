import pandas as pd
from datetime import datetime

from subjects.corr_coef import CorrCoeff
from subjects.game_day import GameDay
from subjects.player import PlrPool
from utils import do_one_day


def do_pd_figures(start_date:datetime,
                  end_date:datetime,
                  plr_pool: PlrPool, 
                  corr_coef:CorrCoeff ) -> tuple[pd.DataFrame,PlrPool]:
    x_date = pd.date_range(start_date, end_date)
    game_day = GameDay(plr_pool=plr_pool, today=start_date)
    total_hand_amounts = []
    day_reses= []
    head_counts = []
    bet_amounts =[]
    for curr_day in x_date:
        day_figures = do_one_day(game_day,curr_day,corr_coef)
        total_hand_amounts.append(day_figures.total_hand_amount)
        day_reses.append(day_figures.day_res)
        head_counts.append(day_figures.head_count)
        bet_amounts.append(day_figures.bet_amount)
    
    fig_dict ={
        'Date': x_date,
        'Heads': head_counts,
        'Total_Bets': bet_amounts,
        'Total_Hands': total_hand_amounts
    }
    return (pd.DataFrame(fig_dict),game_day.plr_pool)
    