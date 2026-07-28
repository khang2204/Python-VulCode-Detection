@classmethod...
if timeout is None:
timeout = cls.TIMEOUT
sock = connect(addr, timeout)
if cls.VERBOSE:
print('connected')
self = cls(sock, ownsock=True)
self._addr = addr
return self
