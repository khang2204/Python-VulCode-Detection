@bot.message_handler(commands=['start'])...
user = users.find_one(message)
current_user_lang = user.language
markup = types.ReplyKeyboardMarkup(one_time_keyboard=True, resize_keyboard=True
    )
markup.row('Русский/English')
markup.row(messages[current_user_lang]['top_cams'])
markup.row(messages[current_user_lang]['top_lens'])
markup.row(messages[current_user_lang]['top_countries'])
bot.send_message(user.chat_id, messages[current_user_lang]['menu_header'],
    reply_markup=markup)
