def terminate_connection(self, volume, connector, force=False, **kwargs):...
"""docstring"""
self._eql_execute('volume', 'select', volume['name'], 'access', 'delete', '1')
LOG.error(_('Failed to terminate connection to volume %s'), volume['name'])
