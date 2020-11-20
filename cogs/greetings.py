import discord
from discord.ext import commands

class Greetings(commands.Cog, name = 'Greeting Events'):
    '''Random Events For Greetings'''
    def __init__(self, bot):
        self.bot = bot
        self._last_member = None

    @commands.Cog.listener()
    async def on_member_join(self, member):
        guild = member.guild
        channel = discord.utils.find(lambda channel: 'welcome' in channel.name.lower(), guild.text_channels)
        msg = f'Welcome {member} to {guild}, have a great time and invite your friends!'
        channel.message.send(msg)
        if channel is None:
          return

    @commands.command()
    async def hello(self, ctx, *, member: discord.Member = None):
        """Says hello"""
        member = member or ctx.author
        if self._last_member is None or self._last_member.id != member.id:
            await ctx.send('Hello {0.name}~'.format(member))
        else:
            await ctx.send('Hello {0.name}... This feels familiar.'.format(member))
        self._last_member = member


def setup(bot):
    bot.add_cog(Greetings(bot))