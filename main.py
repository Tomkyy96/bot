import discord
import os # default module
from dotenv import load_dotenv

load_dotenv() # load all the variables from the env file

bot = discord.Bot(debug_guilds=[470374603848548362])

bot.load_extension(f'cogs.fun')
bot.load_extension(f'cogs.gallery')
bot.load_extension(f'cogs.game')

@bot.event
async def on_ready():
    print(f"{bot.user} is ready and online!")

bot.run(os.getenv('TOKEN'))