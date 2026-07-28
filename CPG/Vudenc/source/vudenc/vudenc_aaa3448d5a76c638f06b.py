@staticmethod...
user = UserService.get_user_by_id(user_id)
if user.username != osm_username:
user.update_username(osm_username)
return user
