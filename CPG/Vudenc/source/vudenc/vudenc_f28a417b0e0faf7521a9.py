def _validate_length(self):...
if frappe.flags.in_install:
return
if self.meta.issingle:
return
column_types_to_check_length = 'varchar', 'int', 'bigint'
for fieldname, value in iteritems(self.get_valid_dict()):
df = self.meta.get_field(fieldname)
if not df or df.fieldtype == 'Check':
column_type = type_map[df.fieldtype][0] or None
default_column_max_length = type_map[df.fieldtype][1] or None
if df and df.fieldtype in type_map and column_type in column_types_to_check_length:
max_length = cint(df.get('length')) or cint(default_column_max_length)
if len(cstr(value)) > max_length:
if self.parentfield and self.idx:
reference = _('{0}, Row {1}').format(_(self.doctype), self.idx)
reference = '{0} {1}'.format(_(self.doctype), self.name)
frappe.throw(_(
    "{0}: '{1}' ({3}) will get truncated, as max characters allowed is {2}"
    ).format(reference, _(df.label), max_length, value), frappe.
    CharacterLengthExceededError, title=_('Value too big'))
