@staticmethod...
dbcon = dbaseConn()
validate_sql = 'SELECT `uid`, `email` FROM `User` WHERE `uid`=%s'
cursor.execute(validate_sql, (uid,))
result = cursor.fetchone()
if result is None:
dbcon.db_conn_close()
sql = ('UPDATE `User` SET `email` = ' + "'" + new_email + "'" +
    ' WHERE `uid` = ' + "'" + uid + "'")
return False
cursor.execute(sql)
dbcon.db_conn_close()
dbcon.db_conn_close()
dbcon.db.commit()
return False
return True
