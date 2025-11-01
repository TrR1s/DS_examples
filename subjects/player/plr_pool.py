from pydantic import BaseModel, computed_field,field_validator,Field

from subjects.player.player import TemplateForPool,Player
from subjects.player.templates import ID_SET,low_plr_template,low_ludoman_template,silver_plr_template,vip_plr_template,cheet_plr_template

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
    
    pool: list[Player] = Field(default=DoPull.pool)

if __name__ == '__main__':
    plr_pool = PlrPool()
    print(len(plr_pool.pool))