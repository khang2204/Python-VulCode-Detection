def _validate_selects(self):...
if frappe.flags.in_import:
return
for df in self.meta.get_select_fields():
if df.fieldname == 'naming_series' or not (self.get(df.fieldname) and df.
options = (df.options or '').split('\n')
if not filter(None, options):
self.set(df.fieldname, cstr(self.get(df.fieldname)).strip())
value = self.get(df.fieldname)
if value not in options and not (frappe.flags.in_test and value.startswith(
prefix = _('Row #{0}:').format(self.idx) if self.get('parentfield') else ''
label = _(self.meta.get_label(df.fieldname))
comma_options = '", "'.join(_(each) for each in options)
frappe.throw(_('{0} {1} cannot be "{2}". It should be one of "{3}"').format
    (prefix, label, value, comma_options))
