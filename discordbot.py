import discord
from discord.ext import tasks
from datetime import datetime

client = discord.Client()

@tasks.loop(seconds=60)
async def loop():
    now = datetime.now().strftime('%m/%d-%H:%M')
    if now == '04/06-20:30':
        alert_channel = client.get_channel(694093239954833412)
        msg = f'DSS説明会まであと15分！'
        await alert_channel.send(msg)

loop.start()

client.run("Njk0MTU0MTcxODAwMDkyNzUy.XooKMA.2D3yvlE5SXzWvYONUbn3Z5ZQFkA")
