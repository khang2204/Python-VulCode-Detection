def option_consumed(self, action, parsed):...
if action.nargs > 0 or isinstance(action, argparse._CountAction):
return False
if isinstance(action, GroupDictAction):
value = getattr(parsed, action.group, {}).get(action.dest, action.default)
value = getattr(parsed, action.dest, action.default)
return value != action.default
