def find_one(self, message: Message) ->User:...
"""docstring"""
user = self.users.get(message.chat.id, None)
if user:
return user
log.debug("Looking up the user in the database as it doesn't appear in cache")
query = (
    f'SELECT first_name, nickname, last_name, language FROM users WHERE chat_id={message.chat.id}'
    )
cursor = db.execute_query(query)
log.error('Cannot lookup the user with chat_id %d in database', message.chat.id
    )
if not cursor.rowcount:
msg = message.from_user
log.info('Adding totally new user to the system...')
log.debug('User %d has been found in the database', message.chat.id)
user = self.add_new_one(message.chat.id, msg.first_name, msg.last_name, msg
    .username, language='en-US', add_to_db=False)
msg = message.from_user
user_data = cursor.fetchall()[0]
return user
user = self.add_new_one(message.chat.id, msg.first_name, msg.last_name, msg
    .username, language='en-US')
user = self.add_new_one(message.chat.id, *user_data, add_to_db=False)
bot.send_message(config.MY_TELEGRAM, text=f'You have a new user! {user}')
return user
log.info('You have a new user! Welcome %s', user)
