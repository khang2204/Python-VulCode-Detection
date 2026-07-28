def handle_new_address(message):...
message_time = datetime.utcfromtimestamp(message.created_utc)
add_history_record(username=str(message.author), comment_or_message=
    'message', action='new_address', reddit_time=message_time.strftime(
    '%Y-%m-%d %H:%M:%S'), comment_text=str(message.body)[:255])
message.reply('not activated yet.')
