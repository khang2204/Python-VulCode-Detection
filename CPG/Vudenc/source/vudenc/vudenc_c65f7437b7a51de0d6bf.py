def complete(self, token, parsed, parser):...
options = [(option[1:] + '=') for action_group in parser._action_groups for
    action in action_group._group_actions for option in action.
    option_strings if option.startswith('=' + token) and not self.
    option_consumed(action, parsed)]
return options
