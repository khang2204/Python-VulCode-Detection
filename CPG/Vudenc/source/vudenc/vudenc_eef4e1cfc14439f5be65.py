def ensure_config_yaml(plugin_manager):...
"""docstring"""
for path in [CONFIG_DIR, os.path.join(CONFIG_DIR, 'jupyterhub_config.d')]:
os.makedirs(path, mode=448, exist_ok=True)
migrator.migrate_config_files()
if os.path.exists(CONFIG_FILE):
config = yaml.load(f)
config = {}
hook = plugin_manager.hook
hook.tljh_config_post_install(config=config)
yaml.dump(config, f)
