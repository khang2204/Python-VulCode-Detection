def add_separator(view):...
"""docstring"""
if not has_meta(view):
view.run_command('move_to', {'to': 'eof'})
view.run_command('insert_snippet', {'contents': '\n\n' + meta_separator()})
view.run_command('move_to', {'to': 'bof'})
