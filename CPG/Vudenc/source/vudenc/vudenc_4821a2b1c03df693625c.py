def pre(self, submit_type, data):...
"""docstring"""
if submit_type not in ('strings', 'files'):
log.error("Bad parameter '%s' for submit_type", submit_type)
path_tmp = Folders.create_temp()
return False
submit_data = {'data': [], 'errors': []}
if submit_type == 'strings':
for line in data:
if submit_type == 'files':
self._handle_string(submit_data, path_tmp, line)
for entry in data:
return Database().add_submit(path_tmp, submit_type, submit_data)
filename = Storage.get_filename_from_path(entry['name'])
filepath = Files.create(path_tmp, filename, entry['data'])
submit_data['data'].append({'type': 'file', 'data': filepath})
