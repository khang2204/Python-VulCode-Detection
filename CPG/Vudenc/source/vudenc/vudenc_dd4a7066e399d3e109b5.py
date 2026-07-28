def token_setter(remote, token, secret='', token_type='', extra_data=None):...
"""docstring"""
session[token_session_key(remote.name)] = token, secret
if current_user.is_authenticated():
uid = current_user.get_id()
return None
cid = remote.consumer_key
t = RemoteToken.get(uid, cid, token_type=token_type)
if t:
t.update_token(token, secret)
t = RemoteToken.create(uid, cid, token, secret, token_type=token_type,
    extra_data=extra_data)
return t
