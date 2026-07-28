@staticmethod...
"""docstring"""
user = UserService.get_user_by_id(user_id)
user_level = MappingLevel(user.mapping_level)
if user_level == MappingLevel.ADVANCED:
return
intermediate_level = current_app.config['MAPPER_LEVEL_INTERMEDIATE']
advanced_level = current_app.config['MAPPER_LEVEL_ADVANCED']
osm_details = OSMService.get_osm_details_for_user(user_id)
current_app.logger.error('Error attempting to update mapper level')
user.save()
if osm_details.changeset_count > advanced_level and user.mapping_level != MappingLevel.ADVANCED.value:
return
return user
user.mapping_level = MappingLevel.ADVANCED.value
if intermediate_level < osm_details.changeset_count < advanced_level and user.mapping_level != MappingLevel.INTERMEDIATE.value:
UserService.notify_level_upgrade(user_id, user.username, 'ADVANCED')
user.mapping_level = MappingLevel.INTERMEDIATE.value
UserService.notify_level_upgrade(user_id, user.username, 'INTERMEDIATE')
