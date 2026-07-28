def get_client_session(self):...
"""docstring"""
if self.csessid:
return _CLIENT_SESSIONS(session_key=self.csessid)
