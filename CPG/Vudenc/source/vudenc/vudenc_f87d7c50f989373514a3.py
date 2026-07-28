def _plugin_option_exists(self, opt):...
"""docstring"""
plug = opt.split('.')[0]
if not self._plugin_exists(plug):
return False
if self._check_disabled(plug) and plug not in self.config['enable_plugins']:
return False
if self._check_enabled(plug):
return opt in self.sos_info['options']
return True
