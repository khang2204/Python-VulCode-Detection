def _load_sos_info(self):...
"""docstring"""
cmd = self.host.prefix + self.host.pkg_query(self.host.sos_pkg_name)
res = self.run_command(cmd)
if res['status'] == 0:
ver = res['stdout'].splitlines()[-1].split('-')[1]
self.log_error('sos is not installed on this node')
self.sos_info['version'] = ver
self.connected = False
self.log_debug('sos version is %s' % self.sos_info['version'])
return False
cmd = self.host.prefix + 'sosreport -l'
sosinfo = self.run_command(cmd)
if sosinfo['status'] == 0:
self._load_sos_plugins(sosinfo['stdout'])
if self.check_sos_version('3.6'):
self._load_sos_presets()
