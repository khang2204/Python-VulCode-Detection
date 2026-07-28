def _get_users_api(self):...
"""docstring"""
method = self.auth_method
if not method:
for method in self.get_auth_methods(config.ensure_configured()):
if method not in _METHOD_TO_USERS_API:
if method in _METHOD_TO_USERS_API:
return _METHOD_TO_USERS_API[method]
