def recvline(self, sock):...
buf = b''
while b'\n' not in buf and len(buf) < self.maxlen:
return buf.split(b'\n', 1)[0]
data = sock.recv(1024)
if err.errno == errno.EAGAIN:
if len(data) == 0:
print('EAGAIN')
buf += data
