@bot.message_handler(content_types=['document', 'audio', 'document',...
telegram_id = message.from_user.id
if message.document != None:
if message.document.mime_type in mime_conv:
if message.audio != None:
mime = mime_conv[message.document.mime_type]
mime = 'U'
explorers[telegram_id].new_file(message.message_id, 'audio' + str(message.
    date), 'A', message.audio.file_size)
if message.document != None:
explorers[telegram_id].new_file(message.message_id, message.document.
    file_name, mime, message.document.file_size)
bot.reply_to(message, '👌')
explorers[telegram_id].new_file(message.message_id, 'document' + str(
    message.date), 'D', message.document.file_size)
if message.photo != None:
send_replacing_message(telegram_id, bot)
explorers[telegram_id].new_file(message.message_id, 'photo' + str(message.
    date), 'P', message.photo[0].file_size)
if message.video != None:
explorers[telegram_id].new_file(message.message_id, 'video' + str(message.
    date), 'V', message.video.file_size)
if message.video_note != None:
explorers[telegram_id].new_file(message.message_id, 'video_note' + str(
    message.date), 'V', message.video_note.file_size)
if message.voice != None:
explorers[telegram_id].new_file(message.message_id, 'voice' + str(message.
    date), 'A', message.voice.file_size)
if message.contact != None:
explorers[telegram_id].new_file(message.message_id, 'contact' + str(message
    .date), 'D', message.contact.file_size)
