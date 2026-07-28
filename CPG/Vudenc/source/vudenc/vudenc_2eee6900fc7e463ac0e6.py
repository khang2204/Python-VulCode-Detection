def create_field(self, name):...
field_string = '{0} {1}({2})'.format(name, self.model_class._meta.database.
    TYPES[self.TYPE], self.max_length)
if self.unique:
field_string += ' UNIQUE'
return field_string
