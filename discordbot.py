import discord
from discord.ext import tasks
from datetime import datetime, timedelta

client = discord.Client()

@tasks.loop(seconds=60)
async def loop():
    prenow = datetime.utcnow() + timedelta(hours=9)
    now = prenow.strftime('%y/%m/%d-%H:%M')
    if now == '20/04/07-12:20':
        alert_channel = client.get_channel(694093239954833412)
        msg = f'DSS説明会まであと15分！'
        await alert_channel.send(msg)

loop.start()

client.run("Njk0MTU0MTcxODAwMDkyNzUy.Xovwaw.QjYQAX2g1xjsbr0-ZOj0xa0pPWM")
