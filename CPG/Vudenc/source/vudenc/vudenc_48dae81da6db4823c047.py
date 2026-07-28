@staticmethod...
"""docstring"""
name = cmd.name
if not cmd.enabled:
name = f'~~{name}~~'
if cmd.hidden:
name = f'*{name}*'
if isinstance(cmd, neko.GroupMixin) and getattr(cmd, 'commands'):
name = f'{name}\\*'
if is_full:
name = f'{cmd.full_parent_name} {name}'.strip()
return name
