import discord
from discord.ext import commands

class Gallery(commands.Cog):
  def __init__(self, bot):
    self.bot = bot

  @commands.Cog.listener()
  async def on_message(self, message):
    if message.channel.id == 534453069530923019 or message.channel.id == 470914126927888385:
      await message.channel.create_thread(
        name="Komentarze",
        message=message,
        type=discord.ChannelType.public_thread,
        auto_archive_duration=60, reason=None)

def setup(bot):
    bot.add_cog(Gallery(bot))