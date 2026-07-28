@staticmethod...
"""docstring"""
user = UserService.get_user_by_username(user_name)
return User.get_mapped_projects(user.id, preferred_locale)
