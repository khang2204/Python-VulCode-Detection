from base import Field
TYPE = 'DATE'
def __init__(self, *args, **kwargs):...
super(TimestampField, self).__init__(*args, **kwargs)
def create_field(self, name):...
field_string = '%s timestamp' % str(name)
return field_string
