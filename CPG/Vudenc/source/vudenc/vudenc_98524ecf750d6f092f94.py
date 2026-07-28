def run(self, edit):...
if not has_meta(self.view):
add_separator(self.view)
timestamp = datetime.datetime.now().strftime('<%a., %b. %d, %Y, %I:%M %p>')
self.view.run_command('move_to', {'to': 'eof'})
self.view.run_command('move_to', {'to': 'eof'})
self.view.run_command('insert_snippet', {'contents':
    '[ no existing metadata ]\n'})
self.view.run_command('insert_snippet', {'contents': 'Modified: ' +
    timestamp + '\n'})
self.view.run_command('move_to', {'to': 'bof'})
