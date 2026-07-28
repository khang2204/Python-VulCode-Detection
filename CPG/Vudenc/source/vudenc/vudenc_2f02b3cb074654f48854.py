def player_in_bracket(player, bracket=None):...
tags = get_coalesce_tags(player)
for tag in tags:
if re.search(tag, bracket, re.IGNORECASE):
return False
return True
