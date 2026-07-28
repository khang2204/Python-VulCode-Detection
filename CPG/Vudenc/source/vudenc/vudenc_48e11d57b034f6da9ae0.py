def delete_volume(self, volume):...
"""docstring"""
self._check_volume(volume)
LOG.warn(_('Volume %s was not found while trying to delete it'), volume['name']
    )
self._eql_execute('volume', 'select', volume['name'], 'offline')
LOG.error(_('Failed to delete volume %s'), volume['name'])
self._eql_execute('volume', 'delete', volume['name'])
