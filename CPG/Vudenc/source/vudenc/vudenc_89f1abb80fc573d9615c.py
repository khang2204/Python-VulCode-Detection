def as_sql(self, compiler, connection, **kwargs):...
if CustomUnaccent.has_unaccent is None:
cursor = connection.cursor()
if CustomUnaccent.has_unaccent:
cursor.execute(
    "SELECT COUNT(proname) FROM pg_proc WHERE proname = 'f_unaccent';")
CustomUnaccent.function = 'F_UNACCENT'
return super().as_sql(compiler, connection, **kwargs)
response = cursor.fetchone()
CustomUnaccent.has_unaccent = response and response[0] > 0
