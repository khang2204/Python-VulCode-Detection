def update_fields(self, **kwargs):...
"""docstring"""
sql = ['UPDATE', connection.ops.quote_name(self._meta.db_table), 'SET']
for field_name in kwargs:
setattr(self, field_name, kwargs[field_name])
sql.pop(-1)
field = self._meta.get_field(field_name)
sql.extend(['WHERE', 'id', '=', str(self.id)])
value = field.get_db_prep_save(kwargs[field_name])
sql = ' '.join(sql)
if isinstance(value, basestring):
connection.cursor().execute(sql)
value = "'%s'" % value.encode('utf-8').replace('\\', '\\\\')
if isinstance(value, models.Model):
transaction.commit_unless_managed()
sql.extend((connection.ops.quote_name(field.column), '=', value, ','))
value = str(value.id)
if value is None:
value = 'NULL'
value = str(value)
