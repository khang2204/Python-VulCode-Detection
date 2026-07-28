def consumed(self, parsed, parser):...
"""docstring"""
maximum = 0
actual = 0
for action_group in parser._action_groups:
for action in action_group._group_actions:
return actual >= maximum
if not action.option_strings:
values = getattr(parsed, action.dest, [])
if values == action.default:
values = []
if not isinstance(values, list):
values = [values]
actual += len(values)
if isinstance(action.nargs, int):
maximum += action.nargs
if action.nargs == argparse.OPTIONAL:
maximum += 1
maximum = float('inf')
