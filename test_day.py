import json
from subjects.player import PlrPool,Player
from subjects.game_day import GameDay,DayFigures

plr_pool = PlrPool()
print(len(plr_pool.pool))
game_day = GameDay(
    plr_pool=plr_pool
)

day_fig = game_day.dayfig

plr1 = day_fig.day_plr_pool[0]


pretty_json = json.dumps(plr1.model_dump(), indent=4)
print(pretty_json)