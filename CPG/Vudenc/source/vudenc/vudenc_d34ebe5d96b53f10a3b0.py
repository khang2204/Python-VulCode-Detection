def get_permission_query_conditions(self):...
condition_methods = frappe.get_hooks('permission_query_conditions', {}).get(
    self.doctype, [])
if condition_methods:
conditions = []
for method in condition_methods:
c = frappe.call(frappe.get_attr(method), self.user)
return ' and '.join(conditions) if conditions else None
if c:
conditions.append(c)
