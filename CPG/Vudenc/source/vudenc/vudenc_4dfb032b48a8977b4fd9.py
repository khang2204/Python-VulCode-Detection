@bot.message_handler(commands=['start'])...
telegram_id = message.from_user.id
bot.send_message(telegram_id,
    """- Write /start to begin
- You can send files, images, videos, etc. and they will be stored in your current path
- If you write a message to the bot, it will make a directory with that name in the current path
- I have tried to make this bot as similar as possible to a basic file explorer
- You can donate using /donate"""
    )
db.insert('user', {'name': message.from_user.username, 'telegram_id':
    telegram_id}, {'telegram_id': telegram_id})
user_id = db.select('user', 'telegram_id = ' + str(telegram_id))[0]['id']
db.insert('directory', {'name': '/', 'parent_directory_id': 'NULL',
    'user_id': user_id})
explorers[telegram_id] = Explorer(telegram_id)
send_replacing_message(telegram_id, bot)
