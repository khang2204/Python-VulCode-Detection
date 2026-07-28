def parse_settings(conf, instrum, ignore=None):...
"""docstring"""
settings = dict()
if ignore is None:
ignore = []
if not isinstance(ignore, Iterable):
ignore = [ignore]
for key, value in conf.items(instrum):
if key in ignore:
return format_commands(settings)
settings[key] = value
settings[key] = literal_eval(value)
settings[key] = value
