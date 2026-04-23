import asyncio
import sqlite3
import discord
from discord.ext import commands

DB_PATH = "database/money.db"

class Money(commands.cog):
    def __init__(self, bot):
        self.bot = bot
        self.conn_obj = sqlite3.connect(DB_PATH)
        self.cursor_obj = self.conn_obj.cursor()
        self.curser_obj.execute(
            '''CREATE TABLE IF NOT EXISTS users
                 (user_id TEXT PRIMARY KEY, balance INTEGER NOT NULL DEFAULT 0)''')
        self.conn_obj.commit()
        self.conn_obj.close()
        
        


        
