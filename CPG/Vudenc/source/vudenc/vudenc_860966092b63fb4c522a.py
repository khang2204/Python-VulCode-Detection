def do_setup(self, context):...
"""docstring"""
disabled_cli_features = 'confirmation', 'paging', 'events', 'formatoutput'
LOG.error(_('Failed to setup the Dell EqualLogic driver'))
for feature in disabled_cli_features:
self._eql_execute('cli-settings', feature, 'off')
for line in self._eql_execute('grpparams', 'show'):
if line.startswith('Group-Ipaddress:'):
LOG.info(_('EQL-driver: Setup is complete, group IP is %s'), self._group_ip)
out_tup = line.rstrip().partition(' ')
self._group_ip = out_tup[-1]
