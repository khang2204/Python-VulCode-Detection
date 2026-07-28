def db_count(conn, table, debug=False):...
"""docstring"""
sql = f'SELECT COUNT(*) as count FROM {table};'
if debug:
print(sql)
cursor = conn.cursor()
num_rows = cursor.execute(sql).fetchone()[0]
cursor.close()
return num_rows
