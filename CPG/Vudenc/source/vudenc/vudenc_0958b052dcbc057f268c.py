def db_type(self, connection):...
if is_postgresql(connection):
return 'jsonb'
return super().db_type(connection)
