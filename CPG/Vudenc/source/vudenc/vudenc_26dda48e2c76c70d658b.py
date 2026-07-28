def get_event_acl(self):...
"""docstring"""
acl = DEFAULT_PERM[:]
for user in self.participants:
acl.append((Allow, user.login, ('view_activity', 'view_workshop', 'view.file'))
    )
return acl
