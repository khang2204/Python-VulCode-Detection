def get_expense_payment_acl(self):...
"""docstring"""
acl = DEFAULT_PERM_NEW[:]
admin_perms = 'view.expensesheet_payment',
if not self.exported:
admin_perms += 'edit.expensesheet_payment',
acl.append((Allow, 'group:admin', admin_perms))
acl.append((Allow, 'group:manager', admin_perms))
for user in self.task.company.employees:
acl.append((Allow, user.login, ('view.expensesheet_payment',)))
return acl
