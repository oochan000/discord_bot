import discord
from discord.ext import tasks, commands
from datetime import datetime, timedelta
import asyncio
import os

bot = commands.Bot(command_prefix="$")

token = os.environ['DISCORD_BOT_TOKEN']

@tasks.loop(seconds=30)
async def loop():
    prenow = datetime.utcnow() + timedelta(hours=9)
    now = prenow.strftime('%H:%M')
    if now == '22:58':
        voice = await bot.get_channel(692958909476110409).connect()
        voice.play(discord.FFmpegPCMAudio('Shannons_Lullaby.mp3'))
        await asyncio.sleep(130)
        await voice.disconnect()
    elif now == '23:58':
        voice = await bot.get_channel(692958909476110409).connect()
        voice.play(discord.FFmpegPCMAudio('Shannons_Lullaby.mp3'))
        await asyncio.sleep(130)
        await voice.disconnect()

@bot.command(aliases=["play", "play_s", "play_S", "play_Shannon", "play_Shannons", "play_Shannons_Lullaby", "play_shannon", "play_shannons", "play_shannons_lullaby"])
async def play(ctx):
    voice = await bot.get_channel(692958909476110409).connect()
    voice.play(discord.FFmpegPCMAudio('Shannons_Lullaby.mp3'))
    await asyncio.sleep(130)
    await voice.disconnect()

loop.start()

bot.run(token)
