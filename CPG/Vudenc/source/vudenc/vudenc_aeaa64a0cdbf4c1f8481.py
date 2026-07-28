@staticmethod...
sql = ('SELECT jdk_entries.id, jdk_entries.title ' + 'FROM jdk_entries ' +
    'ORDER BY date_last_modified DESC ' + 'LIMIT 30;')
return db_execute(sql, True)
