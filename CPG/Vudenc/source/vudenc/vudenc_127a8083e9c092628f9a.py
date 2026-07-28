def find_action(self, keyword, parsed, parser):...
for action_group in parser._action_groups:
for action in action_group._group_actions:
if action.dest == keyword:
return action
