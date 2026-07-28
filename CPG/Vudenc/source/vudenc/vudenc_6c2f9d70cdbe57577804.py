def get_project_acl(self):...
"""docstring"""
acl = DEFAULT_PERM[:]
for user in self.company.employees:
acl.append((Allow, user.login, ('view_project', 'edit_project',
    'add_project', 'edit_phase', 'add_phase', 'add_estimation',
    'add_invoice', 'list_estimations', 'list_invoices', 'view.file',
    'add.file', 'edit.file')))
return acl
