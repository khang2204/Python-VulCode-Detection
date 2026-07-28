def handle_balance(message):...
username = str(message.author)
message_time = datetime.utcfromtimestamp(message.created_utc)
add_history_record(username=str(message.author), comment_or_message=
    'message', reddit_time=message_time.strftime('%Y-%m-%d %H:%M:%S'),
    action='balance', comment_text=str(message.body)[:255])
mycursor.execute("SELECT address FROM accounts WHERE username='%s'" % username)
result = mycursor.fetchall()
if len(result) > 0:
results = check_balance(result[0][0])
reddit.redditor(username).message('Nano Tipper Z: No account registered.',
    'You do not have an open account yet')
response = (
    """At address %s, you currently have %s Nano available, and %s Nano unpocketed. To pocket any, create a new message containing the word 'receive'

https://www.nanode.co/account/%s"""
     % (result[0][0], results[0] / 10 ** 30, results[1] / 10 ** 30, result[
    0][0]))
reddit.redditor(username).message('Nano Tipper Z account balance', response)
return None
