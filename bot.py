import discord
from discord.ext import commands
import modules.settings as settings


TOKEN = settings.TKN


bot = commands.Bot(command_prefix="!", intents=discord.Intents.all())

#!rdy
#応答確認
@bot.command()
async def rdy(ctx):
    await ctx.send("yes")

@bot.command()
async def sonuda_now(ctx):
    #ステータス設定
    status = 2
    if status == 2:
         status_str = "そぬだは、暇していますよ。"
    elif status == 1:
         status_str = "そぬだは、ゲームしてます。"
    elif status == 2:
         status_str = "そぬだは、就寝中です。"
    elif status == 3:
         status_str = "そぬだは、仕事中をしてます。"
    elif status == 4:
         status_str = "そぬだは、私の記録パターン外の行動中です。"
        
    await ctx.send(status_str)

bot.run(TOKEN)