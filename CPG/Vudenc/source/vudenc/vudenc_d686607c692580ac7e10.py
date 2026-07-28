def append_table(self, table_name):...
self.tables.append(table_name)
doctype = table_name[4:-1]
if not self.flags.ignore_permissions and not frappe.has_permission(doctype):
frappe.flags.error_message = _('Insufficient Permission for {0}').format(frappe
    .bold(doctype))
