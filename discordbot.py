import discord
import asyncio
import os
from datetime import datetime, timedelta
from discord.ext import commands

token = os.environ['DISCORD_BOT_TOKEN']

client = commands.Bot(command_prefix='$')

@client.event
async def time_check():
    await client.wait_until_ready()
    while not client.is_closed:
        prenow = datetime.utcnow() + timedelta(hours=9)
        now = prenow.strftime('%H:%M')

        if now == '15:10':
            voice = await client.get_channel(692958909476110409).connect()
            voice.play(discord.FFmpegPCMAudio('Shannons_Lullaby.mp3'))
            await asyncio.sleep(130)
            await voice.disconnect()
        elif now == '23:58':
            voice = await client.get_channel(692958909476110409).connect()
            voice.play(discord.FFmpegPCMAudio('Shannons_Lullaby.mp3'))
            await asyncio.sleep(130)
            await voice.disconnect()
        else:
            await asyncio.sleep(1)

client.loop.create_task(time_check())

client.run(token)
