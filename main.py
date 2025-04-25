from discord.ext import commands
import discord
from os import getenv, listdir
from dotenv import load_dotenv
import logging
import ast
import pandas

# .env
load_dotenv()

# Set the logging
logging.basicConfig(level=logging.INFO)
handler = logging.FileHandler(filename='discord.log', encoding='utf-8', mode='w')

# Intents
intents = discord.Intents.default()
intents.message_content = True

# bot instances
bot = commands.Bot(command_prefix="!", intents=intents.all(), help_command=None)

# listen to events and commands
@bot.event
async def on_ready():
    print(f'We have logged in as {bot.user}')

    for filename in listdir("./cogs"):
        if filename.endswith(".py"):
            await bot.load_extension(f"cogs.{filename[:-3]}")


# run the bot
bot.run(getenv('DISCORD_TOKEN'), log_handler=handler)
