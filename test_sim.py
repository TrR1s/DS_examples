from datetime import datetime 
from utils import simulator_period,save_sim_resuls

start_date = datetime.strptime("01-1-2022", "%d-%m-%Y")
end_date = datetime.strptime("01-5-2022", "%d-%m-%Y")

casino_fig, plr_pool = simulator_period(start_date,end_date)
save_sim_resuls(casino_fig, plr_pool)