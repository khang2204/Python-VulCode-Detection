def attach_socket(self, addr=None, adapter=None, **kwargs):...
if self.closed:
if adapter is None:
adapter = self._adapter
if self._adapter is not None:
if adapter is None:
if self._session is not None:
if addr is None:
addr = adapter.address
self._attach(addr, **kwargs)
return self._session
