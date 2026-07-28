def stop_debugging(self):...
if self.closed:
if self._adapter is None:
if self._session is not None:
self._detach()
self._adapter.close()
self._adapter = None
