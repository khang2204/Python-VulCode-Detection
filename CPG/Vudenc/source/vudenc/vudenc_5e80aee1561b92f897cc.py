def as_sql(self, compiler, connection):...
if is_postgresql(connection):
lhs, lhs_params = self.process_lhs(compiler, connection)
rhs, rhs_params = self.process_rhs(compiler, connection)
assert len(rhs_params) == 1, _('A string must be provided as argument')
params = lhs_params + rhs_params
return '%s ? %s' % (lhs, rhs), params
