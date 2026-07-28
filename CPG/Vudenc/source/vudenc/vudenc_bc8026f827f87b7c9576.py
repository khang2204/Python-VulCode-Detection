def sanitize_fields(self):...
"""docstring"""
regex = re.compile('^.*[,();].*')
blacklisted_keywords = ['select', 'create', 'insert', 'delete', 'drop',
    'update', 'case']
blacklisted_functions = ['concat', 'concat_ws', 'if', 'ifnull', 'nullif',
    'coalesce', 'connection_id', 'current_user', 'database',
    'last_insert_id', 'session_user', 'system_user', 'user', 'version']
def _raise_exception():...
frappe.throw(_('Cannot use sub-query or function in fields'), frappe.DataError)
for field in self.fields:
if regex.match(field):
if any(keyword in field.lower() for keyword in blacklisted_keywords):
_raise_exception()
if any('{0}('.format(keyword) in field.lower() for keyword in
_raise_exception()
