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
  await channel.send(content=i)

clientDC.run('MTAwNzQ5ODA2MDU1MDYzNTU3MA.GB40C9.UaxN-iX5rt8JOivchwoQfIXVm7nxQl0x-ymuPo')
