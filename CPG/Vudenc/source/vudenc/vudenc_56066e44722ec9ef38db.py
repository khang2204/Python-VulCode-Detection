def test_alias_in_alias(self):...
body = {'groupby': ['tags_key', 'tags_value']}
assert column_expr('tags_key', body
    ) == '(((arrayJoin(arrayMap((x,y) -> [x,y], tags.key, tags.value)) AS all_tags))[1] AS tags_key)'
assert column_expr('tags_key', body) == 'tags_key'
assert column_expr('tags_value', body) == '((all_tags)[2] AS tags_value)'
