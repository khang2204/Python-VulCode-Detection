def get_valid_dict(self, sanitize=True, convert_dates_to_str=False):...
d = frappe._dict()
for fieldname in self.meta.get_valid_columns():
d[fieldname] = self.get(fieldname)
return d
if not sanitize and d[fieldname] is None:
df = self.meta.get_field(fieldname)
if df:
if df.fieldtype == 'Check':
if d[fieldname] == None:
if df.fieldtype == 'Int' and not isinstance(d[fieldname], int):
d[fieldname] = 0
if not isinstance(d[fieldname], int) or d[fieldname] > 1:
d[fieldname] = cint(d[fieldname])
if df.fieldtype in ('Currency', 'Float', 'Percent') and not isinstance(d[
if isinstance(d[fieldname], list) and df.fieldtype != 'Table':
d[fieldname] = 1 if cint(d[fieldname]) else 0
d[fieldname] = flt(d[fieldname])
if df.fieldtype in ('Datetime', 'Date', 'Time') and d[fieldname] == '':
frappe.throw(_('Value for {0} cannot be a list').format(_(df.label)))
if convert_dates_to_str and isinstance(d[fieldname], (datetime.datetime,
d[fieldname] = None
if df.get('unique') and cstr(d[fieldname]).strip() == '':
d[fieldname] = str(d[fieldname])
d[fieldname] = None
