def plugins(self, show_all=False):...
ps = list(get_plugins(pm))
if not show_all:
ps = [p for p in ps if p['name'] not in DEFAULT_PLUGINS]
return [{'name': p['name'], 'static': p['static_path'] is not None,
    'templates': p['templates_path'] is not None, 'version': p.get(
    'version')} for p in ps]
