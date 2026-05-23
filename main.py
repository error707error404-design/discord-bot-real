import discord
from discord.ext import commands
import os

TOKEN = os.getenv("MTUwNzM1MzAwNzc5MTE0OTEzNw.Ga6jkC.RhzTk-n7Z-t6xrfVlAwg5JYUND1hhCEKoocQSI")

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix="!", intents=intents)

@bot.event
async def on_ready():
    print("봇 실행 성공!")

@bot.command()
async def 핑(ctx):
    await ctx.send("퐁!")

bot.run(TOKEN)
