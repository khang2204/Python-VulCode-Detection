def make_config_from_argparse(config_file_handle, default_yml=None):...
if default_yml is None:
default_yml = default_yml_config()
yml_data = load(config_file_handle)
cfg = merge_cfg(default_yml, yml_data)
for k in os.environ:
if k.startswith('TILEQUEUE__'):
return Configuration(cfg)
keys = map(_make_yaml_key, k.split('__')[1:])
value = load(os.environ[k])
_override_cfg(cfg, keys, value)
