def _detach(self):...
session = self._session
if session is None:
return
self._session = None
session.close()
