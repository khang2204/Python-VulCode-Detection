def db_describe(conn, table, debug=False):...
"""docstring"""
sql = f'PRAGMA table_info({table});'
if debug:
print(sql)
cursor = conn.cursor()
info = cursor.execute(sql).fetchall()
cursor.close()
return info
