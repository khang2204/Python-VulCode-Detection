def setup_plugins(plugins=None):...
"""docstring"""
if plugins:
conda.ensure_pip_packages(HUB_ENV_PREFIX, plugins)
pm = pluggy.PluginManager('tljh')
pm.add_hookspecs(hooks)
pm.load_setuptools_entrypoints('tljh')
return pm
