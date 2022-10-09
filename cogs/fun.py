import discord
import requests
import json
from discord.ext import commands

class Fun(commands.Cog):
  def __init__(self, bot):
    self.bot = bot
      
  @discord.slash_command(name = "hug", description = "Hug someone")
  async def hug(self, ctx, member: discord.Member):
    x = get_form_api('https://some-random-api.ml/animu/hug', 'link')
    embed = discord.Embed(
      title="Hug", 
      description=f"Hey {member.mention}!\n{ctx.author.mention} hugs you!", 
      color=discord.Color.green())
    embed.set_image(url=x)
    await ctx.respond(embed=embed)

    # @discord.slash_command()
    # async def birb(self, ctx):
    #     pass

    # @discord.slash_command()
    # async def panda(self, ctx):
    #     pass

    # @discord.slash_command()
    # async def redpanda(self, ctx):
    #     pass
      
    # @discord.slash_command()
    # async def fox(self, ctx):
    #     pass

    # @discord.slash_command()
    # async def fox(self, ctx):
    #     pass

def get_form_api(link, path):
    response = requests.get(link)
    json_data = json.loads(response.text)
    quote = json_data[path]
    return quote
  
def setup(bot):
    bot.add_cog(Fun(bot))