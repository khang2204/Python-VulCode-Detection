from base import Field
TYPE = 'INT'
def __init__(self, *args, **kwargs):...
super(IntegerField, self).__init__(*args, **kwargs)
def create_field(self, name):...
field_string = '%s int' % str(name)
if self.unique:
field_string += ' UNIQUE'
return field_string
