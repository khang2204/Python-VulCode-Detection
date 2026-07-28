def oauth1_token_setter(remote, resp, token_type='', extra_data=None):...
"""docstring"""
return token_setter(remote, resp['oauth_token'], secret=resp[
    'oauth_token_secret'], extra_data=extra_data, token_type=token_type)
