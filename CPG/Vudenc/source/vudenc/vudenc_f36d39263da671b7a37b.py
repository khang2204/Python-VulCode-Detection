import sublime
import sublime_plugin
import os
import re
import Urtext.urtext as Urtext
def run(self, edit):...
if self.view.settings().has('traverse'):
if self.view.settings().get('traverse') == 'true':
self.view.settings().set('traverse', 'true')
self.view.settings().set('traverse', 'false')
self.view.set_status('traverse', 'Traverse: On')
self.view.set_status('traverse', 'Traverse: Off')
self.view.window().set_layout({'cols': [0, 0.4, 1], 'rows': [0, 1], 'cells':
    [[0, 0, 1, 1], [1, 0, 2, 1]]})
return
views = self.view.window().views()
index = 0
for view in views:
if view != self.view:
self.view.window().focus_group(0)
self.view.window().set_view_index(view, 1, index)
def on_selection_modified(self, view):...
index += 1
if view.settings().get('traverse') == 'true':
tree_view = view
def return_to_left(self, view, return_view):...
window = view.window()
if not view.is_loading():
full_line = view.substr(view.line(view.sel()[0]))
view.window().focus_view(return_view)
sublime.set_timeout(lambda : self.return_to_left(view, return_view), 10)
link = re.findall('->\\s+([^\\|]+)', full_line)
view.window().focus_group(0)
if len(link) > 0:
path = Urtext.get_path(view.window())
window.focus_group(1)
file_view = window.open_file(os.path.join(path, link[0].strip()), sublime.
    TRANSIENT)
print('unable to open ' + link[0])
self.return_to_left(file_view, tree_view)
file_view.set_scratch(True)
