@staticmethod...
"""docstring"""
user = UserService.get_user_by_id(user_id)
user.set_is_expert(is_expert)
return user
