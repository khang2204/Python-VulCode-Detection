def handle_minimum(message):...
message_time = datetime.utcfromtimestamp(message.created_utc)
username = str(message.author)
parsed_text = message.body.replace('\\', '').split('\n')[0].split(' ')
if len(parsed_text) < 2:
response = (
    "I couldn't parse your command. I was expecting 'minimum <amount>'. Be sure to check your spacing."
    )
if parsed_text[1].lower() == 'nan' or 'inf' in parsed_text[1].lower():
message.reply(response)
response = (
    "'%s' didn't look like a number to me. If it is blank, there might be extra spaces in the command."
    )
amount = float(parsed_text[1])
response = (
    "'%s' didn't look like a number to me. If it is blank, there might be extra spaces in the command."
    )
if nano_to_raw(amount) < nano_to_raw(0.01):
return None
message.reply(response)
message.reply(response)
response = 'The overall tip minimum is 0.01 Nano.'
sql = 'SELECT address FROM accounts WHERE username=%s'
message.reply(response)
val = username,
mycursor.execute(sql, val)
result = mycursor.fetchall()
print(result)
if len(result) > 0:
add_history_record(username=username, action='minimum', amount=nano_to_raw(
    amount), address=result[0][0], comment_or_message='message',
    reddit_time=message_time.strftime('%Y-%m-%d %H:%M:%S'), comment_text=
    str(message.body)[:255])
add_history_record(username=username, action='minimum', reddit_time=
    message_time.strftime('%Y-%m-%d %H:%M:%S'), amount=nano_to_raw(amount),
    comment_text=str(message.body)[:255])
sql = 'UPDATE accounts SET minimum = %s WHERE username = %s'
response = (
    "You do not currently have an account open. To create one, respond with the text 'create' in the message body."
    )
print(amount)
message.reply(response)
print(nano_to_raw(amount))
val = str(nano_to_raw(amount)), username
print(val)
mycursor.execute(sql, val)
mydb.commit()
response = 'Updating tip minimum to %s' % amount
message.reply(response)
