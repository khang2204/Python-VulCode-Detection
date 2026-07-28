from datetime import date, datetime
import simplejson as json
import time
from base import BaseTest
from snuba.util import all_referenced_columns, column_expr, complex_column_expr, conditions_expr, escape_literal, tuplify, Timer
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
def test_alias_in_alias(self):...
body = {'groupby': ['tags_key', 'tags_value']}
assert column_expr('tags_key', body
    ) == '(((arrayJoin(arrayMap((x,y) -> [x,y], tags.key, tags.value)) AS all_tags))[1] AS tags_key)'
assert column_expr('tags_key', body) == 'tags_key'
assert column_expr('tags_value', body) == '((all_tags)[2] AS tags_value)'
def test_escape(self):...
assert escape_literal("'") == "'\\''"
assert escape_literal(date(2001, 1, 1)) == "toDate('2001-01-01')"
assert escape_literal(datetime(2001, 1, 1, 1, 1, 1)
    ) == "toDateTime('2001-01-01T01:01:01')"
assert escape_literal([1, 'a', date(2001, 1, 1)]
    ) == "(1, 'a', toDate('2001-01-01'))"
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
def test_duplicate_expression_alias(self):...
body = {'aggregations': [['topK(3)', 'logger', 'dupe_alias'], ['uniq',
    'environment', 'dupe_alias']]}
exprs = [column_expr(col, body, alias, agg) for agg, col, alias in body[
    'aggregations']]
assert exprs == ['(topK(3)(logger) AS dupe_alias)', 'dupe_alias']
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
def test_timer(self):...
t = Timer()
time.sleep(0.001)
t.mark('thing1')
time.sleep(0.001)
t.mark('thing2')
snapshot = t.finish()
time.sleep(0.001)
t.mark('thing1')
time.sleep(0.001)
t.mark('thing2')
snapshot_2 = t.finish()
assert snapshot['marks_ms'].keys() == snapshot_2['marks_ms'].keys()
assert snapshot['marks_ms']['thing1'] < snapshot_2['marks_ms']['thing1']
assert snapshot['marks_ms']['thing2'] < snapshot_2['marks_ms']['thing2']
