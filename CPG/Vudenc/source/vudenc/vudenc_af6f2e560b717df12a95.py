def _init_child(self, value, key):...
if not self.doctype:
return value
if not isinstance(value, BaseDocument):
if 'doctype' not in value:
value.parent = self.name
value['doctype'] = self.get_table_field_doctype(key)
value = get_controller(value['doctype'])(value)
value.parenttype = self.doctype
if not value['doctype']:
value.init_valid_columns()
value.parentfield = key
if value.docstatus is None:
value.docstatus = 0
if not getattr(value, 'idx', None):
value.idx = len(self.get(key) or []) + 1
if not getattr(value, 'name', None):
value.__dict__['__islocal'] = 1
return value
