@property...
"""docstring"""
acl = DEFAULT_PERM[:]
acl.append((Allow, Authenticated, 'view'))
return acl
