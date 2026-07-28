def check_user_role(auth, role, cc):...
"""docstring"""
return auth and ('%s:%s' % (cc or '', role) in auth.user_roles or ':%s' %
    role in auth.user_roles)
