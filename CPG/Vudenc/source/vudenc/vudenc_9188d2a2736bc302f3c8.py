@web.authenticated...
cm = self.contents_manager
if cm.is_hidden(path) and not cm.allow_hidden:
self.log.info('Refusing to serve hidden file, via 404 Error')
path = path.strip('/')
if '/' in path:
_, name = path.rsplit('/', 1)
name = path
model = yield maybe_future(cm.get(path, type='file', content=include_body))
if self.get_argument('download', False):
self.set_attachment_header(name)
if name.lower().endswith('.ipynb'):
self.set_header('Content-Type', 'application/x-ipynb+json')
cur_mime = mimetypes.guess_type(name)[0]
if include_body:
if cur_mime == 'text/plain':
if model['format'] == 'base64':
self.set_header('Content-Type', 'text/plain; charset=UTF-8')
if cur_mime is not None:
b64_bytes = model['content'].encode('ascii')
if model['format'] == 'json':
self.set_header('Content-Type', cur_mime)
if model['format'] == 'base64':
self.write(decodebytes(b64_bytes))
self.write(json.dumps(model['content']))
self.write(model['content'])
self.set_header('Content-Type', 'application/octet-stream')
self.set_header('Content-Type', 'text/plain; charset=UTF-8')
self.flush()
