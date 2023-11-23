# imports and stuff
import discord
from discord.ext import commands 
import asyncio
import os
import random
from discord.utils import get
intents=discord.Intents.all()
client = discord.Client(intents=discord.Intents.all())
client = commands.Bot(command_prefix='.',intents=intents)
client.remove_command('help')

# clears msgs
@client.command(aliases = ['pu'])
async def purge(ctx,amount = 1):
 await ctx.channel.purge(limit=amount+1)

# kicks members 
@client.command(aliases = ['k'])
async def kick(ctx, member : discord.Member, *, reason=None):
    await member.kick(reason=reason)
    await ctx.send('{0} was kicked'.format(member))
    await member.send('You were kicked by {0}'.format(ctx.author))


# ping
@client.command(aliases = ['ping'])
async def latency(ctx):
  ping_embed= discord.Embed(
    title = 'LATENCY CHECK',
    description = '{0}ms'.format(round(client.latency*100,2)),
    colour = 0xaaff00
  )
  ping_embed.set_thumbnail(url = 'https://media.discordapp.net/attachments/982644043420930048/982916949208076288/bruh.png?')
  ping_embed.set_author(name='Ashu' , icon_url = 'https://media.discordapp.net/attachments/982644043420930048/982916948130144266/1645760017380.gif?')
  ping_embed.set_footer(text='Thanks for using | {0}'.format(ctx.guild), icon_url='https://media.discordapp.net/attachments/982644043420930048/982916949208076288/bruh.png?')
  await ctx.send(embed = ping_embed)


# is it?(YES/NO)
@client.command(aliases = ['is?'])
async def is_it_true(ctx,*,ques):
  is_it_embed = discord.Embed(
    colour = 0x00ffbf
  )
  is_it_embed.set_author(name='Ashu' , icon_url='https://media.discordapp.net/attachments/982644043420930048/982916948130144266/1645760017380.gif?')
  is_it_embed.set_footer(text='Thanks for using | {0}'.format(ctx.guild), icon_url='https://media.discordapp.net/attachments/982644043420930048/982916949208076288/bruh.png?')
  is_it_embed.add_field(name='{0}'.format(ques) , value='{0}'.format(random.choice(list_is_true)))
  await ctx.send(embed = is_it_embed)
list_is_true = ['Yes, Ofcourse.',
           '''Nah, Don't think so.''',
           'umm, IDK.']

# dict for aliases
aliasdict = {'PURGE':'-pu','LATENCY':'-ping','IS_IT_TRUE':'-is?','SHOW_ALIAS':'-alias','ROCK PAPER SCISSOR':'-rps','KICK':'-k','FREE NITRO':'-freenitro',}

# show aliases
@client.command(aliases = ['alias'])
async def show_alias(ctx):
  aliases_embed = discord.Embed(
    title = 'Aliases of Commands',
    colour = 0xc164ff
  )
  aliases_embed.set_thumbnail(url = 'https://media.discordapp.net/attachments/982644043420930048/982916949208076288/bruh.png?')
  aliases_embed.set_author(name='Ashu' , icon_url = 'https://media.discordapp.net/attachments/982644043420930048/982916948130144266/1645760017380.gif?')
  aliases_embed.set_footer(text='Thanks for using | {0}'.format(ctx.guild), icon_url='https://media.discordapp.net/attachments/982644043420930048/982916949208076288/bruh.png?')
  for i in aliasdict:
    aliases_embed.add_field(name=i,value=aliasdict[i],inline=False)
  # aliases_embed.add_field(name = 'PURGE',value='-pu',inline=False)
  # aliases_embed.add_field(name = 'LATENCY',value='-ping',inline=False)
  # aliases_embed.add_field(name = 'IS_IT_TRUE',value='-is?',inline=False)
  # aliases_embed.add_field(name = 'SHOW_ALIAS',value='-alias',inline=False)
  # aliases_embed.add_field(name = 'KICK',value='-k',inline=False)
  # aliases_embed.add_field(name = 'ROCK PAPER SCISSORS',value='-rps',inline=False)
  # aliases_embed.add_field(name = 'FREE NITRO',value='-freenitro',inline=False)
  await ctx.send(embed = aliases_embed)


