import numpy as np 
from datetime import datetime

from pydantic import BaseModel, computed_field,field_validator,Field

class TotalFig(BaseModel):
    sum: float|int= Field(default=0)
    mean: float = Field(default=0)
    std: float = Field(default=0)
    

class SessionFigures(BaseModel):
    bet_amount:float
    hand_amount: int
    result: float
    
class PlayerFigures(BaseModel):
    last_visit: str= Field(default='1/1/2000')
    visits: int = Field(default=0)
    results: list[float] = Field(default=[])
    hand_amounts: list[int] = Field(default=[])
    bet_amounts: list[float] = Field(default=[])
    
    @computed_field
    def total_results(self)-> TotalFig:
        if len(self.results) ==0: 
            return TotalFig(sum=0,
                            mean=0,
                            std=0)
        res_np = np.array(self.results)
        return TotalFig(sum=res_np.sum(),
                        mean=res_np.mean(),
                        std=res_np.std())
    
    @computed_field
    def total_hands(self)-> TotalFig:
        if len(self.hand_amounts) ==0: 
            return TotalFig(sum=0,
                            mean=0,
                            std=0)
        hands_np = np.array(self.hand_amounts)
        return TotalFig(sum=hands_np.sum(),
                        mean=hands_np.mean(),
                        std=hands_np.std())
        
    @computed_field
    def total_bets(self)-> TotalFig:
        if len(self.bet_amounts) ==0: 
            return TotalFig(sum=0,
                            mean=0,
                            std=0)
        bets_np = np.array(self.bet_amounts)
        return TotalFig(sum=bets_np.sum(),
                        mean=bets_np.mean(),
                        std=bets_np.std())


if __name__ == '__main__':
    plr_stl = PlayerFigures(
        visits= 15,
    results = [156,12,12,156,126,141],
    hand_amounts= [1556,1542,5512,156,126,141])
    
    print(plr_stl)