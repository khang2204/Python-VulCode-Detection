def db_update_file_details(path):...
"""docstring"""
file_size = get_file_size(path)
file_age = get_file_age(path)
file_id = db_get_file_details(path)['id']
params = [file_size, file_age, file_id]
cur.execute('UPDATE files SET size=%s, age=%s, passes=0 WHERE id=%s;', params)
db.commit()
return
