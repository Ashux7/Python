# imports and stuff
import discord
from discord.ext import commands 
import asyncio
import os
import random
client = discord.Client
client = commands.Bot(command_prefix = '-')


# music
# music/joining
@client.command()
async def join(ctx):
  voice_channel = ctx.author.voice.channel
  if ctx.voice_client is voice_channel:
    await voice_channel.connect() #connects to channel
  else:
    await ctx.voice_client.move_to(voice_channel) #moves to other channel
# music/leaving
@client.command()
async def leave(ctx):
  if ctx.voice_client.is_connected():
    await ctx.voice_client.disconnect()
  else:
    await ctx.send('Imagine not inviting and asking to leave. So NAB!')
# music/pause
@client.command()
async def pause(ctx):
  if ctx.voice_client.is_playing():
    ctx.voice_client.pause()
  else:
    ctx.send('Imagine not playing and asking to keep quiet. So NAB!')
# music/resume
@client.command()
async def resume(ctx):
  if ctx.voice_client.is_paused():
    ctx.voice_client.resume()
  else:
    ctx.send('''Imagine there's nothing to play but asking to play. So NAB!''')
# music/stop
@client.command()
async def stop(ctx):
  if ctx.voice_client.is_playing():
    ctx.voice_client.stop()
  else:
    ctx.send('''Imagine nothing is playing but asking to stop. So NAB!''')
# music/playing
@client.command()
async def play(ctx ,*,url : str):
  await ctx.send()

# startup
async def ch_pr():
  print('Bot is up!')
  await client.wait_until_ready()
  statuses = ['Ashu' , '-help']
  while not client.is_closed():
    status = random.choice(statuses)
    await client.change_presence(status = discord.Status.dnd ,activity=discord.Activity(type = discord.ActivityType.listening, name=status))
    await asyncio.sleep(7)
client.loop.create_task(ch_pr())


client.run('')