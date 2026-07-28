def _override_cfg(container, yamlkeys, value):...
"""docstring"""
key = yamlkeys[0]
rest = yamlkeys[1:]
if len(rest) == 0:
container[key] = value
if key in container:
_override_cfg(container, rest, value)
subtree = {}
_override_cfg(subtree, rest, value)
container[key] = subtree
