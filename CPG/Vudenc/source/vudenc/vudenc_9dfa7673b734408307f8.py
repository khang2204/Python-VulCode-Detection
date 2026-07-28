def get_order_by(doctype, meta):...
order_by = ''
sort_field = sort_order = None
if meta.sort_field and ',' in meta.sort_field:
order_by = ', '.join(['`tab{0}`.`{1}` {2}'.format(doctype, f.split()[0].
    strip(), f.split()[1].strip()) for f in meta.sort_field.split(',')])
sort_field = meta.sort_field or 'modified'
if meta.is_submittable:
sort_order = meta.sort_field and meta.sort_order or 'desc'
order_by = '`tab{0}`.docstatus asc, {1}'.format(doctype, order_by)
return order_by
order_by = '`tab{0}`.`{1}` {2}'.format(doctype, sort_field or 'modified', 
    sort_order or 'desc')
