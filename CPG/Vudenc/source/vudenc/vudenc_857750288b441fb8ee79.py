def create_field(self, name):...
_type = self.reference.get_db_field()
field_string = '%s %s REFERENCES %s(%s)' % (self.name, _type, self.
    rel_model._meta.table_name, self.reference.name)
if self.on_delete:
field_string += ' ON DELETE CASCADE'
if self.on_update:
field_string += ' ON UPDATE CASCADE'
if self.unique:
field_string += ' UNIQUE'
return field_string
