from datetime import datetime 
import pandas as pd
import json

from utils import do_pd_figures
from subjects.player import PlrPool,Player
from subjects.corr_coef import CorrCoeff
import matplotlib.pyplot as plt

start_date = datetime.strptime("01-7-2022", "%d-%m-%Y")
end_date = datetime.strptime("01-8-2022", "%d-%m-%Y")
plr_pool = PlrPool()
corr_coef = CorrCoeff()
pd_fig, plr_pool = do_pd_figures(start_date,end_date,plr_pool,corr_coef)

print(pd_fig.head())
pretty_json = json.dumps(plr_pool.model_dump(), indent=4)
print(pretty_json)
plr_pool_json_string = plr_pool.model_dump_json(indent=2)
plr_pool_frm_1 = PlrPool.model_validate_json(plr_pool_json_string) 
print(plr_pool_json_string)

# with open("plr_pool.json", 'w') as f:
#     json.dump(plr_pool_json_string, f, indent=4)