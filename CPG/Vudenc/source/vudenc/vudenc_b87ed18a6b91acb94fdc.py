def run(self, edit):...
self.errors = []
oldest_known_filename = self.find_oldest_node(self.view.file_name())
self.tree = Node(oldest_known_filename)
self.build_node_tree('ROOT -> ' + oldest_known_filename)
render = ''
for pre, fill, node in RenderTree(self.tree):
render += '%s %s' % (pre, node.name) + '\n'
window = self.view.window()
window.focus_group(0)
new_view = self.view.window().new_file()
new_view.run_command('insert_snippet', {'contents': render})
new_view.run_command('insert_snippet', {'contents': '\n'.join(self.errors)})
