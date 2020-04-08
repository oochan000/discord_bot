import discord
from discord.ext import tasks
from datetime import datetime, timedelta
import asyncio
import os

client = discord.Client()

token = os.environ['DISCORD_BOT_TOKEN']

@tasks.loop(seconds=30)
async def loop():
    prenow = datetime.utcnow() + timedelta(hours=9)
    now = prenow.strftime('%H:%M')
    now2 = prenow.strftime('%y/%m/%d-%H:%M')
    if now == '22:58':
        voice = await client.get_channel(692958909476110409).connect()
        voice.play(discord.FFmpegPCMAudio('Shannons_Lullaby.mp3'))
        await asyncio.sleep(130)
        await voice.disconnect()
    elif now == '23:58':
        voice = await client.get_channel(692958909476110409).connect()
        voice.play(discord.FFmpegPCMAudio('Shannons_Lullaby.mp3'))
        await asyncio.sleep(130)
        await voice.disconnect()
    elif now2 == '20/04/08-14:55':
        alert_channel = await client.get_channel(692958909476110408)
        await alert_channel.send("DSSまであと5分！")

loop.start()

client.run(token)
