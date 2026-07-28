@staticmethod...
"""docstring"""
user = UserService.get_user_by_id(user_id)
if UserRole(user.role) == UserRole.READ_ONLY:
return True
return False
