@staticmethod...
"""docstring"""
user = UserService.get_user_by_id(user_id)
if UserRole(user.role) in [UserRole.VALIDATOR, UserRole.ADMIN, UserRole.
return True
return False
