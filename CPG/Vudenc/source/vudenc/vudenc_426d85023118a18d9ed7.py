@staticmethod...
"""docstring"""
requested_level = MappingLevel[level.upper()]
user = UserService.get_user_by_username(username)
user.set_mapping_level(requested_level)
return user
