@staticmethod...
"""docstring"""
user = UserService.get_user_by_id(user_id)
return user.has_user_accepted_licence(license_id)
