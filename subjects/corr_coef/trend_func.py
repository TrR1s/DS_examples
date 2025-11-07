
from datetime import datetime
import numpy as np

class TrendFunc():
    @staticmethod
    def none_func(x_date, max_coef=1.5) ->None:
        return None
    
    @staticmethod    
    def make_trend_dict_line(x_date, max_coef=0.7) -> dict[datetime:float]:
        x_d =list(x_date)
        x = np.arange(len(x_d))
        y = max_coef*x/x.shape
        return dict(zip(x_d, y))