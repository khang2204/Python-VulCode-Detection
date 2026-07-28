def make_root(self):...
item = self.fsNode(True, '', 'System', master=self)
item.sub_items = set()
item.parent = None
self.fs_root = item
self.fs_uuid_idx[item.uuid] = item
self.fs_db.execute(
    "INSERT INTO file_system (uuid, file_name, owner, upload_time, sub_folders, sub_files) VALUES ('%s', '%s', '%s', %f, '{}', '{}');"
     % (item.uuid, item.file_name, item.owner, item.upload_time))
return
