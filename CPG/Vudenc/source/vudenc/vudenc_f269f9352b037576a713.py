def token_delete(remote, token=''):...
"""docstring"""
session_key = token_session_key(remote.name)
return session.pop(session_key, None)
