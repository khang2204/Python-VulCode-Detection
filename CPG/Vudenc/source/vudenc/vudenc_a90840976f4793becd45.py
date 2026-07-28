def db_execute(sql, expect_return_values=False):...
db_connection = sqlite3.connect(DB_FILE)
db_cursor = db_connection.cursor()
db_cursor.execute(sql)
if expect_return_values:
return_values = db_cursor.fetchall()
return_values = None
db_connection.close()
db_connection.commit()
return return_values
