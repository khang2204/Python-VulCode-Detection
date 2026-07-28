@staticmethod...
"""docstring"""
requested_user = UserService.get_user_by_username(requested_username)
logged_in_user = UserService.get_user_by_id(logged_in_user_id)
UserService.check_and_update_mapper_level(requested_user.id)
return requested_user.as_dto(logged_in_user.username)
