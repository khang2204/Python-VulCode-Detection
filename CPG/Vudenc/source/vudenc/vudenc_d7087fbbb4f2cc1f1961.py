def get_messages(page):...
"""docstring"""
con = sql.connect('./resources/messages.db')
return_obj = []
cmd = (
    """SELECT * FROM messages 
             ORDER BY timeposted DESC 
             LIMIT 25 OFFSET {0};
    """
    .format(str(25 * (page - 1))))
cur = con.cursor()
print(''.join(traceback.format_exception(etype=type(e), value=e, tb=e.
    __traceback__)))
con.close()
cur.execute(cmd)
con.rollback()
return return_obj
messages = cur.fetchall()
return_obj = {'error': 'error getting messages'}
if cur.rowcount != 0:
for message in messages:
return_obj = []
return_obj.append({'id': message[0], 'content': message[1], 'posterId':
    message[2], 'posterUsername': message[3], 'posterFirstname': message[4],
    'posterLastname': message[5], 'likes': message[6], 'comments': 
    __get_comments(message[7]) if message[7] is not None else None,
    'timePosted': message[8], 'eventTime': message[9]})
