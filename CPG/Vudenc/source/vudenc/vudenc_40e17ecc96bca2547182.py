def db_insert(conn, table, columns, values, debug=False):...
"""docstring"""
col_str = str(columns).replace("'", '`')
sql = f'INSERT INTO {table} {col_str} VALUES {values};'
if debug:
print(sql)
cursor = conn.cursor()
cursor.execute(sql)
conn.commit()
