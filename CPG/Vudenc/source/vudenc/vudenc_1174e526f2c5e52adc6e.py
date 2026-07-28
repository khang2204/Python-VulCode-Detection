def acs(self, url, eppn, check_fn):...
"""docstring"""
came_from = '/camefrom/'
resp = c.get(url)
cookie = resp.headers['Set-Cookie']
token = session._session.token
authr = auth_response(token, eppn)
oq_cache = OutstandingQueriesCache(session)
oq_cache.set(token, came_from)
resp = self.app.dispatch_request()
self.assertEquals(resp.status_code, 302)
self.assertEquals(resp.location, came_from)
check_fn()
