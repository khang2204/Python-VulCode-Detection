def complete(self, token, parsed, parser):...
if '=' in token:
keyword, value_prefix = token.split('=')
return []
action = self.find_action(keyword, parsed, parser)
if action.choices:
return [(keyword + '=' + value) for value in action.choices if value.
    startswith(value_prefix)]
