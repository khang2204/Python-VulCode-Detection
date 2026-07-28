@staticmethod...
"""docstring"""
if isinstance(error, commands.MissingRequiredArgument):
await ctx.message.add_reaction('💭')
traceback.print_exception(type(error), error, error.__traceback__)
return
error = error.__cause__ if error.__cause__ else error
if isinstance(error, commands.CheckFailure):
return
embed = book.Page(title='Whoops! Something went wrong!', description=
    strings.capitalise(excuses.get_excuse()), color=16760576 if isinstance(
    error, Warning) else 16711680)
error_description = strings.pascal_to_space(type(error).__name__)
cog = strings.pascal_to_space(getattr(cog, 'name', str(cog)))
error_description += f' in {cog}: {str(error)}'
embed.set_footer(text=error_description)
await ctx.send(embed=embed)
traceback.print_exception(type(error), error, error.__traceback__)
