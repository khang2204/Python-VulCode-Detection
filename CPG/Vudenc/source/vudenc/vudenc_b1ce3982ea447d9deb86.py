from base import Field
TYPE = 'BOOL'
def __init__(self, *args, **kwargs):...
super(BooleanField, self).__init__(*args, **kwargs)
def create_field(self, name):...
field_string = '%s bool' % str(name)
return field_string
