""" 
Testing of Discord Bot
"""

import discord
import os
from dotenv import load_dotenv

load_dotenv()
DISCORD_KEY = os.getenv('DISCORD_KEY')

intents = discord.Intents.default()
intents.message_content = True

client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print(f'Logged in as {client.user}')

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('$hello'):
        await message.channel.send('Hello!')

client.run(DISCORD_KEY)