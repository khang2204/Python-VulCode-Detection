def tx_file(self, path):...
sz = os.path.getsize(path)
mime = mimetypes.guess_type(path)[0]
header = (
    'HTTP/1.1 200 OK\r\nConnection: Keep-Alive\r\nContent-Type: {}\r\nContent-Length: {}\r\n\r\n'
    .format(mime, sz).encode('utf-8'))
if self.ok:
self.s.send(header)
while self.ok:
buf = f.read(4096)
if not buf:
self.s.send(buf)
