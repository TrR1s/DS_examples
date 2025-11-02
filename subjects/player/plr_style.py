from pydantic import BaseModel, computed_field,field_validator,Field
from scipy import stats

from subjects.player.plr_fig import SessionFigures



class PlrStyle(BaseModel):
    ev:float
    std:float
    bet: float
    base_hand_amount: int
    std_hand_amount: float
    corr_coef: float = Field(default=1)
    
    # @computed_field
    def sess_fig(self) -> SessionFigures:
        session_hand_amount = int(stats.norm(self.base_hand_amount,self.std_hand_amount).rvs())
        ev_session =  session_hand_amount * self.bet*self.ev
        bet_amount =session_hand_amount * self.bet
        std_session = (session_hand_amount**0.5)*self.bet*self.std
        res_session = stats.norm(ev_session,std_session).rvs()
        
        return SessionFigures(hand_amount=session_hand_amount,result=res_session,bet_amount=bet_amount)
    
    
if __name__ == '__main__':
    plr_stl = PlrStyle(ev=-0.01,std=1.1,bet=25, base_hand_amount=90,std_hand_amount=15)
    print(plr_stl.sess_fig)