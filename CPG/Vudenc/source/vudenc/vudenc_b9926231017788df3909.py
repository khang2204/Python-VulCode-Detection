def db_init(conn, table, columns, debug=False):...
"""docstring"""
column_str = ', '.join([('`' + str(c) + '` DOUBLE DEFAULT NULL') for c in
    columns])
sql = (
    f'CREATE TABLE {table}(`TIMESTAMP` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP, {column_str});'
    )
if debug:
print(sql)
cursor = conn.cursor()
cursor.execute(sql)
cursor.close()
