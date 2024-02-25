import discord
from discord.ext import commands
import settings

TOKEN = settings.TKN


bot = commands.Bot(command_prefix="!", intents=discord.Intents.all())

#!rdy
#応答確認
@bot.command()
async def rdy(ctx):
    await ctx.send("yes")


#/rdy
@bot.tree.command(name="rdy", description="rdy.")
async def ping(interaction: discord.Interaction):
    await interaction.response.send_message("yes")

bot.run(TOKEN)