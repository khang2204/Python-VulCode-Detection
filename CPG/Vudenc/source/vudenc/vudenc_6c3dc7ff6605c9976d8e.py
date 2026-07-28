from base import Field
name = 'id'
TYPE = 'INT'
def __init__(self, name=None, *args, **kwargs):...
super(PrimaryKeyField, self).__init__(*args, **kwargs)
def create_field(self, name):...
field_string = 'id SERIAL PRIMARY KEY'
return field_string
