from pydantic import BaseModel, computed_field,field_validator,Field
from scipy import stats
import random
from datetime import datetime

from subjects.player.plr_fig import PlayerFigures,SessionFigures
from subjects.player.plr_style import PlrStyle

class Player(BaseModel):
    id: int
    style: PlrStyle
    fig: PlayerFigures
    
    def play_one_session(self,game_date: datetime):
        self.fig.last_visit = game_date.strftime("%d/%m/%Y")
        self.fig.visits +=1
        sess_fig = self.style.sess_fig()
        self.fig.results.append(sess_fig.result)
        self.fig.hand_amounts.append(sess_fig.hand_amount)
        self.fig.bet_amounts.append(sess_fig.bet_amount)
    
    def __hash__(self):
        return hash(self.id)
    


class TemplateForPool(BaseModel):
    id_set:set[int]
    pool_depth: int
    ev:float
    std:float
    bet: float
    base_hand_amount: int
    std_hand_amount: int
    inner_std_proportion: float = Field(default=0.03)
    
    def do_one_plr(self) -> Player|None:
        if len(self.id_set) == 0:
            return None
        plr_ev = stats.norm(self.ev,abs(self.ev*self.inner_std_proportion)).rvs()
        plr_std = stats.norm(self.std,abs(self.std*self.inner_std_proportion)).rvs()
        plr_bet = stats.norm(self.bet,abs(self.bet*self.inner_std_proportion)).rvs()
        plr_base_hand_amount = int(stats.norm(self.base_hand_amount,abs(self.base_hand_amount*self.inner_std_proportion)).rvs())
        plr_std_hand_amount = stats.norm(self.std_hand_amount,abs(self.std_hand_amount*self.inner_std_proportion)).rvs()
        plr_stl = PlrStyle(ev=plr_ev,
                           std=plr_std,
                           bet=plr_bet, 
                           base_hand_amount=plr_base_hand_amount,
                           std_hand_amount=plr_std_hand_amount
                           )
        plr_id = random.choice(list(self.id_set))
        self.id_set.remove(plr_id)
        return Player(
            id=plr_id,
            style=plr_stl,
            fig= PlayerFigures()
            
        )
        
    def do_pool(self) -> set[Player]|None:
        if len(self.id_set) < self.pool_depth:
            return None
        plr_pool = set()
        for _ in range(self.pool_depth):
            plr_pool.add(self.do_one_plr())
    
        return plr_pool
if __name__ == '__main__':
    import json
    
    plr_template = TemplateForPool(
            id_set= set(range(100,200)),
            pool_depth = 5,
            ev = -0.02,
            std = 1.4,
            bet = 10,
            base_hand_amount =70,
            std_hand_amount = 12,
    
    )
    plr_pool = plr_template.do_pool()
    for curr_plr in plr_pool:
        pretty_json = json.dumps(curr_plr.model_dump(), indent=4)
        print(pretty_json)
    
    print(plr_template.id_set)