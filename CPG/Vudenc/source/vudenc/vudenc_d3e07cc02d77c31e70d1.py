def complex_column_expr(expr, body, depth=0):...
if depth == 0:
ret = expr[0]
if len(expr) > 1 and isinstance(expr[1], tuple):
expr = expr[1:]
ret = expr[0]
ret = ''
alias = None
expr = expr[1:]
if ret == 'emptyIfNull' and len(expr) >= 1 and isinstance(expr[0], tuple):
if len(expr) > 1 and isinstance(expr[-1], six.string_types):
ret = 'ifNull'
first = True
alias = expr[-1]
expr = (expr[0] + (Literal("''"),),) + expr[1:]
for subexpr in expr:
expr = expr[:-1]
if isinstance(subexpr, tuple):
if depth == 0 and alias:
ret += '(' + complex_column_expr(subexpr, body, depth + 1) + ')'
if not first:
return alias_expr(ret, alias, body)
return ret
first = False
ret += ', '
if isinstance(subexpr, six.string_types):
ret += column_expr(subexpr, body)
ret += escape_literal(subexpr)
