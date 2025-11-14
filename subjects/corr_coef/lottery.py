from pydantic import BaseModel, computed_field,field_validator,Field
from datetime import datetime,timedelta 
import math


def lottery_add_coeff(days_to_lottery: int,prize:int, gravity_const:float) -> float:
    return gravity_const*math.log2(prize)/((days_to_lottery+1)**2)



class LotteryFig(BaseModel):
        prize:int = Field(default=1000)
        day_lottery: datetime|None
        gravity_const: float = Field(default=0.25)
        threshold_coeff_min: int = Field(default=0.1)

        @computed_field
        def start_horizon_data(self) -> datetime:
            maximum_days = 180
            for days_to_lottery in range(1,maximum_days):
                add_coef = lottery_add_coeff(days_to_lottery,self.prize,self.gravity_const)
                if add_coef <= self.threshold_coeff_min:
                    return self.day_lottery - timedelta(days=days_to_lottery)
            return self.day_lottery - timedelta(days=maximum_days)
        
class LotteryCoeff(BaseModel):
        today: datetime|None  = Field(default=None)
        lottery_fig: LotteryFig
        
        @computed_field
        def add_coef(self) -> float:
            if self.today is None:
                return 0
            days_to_lottery = (self.lottery_fig.day_lottery - self.today).days
            if days_to_lottery < 0: 
                return 0
            add_coef = lottery_add_coeff(days_to_lottery,self.lottery_fig.prize,self.lottery_fig.gravity_const)
            return add_coef
        
        
class LotteryScheldure(BaseModel):
    lottery_list: list[LotteryCoeff] = Field(default=[])
    today: datetime|None  = Field(default=None)
    
    
    @computed_field 
    def total_add_coef(self) -> float:
        if self.today is None or self.lottery_list == []:
            return 0
        total_add_coef = 0
        for curr_lottery in self.lottery_list:
            if self.today < curr_lottery.lottery_fig.start_horizon_data or self.today > curr_lottery.lottery_fig.day_lottery:
                continue
            curr_lottery.today = self.today
            total_add_coef +=  curr_lottery.add_coef 
                                
        return total_add_coef
    
if __name__ == '__main__':

    
    lottery_fig = LotteryFig(day_lottery = datetime.strptime("05/05/2017", "%d/%m/%Y") )
    lottery_coef = LotteryCoeff(lottery_fig = lottery_fig)
    lottery_fig_2 = LotteryFig(day_lottery = datetime.strptime("07/05/2017", "%d/%m/%Y") )
    lottery_coef_2 = LotteryCoeff(lottery_fig = lottery_fig_2)
    lottery_scheldure =LotteryScheldure(lottery_list = [lottery_coef,lottery_coef_2])
    lottery_scheldure.today = datetime.strptime("06/05/2017", "%d/%m/%Y")
    print(lottery_scheldure.total_add_coef)
    