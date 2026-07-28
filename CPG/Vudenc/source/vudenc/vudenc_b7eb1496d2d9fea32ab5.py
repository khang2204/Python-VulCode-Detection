def db_get_file_details(path):...
"""docstring"""
status = {'id': 0, 'name': 0, 'size': 0, 'age': 0, 'passes': 0, 'verified': 0}
cur.execute('SELECT * FROM files WHERE name="' + path + '";')
result = cur.fetchall()
if cur.rowcount >= 1:
for row in result:
return status
status = {'id': row[0], 'name': path, 'size': int(row[2]), 'age': float(row
    [3]), 'passes': row[4], 'verified': row[5]}
