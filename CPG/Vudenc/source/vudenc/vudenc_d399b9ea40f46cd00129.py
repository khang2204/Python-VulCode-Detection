def extend_volume(self, volume, new_size):...
"""docstring"""
self._eql_execute('volume', 'select', volume['name'], 'size', '%sG' % new_size)
LOG.error(_(
    'Failed to extend_volume %(name)s from %(current_size)sGB to %(new_size)sGB'
    ), {'name': volume['name'], 'current_size': volume['size'], 'new_size':
    new_size})
