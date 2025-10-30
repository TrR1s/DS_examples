from pydantic import BaseModel, computed_field,field_validator,Field
import numpy as np 

class TotalFig(BaseModel):
    sum: float|int= Field(default=0)
    mean: float = Field(default=0)
    std: float = Field(default=0)
    

class SessionFigures(BaseModel):
    hand_amount: int
    result: float
    
class PlayerFigures(BaseModel):
    visits: int = Field(default=0)
    results: list[float] = Field(default=[])
    hand_amounts: list[int] = Field(default=[])
    
    @computed_field
    def total_results(self)-> TotalFig:
        res_np = np.array(self.results)
        return TotalFig(sum=res_np.sum(),
                        mean=res_np.mean(),
                        std=res_np.std(ddof=1))
    
    @computed_field
    def total_hands(self)-> TotalFig:
        hands_np = np.array(self.hand_amounts)
        return TotalFig(sum=hands_np.sum(),
                        mean=hands_np.mean(),
                        std=hands_np.std(ddof=1))


if __name__ == '__main__':
    plr_stl = PlayerFigures(
        visits= 15,
    results = [156,12,12,156,126,141],
    hand_amounts= [1556,1542,5512,156,126,141])
    
    print(plr_stl)