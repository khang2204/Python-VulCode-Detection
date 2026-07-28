def detach(self, adapter=None):...
if self.closed:
if self._session is None:
if adapter is None:
adapter = self._adapter
assert adapter is not None
if not self._session.is_client:
self._detach()
