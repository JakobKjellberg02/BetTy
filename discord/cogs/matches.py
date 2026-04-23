import discord
from discord.ext import commands
from util.scraper import getMatchesForToday

class RiskButtons(discord.ui.View):
    @discord.ui.button(label="Low Risk", style=discord.ButtonStyle.success) 
    async def low_risk(self, interaction: discord.Interaction, button: discord.ui.Button):
        await interaction.response.send_message("Low risk not implemented yet.", ephemeral=True)

    @discord.ui.button(label="Medium Risk", style=discord.ButtonStyle.primary)  
    async def medium_risk(self, interaction: discord.Interaction, button: discord.ui.Button):
        await interaction.response.send_message("Medium risk not implemented yet.", ephemeral=True)

    @discord.ui.button(label="High Risk", style=discord.ButtonStyle.danger)  
    async def high_risk(self, interaction: discord.Interaction, button: discord.ui.Button):
        await interaction.response.send_message("High risk not implemented yet.", ephemeral=True)

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
            embed.add_field(name=match, value="Odds: ?", inline=False)

        view = RiskButtons()
        await ctx.send(embed=embed, view=view)

async def setup(bot):
    await bot.add_cog(Matches(bot))