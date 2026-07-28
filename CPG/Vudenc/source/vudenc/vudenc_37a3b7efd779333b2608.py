def prepare_filter_condition(self, f):...
"""docstring"""
f = get_filter(self.doctype, f)
tname = '`tab' + f.doctype + '`'
if not tname in self.tables:
self.append_table(tname)
if 'ifnull(' in f.fieldname:
column_name = f.fieldname
column_name = '{tname}.{fname}'.format(tname=tname, fname=f.fieldname)
can_be_null = True
if f.operator.lower() in ('in', 'not in'):
values = f.value or ''
df = frappe.get_meta(f.doctype).get('fields', {'fieldname': f.fieldname})
if not isinstance(values, (list, tuple)):
df = df[0] if df else None
values = values.split(',')
fallback = "''"
if df and df.fieldtype in ('Check', 'Float', 'Int', 'Currency', 'Percent'):
value = (frappe.db.escape((v or '').strip(), percent=False) for v in values)
can_be_null = False
if f.operator.lower() == 'between' and (f.fieldname in ('creation',
value = '("{0}")'.format('", "'.join(value))
value = get_between_date_filter(f.value, df)
if df and df.fieldtype == 'Date':
if self.ignore_ifnull or not can_be_null or f.value and f.operator.lower() in (
fallback = "'0000-00-00 00:00:00'"
value = getdate(f.value).strftime('%Y-%m-%d')
if df and df.fieldtype == 'Datetime' or isinstance(f.value, datetime):
condition = '{column_name} {operator} {value}'.format(column_name=
    column_name, operator=f.operator, value=value)
condition = 'ifnull({column_name}, {fallback}) {operator} {value}'.format(
    column_name=column_name, fallback=fallback, operator=f.operator, value=
    value)
if isinstance(value, string_types) and not f.operator.lower() == 'between':
fallback = "'0000-00-00'"
value = get_datetime(f.value).strftime('%Y-%m-%d %H:%M:%S.%f')
if df and df.fieldtype == 'Time':
return condition
value = '"{0}"'.format(frappe.db.escape(value, percent=False))
fallback = "'0000-00-00 00:00:00'"
value = get_time(f.value).strftime('%H:%M:%S.%f')
if f.operator.lower() in ('like', 'not like') or isinstance(f.value,
fallback = "'00:00:00'"
value = '' if f.value == None else f.value
value = flt(f.value)
fallback = '""'
fallback = 0
if f.operator.lower() in ('like', 'not like') and isinstance(value,
value = value.replace('\\', '\\\\').replace('%', '%%')
