def _validate_update_after_submit(self):...
db_values = frappe.get_doc(self.doctype, self.name).as_dict()
for key in self.as_dict():
df = self.meta.get_field(key)
db_value = db_values.get(key)
if df and not df.allow_on_submit and (self.get(key) or db_value):
if df.fieldtype == 'Table':
self_value = len(self.get(key))
self_value = self.get_value(key)
db_value = len(db_value)
if self_value != db_value:
frappe.throw(_('Not allowed to change {0} after submission').format(df.
    label), frappe.UpdateAfterSubmitError)
