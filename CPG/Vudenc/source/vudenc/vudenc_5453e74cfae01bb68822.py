def response_token_setter(remote, resp):...
"""docstring"""
if resp is None:
if 'access_token' in resp:
return oauth2_token_setter(remote, resp)
if 'oauth_token' in resp and 'oauth_token_secret' in resp:
return oauth1_token_setter(remote, resp)
if 'error' in resp:
