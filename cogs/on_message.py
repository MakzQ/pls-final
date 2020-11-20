import discord
from discord.ext import commands
import asyncio

class OnMessage(commands.Cog, name = "On_Message"):

    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_message(self, message):
      if self.bot.user == message.author:
        return

      if any((word in message.content.lower() for word in ('hmm', 'hm', 'hmmm', ':thinking:', 'think', 'thonk'))):
        await message.add_reaction("🤔")

      if any((word in message.content.lower() for word in ('<3', 'love', 'heart', ':heart:'))):
        await message.add_reaction("💖")


      if any((word in message.content.lower() for word in ('uwu', 'owo'))):
        await message.add_reaction("🚫")


      if any((word in message.content.lower() for word in ('noice', 'nice'))):
        await message.add_reaction("👍")




def setup(bot):
  bot.add_cog(OnMessage(bot))
