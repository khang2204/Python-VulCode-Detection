def _close(self):...
if self._session is not None:
if self._adapter is not None:
self._session.close()
self._adapter.close()
