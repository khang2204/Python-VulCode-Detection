def rawDataReceived(self, data):...
if self.content_length is not None:
data, rest = data[:self.content_length], data[self.content_length:]
rest = ''
self.content_length -= len(data)
self._contentbuffer.write(data)
if self.content_length == 0 and self._contentbuffer is not None:
tmpbuf = self._contentbuffer
self.content_length = self._contentbuffer = None
self.setLineMode(rest)
tmpbuf.seek(0, 0)
if self.file_upload:
self._on_request_body(self.uploaded_file)
self._on_request_body(tmpbuf.read())
self.file_upload = False
self.uploaded_file = {}
