@frappe.whitelist()...
"""docstring"""
kwargs.pop('cmd', None)
return DatabaseQuery(doctype).execute(None, *args, **kwargs)
