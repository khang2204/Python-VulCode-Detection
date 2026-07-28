def get_holder_types(tree):...
"""docstring"""
types = {(tree['dev_type'], tree['device'])}
for holder in tree['holders']:
types.update(get_holder_types(holder))
return types
