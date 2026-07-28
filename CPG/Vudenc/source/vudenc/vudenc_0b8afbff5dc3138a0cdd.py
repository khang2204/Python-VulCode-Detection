def add_user(username, firstname, lastname, bio, password):...
"""docstring"""
added = False
con = sql.connect('./resources/users.db')
cmd = """INSERT INTO users (username, firstname, lastname, bio, password)
             VALUES (?, ?, ?, ?, ?);
             """
cur = con.cursor()
print(''.join(traceback.format_exception(etype=type(e), value=e, tb=e.
    __traceback__)))
con.close()
cur.execute(cmd, (new_bio, new_password))
con.rollback()
return added
con.commit()
added = False
added = True
