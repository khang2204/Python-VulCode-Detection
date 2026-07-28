def test_referenced_columns(self):...
body = {'conditions': [['a', '=', '1'], ['b', '=', '1']]}
assert all_referenced_columns(body) == set(['a', 'b'])
body = {'conditions': [['a', '=', '1'], [['b', '=', '1'], ['c', '=', '1']]]}
assert all_referenced_columns(body) == set(['a', 'b', 'c'])
body = {'conditions': [['a', '=', '1'], [['b', '=', '1'], [['foo', ['c']],
    '=', '1']]]}
assert all_referenced_columns(body) == set(['a', 'b', 'c'])
body = {'conditions': [['a', '=', '1'], [['b', '=', '1'], [['foo', ['c', [
    'bar', ['d']]]], '=', '1']]]}
assert all_referenced_columns(body) == set(['a', 'b', 'c', 'd'])
body = {'arrayjoin': 'tags_key', 'groupby': ['time', 'issue'], 'orderby':
    '-time', 'selected_columns': ['issue', 'time', ['foo', ['c', ['bar', [
    'd']]]]], 'aggregations': [['uniq', 'tags_value', 'values_seen']]}
assert all_referenced_columns(body) == set(['tags_key', 'tags_value',
    'time', 'issue', 'c', 'd'])
