@bot.callback_query_handler(func=lambda call: True)...
telegram_id = call.from_user.id
action = call.data[:1]
content_id = call.data[1:]
if call.data == '..':
explorers[telegram_id].go_to_parent_directory()
if action == 'd':
send_replacing_message(telegram_id, bot)
explorers[telegram_id].go_to_directory(content_id)
if action == 'f':
content_id = db.select('file', 'id = ' + content_id)[0]['telegram_id']
if action == 'r':
bot.forward_message(telegram_id, telegram_id, content_id)
is_directory = content_id[:1] == 'd'
content_id = content_id[1:]
if is_directory:
explorers[telegram_id].remove_directories([content_id])
explorers[telegram_id].remove_files([content_id])
