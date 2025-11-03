import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from matplotlib.ticker import NullFormatter
from scipy import stats
import plotly.express as px
pl_fig = pd.read_csv("plr_fig.csv")
# hist_show = pl_fig[['res_mean','hands_mean','bets_mean', 'visits']].hist(figsize=(12,6), bins=30)
px.scatter_3d(
    pl_fig,
    x='res_mean',
    y='bets_mean',
    z='visits',
    color='visits'
).show()