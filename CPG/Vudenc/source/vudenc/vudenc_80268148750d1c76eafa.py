def test_multiple_bindings(self):...
"""docstring"""
self.cursor.execute('create table t1(n int)')
self.cursor.execute('insert into t1 values (?)', 1)
self.cursor.execute('insert into t1 values (?)', 2)
self.cursor.execute('insert into t1 values (?)', 3)
for i in range(3):
self.cursor.execute('select n from t1 where n < ?', 10)
self.cursor.execute('select n from t1 where n < 3')
