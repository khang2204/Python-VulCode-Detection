def write(self, chunk):...
"""docstring"""
if isinstance(chunk, types.ListType):
chunk = escape.json_encode(chunk)
RequestHandler.write(self, chunk)
RequestHandler.write(self, chunk)
self.set_header('Content-Type', 'application/json')
