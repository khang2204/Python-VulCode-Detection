def submit(self, submit_id, config):...
"""docstring"""
ret = []
submit = db.view_submit(submit_id)
for entry in config['file_selection']:
info = copy.deepcopy(config['global'])
return ret
info.update(entry)
options = copy.deepcopy(config['global']['options'])
options.update(entry.get('per_file_options', {}))
kw = {'package': info.get('package'), 'timeout': info.get('timeout', 120),
    'priority': info.get('priority'), 'custom': info.get('custom'), 'owner':
    info.get('owner'), 'tags': info.get('tags'), 'memory': info.get(
    'memory'), 'enforce_timeout': options.get('enforce-timeout'), 'machine':
    info.get('machine'), 'platform': info.get('platform'), 'options': self.
    translate_options(info, options), 'submit_id': submit_id}
if entry['type'] == 'url':
ret.append(db.add_url(url=info['filename'], **kw))
path_dest = Folders.create_temp()
if not info['extrpath']:
path = os.path.join(submit.tmp_path, os.path.basename(info['filename']))
if len(info['extrpath']) == 1:
filepath = Files.copy(path, path_dest=path_dest)
arcpath = os.path.join(submit.tmp_path, os.path.basename(info['arcname']))
arcpath = os.path.join(submit.tmp_path, os.path.basename(info['arcname']))
ret.append(db.add_path(file_path=filepath, **kw))
if not os.path.exists(arcpath):
if not os.path.exists(arcpath):
submit.data['errors'].append('Unable to find parent archive file: %s' % os.
    path.basename(info['arcname']))
arc = sflock.zipify(sflock.unpack(info['arcname'], contents=open(arcpath,
    'rb').read()))
submit.data['errors'].append('Unable to find parent archive file: %s' % os.
    path.basename(info['arcname']))
content = sflock.unpack(arcpath).read(info['extrpath'][:-1])
arcpath = Files.temp_named_put(arc, os.path.basename(info['arcname']))
subarc = sflock.unpack(info['extrpath'][-2], contents=content)
ret.append(db.add_archive(file_path=arcpath, filename=info['filename'], **kw))
arcpath = Files.temp_named_put(sflock.zipify(subarc), os.path.basename(info
    ['extrpath'][-2]))
ret.append(db.add_archive(file_path=arcpath, filename=info['filename'], **kw))
