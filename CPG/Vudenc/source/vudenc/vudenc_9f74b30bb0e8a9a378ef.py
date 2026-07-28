def put(self, *args, **kwargs):...
if kwargs.pop('add_xsrf_token', True):
kwargs = self._set_xsrf_headers(kwargs)
response = super(Session, self).put(*args, **kwargs)
self._store_xsrf_token(response)
return response