# rps
@client.command()
async def rps(ctx ,*, picked_opt : str):
  rps_list = ['rock' , 'paper' , 'scissors']
  rps_bot = random.choice(rps_list)
  
  rps_win_embed = discord.Embed(
    title = 'You Won!',
    colour = 0x00ff00
  )
  rps_win_embed.set_thumbnail(url = 'https://media.discordapp.net/attachments/982644043420930048/982916949208076288/bruh.png?')
  rps_win_embed.set_author(name='Ashu' , icon_url = 'https://media.discordapp.net/attachments/982644043420930048/982916948130144266/1645760017380.gif?')
  rps_win_embed.set_footer(text='GG, I guess. | {0}'.format(ctx.guild), icon_url='https://media.discordapp.net/attachments/982644043420930048/982916949208076288/bruh.png?')
  rps_win_embed.add_field(name = 'Your Choice' , value ='{0}'.format(picked_opt))
  rps_win_embed.add_field(name = 'My Choice' , value ='{0}'.format(rps_bot))

  rps_lose_embed = discord.Embed(
    title = 'You Lost!',
    colour = 0xff0000
  )
  rps_lose_embed.set_thumbnail(url = 'https://media.discordapp.net/attachments/982644043420930048/982916949208076288/bruh.png?')
  rps_lose_embed.set_author(name='Ashu' , icon_url = 'https://media.discordapp.net/attachments/982644043420930048/982916948130144266/1645760017380.gif?')
  rps_lose_embed.set_footer(text='Imagine losing to a bot. | {0}'.format(ctx.guild), icon_url='https://media.discordapp.net/attachments/982644043420930048/982916949208076288/bruh.png?')
  rps_lose_embed.add_field(name = 'Your Choice' , value ='{0}'.format(picked_opt))
  rps_lose_embed.add_field(name = 'My Choice' , value ='{0}'.format(rps_bot))

  rps_tie_embed = discord.Embed(
    title = 'Tied',
    colour = 0x0000ff
  )
  rps_tie_embed.set_thumbnail(url = 'https://media.discordapp.net/attachments/982644043420930048/982916949208076288/bruh.png?')
  rps_tie_embed.set_author(name='Ashu' , icon_url = 'https://media.discordapp.net/attachments/982644043420930048/982916948130144266/1645760017380.gif?')
  rps_tie_embed.set_footer(text='Bruh,TIE. | {0}'.format(ctx.guild), icon_url='https://media.discordapp.net/attachments/982644043420930048/982916949208076288/bruh.png?')
  rps_tie_embed.add_field(name = 'Your Choice' , value = '{0}'.format(picked_opt))
  rps_tie_embed.add_field(name = 'My Choice' , value = '{0}'.format(rps_bot))


  if rps_bot == 'rock' and picked_opt == 'paper':
    await ctx.send(embed = rps_win_embed)
  if rps_bot == 'rock' and picked_opt == 'scissors':
    await ctx.send(embed  = rps_lose_embed)
  if rps_bot == 'rock' and picked_opt == 'rock':
    await ctx.send(embed = rps_tie_embed)
  if rps_bot == 'paper' and picked_opt == 'scissors':
    await ctx.send(embed = rps_win_embed)
  if rps_bot == 'paper' and picked_opt == 'rock':
    await ctx.send(embed  = rps_lose_embed)
  if rps_bot == 'paper' and picked_opt == 'paper':
    await ctx.send(embed = rps_tie_embed)
  if rps_bot == 'scissors' and picked_opt == 'rock':
    await ctx.send(embed = rps_win_embed)
  if rps_bot == 'scissors' and picked_opt == 'paper':
    await ctx.send(embed  = rps_lose_embed)
  if rps_bot == 'scissors' and picked_opt == 'scissors':
    await ctx.send(embed = rps_tie_embed)
  if picked_opt != 'scissors' and picked_opt != 'rock' and picked_opt != 'paper':
    await ctx.send('Imagine sucking in RPS. LOL')
  
