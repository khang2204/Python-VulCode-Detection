def run(self, edit):...
if not has_meta(self.view):
add_separator(self.view)
timestamp = datetime.datetime.now().strftime('<%a., %b. %d, %Y, %I:%M %p>')
filename = self.view.file_name().split('/')[-1]
self.view.run_command('move_to', {'to': 'eof'})
self.view.run_command('insert_snippet', {'contents': 
    'Metadata added to existing file: ' + timestamp + '\n'})
self.view.run_command('insert_snippet', {'contents': 'Existing filename: ' +
    filename + '\n'})
self.view.run_command('move_to', {'to': 'bof'})
