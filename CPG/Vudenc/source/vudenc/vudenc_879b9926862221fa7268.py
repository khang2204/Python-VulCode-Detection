def _copy_recursive(self, item, target_par, new_owner):...
"""docstring"""
target_node = target_par.sub_names_idx[item.file_name]
for i_sub in item.sub_items:
i_sub.parent = item
item.uuid = get_new_uuid(None, self.fs_uuid_idx)
item.sub_names_idx[i_sub.file_name] = i_sub
self.fs_uuid_idx[item.uuid] = item
self._copy_recursive(i_sub, target_node, new_owner)
item.upload_time = get_current_time()
if new_owner:
item.owner = new_owner
if item.is_dir:
self._insert_in_db(item)
return
