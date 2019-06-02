import discord
from discord.ext import commands
import FirstBot.gamedeal as gd
class MyClient(discord.Client):
    async def on_ready(self):
        print("Logged in as")
        print(self.user.name)
        print(self.user.id)
        print('------')

    async def on_message(self, message):
        gameinfo = message.content[1:].split(', ')
        print(gameinfo)
        if len(gameinfo) == 2:
             game_deal_list = sorted(gd.look_up_game(gameinfo[0], gameinfo[1]), key=lambda a: a.sale_price)
             for i in game_deal_list[:5]:
                 await message.channel.send(i)


if __name__ == "__main__":
    client = MyClient()
    client.run('NTg0NTIyNjU3NzQ0Mjg5Nzky.XPMKnA.SUrS3JhLkjuqKJw49Y29rpPP7uQ')
