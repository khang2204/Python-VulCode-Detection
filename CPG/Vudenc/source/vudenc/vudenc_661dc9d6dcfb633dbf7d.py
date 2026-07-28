def get_base_acl(self):...
"""docstring"""
acl = DEFAULT_PERM[:]
acl.append((Allow, Authenticated, 'view'))
return acl
