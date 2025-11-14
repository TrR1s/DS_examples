import pandas as pd
from datetime import datetime
import json
import numpy as np

from subjects.corr_coef import CorrCoeff,TrendFunc,TrendCoeff,LotteryScheldure
from subjects.game_day import GameDay
from subjects.player import PlrPool
from utils import do_one_day
from utils.do_csv_players_from_json import do_csv_players_frm_json

class DefaultPoolCorr():
    plr_pool = PlrPool()
    corr_coef = CorrCoeff()


def simulator_period(start_date:datetime,
                  end_date:datetime,
                  plr_pool =DefaultPoolCorr.plr_pool, 
                  trend_func =  TrendFunc.none_func,
                  lottery_scheldure =None,
                  ) -> tuple[pd.DataFrame,PlrPool]:
    
    x_date = pd.date_range(start_date, end_date)
    corr_coef =  DefaultPoolCorr.corr_coef
    trend = TrendCoeff(today=start_date)
    trend.trend_dict = trend_func(x_date)
    corr_coef.trend = trend
    corr_coef.lottery_scheldue = lottery_scheldure
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
        'Day_Result': day_reses,
        'Total_Bets': bet_amounts,
        'Total_Hands': total_hand_amounts
    }
    return (pd.DataFrame(fig_dict),game_day.plr_pool)


def save_sim_resuls(casino_fig:pd.DataFrame, plr_pool: PlrPool, casino_fig_file_name = 'casino_fig.csv', plr_pool_file_name = "plr_pool"):
    
    casino_fig.to_csv(casino_fig_file_name, index=False)
    plr_pool_json_string = plr_pool.model_dump_json(indent=2)
    json_file_name = f'{plr_pool_file_name}.json' 
    csv_file_name = f'{plr_pool_file_name}.csv' 
    with open(json_file_name, 'w') as f:
        json.dump(plr_pool_json_string, f, indent=4)
    do_csv_players_frm_json(json_file_name,csv_file_name)
    
    