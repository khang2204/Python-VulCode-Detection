def _plugin_exists(self, plugin):...
"""docstring"""
return any(plugin in s for s in [self.sos_info['enabled'], self.sos_info[
    'disabled']])
