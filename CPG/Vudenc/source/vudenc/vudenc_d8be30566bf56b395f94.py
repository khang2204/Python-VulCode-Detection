def test_duplicate_expression_alias(self):...
body = {'aggregations': [['topK(3)', 'logger', 'dupe_alias'], ['uniq',
    'environment', 'dupe_alias']]}
exprs = [column_expr(col, body, alias, agg) for agg, col, alias in body[
    'aggregations']]
assert exprs == ['(topK(3)(logger) AS dupe_alias)', 'dupe_alias']
