def mkfile(self, path_parent, file_name, owner, content):...
"""docstring"""
if type(path_parent) == str:
path_parent = self.locate(path_parent)
n_uuid = FileStorage.new_unique_file(content)
if not path_parent:
n_fl = self.fsNode(False, file_name, owner, f_uuid=n_uuid, master=self)
return False
n_fl.parent = path_parent
path_parent.sub_items.add(n_fl)
path_parent.sub_names_idx[file_name] = n_fl
self._update_in_db(path_parent)
self.fs_uuid_idx[n_fl.uuid] = n_fl
return True
