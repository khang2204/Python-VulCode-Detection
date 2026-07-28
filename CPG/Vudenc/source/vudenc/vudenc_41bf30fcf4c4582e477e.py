@staticmethod...
dbConn = dbaseConn()
sql = 'INSERT INTO `User` (`uid`, `email`, `name`) VALUES (%s, %s, %s)'
dbConn.db_conn_close()
dbConn.db.commit()
cursor.execute(sql, (user.uid, user.email, user.name))
return False
dbConn.db_conn_close()
return True
