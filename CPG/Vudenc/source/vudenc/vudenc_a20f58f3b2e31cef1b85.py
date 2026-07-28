def remove(self, path):...
"""docstring"""
if type(path) == str:
path = self.locate(path)
par = path.parent
if not path:
self._remove_recursive(path)
return False
if par:
par.sub_items.remove(path)
return True
self._update_in_db(par)
