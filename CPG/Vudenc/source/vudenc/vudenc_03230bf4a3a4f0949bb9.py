def test_column_expr(self):...
body = {'granularity': 86400}
assert column_expr('tags[foo]', body.copy()
    ) == "(tags.value[indexOf(tags.key, 'foo')] AS `tags[foo]`)"
assert column_expr('tags[server_name]', body.copy()
    ) == '(server_name AS `tags[server_name]`)'
assert column_expr('tags[app.device]', body.copy()
    ) == '(app_device AS `tags[app.device]`)'
assert column_expr('tags_key', body.copy()
    ) == '(arrayJoin(tags.key) AS tags_key)'
tag_group_body = {'groupby': ['tags_key', 'tags_value']}
assert column_expr('tags_key', tag_group_body
    ) == '(((arrayJoin(arrayMap((x,y) -> [x,y], tags.key, tags.value)) AS all_tags))[1] AS tags_key)'
assert column_expr('time', body.copy()) == '(toDate(timestamp) AS time)'
assert column_expr('col', body.copy(), aggregate='sum') == '(sum(col) AS col)'
assert column_expr(None, body.copy(), alias='sum', aggregate='sum') == 'sum'
assert column_expr('col', body.copy(), alias='summation', aggregate='sum'
    ) == '(sum(col) AS summation)'
assert column_expr('', body.copy(), alias='count', aggregate='count()'
    ) == '(count() AS count)'
assert column_expr('', body.copy(), alias='aggregate', aggregate='count()'
    ) == '(count() AS aggregate)'
assert column_expr('sentry:release', body.copy()) == '`sentry:release`'
assert column_expr('-timestamp', body.copy()) == '-timestamp'
assert column_expr('-sentry:release', body.copy()) == '-`sentry:release`'
assert column_expr("'hello world'", body.copy()) == "'hello world'"
assert column_expr(tuplify(['concat', ['a', "':'", 'b']]), body.copy()
    ) == "concat(a, ':', b)"
group_id_body = body.copy()
assert column_expr('issue', group_id_body) == '(group_id AS issue)'
