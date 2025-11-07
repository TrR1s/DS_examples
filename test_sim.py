from datetime import datetime 
import pandas as pd
from utils import simulator_period,save_sim_resuls
from subjects.corr_coef import TrendFunc

start_date = datetime.strptime("01/1/2022", "%d/%m/%Y")
end_date = datetime.strptime("01/5/2022", "%d/%m/%Y")

casino_fig, plr_pool = simulator_period(start_date,end_date)

# print(len(plr_pool.pool))


save_sim_resuls(casino_fig, plr_pool)
plr_pool_df = pd.read_csv('plr_pool.csv')
print(plr_pool_df.info())
print(casino_fig.info())
casino_fig_df = pd.read_csv('casino_fig.csv', parse_dates = ['Date'])
print(casino_fig_df.info())
# df['Date_String'] = pd.to_datetime(df['Date_String'])