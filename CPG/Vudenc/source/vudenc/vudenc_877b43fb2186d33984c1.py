def _validate_constants(self):...
if frappe.flags.in_import or self.is_new(
return
constants = [d.fieldname for d in self.meta.get('fields', {'set_only_once':
    ('=', 1)})]
if constants:
values = frappe.db.get_value(self.doctype, self.name, constants, as_dict=True)
for fieldname in constants:
df = self.meta.get_field(fieldname)
if df.fieldtype == 'Date' or df.fieldtype == 'Datetime':
value = str(values.get(fieldname))
value = values.get(fieldname)
if self.get(fieldname) != value:
frappe.throw(_('Value cannot be changed for {0}').format(self.meta.
    get_label(fieldname)), frappe.CannotChangeConstantError)
