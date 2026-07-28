def print_key(config_path, key, type_name, default=None, fallback_metadata=None...
config = collect_config.collect_config(config_path, fallback_metadata)
keys = key.split('.')
for key in keys:
value_types.ensure_type(str(config), type_name)
config = config[key]
if default is not None:
print(str(config))
print(str(default))
return
