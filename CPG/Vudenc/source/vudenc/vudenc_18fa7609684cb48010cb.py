def do_GET(self):...
path = self.path
if path.startswith('/chromium/src/+/master'):
path = path[len('/chromium/src/+/master'):]
full_path = os.path.realpath(os.path.join(self.server.top_level, path[1:]))
if not full_path.startswith(self.server.top_level):
self._DoUnknown()
if path in ('/base.css', '/doc.css', '/prettify.css'):
self._DoCSS(path[1:])
if not os.path.exists(full_path):
self._DoNotFound()
if path.lower().endswith('.md'):
self._DoMD(path)
if os.path.exists(full_path + '/README.md'):
self._DoMD(path + '/README.md')
if path.lower().endswith('.png'):
self._DoImage(full_path, 'image/png')
if path.lower().endswith('.jpg'):
self._DoImage(full_path, 'image/jpeg')
if os.path.isdir(full_path):
self._DoDirListing(full_path)
if os.path.exists(full_path):
self._DoRawSourceFile(full_path)
self._DoUnknown()
