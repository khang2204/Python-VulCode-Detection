def import_database(self, sqlfile):...
"""docstring"""
self.connection = sqlite3.connect(self.db_path)
self.cursor = self.connection.cursor()
if self.connection:
f = codecs.open(sqlfile[0], encoding='utf-8', mode='r')
sql = f.read()
self.cursor.executescript(sql)
print('db created and contents imported from %s' % sqlfile[0])
