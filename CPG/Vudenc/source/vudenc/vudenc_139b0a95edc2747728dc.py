def updateDB(conn, sql_update):...
cur = conn.cursor()
result = cur.execute(sql_update)
conn.commit()
print('update data successfull')
return result
