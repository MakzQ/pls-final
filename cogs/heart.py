import discord
from discord.ext import commands

class Hearts(commands.Cog, name = "heart"):

    def __init__(self, bot):
      self.bot = bot

    @commands.command()
    async def heart(self, ctx):
      await ctx.send(f':heart: :heartpulse: :heart_exclamation: :revolving_hearts:')
      await ctx.message.delete()


def setup(bot):
    bot.add_cog(Hearts(bot))