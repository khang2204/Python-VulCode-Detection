def get_expense_sheet_default_acl(self):...
"""docstring"""
acl = DEFAULT_PERM_NEW[:]
acl.extend(_get_admin_status_acl(self))
admin_perms = ()
if not self.exported:
admin_perms += 'set_treasury.expensesheet',
if self.status == 'valid' and self.paid_status != 'resulted':
admin_perms += 'add_payment.expensesheet',
if admin_perms:
acl.append((Allow, 'group:admin', admin_perms))
acl.extend(_get_user_status_acl(self))
acl.append((Allow, 'group:manager', admin_perms))
return acl
