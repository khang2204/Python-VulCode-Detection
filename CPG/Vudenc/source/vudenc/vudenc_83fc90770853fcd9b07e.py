def db_insert_new_file(path):...
"""docstring"""
file_size = get_file_size(path)
file_age = get_file_age(path)
params = [path, file_size, file_age]
cur.execute('INSERT INTO files VALUES (NULL, %s, %s, %s, 0, 0);', params)
db.commit()
return
