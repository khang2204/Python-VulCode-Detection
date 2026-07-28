def test_executemany_one(self):...
"""docstring"""
self.cursor.execute('create table t1(a int, b varchar(10))')
params = [(1, 'test')]
self.cursor.executemany('insert into t1(a, b) values (?,?)', params)
count = self.cursor.execute('select count(*) from t1').fetchone()[0]
self.assertEqual(count, len(params))
self.cursor.execute('select a, b from t1 order by a')
rows = self.cursor.fetchall()
self.assertEqual(count, len(rows))
for param, row in zip(params, rows):
self.assertEqual(param[0], row[0])
self.assertEqual(param[1], row[1])
