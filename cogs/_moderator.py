from discord.ext import commands
from utils import error_msg

class Moderator(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(brief='Bans a user from the server')
    async def ban(self, ctx):
        await ctx.send(error_msg())

    @commands.command(brief='Temporarily bans a user from the server')
    
    async def softban(self, ctx):
        await ctx.send(error_msg())

    @commands.command(brief='Kicks a user from the server')
    async def kick(self, ctx):
        await ctx.send(error_msg())
    
    @commands.command(brief='Server-mutes a user')
    async def mute(self, ctx):
        await ctx.send(error_msg())

    @commands.command(brief='Unmutes a user')
    async def unmute(self, ctx):
        await ctx.send(error_msg())

    @commands.command(brief='Unbans a user from the server')
    async def unban(self, ctx):
        await ctx.send(error_msg())

    @commands.command(brief="Delete a channel's messages")
    async def clear(self, ctx):
        await ctx.send(error_msg())

def setup(bot):
    bot.add_cog(Moderator(bot))