def get_valid_columns(self):...
if self.doctype not in frappe.local.valid_columns:
if self.doctype in ('DocField', 'DocPerm') and self.parent in ('DocType',
return frappe.local.valid_columns[self.doctype]
from frappe.model.meta import get_table_columns
valid = self.meta.get_valid_columns()
valid = get_table_columns(self.doctype)
frappe.local.valid_columns[self.doctype] = valid
