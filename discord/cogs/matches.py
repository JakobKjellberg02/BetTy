import discord
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
        matches = [
            ("Sinner vs Alcaraz", "1,20 - 1,23"),
            ("Kjellberg vs Bothmann", "1,01 - 10,00")
        ]
        for match, odds in matches:
            embed.add_field(name=match, value=f'Odds: {odds}', inline=False)
        await ctx.send(embed=embed)

async def setup(bot):
    await bot.add_cog(Matches(bot))