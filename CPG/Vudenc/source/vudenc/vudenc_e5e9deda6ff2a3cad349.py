def test_close_cnxn(self):...
"""docstring"""
self.cursor.execute('create table t1(id integer, s varchar(20))')
self.cursor.execute('insert into t1 values (?,?)', 1, 'test')
self.cursor.execute('select * from t1')
self.cnxn.close()
self.sql = 'select * from t1'
self.assertRaises(pyodbc.ProgrammingError, self._exec)
