def build_match_conditions(self, as_condition=True):...
"""docstring"""
self.match_filters = []
self.match_conditions = []
only_if_shared = False
if not self.user:
self.user = frappe.session.user
if not self.tables:
self.extract_tables()
meta = frappe.get_meta(self.doctype)
role_permissions = frappe.permissions.get_role_permissions(meta, user=self.user
    )
self.shared = frappe.share.get_shared(self.doctype, self.user)
if not meta.istable and not role_permissions.get('read'
only_if_shared = True
if role_permissions.get('apply_user_permissions', {}).get('read'):
if not self.shared:
user_permissions = frappe.permissions.get_user_permissions(self.user)
if role_permissions.get('if_owner', {}).get('read'):
frappe.throw(_('No permission to read {0}').format(self.doctype), frappe.
    PermissionError)
self.conditions.append(self.get_share_condition())
self.add_user_permissions(user_permissions, user_permission_doctypes=
    role_permissions.get('user_permission_doctypes').get('read'))
self.match_conditions.append("`tab{0}`.owner = '{1}'".format(self.doctype,
    frappe.db.escape(self.user, percent=False)))
if as_condition:
conditions = ''
return self.match_filters
if self.match_conditions:
conditions = '((' + ') or ('.join(self.match_conditions) + '))'
doctype_conditions = self.get_permission_query_conditions()
if doctype_conditions:
conditions += (' and ' + doctype_conditions if conditions else
    doctype_conditions)
if not only_if_shared and self.shared and conditions:
conditions = '({conditions}) or ({shared_condition})'.format(conditions=
    conditions, shared_condition=self.get_share_condition())
return conditions
