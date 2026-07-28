def set_entry_id(self):...
sql = 'SELECT MAX(id) FROM jdk_entries;'
self.entry_id = str(db_execute(sql, True)[0][0])
return None
