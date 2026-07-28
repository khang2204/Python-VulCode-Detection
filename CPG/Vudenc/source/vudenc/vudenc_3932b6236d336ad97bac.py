@frappe.whitelist()...
"""docstring"""
kwargs.pop('cmd', None)
kwargs.pop('ignore_permissions', None)
if frappe.is_table(doctype):
if not kwargs.get('parent'):
return DatabaseQuery(doctype).execute(None, *args, **kwargs)
frappe.flags.error_message = _('Parent is required to get child table data')
check_parent_permission(kwargs.get('parent'), doctype)
