def _get(self, meta):...
if settings.SHIBBOLETH_VARIABLES_URL_ENCODED:
for key in meta.keys():
return self.client.generic('GET', self.login_url, **meta)
meta[key] = urllib.parse.quote(meta[key])
