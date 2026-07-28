async def gen_spec_page(self, ctx: neko.Context, cmd: neko.NekoCommand...
"""docstring"""
pfx = self.bot.command_prefix
fqn = cmd.qualified_name
brief = f"""**{fqn}**
{cmd.brief if cmd.brief else ''}"""
doc_str = neko.remove_single_lines(cmd.help)
usages = cmd.usage.split('|') if cmd.usage else ''
usages = map(lambda u: f'• {pfx}{fqn} {u}', usages)
usages = '\n'.join(sorted(usages))
aliases = sorted(cmd.aliases)
if cmd.parent:
super_command = self.format_command_name(cmd.parent)
super_command = None
can_run = await cmd.can_run(ctx)
if isinstance(cmd, neko.GroupMixin):
def sub_cmd_map(c):...
sub_commands = []
c = self.format_command_name(c)
if getattr(cmd, 'enabled', False) and can_run:
c = f'• {c}'
color = default_color
if not can_run:
return c
page = neko.Page(title=f'Command documentation', description=brief, color=color
    )
color = 0
color = 16711680
if doc_str:
page.add_field(name='Description', value=doc_str, inline=False)
if usages:
page.add_field(name='Usage', value=usages, inline=False)
if aliases:
page.add_field(name='Aliases', value=', '.join(aliases))
if sub_commands:
page.add_field(name='Child commands', value='\n'.join(sub_commands))
if super_command:
page.add_field(name='Parent command', value=super_command)
if not can_run and cmd.enabled:
page.set_footer(text='You do not hve permission to run the command here.')
if not cmd.enabled:
return page
page.set_footer(text='This command has been disabled globally.')
