def test_lower_case(self):...
"""docstring"""
pyodbc.lowercase = True
self.cursor = self.cnxn.cursor()
self.cursor.execute('create table t1(Abc int, dEf int)')
self.cursor.execute('select * from t1')
names = [t[0] for t in self.cursor.description]
names.sort()
self.assertEqual(names, ['abc', 'def'])
pyodbc.lowercase = False
