@bot.message_handler(content_types=['text'])...
current_user_lang = users.find_one(message).language
user = users.find_one(message)
if message.text == 'Русский/English':
new_lang = users.find_one(message).switch_language()
if message.text == messages[current_user_lang]['top_cams']:
if current_user_lang != new_lang:
log.info('User %s asked for top cams', user)
if message.text == messages[current_user_lang]['top_lens']:
bot.send_message(user.chat_id, messages[new_lang]['switch_lang_success'])
bot.send_message(user.chat_id, messages[new_lang]['switch_lang_failure'])
bot.send_message(user.chat_id, text=get_most_popular_items('camera_name',
    message))
log.info('User %s asked for top lens', user)
if message.text == messages[current_user_lang]['top_countries']:
create_main_keyboard(message)
create_main_keyboard(message)
log.info('List of most popular cameras has been returned to %s', user)
bot.send_message(user.chat_id, text=get_most_popular_items('lens_name',
    message))
log.info('User %s asked for top countries', user)
if message.text.lower() == 'admin' and user.chat_id == int(config.MY_TELEGRAM):
users.compare_and_update(user, message)
log.info('List of most popular lens has been returned to %s', user)
lang_table_name = ('country_ru' if current_user_lang == 'ru-RU' else
    'country_en')
keyboard = types.InlineKeyboardMarkup()
log.info('%s sent text message.', user)
bot.send_message(user.chat_id, text=get_most_popular_items(lang_table_name,
    message))
button = types.InlineKeyboardButton
bot.send_message(user.chat_id, messages[current_user_lang]['dont_speak'])
log.info('List of most popular countries has been returned to %s', user)
keyboard.add(button(text='Turn bot off', callback_data='off'))
keyboard.add(button(text='Last active users', callback_data='last active'))
keyboard.add(button(text='Total number of photos were sent', callback_data=
    'total number photos sent'))
keyboard.add(button(text='Number of photos today', callback_data=
    'photos today'))
keyboard.add(button(text='Number of users', callback_data='number of users'))
keyboard.add(button(text='Number of gadgets', callback_data=
    'number of gadgets'))
keyboard.add(button(text='Uptime', callback_data='uptime'))
bot.send_message(config.MY_TELEGRAM, 'Admin commands', reply_markup=keyboard)
