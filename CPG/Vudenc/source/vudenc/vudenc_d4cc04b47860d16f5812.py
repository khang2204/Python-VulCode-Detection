def all_referenced_columns(body):...
"""docstring"""
col_exprs = []
for field in ['arrayjoin', 'groupby', 'orderby', 'selected_columns']:
if field in body:
if 'conditions' in body:
col_exprs.extend(to_list(body[field]))
flat_conditions = list(chain(*[([c] if is_condition(c) else c) for c in
    body['conditions']]))
if 'aggregations' in body:
col_exprs.extend([c[0] for c in flat_conditions])
col_exprs.extend([a[1] for a in body['aggregations']])
return set(chain(*[columns_in_expr(ex) for ex in col_exprs]))
