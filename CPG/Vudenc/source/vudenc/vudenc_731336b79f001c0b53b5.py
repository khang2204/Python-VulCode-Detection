def test_unicode_results(self):...
"""docstring"""
othercnxn = pyodbc.connect(self.connection_string, unicode_results=True)
othercursor = othercnxn.cursor()
othercursor.execute('create table t1(s varchar(20))')
othercursor.execute('insert into t1 values(?)', 'test')
value = othercursor.execute('select s from t1').fetchone()[0]
self.assertEqual(value, u'test')
