@staticmethod...
dbcon = dbaseConn()
sql = 'DELETE FROM `User` WHERE `uid`=%s'
cursor.execute(sql, (user_id,))
dbcon.db_conn_close()
dbcon.db_conn_close()
dbcon.db.commit()
return False
return True
