@bot.message_handler(commands=['donate'])...
markup = telebot.types.InlineKeyboardMarkup()
markup.add(telebot.types.InlineKeyboardButton('PayPal', url=
    'https://www.paypal.me/victor141516'))
bot.send_message(message.from_user.id, 'Thank you!', reply_markup=markup)
