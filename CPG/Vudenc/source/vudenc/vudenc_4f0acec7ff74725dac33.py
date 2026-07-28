@bot.message_handler(content_types=['photo'])...
user = users.find_one(message)
bot.send_message(user.chat_id, messages[user.language]['as_file'])
log.info('%s sent photo as a photo.', user)
