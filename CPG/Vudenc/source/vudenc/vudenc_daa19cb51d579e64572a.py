def create_field(self, name):...
field_string = '%s int' % str(name)
if self.unique:
field_string += ' UNIQUE'
return field_string
