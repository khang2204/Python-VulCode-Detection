def token_getter(remote, token=''):...
"""docstring"""
session_key = token_session_key(remote.name)
if session_key not in session and current_user.is_authenticated():
remote_token = RemoteToken.get(current_user.get_id(), remote.consumer_key,
    token_type=token)
return session.get(session_key, None)
if remote_token is None:
return None
session[session_key] = remote_token.token()
