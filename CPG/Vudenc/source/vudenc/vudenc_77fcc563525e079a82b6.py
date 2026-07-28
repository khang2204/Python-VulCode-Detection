def _get_user_status_acl(self):...
"""docstring"""
acl = []
for user in self.company.employees:
perms = 'view.%s' % self.type_, 'view.file', 'add.file', 'edit.file'
return acl
if self.status in ('draft', 'invalid'):
perms += ('edit.%s' % self.type_, 'wait.%s' % self.type_, 'delete.%s' %
    self.type_, 'draft.%s' % self.type_)
if self.status in ('wait',):
perms += 'draft.%s' % self.type_,
acl.append((Allow, user.login, perms))
