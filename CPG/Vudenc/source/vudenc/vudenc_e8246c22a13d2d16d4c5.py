@commands.group(aliases=['elite', 'ed'])...
"""docstring"""
if ctx.invoked_subcommand is None:
await ctx.send(
    f'Invalid command passed. Try "{self.bot.command_prefix[0]}help eddb"')
