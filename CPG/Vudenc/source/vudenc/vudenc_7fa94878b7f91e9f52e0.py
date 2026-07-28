def get_company_acl(self):...
"""docstring"""
acl = DEFAULT_PERM[:]
acl.extend([(Allow, user.login, ('view_company', 'edit_company',
    'view.file', 'list_customers', 'add_customer', 'list_projects',
    'add_project', 'list_estimations', 'list_invoices',
    'edit_commercial_handling', 'list_expenses', 'add.expense',
    'list_sale_products', 'add_sale_product', 'list_treasury_files',
    'list_activities', 'list_workshops')) for user in self.employees])
return acl
