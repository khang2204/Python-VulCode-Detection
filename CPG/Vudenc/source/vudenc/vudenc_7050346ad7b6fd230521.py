def test_conditions_expr(self):...
conditions = [['a', '=', 1]]
assert conditions_expr(conditions, {}) == 'a = 1'
conditions = [[['a', '=', 1]]]
assert conditions_expr(conditions, {}) == 'a = 1'
conditions = [['a', '=', 1], ['b', '=', 2]]
assert conditions_expr(conditions, {}) == 'a = 1 AND b = 2'
conditions = [[['a', '=', 1], ['b', '=', 2]]]
assert conditions_expr(conditions, {}) == '(a = 1 OR b = 2)'
conditions = [[['a', '=', 1], ['b', '=', 2]], ['c', '=', 3]]
assert conditions_expr(conditions, {}) == '(a = 1 OR b = 2) AND c = 3'
conditions = [[['a', '=', 1], ['b', '=', 2]], [['c', '=', 3], ['d', '=', 4]]]
assert conditions_expr(conditions, {}
    ) == '(a = 1 OR b = 2) AND (c = 3 OR d = 4)'
conditions = [[['a', '=', 1], []]]
assert conditions_expr(conditions, {}) == 'a = 1'
conditions = [[['tags[foo]', '=', 1], ['b', '=', 2]]]
expanded = column_expr('tags[foo]', {})
assert conditions_expr(conditions, {}) == '({} = 1 OR b = 2)'.format(expanded)
reuse_body = {}
conditions = [[['tags[foo]', '=', 1], ['b', '=', 2]]]
column_expr('tags[foo]', reuse_body)
assert conditions_expr(conditions, reuse_body) == '(`tags[foo]` = 1 OR b = 2)'
conditions = [['primary_hash', 'LIKE', '%foo%']]
assert conditions_expr(conditions, {}) == "primary_hash LIKE '%foo%'"
conditions = tuplify([[['notEmpty', ['arrayElement', [
    'exception_stacks.type', 1]]], '=', 1]])
assert conditions_expr(conditions, {}
    ) == 'notEmpty(arrayElement(exception_stacks.type, 1)) = 1'
conditions = tuplify([[['notEmpty', ['tags[sentry:user]']], '=', 1]])
assert conditions_expr(conditions, {}
    ) == 'notEmpty((`sentry:user` AS `tags[sentry:user]`)) = 1'
conditions = tuplify([[['notEmpty', ['tags_key']], '=', 1]])
assert conditions_expr(conditions, {}
    ) == 'notEmpty((arrayJoin(tags.key) AS tags_key)) = 1'
conditions = tuplify([[[['notEmpty', ['tags[sentry:environment]']], '=',
    'dev'], [['notEmpty', ['tags[sentry:environment]']], '=', 'prod']], [[[
    'notEmpty', ['tags[sentry:user]']], '=', 'joe'], [['notEmpty', [
    'tags[sentry:user]']], '=', 'bob']]])
assert conditions_expr(conditions, {}
    ) == "(notEmpty((tags.value[indexOf(tags.key, 'sentry:environment')] AS `tags[sentry:environment]`)) = 'dev' OR notEmpty(`tags[sentry:environment]`) = 'prod') AND (notEmpty((`sentry:user` AS `tags[sentry:user]`)) = 'joe' OR notEmpty(`tags[sentry:user]`) = 'bob')"
conditions = [['exception_frames.filename', 'LIKE', '%foo%']]
assert conditions_expr(conditions, {}
    ) == "arrayExists(x -> assumeNotNull(x LIKE '%foo%'), exception_frames.filename)"
conditions = [['exception_frames.filename', 'NOT LIKE', '%foo%']]
assert conditions_expr(conditions, {}
    ) == "arrayAll(x -> assumeNotNull(x NOT LIKE '%foo%'), exception_frames.filename)"
