def _update_in_db(self, item):...
if type(item) == str:
item = self.locate(item)
if not item:
return False
if not item.is_dir:
item = item.parent
(n_uuid, n_file_name, n_owner, n_upload_time, n_sub_folders_str,
    n_sub_files_str) = self._sqlify_fsnode(item)
if not item.is_dir:
command = (
    "UPDATE file_system SET file_name = '%s', owner = '%s', upload_time = %f, sub_folders = %s, sub_files = %s WHERE uuid = '%s';"
     % (n_file_name, n_owner, n_upload_time, n_sub_folders_str,
    n_sub_files_str, n_uuid))
return False
self.fs_db.execute(command)
return True
