@staticmethod...
"""docstring"""
user_messages = Message.query.filter(Message.to_user_id == user_id).all()
if len(user_messages) == 0:
messages_dto = MessagesDTO()
for message in user_messages:
messages_dto.user_messages.append(message.as_dto())
return messages_dto
