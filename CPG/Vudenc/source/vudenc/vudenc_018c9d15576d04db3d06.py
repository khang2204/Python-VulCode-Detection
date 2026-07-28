def delete_users():...
"""docstring"""
deleted = False
con = sql.connect('./resources/users.db')
cmd = 'DELETE FROM users;'
cur = con.cursor()
cur.execute(cmd)
con.commit()
deleted = True
con.close()
return deleted
