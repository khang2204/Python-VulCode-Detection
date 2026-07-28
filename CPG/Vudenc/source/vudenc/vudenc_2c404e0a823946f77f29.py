@bot.message_handler(func=lambda m: True)...
new_directory_name = message.text
telegram_id = message.from_user.id
explorers[telegram_id].new_directory(new_directory_name)
content = explorers[telegram_id].get_directory_content()
keyboard = content_builder(content, len(explorers[telegram_id].path) > 1)
remove_messages(telegram_id, bot)
message_sent = bot.send_message(telegram_id, explorers[telegram_id].
    get_path_string(), reply_markup=keyboard)
explorers[telegram_id].last_action_message_ids.append(message_sent.message_id)
