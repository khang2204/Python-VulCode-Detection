def as_dict(self, no_nulls=False, no_default_fields=False,...
doc = self.get_valid_dict(convert_dates_to_str=convert_dates_to_str)
doc['doctype'] = self.doctype
for df in self.meta.get_table_fields():
children = self.get(df.fieldname) or []
if no_nulls:
doc[df.fieldname] = [d.as_dict(no_nulls=no_nulls) for d in children]
for k in list(doc):
if no_default_fields:
if doc[k] is None:
for k in list(doc):
for key in ('_user_tags', '__islocal', '__onload', '_liked_by',
if k in default_fields:
if self.get(key):
return doc
doc[key] = self.get(key)
