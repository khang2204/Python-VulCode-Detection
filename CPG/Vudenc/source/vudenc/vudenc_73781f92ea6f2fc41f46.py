def sanitize_fields(self):...
"""docstring"""
sub_query_regex = re.compile('^.*[,();].*')
blacklisted_keywords = ['select', 'create', 'insert', 'delete', 'drop',
    'update', 'case']
blacklisted_functions = ['concat', 'concat_ws', 'if', 'ifnull', 'nullif',
    'coalesce', 'connection_id', 'current_user', 'database',
    'last_insert_id', 'session_user', 'system_user', 'user', 'version']
def _raise_exception():...
frappe.throw(_('Use of sub-query or function is restricted'), frappe.DataError)
def _is_query(field):...
if re.compile('^(select|delete|update|drop|create)\\s').match(field):
_raise_exception()
if re.compile('\\s*[a-zA-z]*\\s*( from | group by | order by | where | join )'
for field in self.fields:
_raise_exception()
if sub_query_regex.match(field):
if any(keyword in field.lower().split() for keyword in blacklisted_keywords):
if re.compile("[a-zA-Z]+\\s*'").match(field):
_raise_exception()
if any('({0}'.format(keyword) in field.lower() for keyword in
_raise_exception()
if re.compile('[a-zA-Z]+\\s*,').match(field):
_raise_exception()
if any('{0}('.format(keyword) in field.lower() for keyword in
_raise_exception()
_is_query(field)
_raise_exception()
