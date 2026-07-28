def create_volume_from_snapshot(self, volume, snapshot):...
"""docstring"""
out = self._eql_execute('volume', 'select', snapshot['volume_name'],
    'snapshot', 'select', snapshot['name'], 'clone', volume['name'])
LOG.error(_('Failed to create volume from snapshot %s'), snapshot['name'])
return self._get_volume_data(out)
