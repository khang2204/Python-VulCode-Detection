from base import Field
TYPE = 'FLOAT'
def __init__(self, *args, **kwargs):...
super(FloatField, self).__init__(*args, **kwargs)
def create_field(self, name):...
field_string = '%s float' % str(name)
return field_string
