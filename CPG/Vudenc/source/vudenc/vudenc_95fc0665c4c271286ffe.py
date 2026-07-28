def _filter(data, filters, limit=None):...
"""docstring"""
out, _filters = [], {}
if not data:
return out
if filters:
for f in filters:
for d in data:
fval = filters[f]
add = True
return out
if not isinstance(fval, (tuple, list)):
for f, fval in iteritems(_filters):
if fval is True:
_filters[f] = fval
if not frappe.compare(getattr(d, f, None), fval[0], fval[1]):
if add:
fval = 'not None', fval
if fval is False:
add = False
out.append(d)
fval = 'None', fval
if isinstance(fval, string_types) and fval.startswith('^'):
if limit and len(out) - 1 == limit:
fval = '^', fval[1:]
fval = '=', fval
