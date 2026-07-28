def _check_volume(self, volume):...
"""docstring"""
command = ['volume', 'select', volume['name'], 'show']
self._eql_execute(*command)
if err.stdout.find('does not exist.\n') > -1:
LOG.debug(_('Volume %s does not exist, it may have already been deleted'),
    volume['name'])
