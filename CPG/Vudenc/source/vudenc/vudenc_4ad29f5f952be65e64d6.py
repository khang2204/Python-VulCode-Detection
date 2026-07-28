def column_expr(column_name, body, alias=None, aggregate=None):...
"""docstring"""
assert column_name or aggregate
assert not aggregate or aggregate and (column_name or alias)
column_name = column_name or ''
if isinstance(column_name, (tuple, list)) and isinstance(column_name[1], (
return complex_column_expr(column_name, body)
if isinstance(column_name, six.string_types) and QUOTED_LITERAL_RE.match(
return escape_literal(column_name[1:-1])
if column_name == settings.TIME_GROUP_COLUMN:
expr = settings.TIME_GROUPS[body['granularity']]
if NESTED_COL_EXPR_RE.match(column_name):
if aggregate:
expr = tag_expr(column_name)
if column_name in ['tags_key', 'tags_value']:
if expr:
alias = escape_col(alias or column_name)
expr = tags_expr(column_name, body)
if column_name == 'issue':
expr = u'{}({})'.format(aggregate, expr)
expr = aggregate
return alias_expr(expr, alias, body)
expr = 'group_id'
expr = escape_col(column_name)
if aggregate == 'uniq':
expr = 'ifNull({}, 0)'.format(expr)
