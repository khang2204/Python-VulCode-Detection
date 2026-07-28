def _sqlify_fsnode(self, item):...
n_uuid = item.uuid
n_file_name = item.file_name
n_owner = item.owner
n_upload_time = item.upload_time
n_sub_folders = list()
n_sub_files = list()
for i_sub in item.sub_items:
if i_sub.is_dir:
n_sub_folders_str = "'{" + ', '.join(i for i in n_sub_folders) + "}'"
n_sub_folders.append('"%s"' % i_sub.uuid)
s_attr = '{%s, %s, %s, %s, %s}' % ('"%s"' % i_sub.uuid, '"%s"' % i_sub.
    file_name, '"%s"' % i_sub.owner, '"%f"' % i_sub.upload_time, '"%s"' %
    i_sub.f_uuid)
n_sub_files_str = "'{" + ', '.join(i for i in n_sub_files) + "}'"
n_sub_files.append(s_attr)
return n_uuid, n_file_name, n_owner, n_upload_time, n_sub_folders_str, n_sub_files_str
