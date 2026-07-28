async def gen_front_page(self, ctx: neko.Context) ->neko.Page:...
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
