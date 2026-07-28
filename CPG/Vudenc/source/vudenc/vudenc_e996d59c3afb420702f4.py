def notify_level_upgrade(user_id: int, username: str, level: str):...
text_template = get_template('level_upgrade_message_en.txt')
if username is not None:
text_template = text_template.replace('[USERNAME]', username)
text_template = text_template.replace('[LEVEL]', level)
level_upgrade_message = Message()
level_upgrade_message.to_user_id = user_id
level_upgrade_message.subject = 'Mapper Level Upgrade '
level_upgrade_message.message = text_template
level_upgrade_message.save()
