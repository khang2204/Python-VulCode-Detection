@commands.command(pass_context=True, name='sr', hidden=True)...
"""docstring"""
author = ctx.message.author
if self.bot.helpers_role not in author.roles and self.bot.staff_role not in author.roles and self.bot.verified_role not in author.roles and self.bot.trusted_role not in author.roles:
msg = (
    '{0} You cannot used this command at this time. Please ask individual staff members if you need help.'
    .format(author.mention))
await self.bot.delete_message(ctx.message)
await self.bot.say(msg)
msg = '❗️ **Assistance requested**: {0} by {1} | {2}#{3} @here'.format(ctx.
    message.channel.mention, author.mention, author.name, ctx.message.
    author.discriminator)
return
if msg_request != '':
embed = discord.Embed(color=discord.Color.gold())
await self.bot.send_message(self.bot.mods_channel, msg, embed=embed if 
    msg_request != '' else None)
embed.description = msg_request
await self.bot.send_message(author,
    '✅ Online staff has been notified of your request in {0}.'.format(ctx.
    message.channel.mention), embed=embed if msg_request != '' else None)
