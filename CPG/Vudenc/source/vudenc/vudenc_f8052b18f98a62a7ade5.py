def load_sqlfs(self, db=Database):...
self.fs_db = db
for item in self.fs_db.execute(
uuid_, file_name, owner, upload_time, sub_folders, sub_files = item
for uuid_ in self.fs_uuid_idx:
n_sub_files = set()
item = self.fs_uuid_idx[uuid_]
def iterate_fsnode(node):...
for fil_idx in sub_files:
if not item.is_dir:
for item in node.sub_items:
s_uuid = fil_idx[0]
n_sub_folders = set()
for n_sub in item.sub_files:
if item.parent:
return
s_file_name = fil_idx[1]
for fol_idx in sub_folders:
item.sub_items.add(n_sub)
for n_sub_uuid in item.sub_folders:
item.parent = node
s_owner = fil_idx[2]
n_sub_folders.add(fol_idx)
fold_elem = self.fsNode(True, file_name, owner, uuid_, upload_time,
    n_sub_folders, n_sub_files, master=self)
item.sub_names_idx[n_sub.file_name] = n_sub
n_sub = self.fs_uuid_idx[n_sub_uuid]
iterate_fsnode(item)
s_upload_time = float(fil_idx[3])
s_upload_time = get_current_time()
s_f_uuid = fil_idx[4]
self.fs_uuid_idx[uuid_] = fold_elem
item.sub_items.add(n_sub)
s_file = self.fsNode(False, s_file_name, s_owner, s_uuid, s_upload_time,
    f_uuid=s_f_uuid, master=self)
item.sub_names_idx[n_sub.file_name] = n_sub
n_sub_files.add(s_file)
self.fs_uuid_idx[s_uuid] = s_file
