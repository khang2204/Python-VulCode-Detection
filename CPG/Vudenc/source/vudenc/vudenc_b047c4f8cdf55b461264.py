def content_builder(content, up=True):...
markup = telebot.types.InlineKeyboardMarkup()
if up:
markup.add(telebot.types.InlineKeyboardButton('⤴️ Go up', callback_data='..'))
if content['directories']:
for each in content['directories']:
if content['files']:
markup.add(telebot.types.InlineKeyboardButton('📁 ' + each['name'],
    callback_data='d' + str(each['id'])), telebot.types.
    InlineKeyboardButton('❌', callback_data='rd' + str(each['id'])))
for each in content['files']:
return markup
if each['mime'] in icon_mime:
icon = icon_mime[each['mime']]
icon = icon_mime['U']
markup.add(telebot.types.InlineKeyboardButton(icon + ' ' + each['name'],
    callback_data='f' + str(each['id'])), telebot.types.
    InlineKeyboardButton('❌', callback_data='rf' + str(each['id'])))
