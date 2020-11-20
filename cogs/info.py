import discord
from discord.ext import commands


class Info(commands.Cog, name = "Information Commands"):
    '''Information About The Bot And Sever etc.'''


    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def guildcount(self, ctx):
        """How many guilds."""
        await ctx.send(f"I'm in {len(self.bot.guilds)} servers!")


    @commands.command(aliases=["mc", "members"])
    async def member_count(self, ctx):
        """How many members"""
        a = ctx.guild.member_count
        b = discord.Embed(
            title=f"Members in {ctx.guild.name}",
            description=f'There are {a} members in this server.',
            color=discord.Color((0xffff00)))
        await ctx.send(embed=b)

    class MemberRoles(commands.MemberConverter):
        async def convert(self, ctx, argument):
            member = await super().convert(ctx, argument)
            return [role.name
                    for role in member.roles[1:]]  # Remove everyone role!


    @commands.command()
    async def roles(self, ctx, *, member: MemberRoles):
        """Tells you a member's roles."""
        await ctx.send('I see the following roles: ' + ', '.join(member))


    # avater command
    @commands.command()
    async def avatar(self,
            ctx, *,
            member: discord.Member = None):  # set the member object to None
        """Avatar of a user"""
        if not member:  # if member is no mentioned
            member = ctx.message.author  # set member as the author
        userAvatar = member.avatar_url
        e = discord.Embed(
            title=f'{member.name}\'s avatar.', colour=discord.Colour((0xffff00)))
        e.set_image(url=f'{userAvatar}')
        await ctx.send(embed=e)


    @commands.command(aliases=["whois"])
    async def userinfo(self, ctx, member: discord.Member = None):
        """Info about a person"""
        if not member:  # if member is no mentioned
            member = ctx.message.author  # set member as the author
        roles = [role for role in member.roles]
        embed = discord.Embed(
            colour=discord.Colour.purple(),
            timestamp=ctx.message.created_at,
            title=f"User Info - {member}")
        embed.set_thumbnail(url=member.avatar_url)
        embed.set_footer(text=f"Requested by {ctx.author}")

        embed.add_field(name="ID:", value=member.id)
        embed.add_field(name="Display Name:", value=member.display_name)

        embed.add_field(
            name="Created Account On:",
            value=member.created_at.strftime("%a, %#d %B %Y, %I:%M %p UTC"))
        embed.add_field(
            name="Joined Server On:",
            value=member.joined_at.strftime("%a, %#d %B %Y, %I:%M %p UTC"))

        embed.add_field(
            name="Roles:", value="".join([role.mention for role in roles]))
        embed.add_field(name="Highest Role:", value=member.top_role.mention)

        await ctx.send(embed=embed)

def setup(bot):
    bot.add_cog(Info(bot))