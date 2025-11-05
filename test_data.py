from datetime import datetime 
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.ticker import NullFormatter

from subjects.corr_coef import CorrCoeff
from subjects.game_day import GameDay,DayFigures
from subjects.player import PlrPool,Player
from utils import do_one_day

start_date = datetime.strptime("01-7-2022", "%d-%m-%Y")
end_date = datetime.strptime("01-7-2023", "%d-%m-%Y")

x_date = pd.date_range(start_date, end_date)

plr_pool = PlrPool()
print(len(plr_pool.pool))

game_day = GameDay(plr_pool=plr_pool,today=start_date)
corr_coef = CorrCoeff()
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
    
f, ax = plt.subplots(4, 1)
f.set_size_inches(9, 7)     # размер 9 x 7 дюймов
f.set_facecolor('#eee')     # цвет фона (светло-серый)
ax[0].set_ylabel('Hand Amount')
ax[0].plot(x_date, total_hand_amounts)
ax[0].grid()
ax[0].xaxis.set_major_formatter(NullFormatter())
ax[1].set_ylabel('head_counts')
ax[1].plot(x_date, head_counts)
ax[1].grid()
ax[1].xaxis.set_major_formatter(NullFormatter())

ax[2].set_ylabel('Bet Amount')
ax[2].plot(x_date, bet_amounts)
ax[2].grid()
ax[2].xaxis.set_major_formatter(NullFormatter())

ax[3].set_ylabel('Day result')
aver_res = np.array(day_reses).mean()
ax[3].axhline(y=aver_res, color='red', linestyle='--', linewidth=2, label='aver_res')
ax[3].plot(x_date, day_reses)
ax[3].grid()
ax[3].tick_params(axis='x', labelrotation=45)
plt.show()

