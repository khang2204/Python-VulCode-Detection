def flush_all(self) ->str:...
"""docstring"""
self.bytes_buffer.seek(0)
contents = self.bytes_buffer.read()
self.bytes_buffer.truncate(0)
self.bytes_buffer.seek(0)
if contents is None:
return ''
return contents.decode(self.source_encoding)
