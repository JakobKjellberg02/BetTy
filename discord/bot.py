""" 
Testing of Discord Bot
"""

import discord
from discord.ext import commands
import os
from dotenv import load_dotenv
import asyncio

load_dotenv()
DISCORD_KEY = os.getenv('DISCORD_KEY')

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix="$", intents=intents)

@bot.event
async def on_ready():
    print(f'Logged in as {bot.user}')

async def main():
    async with bot:
        await bot.load_extension("cogs.matches")
        await bot.start(DISCORD_KEY)

asyncio.run(main())