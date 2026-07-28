def has_missing_keys(minimum_keys, actual_keys, name):...
"""docstring"""
actual_keys = frozenset(actual_keys)
missing = minimum_keys - actual_keys
if missing:
msg_missing = ' missing: %s' % sorted(missing) if missing else ''
return 'Unexpected %s%s; did you make a typo?' % (name, msg_missing)
