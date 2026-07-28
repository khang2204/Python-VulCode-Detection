def saveChanges(self):...
conn, cur = self.connectionAndCursor()
SQLObjectStore.saveChanges(self)
conn.rollback()
conn.commit()
if not self.setting('IgnoreSQLWarnings', False):
conn.rollback()
