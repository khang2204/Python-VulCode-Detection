def test_row_execute(self):...
"""docstring"""
self.cursor.execute('create table t1(n int, s varchar(10))')
self.cursor.execute("insert into t1 values (1, 'a')")
row = self.cursor.execute('select n, s from t1').fetchone()
self.assertNotEqual(row, None)
self.cursor.execute('create table t2(n int, s varchar(10))')
self.cursor.execute('insert into t2 values (?, ?)', row)
