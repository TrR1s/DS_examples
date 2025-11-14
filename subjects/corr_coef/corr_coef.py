from pydantic import BaseModel, computed_field,field_validator,Field
from datetime import datetime

from subjects.corr_coef.lottery import LotteryCoeff, LotteryScheldure
from subjects.corr_coef.week_day import WeekDayCoef 
from subjects.corr_coef.trend import TrendCoeff 

class CorrCoeff(BaseModel):
    today: datetime=Field(default=datetime.today())
    lottery_scheldue: LotteryScheldure|None = Field(default=None)
    week_day: WeekDayCoef|None = Field(default=WeekDayCoef())
    trend: TrendCoeff|None = Field(default=None)
    
    @computed_field
    def lottery_add(self)->float:
        if self.lottery_scheldue is None:
            return 0
        self.lottery_scheldue.today = self.today
        return self.lottery_scheldue.total_add_coef
    
    @computed_field
    def week_day_add(self)->float:
        if self.week_day is None:
            return 0
        self.week_day.today = self.today
        return self.week_day.add_coef
    
    @computed_field
    def trend_add(self)->float:
        if self.trend is None:
            return 0
        self.trend.today = self.today
        return self.trend.add_coef
    
    @computed_field
    def coeff(self) -> float:
        return 1+self.week_day_add +self.lottery_add + self.trend_add
    
    
if __name__ == '__main__':
    from lottery import LotteryFig
    
    trend_coeff = TrendCoeff(today=datetime.strptime("05/05/2017", "%d/%m/%Y"))
    week_coeff = WeekDayCoef(today=datetime.strptime("05/05/2017", "%d/%m/%Y"))
    lottery_fig = LotteryFig(day_lottery = datetime.strptime("05/05/2017", "%d/%m/%Y") )
    lottery_coef = LotteryCoeff(today=datetime.strptime("05/05/2017", "%d/%m/%Y"), lottery_fig = lottery_fig)
    corr_coef = CorrCoeff(
        lottery_scheldue=lottery_coef,
        week_day=week_coeff,
        trend=trend_coeff, 
        today=datetime.strptime("05/05/2017", "%d/%m/%Y")
        )
    
    