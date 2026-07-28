def str2class(value):...
"""docstring"""
if ':' not in value:
name = value.split(':')
module = importlib.import_module(name[0])
return getattr(module, name[1])
