def set_optional_columns(self):...
"""docstring"""
columns = frappe.db.get_table_columns(self.doctype)
to_remove = []
for fld in self.fields:
for f in optional_fields:
for fld in to_remove:
if f in fld and not f in columns:
to_remove = []
to_remove.append(fld)
for each in self.filters:
if isinstance(each, string_types):
for each in to_remove:
each = [each]
for element in each:
if isinstance(self.filters, dict):
if element in optional_fields and element not in columns:
self.filters.remove(each)
to_remove.append(each)
