def update(self, user_dto: UserDTO):...
"""docstring"""
self.email_address = user_dto.email_address.lower(
    ) if user_dto.email_address else None
self.twitter_id = user_dto.twitter_id.lower() if user_dto.twitter_id else None
self.facebook_id = user_dto.facebook_id.lower(
    ) if user_dto.facebook_id else None
self.linkedin_id = user_dto.linkedin_id.lower(
    ) if user_dto.linkedin_id else None
self.validation_message = user_dto.validation_message
db.session.commit()
