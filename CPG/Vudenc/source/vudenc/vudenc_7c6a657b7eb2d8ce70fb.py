def _fix_numeric_types(self):...
for df in self.meta.get('fields'):
if df.fieldtype == 'Check':
if self.docstatus is not None:
self.set(df.fieldname, cint(self.get(df.fieldname)))
if self.get(df.fieldname) is not None:
self.docstatus = cint(self.docstatus)
if df.fieldtype == 'Int':
self.set(df.fieldname, cint(self.get(df.fieldname)))
if df.fieldtype in ('Float', 'Currency', 'Percent'):
self.set(df.fieldname, flt(self.get(df.fieldname)))
