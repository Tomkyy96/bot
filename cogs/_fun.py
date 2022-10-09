import discord
import os

from discord.ext import commands
from utils import *

class Fun(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    
    @commands.command(brief="Find some cute birb pictures", aliases=["bird"])
    async def birb(self, ctx):
        x, str = get_form_api_v2('https://some-random-api.ml/animal/birb', 'image')
        embed = discord.Embed(title="Birb", description=str, color=discord.Color.green())
        embed.set_image(url=x)
        if check_channel(ctx.channel.id): await ctx.send(embed=embed)

    @commands.command(brief="Find some cute dog pictures")
    async def dog(self, ctx):
        x, str = get_form_api_v2('https://some-random-api.ml/animal/dog', 'image')
        embed = discord.Embed(title="Dog", description=str, color=discord.Color.green())
        embed.set_image(url=x)
        if check_channel(ctx.channel.id): await ctx.send(embed=embed)

    @commands.command(brief="Find some cute cat pictures")
    async def cat(self, ctx):
        x, str = get_form_api_v2('https://some-random-api.ml/animal/cat', 'image')
        embed = discord.Embed(title="Cat", description=str, color=discord.Color.green())
        embed.set_image(url=x)
        if check_channel(ctx.channel.id): await ctx.send(embed=embed)

    @commands.command(brief="Find some cute panda pictures")
    async def panda(self, ctx):
        x, str = get_form_api_v2('https://some-random-api.ml/animal/panda', 'image')
        embed = discord.Embed(title="Panda", description=str, color=discord.Color.green())
        embed.set_image(url=x)
        if check_channel(ctx.channel.id): await ctx.send(embed=embed)

    @commands.command(brief="Find some cute red panda pictures")
    async def redpanda(self, ctx):
        x, str = get_form_api_v2('https://some-random-api.ml/animal/red_panda', 'image')
        embed = discord.Embed(title="Red panda", description=str, color=discord.Color.green())
        embed.set_image(url=x)
        if check_channel(ctx.channel.id): await ctx.send(embed=embed)

    @commands.command(brief="Find some cute fox pictures", aliases=[""])
    async def fox(self, ctx):
        x, str = get_form_api_v2('https://some-random-api.ml/animal/fox', 'image')
        embed = discord.Embed(title="Fox", description=str, color=discord.Color.green())
        embed.set_image(url=x)
        if check_channel(ctx.channel.id): await ctx.send(embed=embed)
    
    @commands.command(brief="Find some food pictures")
    async def food(self, ctx):
        x = get_form_api('https://foodish-api.herokuapp.com/api/', 'image')
        embed = discord.Embed(title="Food", description='', color=discord.Color.green())
        embed.set_image(url=x)
        if check_channel(ctx.channel.id): await ctx.send(embed=embed)

    @commands.command(pass_context=True, brief="Hug someone", aliases=["h"])
    async def hug(self, ctx, member: discord.Member = None):
        x = get_form_api('https://some-random-api.ml/animu/hug', 'link')
        if not member:
            await ctx.send("Pick someone 😏")
        else:
            embed = discord.Embed(title="Hug", description="Hey %s!\n %s hugs you!" % (member.mention, ctx.message.author.mention), color=discord.Color.green())
            embed.set_image(url=x)
            await ctx.send(embed=embed)

def setup(bot):
    bot.add_cog(Fun(bot))