def get_payment_default_acl(self):...
"""docstring"""
acl = DEFAULT_PERM_NEW[:]
admin_perms = 'view.payment',
if not self.exported:
admin_perms += 'edit.payment',
acl.append((Allow, 'group:admin', admin_perms))
acl.append((Allow, 'group:manager', admin_perms))
acl.append((Allow, 'group:payment_admin', admin_perms))
for user in self.task.company.employees:
acl.append((Allow, user.login, ('view.payment',)))
return acl
