def handle_send_nano(message, parsed_text, comment_or_message):...
user_or_address = ''
private_key = ''
adrress = ''
recipient = ''
recipient_username = ''
recipient_address = ''
message_time = datetime.utcfromtimestamp(message.created_utc)
username = str(message.author)
entry_id = add_history_record(username=username, action='send',
    comment_or_message=comment_or_message, comment_id=message.id,
    reddit_time=message_time.strftime('%Y-%m-%d %H:%M:%S'), comment_text=
    str(message.body)[:255])
if len(parsed_text) >= 3:
amount = parsed_text[1]
if len(parsed_text) == 2:
recipient = parsed_text[2]
sql = 'UPDATE history SET notes = %s WHERE id = %s'
if parsed_text[1].lower() == 'nan' or 'inf' in parsed_text[1].lower():
val = 'could not find tip amount', entry_id
sql = 'UPDATE history SET notes = %s WHERE id = %s'
amount = float(parsed_text[1])
sql = 'UPDATE history SET notes = %s WHERE id = %s'
if amount < program_minimum:
mycursor.execute(sql, val)
val = 'could not parse amount', entry_id
val = 'could not parse amount', entry_id
sql = 'UPDATE history SET notes = %s WHERE id = %s'
mycursor.execute(
    "SELECT address, private_key FROM accounts WHERE username='%s'" % username)
mydb.commit()
mycursor.execute(sql, val)
mycursor.execute(sql, val)
val = 'amount below program limit', entry_id
result = mycursor.fetchall()
return 'Could not read your tip or send command, or find an amount. Be sure the amount and recipient are separated by a space.'
mydb.commit()
mydb.commit()
mycursor.execute(sql, val)
if len(result) < 1:
return "Could not read your tip or send amount. Is '%s' a number?" % parsed_text[
    1]
return "Could not read your tip or send amount. Is '%s' a number?" % parsed_text[
    1]
mydb.commit()
sql = 'UPDATE history SET notes = %s WHERE id = %s'
address = result[0][0]
return 'You must send amounts of Nano above the program limit of %s.' % program_minimum
val = 'sender does not have an account', entry_id
private_key = result[0][1]
mycursor.execute(sql, val)
results = check_balance(result[0][0])
mydb.commit()
if nano_to_raw(amount) > results[0]:
return "You do not have a tip bot account yet. To create one, send me a PM containing the text 'create' in the message body, or get a tip from a fellow redditor!."
sql = 'UPDATE history SET notes = %s WHERE id = %s'
if len(parsed_text) == 2:
val = 'insufficient funds', entry_id
if comment_or_message == 'comment':
if recipient[:3].lower() == '/u/':
mycursor.execute(sql, val)
recipient = str(message.parent().author)
sql = 'UPDATE history SET notes = %s, WHERE id = %s'
recipient = recipient[3:]
if recipient[:5].lower() == 'nano_' or recipient[:4].lower() == 'xrb_':
mydb.commit()
val = 'no recipient specified', entry_id
print(recipient)
success = validate_address(recipient)
print(getattr(reddit.redditor(recipient), 'is_suspended', False))
sql = 'UPDATE history SET notes = %s WHERE id = %s'
user_minimum = -1
return 'You have insufficient funds. Your account has %s pocketed (+%s unpocketed) and you are trying to send %s. If you have unpocketed funds, create a new message containing the text "receive" to pocket your incoming money.' % (
    results[0] / 10 ** 30, results[1] / 10 ** 30, amount)
mycursor.execute(sql, val)
if success['valid'] == '1':
user_or_address = 'user'
val = 'redditor does not exist', entry_id
if user_or_address == 'user':
mydb.commit()
user_or_address = 'address'
print(getattr(reddit.redditor(recipient), 'is_suspended', False))
sql = 'UPDATE history SET notes = %s WHERE id = %s'
mycursor.execute(sql, val)
recipient_username = recipient
recipient_address = recipient
return 'You must specify an amount and a user.'
user_or_address = 'user'
val = 'invalid address or address-like redditor does not exist', entry_id
mydb.commit()
sql = 'SELECT minimum, address FROM accounts WHERE username = %s'
recipient_username = check_registered_by_address(recipient_address)
mycursor.execute(sql, val)
return "Could not find redditor %s. Make sure you aren't writing or copy/pasting markdown." % recipient
val = recipient_username,
if recipient_username:
mydb.commit()
mycursor.execute(sql, val)
sql = 'SELECT minimum, address FROM accounts WHERE username = %s'
if user_minimum >= 0 and recipient_address and recipient_username:
return '%s is neither a valid address or redditor' % recipient
myresult = mycursor.fetchall()
val = recipient_username,
if nano_to_raw(amount) < user_minimum:
if recipient_address:
if len(myresult) > 0:
mycursor.execute(sql, val)
sql = 'UPDATE history SET notes = %s WHERE id = %s'
if user_or_address == 'user':
sql = (
    'UPDATE history SET notes = %s, address = %s, username = %s, recipient_address = %s, amount = %s WHERE id = %s'
    )
