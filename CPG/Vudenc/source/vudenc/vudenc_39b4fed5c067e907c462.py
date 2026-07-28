def get_product_acl(self):...
"""docstring"""
acl = DEFAULT_PERM[:]
for user in self.company.employees:
acl.append((Allow, user.login, ('list_sale_products', 'view_sale_product',
    'edit_sale_product')))
return acl
