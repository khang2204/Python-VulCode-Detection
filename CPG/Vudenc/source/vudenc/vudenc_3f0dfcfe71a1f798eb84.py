def _get_admin_status_acl(self):...
"""docstring"""
perms = ('view.%s' % self.type_, 'admin.%s' % self.type_, 'view.file',
    'add.file', 'edit.file')
if self.status in ('draft', 'wait', 'invalid'):
perms += ('edit.%s' % self.type_, 'valid.%s' % self.type_, 'delete.%s' %
    self.type_, 'draft.%s' % self.type_)
return [(Allow, 'group:admin', perms), (Allow, 'group:manager', perms)]
if self.status == 'wait':
perms += 'invalid.%s' % self.type_,
