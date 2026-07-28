def _parse(self, name, *args):...
if self._parts is None:
charset = self.charset
if not args:
if self._path is not None:
return getattr(self, '_' + name)
setattr(self, '_' + name, args[0])
path = self._path
path = u'' if charset else b''
if charset:
path = url_unescape(b(path, charset)).decode(charset)
path = url_unescape(path)
slash = u'/'
slash = b'/'
self._path = None
if path.startswith(slash):
path = path[1:]
if path.endswith(slash):
self._leading_slash = True
path = path[:-1]
if path == '':
self._trailing_slash = True
self._parts = []
self._parts = path.split(slash)
