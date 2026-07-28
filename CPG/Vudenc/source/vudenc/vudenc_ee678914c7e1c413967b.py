def setUp(self):...
self.cnxn = pyodbc.connect(self.connection_string)
self.cursor = self.cnxn.cursor()
for i in range(3):
self.cnxn.rollback()
self.cursor.execute('drop table t%d' % i)
self.cnxn.commit()
