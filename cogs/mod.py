import discord
from discord.ext import commands



'''Module for moderator commands.'''


class Mod(commands.Cog, name = "Moderation Commands"):

    def __init__(self, bot):
        self.bot = bot

    def are_overwrites_empty(self, overwrites):
        """There is currently no cleaner way to check if a
        PermissionOverwrite object is empty"""
        original = [p for p in iter(overwrites)]
        empty = [p for p in iter(discord.PermissionOverwrite())]
        return original == empty

    @commands.command(pass_context=True)
    async def kick(self, ctx, user: discord.User, *, reason="nice"):
        """Kicks a user (if you have the permission)."""
        if user:
            try:
                await user.kick(reason=reason)
                return_msg = "Kicked user `{}`".format(user.mention)
                if reason:
                    return_msg += " for reason `{}`".format(reason)
                return_msg += "."
                await ctx.message.edit(content=self.bot.bot_prefix + return_msg)
            except discord.Forbidden:
                await ctx.message.edit(content=self.bot.bot_prefix + 'Could not kick user. Not enough permissions.')
        else:
            return await ctx.message.edit(content=self.bot.bot_prefix + 'Could not find user.')


    # TODO: Add reason with ban
    @commands.command(aliases=['hban'], pass_context=True)     
    async def hackban(self, ctx, user_id: int):
        """Bans a user outside of the server."""
        author = ctx.message.author
        guild = author.guild

        user = guild.get_member(user_id)
        if user is not None:
            return await ctx.invoke(self.ban, user=user)

        try:
            await self.bot.http.ban(user_id, guild.id, 0)
            await ctx.message.edit(self.bot.bot_prefix + 'Banned user: %s' % user_id)
        except discord.NotFound:
            await ctx.message.edit(self.bot.bot_prefix + 'Could not find user. '
                               'Invalid user ID was provided.')
        except discord.errors.Forbidden:
            await ctx.message.edit(self.bot.bot_prefix + 'Could not ban user. Not enough permissions.')


    @commands.command(pass_context=True)
    async def ban(self, ctx, user: discord.User, *, reason="nice"):
        """Bans a user (if you have the permission)."""
        if user:
            try:
                await user.ban(reason=reason)
                return_msg = "Banned user `{}`".format(user.mention)
                if reason:
                    return_msg += " for reason `{}`".format(reason)
                return_msg += "."
                await ctx.message.edit(content=self.bot.bot_prefix + return_msg)
            except discord.Forbidden:
                await ctx.message.edit(content=self.bot.bot_prefix + 'Could not ban user. Not enough permissions.')
        else:
            return await ctx.message.edit(content=self.bot.bot_prefix + 'Could not find user.')

    @commands.command(aliases=['sban'], pass_context=True)
    async def softban(self, ctx, user: discord.User, *, reason="nice"):
        """Bans and unbans a user (if you have the permission)."""

        if user:
            try:
                await user.ban(reason=reason)
                await ctx.guild.unban(user)
                return_msg = "Banned and unbanned user `{}`".format(user.mention)
                if reason:
                    return_msg += " for reason `{}`".format(reason)
                return_msg += "."
                await ctx.message.edit(content=self.bot.bot_prefix + return_msg)
            except discord.Forbidden:
                await ctx.message.edit(content=self.bot.bot_prefix + 'Could not softban user. Not enough permissions.')
        else:
            return await ctx.message.edit(content=self.bot.bot_prefix + 'Could not find user.')



    @commands.has_permissions(manage_messages=True)
    @commands.command(aliases=['p'], pass_context=True, no_pm=True)
    async def purge(self, ctx, msgs: int, members="everyone", *, txt=None):
        """Purge last n messages or nmessages with a word. Requires Manage Messages permission. [p]help purge for more info.
        
        Ex:
        
        [p]purge 20 - deletes the last 20 messages in a channel sent by anyone.
        [p]purge 20 everyone stuff - deletes any messages in the last 20 messages that contain the word 'stuff'.
        [p]purge 20 @appu1232 - deletes any messages in the last 20 messages that were sent by appu1232.
        [p]purge 20 "@appu1232, LyricLy, 435254873976547426" hello - deletes any messages in the last 20 messages that were sent by appu1232, LyricLy or thecommondude that contain the word 'stuff'.
        """
        await ctx.message.delete()
        member_object_list = []
        if members != "everyone":
            member_list = [x.strip() for x in members.split(",")]
            for member in member_list:
                if "@" in member:
                    member = member[3 if "!" in member else 2:-1]
                if member.isdigit():
                    member_object = ctx.guild.get_member(int(member))
                else:
                    member_object = ctx.guild.get_member_named(member)
                if not member_object:
                    return await ctx.send(self.bot.bot_prefix + "Invalid user.")
                else:
                    member_object_list.append(member_object)

        if msgs < 10000:
            async for message in ctx.message.channel.history(limit=msgs):
                try:
                    if txt:
                        if not txt.lower() in message.content.lower():
                            continue
                    if member_object_list:
                        if not message.author in member_object_list:
                            continue

                    await message.delete()
                except discord.Forbidden:
                    await ctx.send(self.bot.bot_prefix + "You do not have permission to delete other users' messages. Use {}delete instead to delete your own messages.".format(self.bot.cmd_prefix))
        else:
            await ctx.send(self.bot.bot_prefix + 'Too many messages to delete. Enter a number < 10000')






def setup(bot):
    bot.add_cog(Mod(bot))