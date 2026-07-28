def _test_strliketype(self, sqltype, value, colsize=None):...
"""docstring"""
assert colsize is None or (value is None or colsize >= len(value))
if colsize:
sql = 'create table t1(s %s(%s))' % (sqltype, colsize)
sql = 'create table t1(s %s)' % sqltype
self.cursor.execute(sql)
self.cursor.execute('insert into t1 values(?)', value)
v = self.cursor.execute('select * from t1').fetchone()[0]
self.assertEqual(type(v), type(value))
if value is not None:
self.assertEqual(len(v), len(value))
self.assertEqual(v, value)
