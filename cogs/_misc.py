from discord.ext import commands
from utils import *
import discord
from discord.ext.commands import MissingPermissions

class Misc(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(brief="Get server info/stats", aliases=["status"])
    async def serverinfo(self, ctx, *args):
        embed = discord.Embed(color=discord.Color.green())
        embed.set_author(name=ctx.guild.name, icon_url=ctx.guild.icon_url)
        embed.set_thumbnail(url=ctx.guild.icon_url)
        embed.add_field(name="Owner", value=ctx.guild.owner)
        embed.add_field(name="Text Channels", value=len(ctx.guild.text_channels))
        embed.add_field(name="Voice Channels", value=len(ctx.guild.voice_channels))
        embed.add_field(name="Members", value=ctx.guild.member_count)
        embed.add_field(name="Online Members", value=sum(member.status==discord.Status.online and not member.bot for member in ctx.guild.members))
        embed.add_field(name="Offline Members", value=sum(member.status==discord.Status.offline and not member.bot for member in ctx.guild.members))
        embed.add_field(name="Bots", value=sum(member.bot for member in ctx.guild.members))
        embed.add_field(name="Roles", value=len(ctx.guild.roles))
        embed.add_field(name="Server Boosts", value=ctx.guild.premium_subscription_count)
        embed.set_footer(text='ID: %s | Server Created • %0.16s' % (ctx.guild.id, ctx.guild.created_at))
        if check_channel(ctx.channel.id): await ctx.send(embed = embed)

    @commands.command(brief="Get user information")
    async def whois(self, ctx, member: discord.Member = None):
        b=0    
        if not member:
            mention = []
            for role in ctx.author.roles:
                if role.name != "@everyone":
                    mention.append(role.mention)
            if not mention:
                pass
            else:
                b = " ".join(mention)
            embed = discord.Embed(color=discord.Color.green(), description=ctx.message.author.mention)
            embed.set_author(name=ctx.author, icon_url=ctx.message.author.avatar_url)
            embed.set_thumbnail(url=ctx.message.author.avatar_url)
            embed.add_field(name="Joined", value='%0.16s' % (ctx.message.author.joined_at), inline=True )
            embed.add_field(name="Registered", value='%0.16s' % (ctx.message.author.created_at), inline=True )
            embed.add_field(name="Roles [%i]" % (len(ctx.author.roles)-1), value=b, inline=False)
            embed.set_footer(text='ID: %s' % (ctx.author.id))
            if check_channel(ctx.channel.id): await ctx.send(embed = embed)
        else:
            mention = []
            for role in member.roles:
                if role.name != "@everyone":
                    mention.append(role.mention)
            if not mention:
                pass
            else:
                b = " ".join(mention)
            embed = discord.Embed(color=discord.Color.green(), description=member.mention)
            embed.set_author(name=member, icon_url=member.avatar_url)
            embed.set_thumbnail(url=member.avatar_url)
            embed.add_field(name="Joined", value='%0.16s' % (member.joined_at), inline=True )
            embed.add_field(name="Registered", value='%0.16s' % (member.created_at), inline=True )
            embed.add_field(name="Roles [%i]" % (len(member.roles)-1), value=b, inline=False)
            embed.set_footer(text='ID: %s' % (member.id))
            if check_channel(ctx.channel.id): await ctx.send(embed = embed)

    @commands.command(hidden=True)
    async def notyet(self,ctx):
        await ctx.send(error_msg())

    @commands.command(brief="Send random joke")
    async def joke(self,ctx):
        if check_channel(ctx.channel.id): await ctx.send(get_form_api('https://some-random-api.ml/joke', 'joke'))
    
    @commands.command(brief="Send random pic with meme")
    async def meme(self,ctx):
        x = get_form_api('https://some-random-api.ml/meme', 'image')
        embed = discord.Embed(title="Meme", description='', color=discord.Color.green())
        embed.set_image(url=x)
        if check_channel(ctx.channel.id): await ctx.send(embed=embed)

    @commands.command()
    async def ping(self, ctx):
        await ctx.send(f'pong!\n{round(self.bot.latency * 1000)}ms')
    
    @commands.has_permissions(administrator=True)
    @commands.command(hidden=True)
    async def edit(self, arg, arg1, arg2, arg3):
        channel = self.bot.get_channel(int(arg1))
        message = await channel.fetch_message(int(arg2))
        await message.edit(content = str(arg3))
    @edit.error
    async def test_error(self, ctx, error):
        if isinstance(error, MissingPermissions):
            await ctx.send(f'You dont have permissions')

    @commands.has_permissions(administrator=True)
    @commands.command(hidden=True)
    async def test(self, ctx):
        await ctx.send(check_channel(ctx.channel.id))
    @test.error
    async def test_error(self, ctx, error):
        if isinstance(error, MissingPermissions):
            pass
        
    @commands.command(brief="Make quote")
    async def quote(self,ctx,member: discord.Member = None, *args):
        if not member:
            pass
        else:
            username = member.display_name
            avatar = str(member.avatar_url)
            comment = 'ㅤ'.join(args)
            comment.replace("?", "%3f")
            comment.strip('"')
            await ctx.send('https://some-random-api.ml/canvas/youtube-comment?username='+username+'&comment='+comment+'&avatar='+avatar[:-15])

def setup(bot):
    bot.add_cog(Misc(bot))  