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
await bk.send()
