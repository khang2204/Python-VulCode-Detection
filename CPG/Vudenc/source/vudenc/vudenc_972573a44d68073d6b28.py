def set_order_by(self, args):...
meta = frappe.get_meta(self.doctype)
if self.order_by:
args.order_by = self.order_by
args.order_by = ''
group_function_without_group_by = len(self.fields) == 1 and (self.fields[0]
    .lower().startswith('count(') or self.fields[0].lower().startswith(
    'min(') or self.fields[0].lower().startswith('max(')) and not self.group_by
if not group_function_without_group_by:
sort_field = sort_order = None
if meta.sort_field and ',' in meta.sort_field:
args.order_by = ', '.join(['`tab{0}`.`{1}` {2}'.format(self.doctype, f.
    split()[0].strip(), f.split()[1].strip()) for f in meta.sort_field.
    split(',')])
sort_field = meta.sort_field or 'modified'
if meta.is_submittable:
sort_order = meta.sort_field and meta.sort_order or 'desc'
args.order_by = '`tab{0}`.docstatus asc, {1}'.format(self.doctype, args.
    order_by)
args.order_by = '`tab{0}`.`{1}` {2}'.format(self.doctype, sort_field or
    'modified', sort_order or 'desc')
