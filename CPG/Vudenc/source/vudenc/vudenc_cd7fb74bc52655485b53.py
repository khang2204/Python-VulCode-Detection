@staticmethod...
"""docstring"""
requested_role = UserRole[role.upper()]
admin = UserService.get_user_by_id(admin_user_id)
admin_role = UserRole(admin.role)
if admin_role == UserRole.PROJECT_MANAGER and requested_role == UserRole.ADMIN:
if admin_role == UserRole.PROJECT_MANAGER and requested_role == UserRole.PROJECT_MANAGER:
user = UserService.get_user_by_username(username)
user.set_user_role(requested_role)
