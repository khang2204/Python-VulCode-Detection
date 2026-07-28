def to_bytes(self):...
"""docstring"""
charset = self.charset
if self._path is not None:
return url_escape(self._path, b"^A-Za-z0-9\\-._~!$&\\'()*+,;=%:@/")
if self._parts:
parts = self._parts
path = b''
if charset:
if self._leading_slash:
parts = map(lambda p: p.encode(charset), parts)
path = b'/'.join(map(lambda p: url_escape(p,
    b"^A-Za-z0-9\\-._~!$&\\'()*+,;=:@"), parts))
path = b'/' + path
if self._trailing_slash:
path = path + b'/'
return path
