def load_configfile(configpath):...
"""docstring"""
config = _load_configfile(configpath)
if not isinstance(config, dict):
return config
