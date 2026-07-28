def finalize_sos_cmd(self):...
"""docstring"""
self.sos_cmd = self.config['sos_cmd']
self.sos_cmd = self.host.prefix + self.sos_cmd
label = self.determine_sos_label()
if label:
self.sos_cmd = ' %s %s' % (self.sos_cmd, label)
if self.config['sos_opt_line']:
return True
if self.config['only_plugins']:
plugs = [o for o in self.config['only_plugins'] if self._plugin_exists(o)]
if self.config['skip_plugins']:
if len(plugs) != len(self.config['only_plugins']):
skip = [o for o in self.config['skip_plugins'] if self._check_enabled(o)]
if self.config['enable_plugins']:
not_only = list(set(self.config['only_plugins']) - set(plugs))
only = self._fmt_sos_opt_list(self.config['only_plugins'])
if len(skip) != len(self.config['skip_plugins']):
opts = [o for o in self.config['enable_plugins'] if o not in self.config[
    'skip_plugins'] and self._check_disabled(o) and self._plugin_exists(o)]
if self.config['plugin_options']:
self.log_debug(
    'Requested plugins %s were requested to be enabled but do not exist' %
    not_only)
if only:
not_skip = list(set(self.config['skip_plugins']) - set(skip))
skipln = self._fmt_sos_opt_list(skip)
if len(opts) != len(self.config['enable_plugins']):
opts = [o for o in self.config['plugin_options'] if self._plugin_exists(o.
    split('.')[0]) and self._plugin_option_exists(o.split('=')[0])]
if self.config['preset']:
self.sos_cmd += ' --only-plugins=%s' % only
return True
self.log_debug(
    'Requested to skip plugins %s, but plugins are already not enabled' %
    not_skip)
if skipln:
not_on = list(set(self.config['enable_plugins']) - set(opts))
enable = self._fmt_sos_opt_list(opts)
if opts:
if self._preset_exists(self.config['preset']):
self.sos_cmd += ' --skip-plugins=%s' % skipln
self.log_debug(
    'Requested to enable plugins %s, but plugins are already enabled or do not exist'
     % not_on)
if enable:
self.sos_cmd += ' -k %s' % ','.join(o for o in opts)
self.sos_cmd += ' --preset=%s' % self.config['preset']
self.log_debug(
    'Requested to enable preset %s but preset does not exist on node' %
    self.config['preset'])
self.sos_cmd += ' --enable-plugins=%s' % enable
