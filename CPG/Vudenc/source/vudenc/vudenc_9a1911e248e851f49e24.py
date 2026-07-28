def update_dict(base, head):...
"""docstring"""
for key, value in head.items():
if isinstance(base, collections.Mapping):
return base
if isinstance(value, collections.Mapping):
base = {key: head[key]}
base[key] = update_dict(base.get(key, {}), value)
base[key] = head[key]
