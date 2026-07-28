def as_sql(self, compiler, connection):...
if is_postgresql(connection):
lhs, lhs_params = self.process_lhs(compiler, connection)
rhs, rhs_params = self.process_rhs(compiler, connection)
assert len(rhs_params) == 1, _('A boolean must be provided as argument')
value, *junk = rhs_params
assert isinstance(value, bool), _('Lookup argument must be a boolean')
rhs = ','.join(['%s'] * len(self.empty_values))
if value:
return '%s IS NULL OR %s::text IN (%s)' % (lhs, lhs, rhs), self.empty_values
return '%s IS NOT NULL AND %s::text NOT IN (%s)' % (lhs, lhs, rhs
    ), self.empty_values
