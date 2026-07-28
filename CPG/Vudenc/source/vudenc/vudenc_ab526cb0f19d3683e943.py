def new_client_for(self, *uri_segments):...
uri = self._build_url('/'.join(uri_segments))
return self.__class__(self._conn, url_prefix=uri, default_headers=self.
    _default_headers, client_obj=self)
