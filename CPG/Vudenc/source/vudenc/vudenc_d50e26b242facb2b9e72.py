def get_one_user(user_id):...
"""docstring"""
conn = sqlite3.connect(DB_FILE)
sql = 'select * from home_user WHERE id={};'.format(user_id)
print('sql', sql)
cursor = conn.cursor()
cursor.execute(sql)
res = cursor.fetchall()
return res
