def test_row_executemany(self):...
"""docstring"""
self.cursor.execute('create table t1(n int, s varchar(10))')
for i in range(3):
self.cursor.execute('insert into t1 values (?, ?)', i, chr(ord('a') + i))
rows = self.cursor.execute('select n, s from t1').fetchall()
self.assertNotEqual(len(rows), 0)
self.cursor.execute('create table t2(n int, s varchar(10))')
self.cursor.executemany('insert into t2 values (?, ?)', rows)
