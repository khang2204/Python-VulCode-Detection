def populate_entry_data(self):...
sql = ('SELECT jdk_entries.title, jdk_entries.body ' + 'FROM jdk_entries ' +
    'WHERE jdk_entries.id = ' + self.entry_id + ';')
self.title, self.body = db_execute(sql, True)[0]
return None
