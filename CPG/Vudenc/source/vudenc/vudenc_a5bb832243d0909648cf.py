def test_executemany_failure(self):...
"""docstring"""
self.cursor.execute('create table t1(a int, b varchar(10))')
params = [(1, 'good'), ('error', 'not an int'), (3, 'good')]
self.assertRaises(pyodbc.Error, self.cursor.executemany,
    'insert into t1(a, b) value (?, ?)', params)
