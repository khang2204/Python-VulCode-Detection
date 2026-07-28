def move(self, source, target_parent):...
if type(source) == str:
source = self.locate(source)
if type(target_parent) == str:
target_parent = self.locate(target_parent)
if not source or not target_parent:
return False
par = source.parent
par.sub_items.remove(source)
source.parent = target_parent
target_parent.sub_items.add(source)
target_parent.sub_names_idx[source.file_name] = source
self._update_in_db(par)
self._update_in_db(target_parent)
return
