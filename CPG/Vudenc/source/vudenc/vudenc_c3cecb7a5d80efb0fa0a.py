"""
Implementation of a help command.
"""
import asyncio
import inspect
import random
import discord
import neko
__all__ = ['HelpCog', 'ActivityChangerCog', 'setup']
default_color = 2003199
"""Provides the inner methods with access to bot directly."""
permissions = (neko.Permissions.SEND_MESSAGES | neko.Permissions.
    ADD_REACTIONS | neko.Permissions.READ_MESSAGES | neko.Permissions.
    MANAGE_MESSAGES)
def __init__(self, bot: neko.NekoBot):...
"""docstring"""
self.bot = bot
@neko.command(name='rtfm', brief=...
"""docstring"""
bk = neko.Book(ctx)
command_to_page = {}
bk += await self.gen_front_page(ctx)
command_to_page[None] = 0
cmds = sorted(set(self.bot.walk_commands()), key=lambda c: c.qualified_name)
offset = len(bk)
for i, cmd in enumerate(cmds):
bk += await self.gen_spec_page(ctx, cmd)
page_index = command_to_page[query]
await ctx.send(f'I could not find a command called {query}!')
bk.index = page_index
command_to_page[cmd.qualified_name] = i + offset
async def gen_front_page(self, ctx: neko.Context) ->neko.Page:...
await bk.send()
"""docstring"""
desc = f'{neko.__copyright__} under the {neko.__license__} license.\n\n'
doc_str = inspect.getdoc(neko)
doc_str = inspect.cleandoc(doc_str if doc_str else '')
desc += neko.remove_single_lines(doc_str)
page = neko.Page(title=f'{neko.__title__} v{neko.__version__}', description
    =desc, color=default_color, url=neko.__repository__)
page.set_thumbnail(url=self.bot.user.avatar_url)
page.add_field(name='Repository', value=neko.__repository__)
is_bot_owner = await self.bot.is_owner(ctx.author)
cmds = sorted(self.bot.commands, key=lambda c: c.name)
cmds = [self.format_command_name(cmd) for cmd in cmds if is_bot_owner or 
    not cmd.hidden]
page.add_field(name='Available commands', value=', '.join(cmds), inline=False)
return page
