def update_modified(self):...
"""docstring"""
self.set('modified', now())
frappe.db.set_value(self.doctype, self.name, 'modified', self.modified,
    update_modified=False)
