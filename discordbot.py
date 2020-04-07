import discord
from discord.ext import tasks
from datetime import datetime, timedelta
import os

client = discord.Client()

token = os.environ['DISCORD_BOT_TOKEN']

@tasks.loop(seconds=10)
async def loop():
    prenow = datetime.utcnow() + timedelta(hours=9)
    now = prenow.strftime('%H:%M')
    if now == '13:55':
        voice = await client.get_channel(692958909476110409).connect()
        voice.play(discord.FFmpegPCMAudio('Shannons_Lullaby.mp3'))
        await voice.disconnect()
    elif now == '14:00':
        voice = await client.get_channel(692958909476110409).connect()
        voice.play(discord.FFmpegPCMAudio('Shannons_Lullaby.mp3'))
        await voice.disconnect()

loop.start()

client.run(token)
