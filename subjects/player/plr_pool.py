from pydantic import BaseModel, computed_field,field_validator,Field
from scipy import stats
import numpy as np

from subjects.player.player import TemplateForPool,Player
from subjects.player.templates import ID_SET,low_plr_template,low_ludoman_template,silver_plr_template,vip_plr_template,cheet_plr_template



def do_rnd_norm_prob_100(mean:float, std: float,num_plrs = 100) -> list[float]:
    norm_gen = stats.norm(mean,std)
    prob_100 = np.array([norm_gen.cdf(i) for i in range(num_plrs) ])
    prob_100[-1] = 1
    prob_100_swift = np.roll(prob_100, 1)
    prob_100_swift[0] = 0
    prob_100 -=prob_100_swift
    np.random.shuffle(prob_100)
    return list(prob_100)


class RNDRecency():
    
    prob_100_list = do_rnd_norm_prob_100(50,27)

def do_pool(ingredient) -> list[Player]:
    plr_set = set()
    curr_id_pull = ID_SET
    for curr_templ in ingredient:
        curr_templ.id_set = curr_id_pull
        curr_set = curr_templ.do_pool()
        if curr_set is not None:
            plr_set |= curr_set
        curr_id_pull = curr_templ.id_set
    return  list(plr_set)

class DoPull():
    ingredient= [                                           low_plr_template,
                                                            low_ludoman_template,
                                                            silver_plr_template,
                                                            vip_plr_template,
                                                            cheet_plr_template
                                                        ]
    pool = do_pool(ingredient)



class PlrPool(BaseModel):
    prob_100: list[float] = Field(default= RNDRecency.prob_100_list)
    pool: list[Player] = Field(default=DoPull.pool)





if __name__ == '__main__':
    plr_pool = PlrPool()
    print(len(plr_pool.pool))