def add_created_timestamp(view, timestamp):...
"""docstring"""
filename = view.file_name().split('/')[-1]
text_timestamp = timestamp.strftime('<%a., %b. %d, %Y, %I:%M %p>')
view.run_command('move_to', {'to': 'eof'})
view.run_command('insert_snippet', {'contents': '\n\n' + meta_separator() +
    'Created ' + text_timestamp + '\n'})
view.run_command('move_to', {'to': 'bof'})
