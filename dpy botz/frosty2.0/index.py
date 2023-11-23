import discord
from discord import app_commands
import os


intents = discord.Intents.default()
frosty2 = discord.Client(intents=intents)
cmds = app_commands.CommandTree(frosty2)

@cmds.command(name='ping',description='Displays latency')
async def fmcd(ctx):
    await ctx.response.send_message('{0}ms'.format(round(frosty2.latency*100,2)))

@frosty2.event
async def on_ready():
    await cmds.sync()
    print("Bot is ready!")
with open('dpy botz\\frosty2.0\\token.txt') as f:
    ftoken = f.readline()
    ftoken=str(ftoken)

frosty2.run(token=ftoken)