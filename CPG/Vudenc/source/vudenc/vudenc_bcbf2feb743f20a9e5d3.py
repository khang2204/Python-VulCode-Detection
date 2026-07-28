@classmethod...
"""docstring"""
message = cls()
message.subject = dto.subject
message.message = dto.message
message.from_user_id = dto.from_user_id
message.to_user_id = to_user_id
message.project_id = dto.project_id
message.task_id = dto.task_id
if dto.message_type is not None:
message.message_type = MessageType(dto.message_type)
return message
