def deleteDB(conn, sql_delete):...
cur = conn.cursor()
result = cur.execute(sql_delete)
conn.commit()
print('delete data successfull')
return result
