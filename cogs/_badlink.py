import discord
import json
import requests

from models import GuildConfig
from discord.ext import tasks, commands 
from discord.utils import get
from urlextract import URLExtract
from utils import *
from datetime import date

class BadLink(commands.Cog):
        
    def __init__(self, bot):
        self.badlinks = []
        self.bot = bot
        self.urlupdate.start()
        
    def cog_unload(self):
        self.urlupdate.cancel()

    @tasks.loop(hours=168)
    async def urlupdate(self):
        try:
            response = requests.get("https://api.hyperphish.com/gimme-domains")
            self.badlinks = json.loads(response.text)
            print("URL UPDATE DONE")
        except:
            print("URL UPDATE FAILED")

    @urlupdate.before_loop
    async def before_urlupdate(self):
        await self.bot.wait_until_ready()

    @commands.Cog.listener()
    async def on_message(self, message):
            if (message.author.bot):
                return
            query: GuildConfig = await GuildConfig.filter(guild_id=message.guild.id).get_or_none()
            if (query.badlink):
                mcont = message.content
                extractor = URLExtract()
                urls = extractor.find_urls(mcont)
                if urls:
                    if checkx(urls[0], self.badlinks):
                        await message.delete()
                        await message.author.send(f"Your message on {message.guild.name} was deleted because it contains links in our filter!")
                        await message.channel.send(f"Invalid link detected, please investigate who sent BAD URL in chat!")
                        guild = self.bot.get_guild(query.guild_id)
                        member = message.author
                        if (query.badlink_method == 1): #NOTHING
                            return
                        if (query.badlink_method == 2): #REMOVE ROLE
                            role = discord.utils.get(guild.roles, name=query.badlink_rank)
                            await member.remove_roles(role)
                        if (query.badlink_method == 3): #KICK
                            await member.kick(reason = "Phishing link")
                        if (query.badlink_method == 4): #BAN
                            await member.ban(reason = "Phishing link")

# channel = self.bot.get_channel(911717306860732456)
# await channel.send(f"Phishing link detected! User {message.author.mention} Removed BOMBEL role for illegal link! | <@&554705684789198848>")

def setup(bot):
    bot.add_cog(BadLink(bot))

