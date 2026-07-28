"""
Utilities for commands. These inject various pieces of functionality into the
existing discord.py stuff.
"""
import abc
import traceback
import typing
import discord.ext.commands as commands
from neko import excuses, book, strings
__all__ = ['NekoCommand', 'NekoGroup', 'command', 'group']
"""Functionality to be inherited by a command or group type."""
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
"""
    Implementation of a command.
    """
"""
    Implementation of a command group.
    """
def command(self, **kwargs):...
kwargs.setdefault('cls', NekoCommand)
return super().command(**kwargs)
