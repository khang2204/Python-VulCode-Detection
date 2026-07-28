def handle_message(message):...
message_body = str(message.body).lower()
print('Body: **', message_body, '**')
if message.body[0] == ' ':
parsed_text = str(message.body[1:]).lower().replace('\\', '').split('\n')[0
    ].split(' ')
parsed_text = str(message.body).lower().replace('\\', '').split('\n')[0].split(
    ' ')
print('Parsed Text:', parsed_text)
if parsed_text[0].lower() == 'help':
print('Helping')
if parsed_text[0].lower() == 'minimum':
handle_help(message)
print('Setting Minimum')
if parsed_text[0].lower() == 'create':
handle_minimum(message)
print('Creating')
if parsed_text[0].lower() == 'private_key':
handle_create(message)
print('private_keying')
if parsed_text[0].lower() == 'new_address':
print('new address')
if parsed_text[0].lower() == 'send':
print('send via PM')
if parsed_text[0].lower() == 'receive':
handle_send(message)
print('receive')
if parsed_text[0].lower() == 'balance':
handle_receive(message)
print('balance')
add_history_record(username=str(message.author), comment_text=str(message.
    body)[:255], comment_or_message='message')
handle_balance(message)
