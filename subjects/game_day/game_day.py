from pydantic import BaseModel, computed_field,field_validator,Field
from datetime import datetime
import random

from subjects.player import PlrPool,Player

class GameDay(BaseModel):
    plr_pool: PlrPool
    base_hand_count: int= Field(default=20)
    corr_coef: float = Field(default=1.)
    # today: datetime
    @computed_field
    def hand_count(self) -> int:
        return int(self.corr_coef*self.base_hand_count)
    @computed_field
    def day_plr_pool(self) -> set[Player]:
        return set(random.sample(self.plr_pool,self.hand_count))
        
 