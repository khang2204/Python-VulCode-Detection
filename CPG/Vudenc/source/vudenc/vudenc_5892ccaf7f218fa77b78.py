def get_cancelinvoice_default_acl(self):...
"""docstring"""
acl = DEFAULT_PERM_NEW[:]
acl.extend(_get_admin_status_acl(self))
admin_perms = ()
if not self.exported and self.status == 'valid':
admin_perms += 'set_treasury.cancelinvoice', 'set_date.cancelinvoice'
if admin_perms:
acl.append((Allow, 'group:admin', admin_perms))
if self.status != 'valid':
acl.append((Allow, 'group:manager', admin_perms))
acl.append((Allow, 'group:invoice_validation', ('valid.cancelinvoice',)))
acl.extend(_get_user_status_acl(self))
acl.append((Deny, 'group:invoice_validation', ('wait.cancelinvoice',)))
return acl
