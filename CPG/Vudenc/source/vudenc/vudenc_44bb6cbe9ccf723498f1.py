def get_user(self):...
if not hasattr(self, '_user'):
qs = ("select * from account_access where access_token = '%s'" % self.
    access_token)
return self._user
result = self.db.get(qs)
if result:
self._user = result
self._user = None
