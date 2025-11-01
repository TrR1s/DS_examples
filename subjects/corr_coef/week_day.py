from pydantic import BaseModel, computed_field,field_validator,Field
from datetime import datetime 
import pandas as pd


class WeekDayCoef(BaseModel):
    
    week_day_coef:list[float]=Field(default=[-0.5,-0.4,-0.3,-0.4,0.2,0.3,0])
    today: datetime=Field(default=datetime.today()) 
    
    @computed_field
    def week_day_int(self) -> int|None:
        if self.today is None:
            return None
        return datetime.weekday(self.today)
    
    @computed_field
    def add_coef(self) -> float|None:
        if self.week_day_int is None:
            return 0
        return self.week_day_coef[self.week_day_int]
    
if __name__ == '__main__':
    # week_coeff = WeekDayCoef(today=datetime.strptime("05/05/2017", "%d/%m/%Y"))
    week_coeff = WeekDayCoef()
    print(week_coeff)