def __init__(self, connection, url_prefix=None, default_headers=None,...
self._conn = connection
self._url_prefix = url_prefix or ''
self._default_headers = default_headers or {}
