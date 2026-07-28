def get_customer_acl(self):...
"""docstring"""
acl = DEFAULT_PERM[:]
for user in self.company.employees:
acl.append((Allow, user.login, ('view_customer', 'edit_customer')))
return acl
