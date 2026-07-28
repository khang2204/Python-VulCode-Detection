def get_coalesce_tags(player):...
for tags in constants.TAGS_TO_COALESCE:
if player in tags:
return [player]
return tags
