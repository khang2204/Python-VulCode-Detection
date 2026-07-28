@property...
if not hasattr(self, '_meta'):
self._meta = frappe.get_meta(self.doctype)
return self._meta
