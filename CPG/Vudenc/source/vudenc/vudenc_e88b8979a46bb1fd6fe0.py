def plugin_config(self, plugin_name, database=None, table=None, fallback=True):...
"""docstring"""
plugins = self.metadata('plugins', database=database, table=table, fallback
    =fallback)
if plugins is None:
return None
return plugins.get(plugin_name)
