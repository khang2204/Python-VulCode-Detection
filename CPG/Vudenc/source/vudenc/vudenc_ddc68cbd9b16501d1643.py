def precision(self, fieldname, parentfield=None):...
"""docstring"""
from frappe.model.meta import get_field_precision
if parentfield and not isinstance(parentfield, string_types):
parentfield = parentfield.parentfield
cache_key = parentfield or 'main'
if not hasattr(self, '_precision'):
self._precision = frappe._dict()
if cache_key not in self._precision:
self._precision[cache_key] = frappe._dict()
if fieldname not in self._precision[cache_key]:
self._precision[cache_key][fieldname] = None
return self._precision[cache_key][fieldname]
doctype = self.meta.get_field(parentfield
    ).options if parentfield else self.doctype
df = frappe.get_meta(doctype).get_field(fieldname)
if df.fieldtype in ('Currency', 'Float', 'Percent'):
self._precision[cache_key][fieldname] = get_field_precision(df, self)
