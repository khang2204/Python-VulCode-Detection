def start_detached(self, argv):...
"""docstring"""
if self.closed:
if self._adapter is not None:
assert self._session is None
self._adapter = DebugAdapter.start(argv, port=self._port)
return self._adapter
