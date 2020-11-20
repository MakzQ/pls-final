import discord
from discord.ext import commands
import time


class Utils(commands.Cog, name = "Utility Commands"):
    '''Utilites For The Bot, Not Server'''
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def where(self, ctx):
      """Channel and Server"""
      e = discord.Embed(title='Location', colour=discord.Colour.red())
      e.add_field(name='Server:', value=f'{ctx.guild.name}')
      e.add_field(name='Channel:', value=f'{ctx.channel.mention}')

      await ctx.send(embed=e)

    @commands.command()
    async def invite(self, ctx):

      e = discord.Embed(title='Invite', colour=discord.Colour.red())
      e.add_field(
          name='Link:',
          value=
          "https://discord.com/api/oauth2/authorize?client_id=764127561844129793&permissions=8&scope=bot"
      )
      await ctx.send(embed=e)

    @commands.command(aliases = ['ping'])
    async def status(self, ctx):
      '''The bot\'s status'''
      before = time.monotonic()
      message = await ctx.send(':ping_pong: returning!')
      ping = (time.monotonic() - before) * 1000
      await message.edit(content=f":ping_pong: ...  | Pong! Returned in  `{int(ping)}ms`")


def setup(bot):
    bot.add_cog(Utils(bot))