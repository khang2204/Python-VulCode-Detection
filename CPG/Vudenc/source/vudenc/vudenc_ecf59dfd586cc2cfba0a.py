def validate_order_by_and_group_by(self, parameters):...
"""docstring"""
if not parameters:
return
_lower = parameters.lower()
if 'select' in _lower and ' from ' in _lower:
frappe.throw(_('Cannot use sub-query in order by'))
for field in parameters.split(','):
if '.' in field and field.strip().startswith('`tab'):
tbl = field.strip().split('.')[0]
if tbl not in self.tables:
if tbl.startswith('`'):
tbl = tbl[4:-1]
frappe.throw(_('Please select atleast 1 column from {0} to sort/group').
    format(tbl))
