import json
from subjects.player import PlrPool,Player,PlayerFigures
from datetime import datetime 
import pandas as pd

with open("plr_pool.json", "r") as file:
    plr_pool_json_string = json.load(file)
plr_pool = PlrPool.model_validate_json(plr_pool_json_string)

# print(plr_pool_json_string)

pd_dict = {
    'id':[],
    'visits':[],
    'last_visit':[],
    
    'res_sum':[],
    'res_std':[],
    'res_mean':[],
    
    'hands_sum':[],
    'hands_std':[],
    'hands_mean':[],
    
    'bets_sum':[],
    'bets_std':[],
    'bets_mean':[],
}


for curr_plr in plr_pool.pool:
    pd_dict['id'].append(curr_plr.id)
    pd_dict['visits'].append(curr_plr.fig.visits)
    pd_dict['last_visit'].append(curr_plr.fig.last_visit)
    
    pd_dict['res_sum'].append (curr_plr.fig.total_results.sum)
    pd_dict['res_mean'].append(curr_plr.fig.total_results.mean)
    pd_dict['res_std'].append(curr_plr.fig.total_results.std)
    
    pd_dict['hands_sum'].append(curr_plr.fig.total_hands.sum)
    pd_dict['hands_mean'].append(curr_plr.fig.total_hands.mean)
    pd_dict['hands_std'].append(curr_plr.fig.total_hands.std)
    
    pd_dict['bets_sum'].append(curr_plr.fig.total_bets.sum)
    pd_dict['bets_mean'].append(curr_plr.fig.total_bets.mean)
    pd_dict['bets_std'].append (curr_plr.fig.total_bets.std)

plr_fig_df = pd.DataFrame(pd_dict)
# print(plr_fig_df.head)
plr_fig_df.to_csv('plr_fig.csv', index=False)