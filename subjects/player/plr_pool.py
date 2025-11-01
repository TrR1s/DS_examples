from pydantic import BaseModel, computed_field,field_validator,Field

from subjects.player import TemplateForPool,Player
from subjects.player import ID_SET,low_plr_template,low_ludoman_template,silver_plr_template,vip_plr_template,cheet_plr_template




class PlrPool(BaseModel):
    ingredient:list[TemplateForPool] = Field(default=[
                                                        low_plr_template,
                                                        low_ludoman_template,
                                                        silver_plr_template,
                                                        vip_plr_template,
                                                        cheet_plr_template
                                                    ])

    @computed_field
    def pool(self) -> list[Player]:
        plr_set = set()
        curr_id_pull = ID_SET
        for curr_templ in self.ingredient:
            curr_templ.id_set = curr_id_pull
            curr_set = curr_templ.do_pool()
            if curr_set is not None:
                plr_set |= curr_set
            curr_id_pull = curr_templ.id_set
        return  list(plr_set)   

if __name__ == '__main__':
    plr_pool = PlrPool()
    print(len(plr_pool.pool))