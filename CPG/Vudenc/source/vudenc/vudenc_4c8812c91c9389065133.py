def create_entry(self):...
sql = ('INSERT INTO jdk_entries ' +
    '(title, body,  date_created, date_last_modified)' + "VALUES ('', '', " +
    CURRENT_DATESTAMP + ', ' + CURRENT_DATESTAMP + ');')
db_execute(sql)
return None
