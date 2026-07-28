def remove_messages(telegram_id, bot):...
result = []
if explorers[telegram_id].last_action_message_ids:
for message_id in explorers[telegram_id].last_action_message_ids:
return result
result.append(bot.delete_message(telegram_id, message_id))
explorers[telegram_id].last_action_message_ids.remove(message_id)
