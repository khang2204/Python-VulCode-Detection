def _remove_recursive(self, item):...
"""docstring"""
for i_sub in item.sub_items:
self._remove_recursive(i_sub)
self.fs_db.execute("DELETE FROM file_system WHERE uuid = '%s';" % item.uuid)
return
