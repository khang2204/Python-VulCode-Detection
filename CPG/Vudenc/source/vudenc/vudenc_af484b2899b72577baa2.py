@staticmethod...
"""docstring"""
requested_user = UserService.get_user_by_id(requested_user)
return requested_user.as_dto(requested_user.username)