# free nitro
@client.command()
async def freenitro(ctx):
    await ctx.author.send('''Here's your FREE NITRO!!!\n'''+'https://tenor.com/view/rick-astly-rick-rolled-gif-22755440')
    await ctx.send('Check your DMs {0}'.format(ctx.author))

#linkDisplay
# @client.command()
# async def link(ctx,linkx,*,channel_id = 975083202785972274):
#   channel = client.get_channel(channel_id)
#   linkx_embed = discord.Embed(
#     title = 'Link sent by {0}'.format(ctx.author),
#     description = linkx,
#     colour = 0x2f3136

#   )
#   await channel.send(embed=linkx_embed)

#help
@client.command()
async def help(ctx):
  help_embed = discord.Embed(
    title = 'HELP MENU',
    colour = 0xf0ff00
  )
  help_embed.set_thumbnail(url = 'https://media.discordapp.net/attachments/982644043420930048/982916949208076288/bruh.png?')
  help_embed.set_author(name='Ashu' , icon_url = 'https://media.discordapp.net/attachments/982644043420930048/982916948130144266/1645760017380.gif?')
  help_embed.set_footer(text='[] = OPTIONAL ATTRIBUTES , <> = REQUIRED ATTRIBUTES\nThanks for using. | {0}'.format(ctx.guild), icon_url='https://media.discordapp.net/attachments/982644043420930048/982916949208076288/bruh.png?')
  help_embed.add_field(name = 'PURGE' , value = 'Deletes a specific amount of messages as specified by user.\n -purge [amount of messages]' , inline = False)
  help_embed.add_field(name = 'KICK' , value = 'Kicks a member specified by ADMIN.\n -kick <member> [reason]' , inline = False)
  help_embed.add_field(name = 'LATENCY' , value = 'Displays the PING.\n -ping' , inline = False)
  help_embed.add_field(name = 'IS IT TRUE?' , value = 'Says YES or NO to a question.\n -is_it_true <question>' , inline = False)
  help_embed.add_field(name = 'SHOW ALIAS' , value = 'Displays all command aliases.\n -show_alias' , inline = False)
  help_embed.add_field(name = 'ROCK PAPER SCISSORS' , value = 'Classic Rock Paper Scissors.\n -rps <choice>' , inline = False )
  help_embed.add_field(name = 'FREE NITRO' , value = 'Sends a legit FREE NITRO as gift in dm. Possibility = 1/1000.\n -freenitro' , inline = False)
  await ctx.send(embed = help_embed)

# spam
@client.command()
async def spam(ctx,no,*txt):
  no = int(no)
  if no > 500:
    await ctx.send('**The max limit is 500!**')
  else:
    await ctx.channel.purge(limit=1)
    for i in range(no):
      await ctx.send(' '.join(txt))

# choose
@client.command()
async def choose(ctx,optns):
  if optns == None :
    await ctx.send('Kuch choose krne ko to de bkl💀')
  else:
    await ctx.send('I choose {0}'.format(random.choice(optns)))
  
# startup

with open('token.txt') as f:
  token = f.readline()

async def ch_pr():
  print('Bot is up!')
  await client.wait_until_ready()
  statuses = ['Ashuu#3473' , '-help']
  while not client.is_closed():
    status = random.choice(statuses)
    await client.change_presence(status = discord.Status.dnd ,activity=discord.Activity(type = discord.ActivityType.watching,name=status))
    await asyncio.sleep(2)
client.loop.create_task(ch_pr())
client.run(token)