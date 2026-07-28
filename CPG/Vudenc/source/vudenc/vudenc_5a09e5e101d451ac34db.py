@bot.callback_query_handler(func=lambda call: True)...
bot.answer_callback_query(callback_query_id=call.id, show_alert=False)
if call.data == 'off':
if db.disconnect():
if call.data == 'last active':
bot.turn_off()
log.error('Cannot stop bot.')
bot.send_message(config.MY_TELEGRAM, text=get_admin_stat('last active users'))
if call.data == 'total number photos sent':
bot.send_message(chat_id=config.MY_TELEGRAM, text='Cannot stop bot.')
bot.send_message(config.MY_TELEGRAM, text=get_admin_stat(
    'total number photos sent'))
if call.data == 'photos today':
bot.send_message(config.MY_TELEGRAM, text=get_admin_stat('photos today'))
if call.data == 'number of users':
bot.send_message(config.MY_TELEGRAM, text=get_admin_stat('number of users'))
if call.data == 'number of gadgets':
bot.send_message(config.MY_TELEGRAM, text=get_admin_stat('number of gadgets'))
if call.data == 'uptime':
bot.send_message(config.MY_TELEGRAM, text=get_admin_stat('uptime'))
