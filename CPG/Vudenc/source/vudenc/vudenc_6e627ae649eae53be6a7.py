@staticmethod...
"""docstring"""
user = UserService.get_user_by_id(user_id)
return MappingLevel(user.mapping_level)
