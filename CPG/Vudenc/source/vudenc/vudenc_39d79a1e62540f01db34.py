def columns_in_expr(expr):...
"""docstring"""
cols = []
if isinstance(expr, six.string_types):
cols.append(expr.lstrip('-'))
if isinstance(expr, (list, tuple)) and len(expr) >= 2 and isinstance(expr[1
return cols
for func_arg in expr[1]:
cols.extend(columns_in_expr(func_arg))
