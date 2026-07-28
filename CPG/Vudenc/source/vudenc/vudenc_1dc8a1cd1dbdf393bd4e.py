@bot.message_handler(content_types=['document'])...
user = users.find_one(message)
bot.reply_to(message, messages[user.language]['photo_prcs'])
log.info('%s sent photo as a file.', user)
photo_message = PhotoMessage(message, user)
answer = photo_message.prepare_answer()
if answer[0][0]:
lon = answer[0][0]
bot.reply_to(message, answer, parse_mode='Markdown')
lat = answer[0][1]
bot.send_location(user.chat_id, lon, lat, live_period=None)
bot.reply_to(message, answer[1], parse_mode='Markdown')
