import discord
from util.scraper import getMatchesForToday
from discord.ext import commands

class Matches(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def matches(self, ctx):
        embed = discord.Embed(
            title="🎾 Tennis Matches",
            color=discord.Color.green()
        )
        matches = getMatchesForToday()
        for match in matches:
            embed.add_field(name=match, value=f'Odds: ?', inline=False)
        await ctx.send(embed=embed)

async def setup(bot):
    await bot.add_cog(Matches(bot))