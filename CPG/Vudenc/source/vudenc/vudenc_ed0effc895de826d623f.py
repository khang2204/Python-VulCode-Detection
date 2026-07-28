def login_get_current_user(handler):...
if enable_authentication:
cookie = handler.get_secure_cookie('user')
return 'authentication_disabled'
if cookie in authenticated_users:
return cookie
print('Bad/expired cookie received')
return None
