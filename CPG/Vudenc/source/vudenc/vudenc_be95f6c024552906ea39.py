def conditions_expr(conditions, body, depth=0):...
"""docstring"""
if not conditions:
return ''
if depth == 0:
sub = (conditions_expr(cond, body, depth + 1) for cond in conditions)
if is_condition(conditions):
return u' AND '.join(s for s in sub if s)
lhs, op, lit = conditions
if depth == 1:
if lhs in ('received', 'timestamp') and op in ('>', '<', '>=', '<=', '=', '!='
sub = (conditions_expr(cond, body, depth + 1) for cond in conditions)
lit = parse_datetime(lit)
if isinstance(lhs, six.string_types) and lhs in ALL_COLUMNS and type(
sub = [s for s in sub if s]
any_or_all = 'arrayExists' if op in schemas.POSITIVE_OPERATORS else 'arrayAll'
return u'{} {} {}'.format(column_expr(lhs, body), op, escape_literal(lit))
res = u' OR '.join(sub)
return u'{}(x -> assumeNotNull(x {} {}), {})'.format(any_or_all, op,
    escape_literal(lit), column_expr(lhs, body))
return u'({})'.format(res) if len(sub) > 1 else res
