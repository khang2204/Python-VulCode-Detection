def handle_comment(message):...
if message.body[0] == ' ':
parsed_text = str(message.body[1:]).lower().replace('\\', '').split('\n')[0
    ].split(' ')
parsed_text = str(message.body).lower().replace('\\', '').split('\n')[0].split(
    ' ')
print(parsed_text)
print(len(parsed_text))
response = handle_send_nano(message, parsed_text, 'comment')
message.reply(response + comment_footer)
