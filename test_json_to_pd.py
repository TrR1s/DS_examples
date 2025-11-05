import pandas as pd
from utils import do_csv_players_frm_json

df_plr = do_csv_players_frm_json()
print(df_plr.head(2))