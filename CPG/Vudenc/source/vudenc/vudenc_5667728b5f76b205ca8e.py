def update_profile(user_id, firstname, lastname, username, password, bio):...
"""docstring"""
updated = False
con = sql.connect('./resources/users.db')
cur = con.cursor()
print(''.join(traceback.format_exception(etype=type(e), value=e, tb=e.
    __traceback__)))
con.close()
"""
        info = (username, firstname, lastname, bio, password)
        cur.execute(cmd, info)
        """
con.rollback()
return updated
if firstname != None:
updated = False
cur.execute('UPDATE users SET firstname = ? WHERE id = ? LIMIT 1;', (
    firstname, user_id))
if lastname != None:
cur.execute('UPDATE users SET lastname = ? WHERE id = ? LIMIT 1;', (
    lastname, user_id))
if username != None:
cur.execute('UPDATE users SET username = ? WHERE id = ? LIMIT 1;', (
    username, user_id))
if password != None:
cur.execute('UPDATE users SET password = ? WHERE id = ? LIMIT 1;', (
    password, user_id))
if bio != None:
cur.execute('UPDATE users SET bio = ? WHERE id = ? LIMIT 1;', (bio, user_id))
con.commit()
updated = True
