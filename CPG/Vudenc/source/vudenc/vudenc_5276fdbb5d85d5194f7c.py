def as_sql(self, qn, connection):...
sql, params = super().as_sql(qn, connection)
sql = '%s::%s' % (sql, self.lhs.output_field.db_type(connection))
return sql, params
