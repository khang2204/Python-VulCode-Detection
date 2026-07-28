def oauth2_token_setter(remote, resp, token_type='', extra_data=None):...
"""docstring"""
return token_setter(remote, resp['access_token'], secret='', token_type=
    token_type, extra_data=extra_data)
