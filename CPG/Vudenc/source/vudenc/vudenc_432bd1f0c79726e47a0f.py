def Update(self, user, is_admin, **kwargs):...
"""docstring"""
if not is_admin:
dirty = False
for k, v in kwargs.iteritems():
assert k in self._properties, k
if dirty:
if getattr(self, k) != v:
user_name = user.email().split('@')[0]
return dirty
setattr(self, k, v)
self.updated_by = user_name
dirty = True
self.Save()
logging.info('Config %s was updated by %s', self.__class__, user_name)
