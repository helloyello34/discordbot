import FirstBot.storeinfo as si
import FirstBot.gamedeal as gd

store_info_list = si.read_store_info()
game_deal_list = gd.look_up_game("farming simulator 15", 30)

for i in game_deal_list:
    print(i)

# https://www.cheapshark.com/browse?title=batman