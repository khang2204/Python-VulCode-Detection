def add_original_filename(view):...
"""docstring"""
filename = view.file_name().split('/')[-1]
view.run_command('move_to', {'to': 'eof'})
view.run_command('insert_snippet', {'contents': 'Original filename: ' +
    filename + '\n'})
view.run_command('move_to', {'to': 'bof'})
