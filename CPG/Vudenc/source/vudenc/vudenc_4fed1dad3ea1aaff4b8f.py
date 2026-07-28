def get_activity_acl(self):...
"""docstring"""
acl = get_event_acl(self)
for companies in self.companies:
for user in companies.employees:
return acl
acl.append((Allow, user.login, ('view_activity', 'view.file')))
