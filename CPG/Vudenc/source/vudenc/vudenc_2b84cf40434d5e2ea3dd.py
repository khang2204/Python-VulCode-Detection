def delete(self, *args, **kwargs):...
kwargs = self._set_xsrf_headers(kwargs)
response = super(Session, self).delete(*args, **kwargs)
self._store_xsrf_token(response)
return response
