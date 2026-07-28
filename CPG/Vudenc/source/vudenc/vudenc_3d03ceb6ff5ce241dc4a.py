def add_user_permissions(self, user_permissions, user_permission_doctypes=None...
user_permission_doctypes = frappe.permissions.get_user_permission_doctypes(
    user_permission_doctypes, user_permissions)
meta = frappe.get_meta(self.doctype)
for doctypes in user_permission_doctypes:
match_filters = {}
match_conditions = []
for df in meta.get_fields_to_check_permissions(doctypes):
user_permission_values = user_permissions.get(df.options, [])
if match_conditions:
cond = 'ifnull(`tab{doctype}`.`{fieldname}`, "")=""'.format(doctype=self.
    doctype, fieldname=df.fieldname)
self.match_conditions.append(' and '.join(match_conditions))
if match_filters:
if user_permission_values:
self.match_filters.append(match_filters)
if not cint(frappe.get_system_settings('apply_strict_user_permissions')):
condition = cond
condition = cond + ' or '
condition = ''
match_conditions.append('({condition})'.format(condition=condition))
condition += '`tab{doctype}`.`{fieldname}` in ({values})'.format(doctype=
    self.doctype, fieldname=df.fieldname, values=', '.join([('"' + frappe.
    db.escape(v, percent=False) + '"') for v in user_permission_values]))
match_filters[df.options] = user_permission_values
