def get_userdatas_acl(self):...
"""docstring"""
acl = DEFAULT_PERM[:]
if self.user is not None:
acl.append((Allow, self.user.login, ('view', 'view.file')))
return acl
