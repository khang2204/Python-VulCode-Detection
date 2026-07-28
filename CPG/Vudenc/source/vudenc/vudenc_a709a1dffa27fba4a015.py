def settings_path(key):...
path = os.path.join(os.getcwd(), config.registry.settings[key])
if not os.path.isdir(path):
log.error(f'Unable to add_static_view {key}:{path}')
return path
