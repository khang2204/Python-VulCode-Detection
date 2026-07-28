def add_outstanding_query(self, came_from):...
"""docstring"""
self.app.dispatch_request()
oq_cache = OutstandingQueriesCache(session)
oq_cache.set(session.token, came_from)
session.persist()
return session.token
