import discord
import json
from discord.ext import commands
import typing


class Lockdown(commands.Cog, name = "Lockdown Command"):
    """
    Channel lockdown commands.
    """

    def __init__(self, bot):
        self.bot = bot
        self.states = {}

    @commands.command(aliases = ['lockdown'])
    @commands.guild_only()
    async def lock(ctx, *, target: typing.Union[discord.Role, discord.Member]):
      ow = ctx.channel.overwritea_for(target)
      ow.send_messages = False
      await ctx.channel.set_permissions(target, overwrite=ow)

    @commands.command()
    @commands.guild_only()
    async def unlock(ctx, *, target:typing.Union[discord.Role, discord.Member]):
      ow = ctx.channel.overwritea_for(target)
      ow.send_messages = True
      await ctx.channel.set_permissions(target, overwrite=ow) 



def setup(bot):
    bot.add_cog(Lockdown(bot))