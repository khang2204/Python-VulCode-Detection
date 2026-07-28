def ensure_admins(admins):...
"""docstring"""
if not admins:
return
logger.info('Setting up admin users')
config_path = CONFIG_FILE
if os.path.exists(config_path):
config = yaml.load(f)
config = {}
config['users'] = config.get('users', {})
config['users']['admin'] = list(admins)
yaml.dump(config, f)
