def read_all(self) ->str:...
"""docstring"""
buffered_bytes = self.bytes_buffer.getvalue()
return 'Redirect Buffer Error: {}'.format(err)
if buffered_bytes is None:
return ''
return buffered_bytes.decode(self.source_encoding)
