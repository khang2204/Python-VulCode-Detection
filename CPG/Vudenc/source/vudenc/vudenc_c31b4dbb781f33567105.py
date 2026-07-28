def copy(self, source, target_parent, new_owner=None):...
"""docstring"""
if type(source) == str:
source = self.locate(source)
if type(target_parent) == str:
target_parent = self.locate(target_parent)
if not source or not target_parent:
return False
target = copy.deepcopy(source)
target.parent = target_parent
target_parent.sub_items.add(target)
target_parent.sub_names_idx[target.file_name] = target
self._copy_recursive(target, target_parent, new_owner)
self._update_in_db(target_parent)
return True
