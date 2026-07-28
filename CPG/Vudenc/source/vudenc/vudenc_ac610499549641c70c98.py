@staticmethod...
dbcon = dbaseConn()
validate_sql = ('SELECT `uid`,`email`,`name` FROM `User` WHERE `uid`=' +
    "'" + uid + "'")
cursor.execute(validate_sql)
result = cursor.fetchone()
print(result)
if result is None:
dbcon.db_conn_close()
update_stmt = ('UPDATE `User` SET `name` = ' + "'" + new_user_name + "'" +
    ' WHERE `uid` = %s')
dbcon.db_conn_close()
return True
return False
print(update_stmt)
return False
cursor.execute(update_stmt, (uid,))
dbcon.db.commit()
