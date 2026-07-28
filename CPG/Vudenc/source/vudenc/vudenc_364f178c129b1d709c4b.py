def as_dto(self, logged_in_username: str) ->UserDTO:...
"""docstring"""
user_dto = UserDTO()
user_dto.id = self.id
user_dto.username = self.username
user_dto.role = UserRole(self.role).name
user_dto.mapping_level = MappingLevel(self.mapping_level).name
user_dto.is_expert = self.is_expert or False
user_dto.date_registered = str(self.date_registered)
user_dto.projects_mapped = len(self.projects_mapped)
user_dto.projects_mapped = 0
user_dto.tasks_mapped = self.tasks_mapped
user_dto.tasks_validated = self.tasks_validated
user_dto.tasks_invalidated = self.tasks_invalidated
user_dto.twitter_id = self.twitter_id
user_dto.linkedin_id = self.linkedin_id
user_dto.facebook_id = self.facebook_id
user_dto.validation_message = self.validation_message
user_dto.total_time_spent = 0
user_dto.time_spent_mapping = 0
user_dto.time_spent_validating = 0
sql = (
    """SELECT SUM(TO_TIMESTAMP(action_text, 'HH24:MI:SS')::TIME) FROM task_history
                WHERE action='LOCKED_FOR_VALIDATION'
                and user_id = {0};"""
    .format(self.id))
total_validation_time = db.engine.execute(sql)
for row in total_validation_time:
total_validation_time = row[0]
sql = (
    """SELECT SUM(TO_TIMESTAMP(action_text, 'HH24:MI:SS')::TIME) FROM task_history
                WHERE action='LOCKED_FOR_MAPPING'
                and user_id = {0};"""
    .format(self.id))
if total_validation_time:
total_mapping_time = db.engine.execute(sql)
total_validation_seconds = total_validation_time.total_seconds()
for row in total_mapping_time:
user_dto.time_spent_validating = total_validation_seconds
total_mapping_time = row[0]
if self.username == logged_in_username:
user_dto.total_time_spent += user_dto.time_spent_validating
if total_mapping_time:
user_dto.email_address = self.email_address
return user_dto
total_mapping_seconds = total_mapping_time.total_seconds()
user_dto.is_email_verified = self.is_email_verified
user_dto.time_spent_mapping = total_mapping_seconds
user_dto.total_time_spent += user_dto.time_spent_mapping
