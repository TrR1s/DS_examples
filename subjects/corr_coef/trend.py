from pydantic import BaseModel, computed_field,field_validator,Field
from datetime import datetime 
import numpy as np




class TrendCoeff(BaseModel):
    # add_coef: float = Field(default=0)
    today: datetime|None= Field(default=None)
    trend_dict: dict[datetime,float]|None = Field(default={})
    
    @computed_field
    def add_coef(self) -> float|None:
        if self.trend_dict is None or self.trend_dict == {} or self.today is None:
            return 0
        return self.trend_dict[self.today]


    
if __name__ == '__main__':
    import pandas as pd
    start_date='1/1/2017'
    end_date ='6/1/2017'
    x_date = pd.date_range(start_date,end_date)
    trend_coeff = TrendCoeff(today=datetime.strptime("05/05/2017", "%d/%m/%Y"))
    print(trend_coeff.add_coef)