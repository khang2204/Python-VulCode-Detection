def as_sql(self, compiler, connection):...
if is_postgresql(connection):
lhs, lhs_params = self.process_lhs(compiler, connection)
rhs, rhs_params = self.process_rhs(compiler, connection)
assert len(rhs_params) == 1, _('A dictionary must be provided as argument')
value, *junk = rhs_params
return '%s %s %s::jsonb' % (lhs, self.lookup_operator, rhs), [json_encode(
    value)]
