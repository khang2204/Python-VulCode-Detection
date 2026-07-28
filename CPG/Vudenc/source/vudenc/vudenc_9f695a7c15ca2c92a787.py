def test_complex_conditions_expr(self):...
body = {}
assert complex_column_expr(tuplify(['count', []]), body.copy()) == 'count()'
assert complex_column_expr(tuplify(['notEmpty', ['foo']]), body.copy()
    ) == 'notEmpty(foo)'
assert complex_column_expr(tuplify(['notEmpty', ['arrayElement', ['foo', 1]
    ]]), body.copy()) == 'notEmpty(arrayElement(foo, 1))'
assert complex_column_expr(tuplify(['foo', ['bar', ['qux'], 'baz']]), body.
    copy()) == 'foo(bar(qux), baz)'
assert complex_column_expr(tuplify(['foo', [], 'a']), body.copy()
    ) == '(foo() AS a)'
assert complex_column_expr(tuplify(['foo', ['b', 'c'], 'd']), body.copy()
    ) == '(foo(b, c) AS d)'
assert complex_column_expr(tuplify(['foo', ['b', 'c', ['d']]]), body.copy()
    ) == 'foo(b, c(d))'
assert complex_column_expr(tuplify(['topK', [3], ['project_id']]), body.copy()
    ) == 'topK(3)(project_id)'
assert complex_column_expr(tuplify(['topK', [3], ['project_id'], 'baz']),
    body.copy()) == '(topK(3)(project_id) AS baz)'
assert complex_column_expr(tuplify(['emptyIfNull', ['project_id']]), body.
    copy()) == "ifNull(project_id, '')"
assert complex_column_expr(tuplify(['emptyIfNull', ['project_id'], 'foo']),
    body.copy()) == "(ifNull(project_id, '') AS foo)"
assert complex_column_expr(tuplify(['positionCaseInsensitive', ['message',
    "'lol 'single' quotes'"]]), body.copy()
    ) == "positionCaseInsensitive(message, 'lol \\'single\\' quotes')"
