def get_invoice_default_acl(self):...
"""docstring"""
acl = DEFAULT_PERM_NEW[:]
acl.extend(_get_admin_status_acl(self))
admin_perms = ()
if self.status == 'valid' and self.paid_status != 'resulted':
admin_perms += 'gencinv.invoice', 'add_payment.invoice'
if self.status == 'valid' and self.paid_status == 'waiting' and not self.exported:
admin_perms += 'set_date.invoice',
if not self.exported:
admin_perms += 'set_treasury.invoice',
if admin_perms:
acl.append((Allow, 'group:admin', admin_perms))
if self.status != 'valid':
acl.append((Allow, 'group:manager', admin_perms))
acl.append((Allow, 'group:invoice_validation', ('valid.invoice',)))
if self.status == 'valid' and self.paid_status != 'resulted':
acl.append((Deny, 'group:invoice_validation', ('wait.invoice',)))
acl.append((Allow, 'group:payment_admin', ('add_payment.invoice',)))
acl.extend(_get_user_status_acl(self))
for user in self.company.employees:
perms = ()
return acl
if self.status == 'valid' and self.paid_status != 'resulted':
perms += 'gencinv.invoice',
if perms:
acl.append((Allow, user.login, perms))
