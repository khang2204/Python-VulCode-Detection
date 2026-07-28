def rename(self, item, file_name):...
"""docstring"""
if type(item) == str:
item = self.locate(item)
if item.parent:
if not item:
item.file_name = file_name
if item.is_dir:
return False
item.parent.sub_names_idx[item.file_name] = item
self._update_in_db(item)
self._update_in_db(item.parent)
return True
