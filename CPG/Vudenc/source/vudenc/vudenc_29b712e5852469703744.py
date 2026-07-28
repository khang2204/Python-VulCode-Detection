def handle_private_key(message):...
author = str(message.author)
message_time = datetime.utcfromtimestamp(message.created_utc)
add_history_record(username=str(message.author), comment_or_message=
    'message', reddit_time=message_time.strftime('%Y-%m-%d %H:%M:%S'),
    action='private_key', comment_text=str(message.body)[:255])
mycursor.execute(
    "SELECT address, private_key FROM accounts WHERE name='%s'" % author)
result = mycursor.fetchall()
if len(result) > 0:
response = """Your account: %s

Your private key: %s""" % (result[0][0],
    result[0][1])
x = reddit.redditor(username).message('No account found.',
    "You do not currently have an account open.To create one, respond with the text 'create' in the message body."
    )
x = reddit.redditor(username).message('New Private Key', response)
return None
return None
