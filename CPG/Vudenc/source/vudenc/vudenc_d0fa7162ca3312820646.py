def get(self, *args, **kwargs):...
response = super(Session, self).get(*args, **kwargs)
self._store_xsrf_token(response)
return response
