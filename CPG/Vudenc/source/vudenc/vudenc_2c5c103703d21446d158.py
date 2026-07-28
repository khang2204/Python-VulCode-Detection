def login(self, eppn, came_from):...
"""docstring"""
session_id = self.add_outstanding_query(came_from)
cookie = self.dump_session_cookie(session_id)
saml_response = auth_response(session_id, eppn)
response1 = self.app.dispatch_request()
cookie = response1.headers['Set-Cookie']
return cookie
