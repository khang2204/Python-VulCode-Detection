def get_user_profile(user_id):...
"""docstring"""
user_con = sql.connect('./resources/users.db')
message_con = sql.connect('./resources/messages.db')
messages = []
user_cur = user_con.cursor()
print(''.join(traceback.format_exception(etype=type(e), value=e, tb=e.
    __traceback__)))
user_con.close()
user_cur.execute('SELECT * FROM users WHERE id = {0} LIMIT 1;'.format(user_id))
user_con.rollback()
message_con.close()
row = user_cur.fetchone()
message_con.rollback()
return success, username, firstname, lastname, bio, messages
message_cur = message_con.cursor()
success = False
cmd = (
    """SELECT * FROM messages
                  WHERE poster_id = {0}
                  ORDER BY timeposted
                  DESC LIMIT 25;
        """
    .format(user_id))
username = firstname = lastname = bio = None
message_cur.execute(cmd)
unformatted_messages = message_cur.fetchall()
if unformatted_messages != None:
for message in unformatted_messages:
messages = None
messages.append({'content': message[1], 'likes': message[6], 'comments':
    message[7], 'timeposted': message[8], 'eventtime': message[9]})
success = True
username = row[1]
firstname = row[2]
lastname = row[3]
bio = row[4]
