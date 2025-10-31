from pydantic import BaseModel, computed_field,field_validator,Field
from datetime import datetime 

class TrendCoeff(BaseModel):
    # add_coef: float = Field(default=0)
    today: datetime|None= Field(default=None)
    trend_list: dict[datetime,float]|None = Field(default={})
    
    @computed_field
    def add_coef(self) -> float|None:
        if self.trend_list is None or self.trend_list == {} or self.today is None:
            return 0
        return self.trend_list[self.today]


    
if __name__ == '__main__':
    trend_coeff = TrendCoeff(today=datetime.strptime("05/05/2017", "%d/%m/%Y"))
    print(trend_coeff)