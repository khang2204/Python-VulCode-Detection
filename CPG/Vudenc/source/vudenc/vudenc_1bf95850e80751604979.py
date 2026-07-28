def reset_values_if_no_permlevel_access(self, has_access_to,...
"""docstring"""
to_reset = []
for df in high_permlevel_fields:
if df.permlevel not in has_access_to and df.fieldtype not in display_fieldtypes:
if to_reset:
to_reset.append(df)
if self.is_new():
ref_doc = frappe.new_doc(self.doctype)
if self.get('parent_doc'):
for df in to_reset:
self.parent_doc.get_latest()
ref_doc = self.get_latest()
self.set(df.fieldname, ref_doc.get(df.fieldname))
ref_doc = [d for d in self.parent_doc.get(self.parentfield) if d.name ==
    self.name][0]
