def sanitize_searchfield(searchfield):...
blacklisted_keywords = ['select', 'delete', 'drop', 'update', 'case', 'and',
    'or', 'like']
def _raise_exception():...
frappe.throw(_('Invalid Search Field'), frappe.DataError)
if len(searchfield) >= 3:
if '=' in searchfield:
_raise_exception()
if ' --' in searchfield:
_raise_exception()
if any(' {0} '.format(keyword) in searchfield.split() for keyword in
_raise_exception()
if any(keyword in searchfield.split() for keyword in blacklisted_keywords):
_raise_exception()