recipient_address = add_new_account(recipient_username)
print(myresult[0])
myresult = mycursor.fetchall()
val = 'below user minimum', entry_id
notes = 'sent to registered redditor'
notes = 'sent to registered address'
val = ('sent to unregistered address', address, username, recipient_address,
    str(nano_to_raw(amount)), entry_id)
x = reddit.redditor(recipient_username).message(
    'Congrats on receiving your first Nano Tip!', 
    """Welcome to Nano Tip Bot! You have just received a Nano tip in the amount of %s at your address of %s. Here is some boilerplate.

"""
     % (amount, recipient_address) + help_text)
user_minimum = int(myresult[0][0])
print(myresult[0])
mycursor.execute(sql, val)
receiving_new_balance = check_balance(recipient_address)
mycursor.execute(sql, val)
sql = (
    'UPDATE history SET notes = %s, address = %s, username = %s, recipient_username = %s, recipient_address = %s, amount = %s WHERE id = %s'
    )
recipient_address = myresult[0][1]
user_minimum = float(myresult[0][0])
mydb.commit()
sql = (
    'UPDATE history SET notes = %s, address = %s, username = %s, recipient_username = %s, recipient_address = %s, amount = %s WHERE id = %s'
    )
mydb.commit()
val = ('new user created', address, username, recipient_username,
    recipient_address, str(nano_to_raw(amount)), entry_id)
return 'Sorry, the user has set a tip minimum of %s. Your tip of %s is below this amount.' % (
    user_minimum / 10 ** 30, amount)
val = notes, address, username, recipient_username, recipient_address, str(
    nano_to_raw(amount)), entry_id
print('Sending Unregistered Address: ', address, private_key, nano_to_raw(
    amount), recipient_address)
mycursor.execute(sql, val)
mycursor.execute(sql, val)
sent = send(address, private_key, nano_to_raw(amount), recipient_address)
mydb.commit()
mydb.commit()
print('Hash: ', sent)
sent = send(address, private_key, nano_to_raw(amount), recipient_address)
print('Sending Nano: ', address, private_key, nano_to_raw(amount),
    recipient_address, recipient_username)
sql = 'UPDATE history SET hash = %s WHERE id = %s'
print('Hash: ', sent)
sent = send(address, private_key, nano_to_raw(amount), recipient_address)
val = sent['hash'], entry_id
sql = 'UPDATE history SET hash = %s WHERE id = %s'
print('Hash: ', sent)
mycursor.execute(sql, val)
val = sent['hash'], entry_id
sql = 'UPDATE history SET hash = %s WHERE id = %s'
mydb.commit()
mycursor.execute(sql, val)
val = sent['hash'], entry_id
return 'Sent %s Nano to address %s.' % (amount, recipient_address)
mydb.commit()
mycursor.execute(sql, val)
print('Sending New Account Address: ', address, private_key, nano_to_raw(
    amount), recipient_address, recipient_username)
mydb.commit()
return 'Creating a new account for %s and sending %s Nano.' % (
    recipient_username, amount)
x = reddit.redditor(recipient_username).message(
    'You just received a new Nano tip!', 
    'You have been tipped %s Nano at your address of %s. Your new account balance will be %s received and %s unpocketed.'
     % (amount, recipient_address, receiving_new_balance[0] / 10 ** 30, 
    receiving_new_balance[1] / 10 ** 30 + amount))
if user_or_address == 'user':
return 'Sent %s Nano to %s.' % (amount, recipient_username)
return 'Sent %s Nano to %s.' % (amount, recipient_address)
