import discord
from discord.ext import commands

class Greetings(commands.Cog):
  def __init__(self, bot):
    self.bot = bot

  @discord.slash_command(description = "Say hello to the bot")
  async def hello(self, ctx):
    await ctx.respond("Hello, this is a slash command from a cog!")

  @discord.slash_command(description = "Say bye to the bot")
  async def bye(self, ctx):
    await ctx.respond("Bye, remember that this is a slash command from a cog!")

  @discord.slash_command(description = "I don't know what is this for")
  async def restricted(self, ctx):
    await ctx.respond("Hi, this is a restricted slash command from a cog!")

def setup(bot):
  bot.add_cog(Greetings(bot))