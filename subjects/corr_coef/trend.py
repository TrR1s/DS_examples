from pydantic import BaseModel, computed_field,field_validator,Field
from datetime import datetime 

class TrendCoeff(BaseModel):
    add_coef: float = Field(default=0)
    today: datetime|None= Field(default=None)
    trend_list: dict[datetime,float]|None = Field(default={})
    
if __name__ == '__main__':
    trend_coeff = TrendCoeff(today=datetime.strptime("05/05/2017", "%d/%m/%Y"))
    print(trend_coeff)