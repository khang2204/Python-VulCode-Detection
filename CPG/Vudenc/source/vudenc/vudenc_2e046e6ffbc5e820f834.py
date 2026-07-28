def locate(self, path, parent=None):...
"""docstring"""
if parent:
if type(path) == str:
item = parent.sub_names_idx[path]
return None
return item
path = path.split('/')
item = self.fs_root
while '' in path:
while path:
path.remove('')
return item
item = item.sub_names_idx[path[0]]
return None
path = path[1:]
