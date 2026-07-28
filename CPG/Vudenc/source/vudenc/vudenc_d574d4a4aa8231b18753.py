def add_message(message, timeposted, eventtime, poster_id, poster_username,...
"""docstring"""
con = sql.connect('./resources/messages.db')
likes = 0
comments = ''
if eventtime == None:
eventtime = 'NULL'
cmd = """INSERT INTO messages (message, poster_id, poster_username,
                 poster_firstname, poster_lastname, likes, comments,
                 timeposted, eventtime)
             VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?);"""
cur = con.cursor()
print(''.join(traceback.format_exception(etype=type(e), value=e, tb=e.
    __traceback__)))
con.close()
info = (message, poster_id, poster_username, poster_firstname,
    poster_lastname, likes, comments, timeposted, eventtime)
con.rollback()
return success
cur.execute(cmd, info)
success = False
con.commit()
success = True
