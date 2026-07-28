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
index += 1
