@classmethod...
"""docstring"""
if conf.USE_OPENID:
cookie_auth = openid_cookie_authentication
cookie_auth = gae_cookie_authentication
return oauth_authentication, cookie_auth, service_to_service_authentication
