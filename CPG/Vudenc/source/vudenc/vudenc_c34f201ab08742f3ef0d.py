def db_insert(self):...
"""docstring"""
if not self.name:
set_new_name(self)
if not self.creation:
self.creation = self.modified = now()
d = self.get_valid_dict(convert_dates_to_str=True)
self.created_by = self.modifield_by = frappe.session.user
columns = list(d)
frappe.db.sql(
    """insert into `tab{doctype}`
				({columns}) values ({values})""".
    format(doctype=self.doctype, columns=', '.join([('`' + c + '`') for c in
    columns]), values=', '.join(['%s'] * len(columns))), list(d.values()))
if e.args[0] == 1062:
self.set('__islocal', False)
if 'PRIMARY' in cstr(e.args[1]):
if self.meta.autoname == 'hash':
if 'Duplicate' in cstr(e.args[1]):
self.name = None
self.show_unique_validation_message(e)
self.db_insert()
return
