import os, time,re, asyncio
import discord
from discord.ext import commands, tasks
intents = discord.Intents().all()
clientDC = commands.Bot(command_prefix='*',intents=intents)
clientDC.remove_command('help')
@clientDC.event
async def on_ready():
  guild=clientDC.get_guild(1004238305094811769)
  channel=guild.get_channel(1004238305094811772)
  i=0
  while True:
    await channel.send(content=i)
    i+=1
a='MTAwNzQ5ODA2MDU1MDYzNTU3MA.GmM_88.'
b='XmOlHNPFAnHreyU_YFgIPY6jYM3v-FLWykShqI'
clientDC.run(a+b)
