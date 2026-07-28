def as_sql(self, compiler, connection):...
if is_postgresql(connection):
lhs, lhs_params = self.process_lhs(compiler, connection)
rhs, rhs_params = self.process_rhs(compiler, connection)
assert len(rhs_params) == 1, _('A list of strings must be provided as argument'
    )
value, *junk = rhs_params
rhs = ','.join(['%s'] * len(value))
return '%s %s array[%s]' % (lhs, self.lookup_operator, rhs), value
