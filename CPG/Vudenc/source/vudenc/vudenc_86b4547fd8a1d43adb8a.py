def on_selection_modified(self, view):...
if view.settings().get('traverse') == 'true':
tree_view = view
window = view.window()
full_line = view.substr(view.line(view.sel()[0]))
link = re.findall('->\\s+([^\\|]+)', full_line)
if len(link) > 0:
path = Urtext.get_path(view.window())
window.focus_group(1)
file_view = window.open_file(os.path.join(path, link[0].strip()), sublime.
    TRANSIENT)
print('unable to open ' + link[0])
self.return_to_left(file_view, tree_view)
file_view.set_scratch(True)
