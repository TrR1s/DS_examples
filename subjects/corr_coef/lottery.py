from pydantic import BaseModel, computed_field,field_validator,Field
from datetime import datetime 
import math

class LotteryFig(BaseModel):
        prize:int = Field(default=1000)
        day_lottery: datetime|None
        gravity_const: float = Field(default=0.25)
        

class LotteryCoeff(BaseModel):
        today: datetime|None
        lottery_fig: LotteryFig
        
        @computed_field
        def add_coef(self) -> float:
            day_to_lottery = (self.lottery_fig.day_lottery - self.today).days
            if day_to_lottery < 0: 
                return 0
            add_coef = self.lottery_fig.gravity_const*math.log2(self.lottery_fig.prize)/((day_to_lottery+1)**2)
            return add_coef
        

if __name__ == '__main__':
    prize = 1000
    day_to_lottery = 1
    gravity_const = 0.25
    f_attraction = math.log2(prize)
    print(f'{f_attraction=}')
    print(gravity_const*f_attraction/(day_to_lottery**2))
    today=datetime.strptime("05/05/2017", "%d/%m/%Y")
    tommorow=datetime.strptime("15/05/2017", "%d/%m/%Y")
    print((today -tommorow).days)
    
    lottery_fig = LotteryFig(day_lottery = datetime.strptime("05/05/2017", "%d/%m/%Y") )
    lottery_coef = LotteryCoeff(today=datetime.strptime("05/05/2017", "%d/%m/%Y"), lottery_fig = lottery_fig)
    print(lottery_fig)
    print(lottery_coef)