import os
from discord.ext import commands
import discord
from discord import *

import aiohttp
import asyncio



bot = commands.Bot(  # Create a new bot
    command_prefix='*',  # Set the prefix
    description='A bot used for general use.',  # Set a description for the bot
 )


version = "v0.0.2"

bot.author_id = '566174391663067136'  # Change to your discord id!!!


@bot.event
async def on_ready():

    
    await bot.change_presence(
                activity=discord.Game(
                   f"with {len(bot.guilds)} servers | *help | {version}"),
                    afk=True)

    bot._last_result = None
    bot.session = aiohttp.ClientSession()


    print(f'Logged in as {bot.user.name} - {bot.user.id}')
    cogs = ['cogs.dev', 'cogs.greetings', 'cogs.heart', 'cogs.info', 'cogs.lockdown', 'cogs.misc', 'cogs.mod', 'cogs.on_message', 'cogs.other']
    for cog in cogs:
        bot.load_extension(cog)
    return





@bot.command()
@commands.is_owner()
async def shutdown(ctx):
  channel = bot.get_channel(774916092103491614)
  msg = 'Bot is shutting down for maintenence in 1 minute.'
  await channel.send(msg)
  await asyncio.sleep(60)
  await msg.delete
  await ctx.bot.logout()

@bot.command()
@commands.is_owner()
async def devstatus(ctx):
      '''The bot\'s status for devs only.'''
      channel = bot.get_channel(774916092103491614)
      await channel.send("The bot is running and will not be closed until it is time, I will remind you when I am closing/shutting down, its not permanent!")


@bot.event
async def on_command_error(ctx, error):
    if isinstance(error, commands.CommandNotFound):
      return await ctx.send(
            "Invalid command try using *help to figure out commands!")
    if isinstance(error, commands.MissingRequiredArgument):
      return await ctx.send('Please pass in all requirements :rolling_eyes:.')
    if isinstance(error, commands.MissingPermissions):
      return await ctx.send("You dont have all the requirements :angry:")

    if isinstance(error, commands.errors.CommandOnCooldown):  
            # isinstance is used to compare 2 thing. If they are the same it returns True in this case were comparing if the error is equal to the other error
      return await ctx.send('The command **{}** is still on cooldown for {:.2f}'.format(ctx.command.name, error.retry_after))


import logging

logger = logging.getLogger('discord')
logger.setLevel(logging.INFO)
handler = logging.FileHandler(
    filename='discord.log', encoding='utf-8', mode='w')
handler.setFormatter(
    logging.Formatter('%(asctime)s:%(levelname)s:%(name)s: %(message)s'))
logger.addHandler(handler)


token = os.environ.get("DISCORD_BOT_SECRET")
bot.run(token)  # Starts the bot