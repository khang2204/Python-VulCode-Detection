def _test_context_manager(self):...
cursor = cnxn.cursor()
cursor.execute('begin')
cursor.execute('create table t1(i int)')
cursor.execute('rollback')
def test():...
cnxn.execute('rollback')
self.assertRaises(pyodbc.Error, test)
