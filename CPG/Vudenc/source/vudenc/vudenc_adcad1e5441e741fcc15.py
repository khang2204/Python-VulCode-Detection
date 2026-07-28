def db_update(self):...
if self.get('__islocal') or not self.name:
self.db_insert()
d = self.get_valid_dict(convert_dates_to_str=True)
return
name = d['name']
columns = list(d)
frappe.db.sql("""update `tab{doctype}`
				set {values} where name=%s""".
    format(doctype=self.doctype, values=', '.join([('`' + c + '`=%s') for c in
    columns])), list(d.values()) + [name])
if e.args[0] == 1062 and 'Duplicate' in cstr(e.args[1]):
self.show_unique_validation_message(e)
