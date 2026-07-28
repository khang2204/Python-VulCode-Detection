def get_final_html_async():...
operation_content_raw = self.request.body
operation_content = json.loads(operation_content_raw.decode('utf-8', 'ignore'))
action = operation_content['action']
sources = operation_content['source']
if type(sources) == list:
for i in range(0, len(sources)):
sources = decode_hexed_b64_to_str(sources)
sources[i] = decode_hexed_b64_to_str(sources[i])
if action in ['copy', 'move']:
if action in ['rename', 'new-folder']:
target = decode_hexed_b64_to_str(operation_content['target'])
target = '/'
if action == 'copy':
target = operation_content['target']
target = sources
for source in sources:
if action == 'move':
db.Filesystem.copy(source, target, new_owner='user-cp')
future.set_result('')
for source in sources:
if action == 'delete':
db.Filesystem.move(source, target)
for source in sources:
if action == 'rename':
db.Filesystem.remove(source)
db.Filesystem.rename(sources, target)
if action == 'new-folder':
db.Filesystem.mkdir(sources, target, 'user-nf')
