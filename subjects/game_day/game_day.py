from pydantic import BaseModel, computed_field,field_validator,Field
import random
from scipy import stats

from subjects.player import PlrPool,Player

class DayFigures(BaseModel):
    total_hand_amount: int= Field(default=0)
    day_res: float= Field(default=0)
    bet_amount: float= Field(default=0)
    head_count: int= Field(default=0)
    day_plr_pool : list[Player] = Field(default=[])
    
    
class GameDay(BaseModel):
    plr_pool: PlrPool= Field(default=PlrPool())
    base_head_count: int= Field(default=20)
    corr_coef: float = Field(default=1.)
    # today: datetime
    @computed_field
    def head_count(self) -> int:
        liambda = int(self.corr_coef*self.base_head_count)
        return int(stats.poisson(liambda).rvs())
    @computed_field
    def dayfig(self) -> DayFigures:
        day_pool = random.sample(self.plr_pool.pool,self.head_count)
        day_res = 0
        hand_amount =0
        bet_amount =0
        for curr_plr in day_pool:
            curr_plr.play_one_session()
            day_res += curr_plr.fig.results[-1]
            bet_amount += curr_plr.fig.bet_amounts[-1]
            hand_amount += curr_plr.fig.hand_amounts[-1]
        
        return DayFigures(total_hand_amount=hand_amount,day_res=-day_res,head_count=self.head_count,day_plr_pool=day_pool,bet_amount=bet_amount)
    
        
        
 