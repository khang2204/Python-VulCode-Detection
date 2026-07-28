def insertDB(conn, sql_insert):...
cur = conn.cursor()
result = cur.execute(sql_insert)
conn.commit()
print('insert data successfull')
return result
