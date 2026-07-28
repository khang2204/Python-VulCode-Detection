@staticmethod...
"""docstring"""
user = UserService.get_user_by_username(username)
osm_dto = OSMService.get_osm_details_for_user(user.id)
return osm_dto
