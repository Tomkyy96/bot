import discord
import os

from discord.ext import commands


class Threads(commands.Cog):
    
    def __init__(self, bot):
        self.bot = bot
 
    
    @commands.command()
    async def crth(self, ctx):
        msg = await ctx.send("whatever")
        # you could also use msg = await channel.fetch_message(some_id)
        await ctx.channel.create_thread(name="test",message=msg, type=discord.ChannelType.public_thread, auto_archive_duration=60, reason=None)

def setup(bot):
    bot.add_cog(Threads(bot))