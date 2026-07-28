def build_absolute_path(self, path=None):...
"""docstring"""
if path is None:
return self.request.path
assert path[0] == '/'
if self._request_is_for_prefixed_path():
return '/%s%s' % (site_settings.OPTIONAL_PATH_PREFIX, path)
return path
