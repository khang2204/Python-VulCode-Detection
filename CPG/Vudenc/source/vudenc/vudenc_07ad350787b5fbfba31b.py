def test_row_description(self):...
"""docstring"""
self.cursor = self.cnxn.cursor()
self.cursor.execute('create table t1(a int, b char(3))')
self.cnxn.commit()
self.cursor.execute("insert into t1 values(1, 'abc')")
row = self.cursor.execute('select * from t1').fetchone()
self.assertEqual(self.cursor.description, row.cursor_description)
