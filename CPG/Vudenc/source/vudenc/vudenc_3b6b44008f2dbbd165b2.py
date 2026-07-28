def get_parentfield_of_doctype(self, doctype):...
fieldname = [df.fieldname for df in self.meta.get_table_fields() if df.
    options == doctype]
return fieldname[0] if fieldname else None
