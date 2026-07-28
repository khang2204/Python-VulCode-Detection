def _attach(self, addr, **kwargs):...
if addr is None:
addr = self._addr
assert addr.host == 'localhost'
self._session = self.SESSION.create_client(addr, **kwargs)
