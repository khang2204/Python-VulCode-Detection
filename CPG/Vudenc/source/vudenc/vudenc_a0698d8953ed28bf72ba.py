def show_unique_validation_message(self, e):...
type, value, traceback = sys.exc_info()
fieldname, label = str(e).split("'")[-2], None
if 'unique_' in fieldname:
fieldname = fieldname.split('_', 1)[1]
df = self.meta.get_field(fieldname)
if df:
label = df.label
frappe.msgprint(_('{0} must be unique'.format(label or fieldname)))
