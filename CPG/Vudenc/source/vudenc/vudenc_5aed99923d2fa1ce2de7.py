def add_history_record(username=None, action=None, sql_time=None, address=...
if sql_time is None:
sql_time = time.strftime('%Y-%m-%d %H:%M:%S')
sql = (
    'INSERT INTO history (username, action, sql_time, address, comment_or_message, recipient_username, recipient_address, amount, hash, comment_id, notes, reddit_time, comment_text) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)'
    )
val = (username, action, sql_time, address, comment_or_message,
    recipient_username, recipient_address, amount, hash, comment_id, notes,
    reddit_time, comment_text)
mycursor.execute(sql, val)
mydb.commit()
return mycursor.lastrowid
