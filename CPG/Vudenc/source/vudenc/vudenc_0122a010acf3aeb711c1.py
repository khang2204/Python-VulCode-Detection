def handle_receive(message):...
message_time = datetime.utcfromtimestamp(message.created_utc)
username = str(message.author)
mycursor.execute(
    "SELECT address, private_key FROM accounts WHERE username='%s'" % username)
result = mycursor.fetchall()
if len(result) > 0:
open_or_receive(result[0][0], result[0][1])
add_history_record(username=username, action='receive', reddit_time=
    message_time.strftime('%Y-%m-%d %H:%M:%S'), comment_or_message='message')
balance = check_balance(result[0][0])
response = (
    "You do not currently have an account open. To create one, respond with the text 'create' in the message body."
    )
add_history_record(username=username, action='receive', reddit_time=
    message_time.strftime('%Y-%m-%d %H:%M:%S'), address=result[0][0],
    comment_or_message='message')
message.reply(response)
response = (
    "You currently have %s Nano available, and %s Nano unpocketed. To pocket any, create a new message containing the word 'receive' in the body"
     % (balance[0] / 10 ** 30, balance[1] / 10 ** 30))
message.reply(response)
