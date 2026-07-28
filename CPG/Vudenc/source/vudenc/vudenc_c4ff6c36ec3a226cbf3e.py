def inspect(self):...
"""docstring"""
if self._inspect:
return self._inspect
self._inspect = {}
for filename in self.files:
if filename is MEMORY:
return self._inspect
self._inspect[':memory:'] = {'hash': '000', 'file': ':memory:', 'size': 0,
    'views': {}, 'tables': {}}
path = Path(filename)
name = path.stem
if name in self._inspect:
self.prepare_connection(conn)
if e.args[0] == 'no such module: VirtualSpatialIndex':
self._inspect[name] = {'hash': inspect_hash(path), 'file': str(path),
    'size': path.stat().st_size, 'views': inspect_views(conn), 'tables':
    inspect_tables(conn, (self.metadata('databases') or {}).get(name, {}))}
