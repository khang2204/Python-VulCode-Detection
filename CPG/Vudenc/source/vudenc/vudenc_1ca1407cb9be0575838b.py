"""
Created on 2012-8-9

@author: diracfang
"""
def __init__(self, db, access_token):...
self.db = db
self.access_token = access_token
def get_user(self):...
if not hasattr(self, '_user'):
qs = ("select * from account_access where access_token = '%s'" % self.
    access_token)
return self._user
result = self.db.get(qs)
if result:
self._user = result
self._user = None
