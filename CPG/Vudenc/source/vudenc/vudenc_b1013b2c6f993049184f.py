def run(self, edit):...
self.path = Urtext.get_path(self.view.window())
self.errors = []
self.visited_files = []
self.backward_visited_files = []
self.tree = Node(self.view.file_name())
root_file = Urtext.UrtextFile(os.path.join(self.path, self.view.file_name()))
root_meta = NodeMetadata(os.path.join(self.path, root_file.filename))
self.build_node_tree(root_meta.get_tag('title')[0] + ' -> ' + root_file.
    filename)
self.build_backward_node_tree(root_meta.get_tag('title')[0] + ' -> ' +
    root_file.filename)
window = self.view.window()
window.focus_group(0)
new_view = self.view.window().new_file()
render = ''
for pre, fill, node in RenderTree(self.backward_tree):
render += '%s%s' % (pre, node.name) + '\n'
render = render.replace('└', '┌')
render = render.split('\n')
render = render[1:]
render_upside_down = ''
for index in range(len(render)):
render_upside_down += render[len(render) - 1 - index] + '\n'
render_upside_down = ''.join(render_upside_down)
new_view.run_command('insert_snippet', {'contents': render_upside_down})
new_view.run_command('insert_snippet', {'contents': '\n'.join(self.errors)})
render = ''
for pre, fill, node in RenderTree(self.tree):
render += '%s%s' % (pre, node.name) + '\n'
new_view.run_command('insert_snippet', {'contents': render})
new_view.run_command('insert_snippet', {'contents': '\n'.join(self.errors)})
new_view.set_scratch(True)
