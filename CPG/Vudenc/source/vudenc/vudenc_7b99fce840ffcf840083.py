def handle_create(message):...
message_time = datetime.utcfromtimestamp(message.created_utc)
add_history_record(username=str(message.author), comment_or_message=
    'message', reddit_time=message_time.strftime('%Y-%m-%d %H:%M:%S'),
    action='create', comment_text=str(message.body)[:255])
username = str(message.author)
mycursor.execute("SELECT address FROM accounts WHERE username='%s'" % username)
result = mycursor.fetchall()
if len(result) is 0:
address = add_new_account(username)
response = (
    """It looks like you already have an account made. Your Nano address is %s. Once Nano is sent to your account, your balance will be unpocketed until you respond and have 'receive' in the message body.

https://www.nanode.co/account/%s"""
     % (result[0][0], result[0][0]))
response = (
    """Hi! I have created a new account for you. Your Nano address is %s. Once Nano is sent to your new account, your balance will be unpocketed until you respond and have 'receive' in the message body.

https://www.nanode.co/account/%s"""
     % (address, address))
x = reddit.redditor(username).message('Nano Tipper Z: Account Creation',
    response)
