def queryDB(conn, sql_select):...
print('query data')
cur = conn.cursor()
cur.execute(sql_select)
rows = cur.fetchall()
return rows
