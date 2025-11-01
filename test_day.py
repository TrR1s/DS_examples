# from subjects.game_day import GameDay
from subjects.player import PlrPool
from subjects.game_day import GameDay


plr_pool = PlrPool()
print(len(plr_pool.pool))
game_day = GameDay(
    plr_pool=plr_pool
)

print(game_day.hand_count)
