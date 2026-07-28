def _find_scalac_plugins(self, scalac_plugins, classpath):...
"""docstring"""
plugin_names = {p for val in scalac_plugins for p in val.split(',')}
if not plugin_names:
return {}
active_plugins = {}
buildroot = get_buildroot()
cp_product = self.context.products.get_data('runtime_classpath')
for classpath_element in classpath:
name = self._maybe_get_plugin_name(classpath_element)
unresolved_plugins = plugin_names - set(active_plugins.keys())
if name in plugin_names:
plugin_target_closure = self._plugin_targets('scalac').get(name, [])
rel_classpath_elements = [os.path.relpath(cpe, buildroot) for cpe in
    ClasspathUtil.internal_classpath(plugin_target_closure, cp_product,
    self._confs)]
rel_classpath_elements = rel_classpath_elements or [classpath_element]
if active_plugins.get(name, rel_classpath_elements) != rel_classpath_elements:
active_plugins[name] = rel_classpath_elements
if len(active_plugins) == len(plugin_names):
return active_plugins
