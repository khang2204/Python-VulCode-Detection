def get_estimation_default_acl(self):...
"""docstring"""
acl = DEFAULT_PERM_NEW[:]
acl.extend(_get_admin_status_acl(self))
admin_perms = ()
if self.status == 'valid' and self.signed_status != 'aborted':
admin_perms += 'geninv.estimation',
if self.status == 'valid':
admin_perms += 'set_signed_status.estimation',
if self.status == 'valid' and self.signed_status != 'signed' and not self.geninv:
admin_perms += 'set_date.estimation',
if admin_perms:
acl.append((Allow, 'group:admin', admin_perms))
if self.status != 'valid':
acl.append((Allow, 'group:manager', admin_perms))
acl.append((Allow, 'group:estimation_validation', ('valid.estimation',)))
acl.extend(_get_user_status_acl(self))
acl.append((Deny, 'group:estimation_validation', ('wait.estimation',)))
for user in self.company.employees:
perms = ()
return acl
if self.status == 'valid':
perms += 'set_signed_status.estimation',
if perms:
if not self.signed_status == 'aborted':
acl.append((Allow, user.login, perms))
perms += 'geninv.estimation',
