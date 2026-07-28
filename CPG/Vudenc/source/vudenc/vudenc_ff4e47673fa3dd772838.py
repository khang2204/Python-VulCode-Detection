def get_user_acl(self):...
"""docstring"""
acl = DEFAULT_PERM[:]
if self.enabled():
acl.append((Allow, self.login, ('view_user', 'edit_user', 'list_holidays',
    'add_holiday', 'edit_holiday', 'list_competences')))
return acl
acl.append((Allow, Authenticated, 'visit'))
