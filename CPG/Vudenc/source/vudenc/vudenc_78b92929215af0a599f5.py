def get_db_field(self):...
if self.model_class._meta.database:
return '{0}({1})'.format(self.model_class._meta.database.TYPES[self.TYPE],
    self.max_length)
return self.TYPE
