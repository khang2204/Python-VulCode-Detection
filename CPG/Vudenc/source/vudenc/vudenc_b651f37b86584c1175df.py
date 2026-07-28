def _external_auth_intercept(request, mode):...
"""docstring"""
if mode == 'login':
return external_auth_login(request)
if mode == 'register':
return external_auth_register(request)
