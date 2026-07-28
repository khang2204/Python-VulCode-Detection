@staticmethod...
dbConn = dbaseConn()
sql = 'SELECT `uid`, `email`, `name` FROM `User` WHERE `uid`=%s'
print(uid)
cursor.execute(sql, (uid,))
result = cursor.fetchone()
print(result)
if result is None:
return None
print(result[0])
dbConn.db_conn_close()
return User(*result)
