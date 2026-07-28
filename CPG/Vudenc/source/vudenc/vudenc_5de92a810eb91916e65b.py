def _insert_in_db(self, item):...
"""docstring"""
if not item.is_dir:
return False
(n_uuid, n_file_name, n_owner, n_upload_time, n_sub_folders_str,
    n_sub_files_str) = self._sqlify_fsnode(item)
self.fs_db.execute(
    "INSERT INTO file_system (uuid, file_name, owner, upload_time, sub_folders, sub_files) VALUES ('%s', '%s', '%s', %f, %s, %s);"
     % (n_uuid, n_file_name, n_owner, n_upload_time, n_sub_folders_str,
    n_sub_files_str))
return
