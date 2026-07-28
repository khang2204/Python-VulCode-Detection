def as_dto(self) ->MessageDTO:...
"""docstring"""
dto = MessageDTO()
dto.message_id = self.id
dto.message = self.message
dto.sent_date = self.date
dto.read = self.read
dto.subject = self.subject
dto.project_id = self.project_id
dto.task_id = self.task_id
if self.message_type is not None:
dto.message_type = MessageType(self.message_type).name
if self.from_user_id:
dto.from_username = self.from_user.username
return dto
