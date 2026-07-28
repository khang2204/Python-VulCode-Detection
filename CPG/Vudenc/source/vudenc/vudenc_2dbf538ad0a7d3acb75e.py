def handle_send(message):...
parsed_text = str(message.body).lower().replace('\\', '').split('\n')[0].split(
    ' ')
response = handle_send_nano(message, parsed_text, 'message')
message.reply(response + comment_footer)
