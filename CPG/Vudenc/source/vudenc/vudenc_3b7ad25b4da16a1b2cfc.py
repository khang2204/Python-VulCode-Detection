@staticmethod...
"""docstring"""
new_user = User()
new_user.id = osm_id
new_user.username = username
intermediate_level = current_app.config['MAPPER_LEVEL_INTERMEDIATE']
advanced_level = current_app.config['MAPPER_LEVEL_ADVANCED']
if changeset_count > advanced_level:
new_user.mapping_level = MappingLevel.ADVANCED.value
if intermediate_level < changeset_count < advanced_level:
new_user.create()
new_user.mapping_level = MappingLevel.INTERMEDIATE.value
new_user.mapping_level = MappingLevel.BEGINNER.value
return new_user
