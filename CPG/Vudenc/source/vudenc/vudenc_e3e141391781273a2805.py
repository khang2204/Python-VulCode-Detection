def listdir(self, path):...
"""docstring"""
if type(path) == str:
path = self.locate(path)
dirs = list()
if not path:
for item in path.sub_items:
return []
attrib = dict()
return dirs
attrib['file-name'] = item.file_name
attrib['file-size'] = 0 if item.is_dir else FileStorage.st_uuid_idx[item.f_uuid
    ].size
attrib['is-dir'] = item.is_dir
attrib['owner'] = item.owner
attrib['upload-time'] = item.upload_time
dirs.append(attrib)
