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
os.system('cp "D:%s" "D:%s"' % (source, target))
future.set_result('')
for source in sources:
if action == 'delete':
os.system('mv "D:%s" "D:%s"' % (source, target))
for source in sources:
if action == 'rename':
os.system('rm "D:%s"' % source)
os.system('rename "D:%s" "%s"' % (sources, target))
if action == 'new-folder':
os.system('mkdir "D:%s%s"' % (sources, target))
