def handle_help(message):...
message_time = datetime.utcfromtimestamp(message.created_utc)
add_history_record(username=str(message.author), action='help',
    comment_or_message='message', reddit_time=message_time.strftime(
    '%Y-%m-%d %H:%M:%S'))
response = help_text
message.reply(response)
