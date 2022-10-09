from discord.ext import commands
from tortoise import Tortoise
from models import GuildConfig

class Events(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_ready(self):
        await Tortoise.init(
            db_url="sqlite://db.sqlite3",
            modules={'models': ['models']}
        )
        await Tortoise.generate_schemas()
        print('Bot is ready')

    @commands.Cog.listener()
    async def on_guild_join(self, guild):
        find = await GuildConfig.filter(guild_id=guild.id)
        if not find:
            new_cfg = GuildConfig(guild_id=guild.id, prefix='!', badlink=True , badlink_method=0, badlink_rank=None)
            await new_cfg.save()
            print("Do work")
        else:
            print("Do nothing")

    # <summary>
    # Komenty do BadLink 
    # <summary>

    #OFF badlink na serwerze
    @commands.command()
    async def disable(self, ctx):
        await GuildConfig.filter(guild_id=ctx.guild.id).update(badlink=False)
        await ctx.send("Disabled")

    #ON badlink na serwerze
    @commands.command()
    async def enable(self, ctx):
        await GuildConfig.filter(guild_id=ctx.guild.id).update(badlink=True)
        await ctx.send("Enabled")

    #Check badlink na serwerze
    @commands.command()
    async def check(self, ctx):
        query: GuildConfig = await GuildConfig.filter(guild_id=ctx.guild.id).get_or_none()
        await ctx.send(f"badlink is {'enabled' if query.badlink else 'disabled'}")

def setup(bot):
    bot.add_cog(Events(bot))