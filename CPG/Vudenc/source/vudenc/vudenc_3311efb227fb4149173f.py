def db_verify_file_integrity(path):...
"""docstring"""
file_id = db_get_file_details(path)['id']
params = [1, file_id]
cur.execute('UPDATE files SET verified=%s WHERE id=%s;', params)
db.commit()
return
