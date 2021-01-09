import discord
from discord.ext \
    import commands
import asyncio
import os
from discord.ext import commands

extensions = ['test']# Your Cog

if __name__ == '__main__':
    for extension in extensions:
        try:
            bot.load_extension(extension)# Cog Load
        except Exception as error:
            print('{} konnte nicht geladen werden. [{}]'.format(extension, error))


@bot.event  # Ready Event
async def on_ready():
    print("Bot Online mit:")
    print("Username: ", bot.user.name)
    print("User ID: ", bot.user.id)


bot.run("TOKEN") # Your Bot Token from https://discord.com/developers/applications
