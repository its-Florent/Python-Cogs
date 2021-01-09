import discord
from discord.ext import commands
import os

bot = commands.Bot(command_prefix=commands.when_mentioned_or("."), case_insensitive=True)

class test(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_message(self, message):
      if message.content.startswith("test"):
        await message.channel.send("TEST!")


def setup(bot):
    bot.add_cog(test(bot))
