def has_unexpected_subset_keys(expected_keys, minimum_keys, actual_keys, name):...
"""docstring"""
actual_keys = frozenset(actual_keys)
superfluous = actual_keys - expected_keys
missing = minimum_keys - actual_keys
if superfluous or missing:
msg_missing = ' missing: %s' % sorted(missing) if missing else ''
msg_superfluous = ' superfluous: %s' % sorted(superfluous
    ) if superfluous else ''
return 'Unexpected %s%s%s; did you make a typo?' % (name, msg_missing,
    msg_superfluous)
