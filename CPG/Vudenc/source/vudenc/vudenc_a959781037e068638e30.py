@staticmethod...
"""docstring"""
log.info('Checking whether user have changed his info or not...')
msg = message.from_user
usr_from_message = User(message.chat.id, msg.first_name, msg.username, msg.
    last_name)
if user.chat_id != usr_from_message.chat_id:
log.error('Wrong user to compare!')
if user.first_name != usr_from_message.first_name:
return
user.first_name = usr_from_message.first_name
if user.nickname != usr_from_message.nickname:
log.info('User has changed his info')
user.nickname = usr_from_message.nickname
if user.last_name != usr_from_message.last_name:
log.debug("Updating user's info in the database...")
user.last_name = usr_from_message.last_name
log.debug("User's info hasn't changed")
query = (
    f"UPDATE users SET first_name='{user.first_name}', nickname='{user.nickname}', last_name='{user.last_name}' WHERE chat_id={user.chat_id}"
    )
return
db.add(query)
log.error('Could not update info about %s in the database', user)
log.debug("User's info has been updated")
