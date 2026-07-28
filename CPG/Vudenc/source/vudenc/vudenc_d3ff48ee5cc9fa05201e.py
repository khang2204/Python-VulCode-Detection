def alias_expr(expr, alias, body):...
"""docstring"""
alias_cache = body.setdefault('alias_cache', [])
if expr == alias:
return expr
if alias in alias_cache:
return alias
alias_cache.append(alias)
return u'({} AS {})'.format(expr, alias)
