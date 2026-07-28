from base import Field
MAX_LENGTH = 255
TYPE = 'CHAR'
def __init__(self, max_length=MAX_LENGTH, *args, **kwargs):...
super(CharField, self).__init__(*args, **kwargs)
self.max_length = max_length
def get_db_field(self):...
if self.model_class._meta.database:
return '{0}({1})'.format(self.model_class._meta.database.TYPES[self.TYPE],
    self.max_length)
return self.TYPE
