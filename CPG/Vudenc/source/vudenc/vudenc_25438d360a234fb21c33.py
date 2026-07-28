def db_increment_passes(path):...
"""docstring"""
file_id = db_get_file_details(path)['id']
file_passes = db_get_file_details(path)['passes'] + 1
params = [file_passes, file_id]
cur.execute('UPDATE files SET passes=%s WHERE id=%s;', params)
db.commit()
return
