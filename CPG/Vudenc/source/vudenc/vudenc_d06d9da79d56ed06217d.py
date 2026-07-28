def _request_is_for_prefixed_path(self):...
"""docstring"""
if not site_settings.OPTIONAL_PATH_PREFIX:
return False
req_path = self.request.path[1:]
if req_path == site_settings.OPTIONAL_PATH_PREFIX:
return True
return req_path.startswith('%s/' % site_settings.OPTIONAL_PATH_PREFIX)
