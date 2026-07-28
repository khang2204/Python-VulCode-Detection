def db_check(conn, table, columns, debug=False):...
"""docstring"""
sql = f'SELECT * FROM {table};'
if debug:
print(sql)
cursor = conn.cursor()
cursor.execute(sql)
db_columns = list(next(zip(*cursor.description)))
for col in columns:
if col not in db_columns:
cursor.close()
cursor.close()
conn.close()
