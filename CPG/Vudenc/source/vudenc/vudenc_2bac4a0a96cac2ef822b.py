def add_new_one(self, chat_id, first_name, nickname, last_name, language,...
"""docstring"""
user = User(chat_id, first_name, nickname, last_name, language)
self.users[chat_id] = user
if add_to_db:
self._add_to_db(user)
return user
