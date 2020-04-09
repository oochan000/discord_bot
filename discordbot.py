import discord
import asyncio
import os
from datetime import datetime, timedelta
from discord.ext import commands

token = os.environ['DISCORD_BOT_TOKEN']

client = commands.Bot(command_prefix='$')

alarm_time = '23:33'#24hrs
channel_id = '692958909476110409'

@client.event
async def time_check():
    await client.wait_until_ready()
    while not client.is_closed:
    	prenow = datetime.utcnow() + timedelta(hours=9)
    	now = prenow.strftime('%H:%M')

        channel = client.get_channel(channel_id)

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
	else
		await asyncio.sleep(1)

@client.event
async def on_message(massage)
	if message.content.startwith("$play")
		voice = await client.get_channel(692958909476110409).connect()
        	voice.play(discord.FFmpegPCMAudio('Shannons_Lullaby.mp3'))
		await asyncio.sleep(130)
		await voice.disconnect()

client.loop.create_task(time_check())

client.run(token)
