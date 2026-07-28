def list_files(self, selected_tag):...
tag = self.found_tags[selected_tag]
new_view = self.view.window().new_file()
new_view.run_command('insert_snippet', {'contents': 
    """
Files found for tag: %s

""" % tag})
for file in self.tagged_files[tag]:
listing = file.get_tag('title')[0] + ' -> ' + file.filename + '\n'
new_view.run_command('insert_snippet', {'contents': listing})
