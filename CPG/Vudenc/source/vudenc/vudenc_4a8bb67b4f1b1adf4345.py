@staticmethod...
"""docstring"""
user = UserService.get_user_by_id(user_id)
if UserRole(user.role) in [UserRole.ADMIN, UserRole.PROJECT_MANAGER]:
return True
return False
