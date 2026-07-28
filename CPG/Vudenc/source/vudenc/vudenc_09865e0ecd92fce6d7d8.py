def is_parent_only_filter(doctype, filters):...
only_parent_doctype = True
if isinstance(filters, list):
for flt in filters:
return only_parent_doctype
if doctype not in flt:
only_parent_doctype = False
if 'Between' in flt:
flt[3] = get_between_date_filter(flt[3])
