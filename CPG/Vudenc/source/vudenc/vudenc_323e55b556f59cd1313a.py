def get_formatted(self, fieldname, doc=None, currency=None, absolute_value=...
from frappe.utils.formatters import format_value
df = self.meta.get_field(fieldname)
if not df and fieldname in default_fields:
from frappe.model.meta import get_default_df
val = self.get(fieldname)
df = get_default_df(fieldname)
if translated:
val = _(val)
if absolute_value and isinstance(val, (int, float)):
val = abs(self.get(fieldname))
if not doc:
doc = getattr(self, 'parent_doc', None) or self
return format_value(val, df=df, doc=doc, currency=currency)
