def mkdir(self, path_parent, file_name, owner):...
"""docstring"""
if type(path_parent) == str:
path_parent = self.locate(path_parent)
n_fl = self.fsNode(True, file_name, owner, master=self)
if not path_parent:
n_fl.parent = path_parent
return False
path_parent.sub_items.add(n_fl)
path_parent.sub_names_idx[file_name] = n_fl
self._update_in_db(path_parent)
self._insert_in_db(n_fl)
self.fs_uuid_idx[n_fl.uuid] = n_fl
return True
